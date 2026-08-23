package screen

import (
	"context"
	"encoding/json"
	"fmt"
	"net/url"
	"os"
	"path/filepath"
	"regexp"
	"strings"
	"time"

	"github.com/chromedp/chromedp"
	"github.com/go-shiori/go-readability"
)

// Result is one screened page bundle.
type Result struct {
	Slug      string
	Dir       string
	URL       string
	FinalURL  string
	Title     string
	Status    int
	FetchedAt time.Time
}

var slugSanitizer = regexp.MustCompile(`[^a-z0-9]+`)

// Screen loads url in headless Chromium, saves screenshot + extracted text.
func Screen(ctx context.Context, repoRoot, rawURL, slug string) (*Result, error) {
	if slug == "" {
		slug = defaultSlug(rawURL)
	}
	outDir := filepath.Join(repoRoot, "research", "discoveries", slug)
	if err := os.MkdirAll(outDir, 0o755); err != nil {
		return nil, err
	}

	opts := append(chromedp.DefaultExecAllocatorOptions[:],
		chromedp.Flag("headless", true),
		chromedp.Flag("disable-gpu", true),
		chromedp.Flag("no-sandbox", true),
	)
	if chromePath := os.Getenv("WEBSCREEN_CHROME_PATH"); chromePath != "" {
		opts = append(opts, chromedp.ExecPath(chromePath))
	}

	allocCtx, cancelAlloc := chromedp.NewExecAllocator(ctx, opts...)
	defer cancelAlloc()

	browserCtx, cancelBrowser := chromedp.NewContext(allocCtx)
	defer cancelBrowser()

	timeout := 30 * time.Second
	if v := os.Getenv("WEBSCREEN_TIMEOUT"); v != "" {
		if d, err := time.ParseDuration(v); err == nil {
			timeout = d
		}
	}
	runCtx, cancelRun := context.WithTimeout(browserCtx, timeout)
	defer cancelRun()

	var title, finalURL, html string
	var png []byte

	tasks := chromedp.Tasks{
		chromedp.Navigate(rawURL),
		chromedp.WaitReady("body", chromedp.ByQuery),
		chromedp.Location(&finalURL),
		chromedp.Title(&title),
		chromedp.OuterHTML("html", &html, chromedp.ByQuery),
		chromedp.FullScreenshot(&png, 90),
	}
	if err := chromedp.Run(runCtx, tasks); err != nil {
		return nil, fmt.Errorf("chromedp: %w", err)
	}

	fetchedAt := time.Now().UTC()
	meta := map[string]any{
		"url":        rawURL,
		"final_url":  finalURL,
		"title":      title,
		"http_status": 200,
		"fetched_at": fetchedAt.Format(time.RFC3339),
		"engine":     "chromedp",
	}
	metaBytes, _ := json.MarshalIndent(meta, "", "  ")
	if err := os.WriteFile(filepath.Join(outDir, "meta.json"), metaBytes, 0o644); err != nil {
		return nil, err
	}
	if err := os.WriteFile(filepath.Join(outDir, "page.png"), png, 0o644); err != nil {
		return nil, err
	}
	if err := os.WriteFile(filepath.Join(outDir, "page.html"), []byte(html), 0o644); err != nil {
		return nil, err
	}

	parsed, _ := url.Parse(finalURL)
	article, err := readability.FromReader(strings.NewReader(html), parsed)
	contentMD := "# " + title + "\n\n"
	contentMD += "> Source: " + finalURL + "\n\n"
	if err == nil && strings.TrimSpace(article.TextContent) != "" {
		contentMD += article.TextContent
	} else {
		contentMD += "(readability extract failed — see page.png)\n"
	}
	if err := os.WriteFile(filepath.Join(outDir, "content.md"), []byte(contentMD), 0o644); err != nil {
		return nil, err
	}

	return &Result{
		Slug:      slug,
		Dir:       outDir,
		URL:       rawURL,
		FinalURL:  finalURL,
		Title:     title,
		Status:    200,
		FetchedAt: fetchedAt,
	}, nil
}

func defaultSlug(rawURL string) string {
	s := strings.ToLower(rawURL)
	s = strings.TrimPrefix(s, "https://")
	s = strings.TrimPrefix(s, "http://")
	s = strings.Split(s, "?")[0]
	s = slugSanitizer.ReplaceAllString(s, "-")
	s = strings.Trim(s, "-")
	if len(s) > 80 {
		s = s[:80]
	}
	date := time.Now().UTC().Format("2006-01-02")
	return date + "-" + s
}

// Slug builds a discovery folder name with optional prefix (e.g. hunt query).
func Slug(prefix, rawURL string) string {
	base := defaultSlug(rawURL)
	if prefix == "" {
		return base
	}
	prefix = slugSanitizer.ReplaceAllString(strings.ToLower(prefix), "-")
	prefix = strings.Trim(prefix, "-")
	if len(prefix) > 40 {
		prefix = prefix[:40]
	}
	return prefix + "-" + base
}
