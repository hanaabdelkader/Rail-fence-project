def decrypt(ciphertext,key_number):
    length = len(ciphertext)
    encrypted_text = "." * length

    cycle = key_number * 2 -2
    #repetition el cycle w double slash 3ashan teb2a integer
    rep = length // cycle

    rail_length = [0]*key_number

    #first rail = number of complete cycles (rep)
    #first rail
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

key_number = int(input("please enter the key: "))
ciphertext = str(input("please enter the ciphertext: "))

decrypt (ciphertext, key_number)