from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

class AESCipher:

    def __init__(self):
        self.key = get_random_bytes(16)

    def encrypt(self, plaintext):

        cipher = AES.new(self.key, AES.MODE_CBC)

        ciphertext = cipher.encrypt(
            pad(plaintext.encode(), AES.block_size)
        )

        return cipher.iv + ciphertext

    def decrypt(self, encrypted_data):

        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]

        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        plaintext = unpad(
            cipher.decrypt(ciphertext),
            AES.block_size
        )

        return plaintext.decode()


if __name__ == "__main__":

    aes = AESCipher()

    text = "This is a confidential message."

    encrypted = aes.encrypt(text)

    print("Ciphertext:", encrypted)

    decrypted = aes.decrypt(encrypted)

    print("Recovered Text:", decrypted)