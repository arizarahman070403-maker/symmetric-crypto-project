import os

os.makedirs("test_files", exist_ok=True)

# 1 KB file
with open("test_files/file_1KB.txt", "w") as f:
    f.write("A" * 1024)

# 100 KB file
with open("test_files/file_100KB.txt", "w") as f:
    f.write("A" * (100 * 1024))

# 1 MB file
with open("test_files/file_1MB.txt", "w") as f:
    f.write("A" * (1024 * 1024))

print("Test files created successfully!") 
