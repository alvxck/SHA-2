import pytest
from hashs.sha1 import sha1

class TestSHA1:
    shortMessage = 'hello world'
    longMessage = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'

    def test_sha1_short(self):
        assert sha1(self.shortMessage) == '2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'

    def test_sha1_long(self):
        assert sha1(self.longMessage) == '99d215382e55598148e2e2cbe6fc743b880ddbbc'
