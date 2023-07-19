message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch.isalpha():
        if ch.islower():
            base = ord('a')
        else:
            base = ord('A')
        shifted = (ord(ch) - base + offset) % 26
        encoded_ch = chr(shifted + base)
    else:
        encoded_ch = ch
    encoded_message += encoded_ch