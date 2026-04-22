import argparse
import json

from .core import harvest_domain, harvest_ip, harvest_url
from .models import OSINTReport, to_stix_like


def main():
    parser = argparse.ArgumentParser(prog="osint-harvester", description="OSINT Harvester CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_domain = sub.add_parser("domain", help="Harvest domain OSINT")
    p_domain.add_argument("domain")
    p_domain.add_argument("--format", choices=["json", "stix"], default="json")

    p_ip = sub.add_parser("ip", help="Harvest IP OSINT")
    p_ip.add_argument("ip")
    p_ip.add_argument("--format", choices=["json", "stix"], default="json")

    p_url = sub.add_parser("url", help="Harvest URL OSINT")
    p_url.add_argument("url")
    p_url.add_argument("--format", choices=["json", "stix"], default="json")

    args = parser.parse_args()

    if args.command == "domain":
        data = harvest_domain(args.domain)
    elif args.command == "ip":
        data = harvest_ip(args.ip)
    else:
        data = harvest_url(args.url)

    if args.format == "json":
        print(json.dumps(data, indent=2, ensure_ascii=False))
    else:
        report = OSINTReport(
            target=data["target"],
            target_type=data["target_type"],
            data=data["data"],
            errors=data["errors"],
        )
        print(json.dumps(to_stix_like(report), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
