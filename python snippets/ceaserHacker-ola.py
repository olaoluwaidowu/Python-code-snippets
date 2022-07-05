# prompt user to specify message to hack
message = input("Enter message you want to hack:").upper().strip()

# alphabets that can be encoded
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# looping through all alphabet
for key in range(len(alphabet)):
    realMessage = ''

    # looping to detect characters in message
    for character in message:
        if character in alphabet:
            
            # To get the position of character in alphabet
            position = alphabet.find(character)

            # decrypt to get the real position with key 
            realPosition = position - key
            if realPosition < 0:
                realPosition += len(alphabet)

            # get real character and add to real message
            realMessage = realMessage + alphabet[realPosition]

        else:
            # add character directly
            realMessage = realMessage + character

            
    # print possible keys and decryption
    print(f"if key is {key}, decripted message is: {realMessage}")
            
            
    


