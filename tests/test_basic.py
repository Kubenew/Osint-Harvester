from osint_harvester import harvest_domain


def test_domain_harvest():
    data = harvest_domain("example.com")
    assert data["target"] == "example.com"
    assert data["target_type"] == "domain"
    assert "dns" in data["data"]
