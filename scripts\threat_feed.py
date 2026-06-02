"""CyberMesh Labs - Threat intelligence feed aggregator."""
import urllib.request
import json

def fetch_abuseipdb(ip: str, api_key: str = "") -> dict:
    """Check IP reputation against AbuseIPDB."""
    if not api_key:
        return {"error": "API key required"}
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}"
    req = urllib.request.Request(url, headers={"Key": api_key, "Accept": "application/json"})
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        return json.loads(resp.read())
    except Exception as e:
        return {"error": str(e)}

def fetch_alienvault(ip: str) -> dict:
    """Check IP against AlienVault OTX."""
    url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip}/general"
    try:
        resp = urllib.request.urlopen(url, timeout=10)
        return json.loads(resp.read())
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import sys
    ip = sys.argv[1] if len(sys.argv) > 1 else "8.8.8.8"
    print(json.dumps(fetch_alienvault(ip), indent=2)[:500])
