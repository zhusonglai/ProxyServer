# test_proxyserver.py
"""
Tests for ProxyServer module.
"""

import unittest
from proxyserver import ProxyServer

class TestProxyServer(unittest.TestCase):
    """Test cases for ProxyServer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProxyServer()
        self.assertIsInstance(instance, ProxyServer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProxyServer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
