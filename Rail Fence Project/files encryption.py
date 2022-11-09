import def_encrypt
import def_decrypt

file1 = open("plaintext.text","w")
L = ["welcome to rail fence encryptor! \n", "i am hana abdelkader \n", "a student at coventry university \n", "i am born february 24,2,2004 \n"]
file1.writelines(L)
file1.close()

file2 = open("plaintext.text","r+")
#print (file2.read())
holder = file2.read()
print (holder)
tt = def_encrypt.encrypt(holder,5)

file1 = open("cipher.txt","w")
file1.writelines(tt)
file1.close()

file2= open("cipher.txt", "r+")
holder = file2.read()
tt = def_decrypt(holder,5)

file1 = open("restored-text.txt","w")
file1.writelines(tt)
file1.close()