from librarian.normalize import canonical_name, canonical_url, github_repo_from_url


def test_canonical_name():
    assert canonical_name(" Material-Maker ") == "material maker"


def test_github_url_collapses_to_repo():
    assert canonical_url("https://www.github.com/RodZill4/material-maker/tree/main?utm_source=x") == \
        "https://github.com/RodZill4/material-maker"


def test_tracking_parameters_are_removed():
    assert canonical_url("https://example.com/tool/?utm_source=x&b=2&a=1") == \
        "https://example.com/tool?a=1&b=2"


def test_youtube_urls_are_normalized():
    assert canonical_url("https://youtu.be/abc123?t=55") == "https://youtube.com/watch?v=abc123"


def test_github_repo_detection():
    assert github_repo_from_url("https://github.com/ucupumar/ucupaint") == "ucupumar/ucupaint"
