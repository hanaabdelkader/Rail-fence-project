print ("Welcome to Rail Fence encryptor! \n To Encrypt Type 1 \n To Decrypt Type 2 \n To Exit type 3" )
import encryption
import def_decrypt
operation = True
while operation:
    X = int(input("Please enter your number: "))
    if X == 1:
        text1 = str(input("Please enter your text: "))
        key = int(input("Please enter your key: "))
        M = encryption.encrypt(key,text1)
        print("The cipher is:", M)
        
    
    elif X == 2:
        text = input("Please enter your encrypted text: ")
        key = int(input("please enter your key: "))

        print("The plaintext is: ", def_decrypt.decrypt(text, key))

    elif X == 3:
        print("Thank you for using my Railfence cipher program")
        operation = False
    else:
        print("Sorry you entered the wrong input")
