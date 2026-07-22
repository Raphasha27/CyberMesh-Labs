"""Tests for CyberMesh-Labs network and threat modules."""
import pytest
from scripts.network_scan import scan_ports, parse_results, generate_report
from scripts.threat_feed import ThreatFeed, fetch_iocs, normalize_indicator

class TestNetworkScan:
    def test_scan_ports_returns_dict(self):
        result = scan_ports("192.168.1.1", ports=[80, 443])
        assert isinstance(result, dict)

    def test_parse_results(self):
        raw = {"192.168.1.1": {"80": "open", "443": "closed"}}
        parsed = parse_results(raw)
        assert "192.168.1.1" in parsed

    def test_generate_report(self):
        data = {"192.168.1.1": {"80": {"state": "open", "service": "http"}}}
        report = generate_report(data, "json")
        assert "192.168.1.1" in report

class TestThreatFeed:
    def test_fetch_iocs(self):
        iocs = fetch_iocs(source="alienvault", limit=5)
        assert len(iocs) <= 5

    def test_normalize_indicator(self):
        ip = "8.8.8.8"
        normalized = normalize_indicator(ip, "ipv4")
        assert normalized == ip

    def test_threat_feed_initialization(self):
        feed = ThreatFeed(api_key="test-key")
        assert feed.api_key == "test-key"
