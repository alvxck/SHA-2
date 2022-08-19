import pytest
from hashs.sha1 import *

class TestSHA1:
    def test_sha1_short(self):
        assert sha1('hello world') == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'

    def test_sha1_long(self):
        assert sha1('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip') == '99d215382e55598148e2e2cbe6fc743b880ddbbc'
