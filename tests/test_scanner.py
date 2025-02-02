import unittest
from scanner.port_scanner import scan_port

class TestPortScanner(unittest.TestCase):
    def test_scan_port(self):
        result = scan_port("8.8.8.8", 53)  # Tester Google DNS
        self.assertIn("ouvert", result.lower())  # Vérifier si le port est ouvert

if __name__ == "__main__":
    unittest.main()
