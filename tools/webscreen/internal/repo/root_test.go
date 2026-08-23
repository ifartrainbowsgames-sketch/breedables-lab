package repo

import (
	"os"
	"path/filepath"
	"testing"
)

func TestRootFindsMkDocs(t *testing.T) {
	// Run from tools/webscreen — should find repo root two levels up.
	root, err := Root()
	if err != nil {
		t.Skip("mkdocs.yml not found from cwd:", err)
	}
	if _, err := os.Stat(filepath.Join(root, "mkdocs.yml")); err != nil {
		t.Fatalf("expected mkdocs.yml in %s", root)
	}
}
