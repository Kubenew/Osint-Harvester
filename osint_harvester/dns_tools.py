import dns.resolver


def dns_lookup(domain: str) -> dict:
    results = {}
    for rtype in ["A", "AAAA", "MX", "NS", "TXT"]:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            results[rtype] = [str(r) for r in answers]
        except Exception:
            results[rtype] = []
    return results
