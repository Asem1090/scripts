import sys
import hashlib
import os

ALGORITHMS = ('md5', 'sha1', 'sha256')

def calculate_hash(file_path, algorithm):
    hash_func = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            hash_func.update(chunk)
    return hash_func.hexdigest()

def verify_checksum(path, checksum):
    if os.path.isfile(path):

        for algo in ALGORITHMS:
            if calculate_hash(path, algo) == checksum:
                return algo
    return ""

def main():
    if len(sys.argv) != 3:
        print("Error: Invalid number of arguments. Args: <path> <checksum>")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.isfile(path):
        print("Error: The specified path is not a file.")
        sys.exit(1)

    checksum = sys.argv[2]
    
    result = verify_checksum(path, checksum)
    if result:
        print(f"Checksum matches ({result})")
    else:
        print(f"Checksum does not match {ALGORITHMS})")
    
if __name__ == "__main__":
    main()