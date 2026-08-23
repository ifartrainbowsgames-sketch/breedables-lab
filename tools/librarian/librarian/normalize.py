from __future__ import annotations

import re
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

TRACKING_PARAMS = {
    "fbclid",
    "gclid",
    "mc_cid",
    "mc_eid",
    "ref",
    "source",
}
TRACKING_PREFIXES = ("utm_",)


def canonical_name(name: str) -> str:
    value = name.casefold().strip()
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def _github_repo_path(path: str) -> str:
    bits = [p for p in path.split("/") if p]
    if len(bits) >= 2:
        return f"/{bits[0]}/{bits[1]}"
    return "/" + "/".join(bits) if bits else ""


def _youtube_video_id(parts) -> str | None:
    host = (parts.hostname or "").casefold()
    path = parts.path.strip("/")
    if host in {"youtu.be", "www.youtu.be"} and path:
        return path.split("/")[0]
    if host in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
        if path == "watch":
            params = dict(parse_qsl(parts.query, keep_blank_values=True))
            return params.get("v")
        if path.startswith("shorts/"):
            return path.split("/", 1)[1].split("/", 1)[0]
    return None


def canonical_url(url: str) -> str:
    raw = url.strip()
    if not raw:
        return ""

    if "://" not in raw:
        raw = "https://" + raw

    parts = urlsplit(raw)
    scheme = (parts.scheme or "https").casefold()
    host = (parts.hostname or "").casefold()
    if host.startswith("www."):
        host = host[4:]

    video_id = _youtube_video_id(parts)
    if video_id:
        return f"https://youtube.com/watch?v={video_id}"

    path = re.sub(r"/+", "/", parts.path or "")
    if host == "github.com":
        path = _github_repo_path(path)

    if path != "/":
        path = path.rstrip("/")

    kept = []
    for key, value in parse_qsl(parts.query, keep_blank_values=True):
        k = key.casefold()
        if k in TRACKING_PARAMS or k.startswith(TRACKING_PREFIXES):
            continue
        kept.append((key, value))
    kept.sort(key=lambda x: (x[0].casefold(), x[1]))

    netloc = host
    if parts.port and not ((scheme == "https" and parts.port == 443) or (scheme == "http" and parts.port == 80)):
        netloc = f"{host}:{parts.port}"

    return urlunsplit((scheme, netloc, path, urlencode(kept), ""))


def github_repo_from_url(url: str) -> str | None:
    normalized = canonical_url(url)
    parts = urlsplit(normalized)
    if parts.hostname != "github.com":
        return None
    bits = [p for p in parts.path.split("/") if p]
    if len(bits) != 2:
        return None
    return f"{bits[0]}/{bits[1]}"
