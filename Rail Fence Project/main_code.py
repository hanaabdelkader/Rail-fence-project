def encrypt(key_number , plaintext):

    cipher = ""
    #how many letters before we return top row
    cycle = key_number * 2 - 2

    
    for row in range(key_number):
        index = 0

        #for the first row
        if row == 0:
            while index < len(plaintext):
            # hayakhod character character men el plaintext
                cipher += plaintext[index]
            #index will increase by the cycle number
                index += cycle

        #for the last row
        elif row == key_number - 1:
            index = row
            while index < len(plaintext):
                cipher += plaintext[index]
                index += cycle
        
        #middle rows
        else:
            left_index = row
            right_index = cycle - row
            while left_index < len(plaintext):
                cipher += plaintext[left_index]

                if right_index < len(plaintext):
                    cipher += plaintext[right_index]

                left_index += cycle
                right_index += cycle
    
    return cipher

def decrypt(ciphertext,key_number):
    length = len(ciphertext)
    encrypted_text = "." * length

    cycle = key_number * 2 -2
    #repetition el cycle and we used the double slash to have an integer
    rep = length // cycle

    rail_length = [0]*key_number


    #first rail and is equal to the numbers of comlete cycles "rep"
    rail_length[0] = rep

    #middle rail
    for i in range(1,key_number -1):
        rail_length[i] = 2 * rep 

    #bottom rail
    rail_length[key_number-1] = rep

    for i in range(length % cycle):
        if i < key_number:
            rail_length[i] += 1
        else:
            rail_length[cycle-i] += 1

    print(rail_length) 

    #replace characters in the top rail fence
    print (encrypted_text)
    index = 0
    dirc = 0
    for c in ciphertext[:rail_length[0]]:
        encrypted_text = encrypted_text[:index] + c + encrypted_text [index+ 1:]
        index += cycle

    dirc += rail_length[0]
    print(encrypted_text)

    #replace characters in the middle rail

    for row in range(1, key_number-1):
        left_index = row
        right_index = cycle - row
        left_char = True
        for c in ciphertext[dirc:dirc+rail_length[row]]:
            if left_char:
                encrypted_text = encrypted_text[:left_index] + c + encrypted_text[left_index+1:]
                left_index += cycle
                left_char = not left_char
            else:
                encrypted_text = encrypted_text[:right_index] + c + encrypted_text[right_index+1:]
                right_index += cycle
                left_char = not left_char

        dirc += rail_length[row]
        print(encrypted_text)


    #last rail
    index = key_number - 1

    for c in ciphertext[dirc:]:
        encrypted_text = encrypted_text[:index] + c + encrypted_text [index+ 1:]
        index += cycle


    print(encrypted_text)
    return encrypted_text


if __name__ == "__main__":
    
    print("Cipher: " , encrypt(4,"codespeedy"))
    print("Cipher: " ,encrypt(4,"hana_rewsha"))

    print("Encrypted text: ",decrypt("ceopedsdey",4))
    print("Encrypted text: ",decrypt("hearwn_saah",4))