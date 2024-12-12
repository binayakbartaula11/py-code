import random
import string

def generate_random_string(length):
    """Generates a random string of specified length using letters and digits."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Input message for encryption
print("\n\n\n")
original_message = input("Enter your message to encrypt: ")

# Encryption Process
separator = generate_random_string(3) 
encrypted_message = ""

for word in original_message.split():
    # Simple encryption: reverse the word and add random characters at the ends
    encrypted_part = generate_random_string(2) + word[::-1] + generate_random_string(2)
    encrypted_message += separator + encrypted_part

print("\n\n\nEncrypted Message:\t", encrypted_message)

# Input encrypted message for decryption
decrypted_input = input("\n\nEnter the encrypted message to decrypt: ")

# Decryption Process
encrypted_parts = decrypted_input.split(separator)[1:]  # Split using the separator and ignore the first empty part
decrypted_message = ""

for encrypted_part in encrypted_parts:
    # Simple decryption: remove padding and reverse the word back
    core_part = encrypted_part[2:-2]
    decrypted_word = core_part[::-1]
    decrypted_message += " " + decrypted_word

print("\n\n\nDecrypted Message:\t", decrypted_message.strip())
