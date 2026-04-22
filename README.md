# osint-harvester

`osint-harvester` is a lightweight OSINT toolkit that collects and normalizes intelligence from multiple sources.

## Features (v0.1.0)

- DNS lookup (A/AAAA/MX/NS/TXT)
- WHOIS lookup
- HTTP header fingerprinting
- Simple IP reputation heuristics
- Export to JSON
- Export to STIX-like JSON format

## Install

```bash
pip install osint-harvester
```

## CLI usage

```bash
osint-harvester domain example.com
osint-harvester ip 8.8.8.8
osint-harvester url https://example.com
```

## Output formats

```bash
osint-harvester domain example.com --format json
osint-harvester domain example.com --format stix
```

## Python usage

```python
from osint_harvester import harvest_domain

data = harvest_domain("example.com")
print(data)
```

## License
MIT
