import os

os.makedirs("test_files", exist_ok=True)

sizes = {
    "file_1KB.txt": 1024,
    "file_100KB.txt": 100 * 1024,
    "file_1MB.txt": 1024 * 1024
}

for filename, size in sizes.items():

    with open(f"test_files/{filename}", "w") as f:
        f.write("A" * size)

print("Test files created successfully.")