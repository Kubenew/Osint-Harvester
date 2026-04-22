import requests


def fetch_headers(url: str, timeout: int = 10) -> dict:
    try:
        r = requests.get(url, timeout=timeout, allow_redirects=True)
        return {
            "final_url": r.url,
            "status_code": r.status_code,
            "headers": dict(r.headers),
        }
    except Exception as e:
        return {"error": str(e)}
