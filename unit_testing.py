import unittest
import encryption
import def_decrypt

class Testmycode(unittest.TestCase):

    def encrypt_test(self):
        text1 = encryption.encrypt(2,"hello world")
        self.assertEqual(text1,"hwe olordllll", "Encryption Failed")

    def decrypt_test(self):
        text1 = def_decrypt.decrypt("hew olordllll", 2, "Decryption Failed")
        self.assertEqual(text1,"hew olordllll", 2, "Decryption Failed")


if __name__ == "__main__":
    unittest.main()