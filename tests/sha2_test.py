import pytest
from hashs.sha2 import sha224, sha256, sha384, sha512, sha512_224, sha512_256

class TestSHA2:
    shortMessage = 'hello world'
    longMessage = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'

    def test_sha224_short(self):
        assert sha224(self.shortMessage) == '2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b'
    
    def test_sha224_long(self):
        assert sha224(self.longMessage) == '1da72422a9273122d0cb256a05195a1aa9db963fd0b8f96773386fa0'

    def test_sha256_short(self):
        assert sha256(self.shortMessage) == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
    
    def test_sha256_long(self):
        assert sha256(self.longMessage) == 'a511b93b6dc0854560cbff02dab131a2bf6e7fb48511b80af9e0bb72bbb9bf0e'

    def test_sha384_short(self):
        assert sha384(self.shortMessage) == 'fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd'
    
    def test_sha384_long(self):
        assert sha384(self.longMessage) == '146b481a1f3a61b1fb59e88d3b4b0ee964cbcafb862ae56c5ee94da72fb715c20187ebcca51414bdf50f95dfa4a812bf'
    
    def test_sha512_short(self):
        assert sha512(self.shortMessage) == '309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f'
    
    def test_sha512_long(self):
        assert sha512(self.longMessage) == 'e4089f39011cbb0ab15ab23ecbb51052813329409e9bafa982f08fcd3e093f96c5970b5ffaf92a5ea36520f82fe798216ac680acf90a291322c97ef72acb8a60'

    def test_sha512_224_short(self):
        assert sha512_224(self.shortMessage) == '22e0d52336f64a998085078b05a6e37b26f8120f43bf4db4c43a64ee'

    def test_sha512_224_long(self):
        assert sha512_224(self.longMessage) == 'f42a39d18a449bc026d4018adc9252623f143d0729fd46d73c31b047'

    def test_sha512_256_short(self):
        assert sha512_256(self.shortMessage) == '0ac561fac838104e3f2e4ad107b4bee3e938bf15f2b15f009ccccd61a913f017'

    def test_sha512_256_long(self):
        assert sha512_256(self.longMessage) == '30f19d82341dc5ecb37b7e7967df9d311cca9c3971b01e3b94ab2064111d34e2'
