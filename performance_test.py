import os
import time
import pandas as pd

from simplified_rc4 import SimplifiedRC4
from aes_block_cipher import AESCipher

files = [
    "test_files/file_1KB.txt",
    "test_files/file_100KB.txt",
    "test_files/file_1MB.txt"
]

rc4 = SimplifiedRC4("SecretKey123")
aes = AESCipher()

results = []

for file in files:

    with open(file, "r") as f:
        data = f.read()

    # RC4 Encryption
    start = time.perf_counter()
    encrypted = rc4.encrypt(data)
    enc_time = time.perf_counter() - start

    start = time.perf_counter()
    rc4.decrypt(encrypted)
    dec_time = time.perf_counter() - start

    results.append([
        os.path.basename(file),
        "RC4",
        enc_time,
        dec_time
    ])

    # AES Encryption
    start = time.perf_counter()
    encrypted = aes.encrypt(data)
    enc_time = time.perf_counter() - start

    start = time.perf_counter()
    aes.decrypt(encrypted)
    dec_time = time.perf_counter() - start

    results.append([
        os.path.basename(file),
        "AES",
        enc_time,
        dec_time
    ])

df = pd.DataFrame(
    results,
    columns=[
        "File",
        "Algorithm",
        "Encryption Time",
        "Decryption Time"
    ]
)

df.to_csv(
    "performance_results.csv",
    index=False
)

print(df)

import matplotlib.pyplot as plt

pivot = df.pivot(
    index="File",
    columns="Algorithm",
    values="Encryption Time"
)

pivot.plot(kind="bar")

plt.title("Encryption Time Comparison")
plt.ylabel("Seconds")
plt.tight_layout()

plt.savefig("performance_graph.png")

plt.show()