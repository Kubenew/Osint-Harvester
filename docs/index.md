# osint-harvester

OSINT collection toolkit for DNS, WHOIS, IP reputation, and HTTP headers.

## Features

- DNS lookup (A/AAAA/MX/NS/TXT)
- WHOIS lookup
- HTTP header fingerprinting
- IP reputation heuristics

## Quick Start

```bash
pip install osint-harvester
```

```python
from osint_harvester import harvest

result = harvest("example.com")
print(result)
```