# Computers are commonly used in encryption. A very simple form of encryption
 #(more accurately "obfuscation") would be to remove the spaces from a message
# and reverse the resulting string. Write, and test, a function that takes a string
 #containing a message and "encrypts" it in this way.
def simple_encrypt(message):
    if not isinstance(message, str):
        raise ValueError("Input must be a string.")

    # Remove spaces and reverse the string
    encrypted_message = ''.join(message.split())[::-1]
    return encrypted_message

# Example usage:
original_message = "Hello, world! This is a simple encryption example."
encrypted_message = simple_encrypt(original_message)
print(f"Original message: {original_message}")
print(f"Encrypted message: {encrypted_message}")