import string
def cipher():
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    message = input("Type your message: ")
    shift_number = input("Type the shift number: ")
    cipherMachine(message, shift_number, action)


def cipherMachine(message, shift_number, operation):
    result = ""
    for index in range(len(message)):
        position = string.ascii_lowercase.find(message[index])
        if operation == "encode":
            result += string.ascii_lowercase[(position + int(shift_number)) % 26]
        elif operation == "decode":
            result += string.ascii_lowercase[(position - int(shift_number)) % 26]
        else:
            print("Invalid option.")

    print(result)

