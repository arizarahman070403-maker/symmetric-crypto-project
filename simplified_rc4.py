class SimplifiedRC4:
    def __init__(self, key):
        self.key = [ord(c) for c in key]

    def generate_keystream(self, length):
        S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + S[i] + self.key[i % len(self.key)]) % 256
            S[i], S[j] = S[j], S[i]
        i = 0
        j = 0
        keystream = []
        for _ in range(length):
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            K = S[(S[i] + S[j]) % 256]
            keystream.append(K)
        return keystream

    def encrypt(self, plaintext):
        plaintext_bytes = plaintext.encode()
        keystream = self.generate_keystream(len(plaintext_bytes))
        return bytes([plaintext_bytes[i] ^ keystream[i] for i in range(len(plaintext_bytes))])

    def decrypt(self, ciphertext):
        keystream = self.generate_keystream(len(ciphertext))
        return bytes([ciphertext[i] ^ keystream[i] for i in range(len(ciphertext))]).decode()