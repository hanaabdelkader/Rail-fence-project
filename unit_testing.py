import unittest
import encryption
import def_decrypt

class Testmycode(unittest.TestCase):

    def encrypt_test(self):
        text1 = encryption.encrypt(6,"welcome to the rail fence")
        self.assertEqual(text1,"w feot elthlnc eicoe aemr", "Encryption Failed")

    def decrypt_test(self):
        text1 = def_decrypt.decrypt("w feot elthlnc eicoe aemr", 6, "Decryption Failed")
        self.assertEqual(text1,"w feot elthlnc eicoe aemr", 6, "Decryption Failed")


if __name__ == "__main__":
    unittest.main()