def encrypt(key_number , plaintext):

    cipher = ""
    #how many letters before we return top row
    cycle = key_number * 2 - 2

    
    for row in range(key_number):
        index = 0

        #for the first row
        if row == 0:
            while index < len(plaintext):
            # will increment every letter from the plaintext into the cipher
                cipher += plaintext[index]
            #index will increase by the cycle number
                index += cycle

        #for the last row
        elif row == key_number-1:
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

