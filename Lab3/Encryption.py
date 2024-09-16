from cryptography.fernet import Fernet # type: ignore

# Generate and print a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Get input from user
user_input = input("Enter a string to encrypt: ")

# Encode the string and encrypt
encoded_input = user_input.encode()  # Encoding the string
encrypted_message = cipher.encrypt(encoded_input)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message)
decoded_message = decrypted_message.decode()  # Decoding the string

print(f"Encrypted: {encrypted_message}")
print(f"Decrypted: {decoded_message}")
