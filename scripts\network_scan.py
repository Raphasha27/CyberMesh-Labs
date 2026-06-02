"""CyberMesh Labs - Network scanning and threat detection utilities."""
import subprocess
import json
import sys
from datetime import datetime

def scan_ports(target: str, ports: str = "1-1024") -> list:
    """Scan common ports on a target using nmap (if available)."""
    try:
        result = subprocess.run(
            ["nmap", "-sV", "-p", ports, target],
            capture_output=True, text=True, timeout=300
        )
        return {"target": target, "results": result.stdout, "timestamp": datetime.now().isoformat()}
    except FileNotFoundError:
        return {"error": "nmap not installed", "target": target}
    except subprocess.TimeoutExpired:
        return {"error": "scan timed out", "target": target}

def check_ssl(target: str) -> dict:
    """Check SSL certificate validity."""
    import ssl, socket
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=target) as s:
            s.settimeout(10)
            s.connect((target, 443))
            cert = s.getpeercert()
            return {
                "target": target,
                "issuer": dict(x[0] for x in cert.get("issuer", [])),
                "expiry": cert.get("notAfter"),
                "valid": True,
            }
    except Exception as e:
        return {"target": target, "error": str(e), "valid": False}

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    print(json.dumps(check_ssl(target), indent=2))
