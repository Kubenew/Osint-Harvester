from .models import OSINTReport
from .dns_tools import dns_lookup
from .whois_tools import whois_lookup
from .http_tools import fetch_headers
from .ip_tools import reverse_dns, basic_ip_reputation


def harvest_domain(domain: str) -> dict:
    report = OSINTReport(target=domain, target_type="domain")
    report.data["dns"] = dns_lookup(domain)
    report.data["whois"] = whois_lookup(domain)
    return report.to_dict()


def harvest_ip(ip: str) -> dict:
    report = OSINTReport(target=ip, target_type="ip")
    report.data["reverse_dns"] = reverse_dns(ip)
    report.data["reputation"] = basic_ip_reputation(ip)
    return report.to_dict()


def harvest_url(url: str) -> dict:
    report = OSINTReport(target=url, target_type="url")
    report.data["http"] = fetch_headers(url)
    return report.to_dict()
