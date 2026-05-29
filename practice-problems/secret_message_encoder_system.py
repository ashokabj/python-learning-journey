def encode_message(message):
    return message[::-1].replace(" ", "#").upper()


message = input("Enter the message: ")

print(f"Encoded message: {encode_message(message)}")