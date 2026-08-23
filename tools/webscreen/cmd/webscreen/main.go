package main

import (
	"context"
	"flag"
	"fmt"
	"os"
	"strings"

	"github.com/ifartrainbowsgames-sketch/breedables-lab/tools/webscreen/internal/repo"
	"github.com/ifartrainbowsgames-sketch/breedables-lab/tools/webscreen/internal/screen"
	"github.com/ifartrainbowsgames-sketch/breedables-lab/tools/webscreen/internal/search"
)

func main() {
	if len(os.Args) < 2 {
		usage()
		os.Exit(2)
	}
	switch os.Args[1] {
	case "screen":
		os.Exit(runScreen(os.Args[2:]))
	case "search":
		os.Exit(runSearch(os.Args[2:]))
	case "hunt":
		os.Exit(runHunt(os.Args[2:]))
	case "help", "-h", "--help":
		usage()
		os.Exit(0)
	default:
		fmt.Fprintf(os.Stderr, "unknown command %q\n", os.Args[1])
		usage()
		os.Exit(2)
	}
}

func usage() {
	fmt.Fprintf(os.Stderr, `Breedables webscreen — Go + Chromium screening & SearXNG search

Usage:
  webscreen screen --url <URL> [--slug <name>]
  webscreen search --query <text> [--limit N]
  webscreen hunt   --query <text> [--limit N]   # search then screen each hit

Env:
  WEBSCREEN_SEARXNG_URL   SearXNG base (default http://127.0.0.1:8080)
  WEBSCREEN_CHROME_PATH   Chrome/Edge binary path
  WEBSCREEN_TIMEOUT       e.g. 45s

Wiki: docs/production/tools/web-research-stack.md
`)
}

func runScreen(args []string) int {
	fs := flag.NewFlagSet("screen", flag.ExitOnError)
	rawURL := fs.String("url", "", "URL to screen (required)")
	slug := fs.String("slug", "", "output folder slug under research/discoveries/")
	_ = fs.Parse(args)
	if *rawURL == "" {
		fmt.Fprintln(os.Stderr, "screen: --url required")
		return 2
	}
	root, err := repo.Root()
	if err != nil {
		fmt.Fprintf(os.Stderr, "repo root: %v\n", err)
		return 1
	}
	res, err := screen.Screen(context.Background(), root, *rawURL, *slug)
	if err != nil {
		fmt.Fprintf(os.Stderr, "screen failed: %v\n", err)
		return 1
	}
	fmt.Printf("saved %s\n  title: %s\n  dir:   %s\n", res.Slug, res.Title, res.Dir)
	return 0
}

func runSearch(args []string) int {
	fs := flag.NewFlagSet("search", flag.ExitOnError)
	query := fs.String("query", "", "search query (required)")
	limit := fs.Int("limit", 10, "max results")
	_ = fs.Parse(args)
	if *query == "" {
		fmt.Fprintln(os.Stderr, "search: --query required")
		return 2
	}
	hits, err := search.SearXNG(context.Background(), *query, *limit)
	if err != nil {
		fmt.Fprintf(os.Stderr, "search failed: %v\n", err)
		return 1
	}
	for i, h := range hits {
		fmt.Printf("%d. %s\n   %s\n", i+1, h.Title, h.URL)
	}
	return 0
}

func runHunt(args []string) int {
	fs := flag.NewFlagSet("hunt", flag.ExitOnError)
	query := fs.String("query", "", "search query (required)")
	limit := fs.Int("limit", 3, "max URLs to screen")
	_ = fs.Parse(args)
	if *query == "" {
		fmt.Fprintln(os.Stderr, "hunt: --query required")
		return 2
	}
	root, err := repo.Root()
	if err != nil {
		fmt.Fprintf(os.Stderr, "repo root: %v\n", err)
		return 1
	}
	hits, err := search.SearXNG(context.Background(), *query, *limit)
	if err != nil {
		fmt.Fprintf(os.Stderr, "search failed: %v\n", err)
		return 1
	}
	if len(hits) == 0 {
		fmt.Println("no results")
		return 0
	}
	for _, h := range hits {
		slug := screen.Slug(slugFromQuery(*query), h.URL)
		fmt.Printf("screening: %s\n", h.URL)
		res, err := screen.Screen(context.Background(), root, h.URL, slug)
		if err != nil {
			fmt.Fprintf(os.Stderr, "  failed: %v\n", err)
			continue
		}
		fmt.Printf("  saved: %s (%s)\n", res.Slug, res.Title)
	}
	return 0
}

func slugFromQuery(query string) string {
	q := strings.ToLower(query)
	q = strings.ReplaceAll(q, " ", "-")
	if len(q) > 30 {
		q = q[:30]
	}
	return q
}
