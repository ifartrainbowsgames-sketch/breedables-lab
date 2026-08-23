package search

import (
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"net/url"
	"os"
	"time"
)

// Hit is one search result.
type Hit struct {
	Title string
	URL   string
}

type searxResponse struct {
	Results []struct {
		Title string `json:"title"`
		URL   string `json:"url"`
	} `json:"results"`
}

// SearXNG queries a self-hosted SearXNG instance.
func SearXNG(ctx context.Context, query string, limit int) ([]Hit, error) {
	base := os.Getenv("WEBSCREEN_SEARXNG_URL")
	if base == "" {
		base = "http://127.0.0.1:8080"
	}
	if limit <= 0 {
		limit = 10
	}

	u, err := url.Parse(base)
	if err != nil {
		return nil, err
	}
	u.Path = "/search"
	q := u.Query()
	q.Set("q", query)
	q.Set("format", "json")
	u.RawQuery = q.Encode()

	req, err := http.NewRequestWithContext(ctx, http.MethodGet, u.String(), nil)
	if err != nil {
		return nil, err
	}

	client := &http.Client{Timeout: 30 * time.Second}
	resp, err := client.Do(req)
	if err != nil {
		return nil, fmt.Errorf("searxng request: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("searxng status %d", resp.StatusCode)
	}

	var payload searxResponse
	if err := json.NewDecoder(resp.Body).Decode(&payload); err != nil {
		return nil, err
	}

	out := make([]Hit, 0, limit)
	for _, r := range payload.Results {
		if r.URL == "" {
			continue
		}
		out = append(out, Hit{Title: r.Title, URL: r.URL})
		if len(out) >= limit {
			break
		}
	}
	return out, nil
}
