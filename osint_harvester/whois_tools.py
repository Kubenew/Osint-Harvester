import whois


def whois_lookup(domain: str) -> dict:
    try:
        w = whois.whois(domain)
        return dict(w)
    except Exception as e:
        return {"error": str(e)}
