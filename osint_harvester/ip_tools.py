import socket


def reverse_dns(ip: str) -> dict:
    try:
        host, _, _ = socket.gethostbyaddr(ip)
        return {"reverse_dns": host}
    except Exception:
        return {"reverse_dns": None}


def basic_ip_reputation(ip: str) -> dict:
    private = ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.")
    return {
        "private_range": private,
        "note": "Heuristic check only. Use real threat intel providers for accurate reputation.",
    }
