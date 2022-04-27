import unittest
from hashs.sha2 import *

class TestSHA224(unittest.TestCase):
    def test_sha224(self):
        self.assertEqual(sha224('hello world'), '2f05477fc24bb4faefd86517156dafdecec45b8ad3cf2522a563582b')
        self.assertEqual(sha224('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), '1da72422a9273122d0cb256a05195a1aa9db963fd0b8f96773386fa0')

    def test_sha256(self):
        self.assertEqual(sha256('hello world'), 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9')
        self.assertEqual(sha256('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), 'a511b93b6dc0854560cbff02dab131a2bf6e7fb48511b80af9e0bb72bbb9bf0e')

    def test_sha384(self):
        self.assertEqual(sha384('hello world'), 'fdbd8e75a67f29f701a4e040385e2e23986303ea10239211af907fcbb83578b3e417cb71ce646efd0819dd8c088de1bd')
        self.assertEqual(sha384('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), '146b481a1f3a61b1fb59e88d3b4b0ee964cbcafb862ae56c5ee94da72fb715c20187ebcca51414bdf50f95dfa4a812bf')
    
    def test_sha512(self):
        self.assertEqual(sha512('hello world'), '309ecc489c12d6eb4cc40f50c902f2b4d0ed77ee511a7c7a9bcd3ca86d4cd86f989dd35bc5ff499670da34255b45b0cfd830e81f605dcf7dc5542e93ae9cd76f')
        self.assertEqual(sha512('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), 'e4089f39011cbb0ab15ab23ecbb51052813329409e9bafa982f08fcd3e093f96c5970b5ffaf92a5ea36520f82fe798216ac680acf90a291322c97ef72acb8a60')


    def test_sha512_224(self):
        self.assertEqual(sha512_224('hello world'), '22e0d52336f64a998085078b05a6e37b26f8120f43bf4db4c43a64ee')
        self.assertEqual(sha512_224('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), 'f42a39d18a449bc026d4018adc9252623f143d0729fd46d73c31b047')

    def test_sha512_256(self):
        self.assertEqual(sha512_256('hello world'), '0ac561fac838104e3f2e4ad107b4bee3e938bf15f2b15f009ccccd61a913f017')
        self.assertEqual(sha512_256('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip'), '30f19d82341dc5ecb37b7e7967df9d311cca9c3971b01e3b94ab2064111d34e2')
