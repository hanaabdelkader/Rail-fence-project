def decrypt(ciphertext,key_number):
    length = len(ciphertext)
    encrypted_text = "." * length

    cycle = key_number * 2 -2
    #repetition el cycle w double slash 3ashan teb2a integer
    rep = length // cycle

    row_length = [0]*key_number

    #first rail = number of complete cycles (rep)
    #first rail
    row_length[0] = rep

    #middle rail
    for i in range(1,key_number -1):
        row_length[i] = 2 * rep 

    #bottom rail
    row_length[key_number-1] = rep

    for i in range(length % cycle):
        if i < key_number:
            row_length[i] += 1
        else:
            row_length[cycle-i] += 1

    print(row_length) 

    #replace characters in the top rail
    print (encrypted_text)
    index = 0
    char_pos = 0
    for c in ciphertext[:row_length[0]]:
        encrypted_text = encrypted_text[:index] + c + encrypted_text [index+ 1:]
        index += cycle

    char_pos += row_length[0]
    print(encrypted_text)

    #replace characters in the middle rail

    for row in range(1, key_number-1):
        left_index = row
        right_index = cycle - row
        left_char = True
        for c in ciphertext[char_pos:char_pos+row_length[row]]:
            if left_char:
                encrypted_text = encrypted_text[:left_index] + c + encrypted_text[left_index+1:]
                left_index += cycle
                left_char = not left_char
            else:
                encrypted_text = encrypted_text[:right_index] + c + encrypted_text[right_index+1:]
                right_index += cycle
                left_char = not left_char

        char_pos += row_length[row]
        print(encrypted_text)


    #replace characters in last rail
    index = key_number - 1

    for c in ciphertext[char_pos:]:
        encrypted_text = encrypted_text[:index] + c + encrypted_text [index+ 1:]
        index += cycle


    print(encrypted_text)
    return encrypted_text
