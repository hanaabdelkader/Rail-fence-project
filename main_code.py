print ("Welcome to Rail Fence encryptor! \n For Encryption Type 1 \n For Decryption Type 2 \n To Exit type 3" )
import encryption
import def_decrypt
active = True
while active:
    X = int(input("Please enter your number: "))
    if X == 1:
        text1 = str(input("Please enter your text: "))
        key = int(input("Please enter your key: "))
        M = encryption.encrypt(key,text1)
        print(M)
        
    
    elif X == 2:
        text = input("Please enter your encrypted text: ")
        key = int(input("please enter your key: "))

        print(def_decrypt.decrypt(text, key))

    elif X == 3:
        print("Thank you for using my Railfence cipher program")
        active = False
    else:
        print("Sorry you entered wrong input")
