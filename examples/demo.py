from osint_harvester import harvest_domain, harvest_ip, harvest_url

print(harvest_domain("example.com"))
print(harvest_ip("8.8.8.8"))
print(harvest_url("https://example.com"))
