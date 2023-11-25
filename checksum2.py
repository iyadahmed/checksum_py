import os
from hashlib import sha256


with open("CHECKSUM", "r") as checksum_file:
    for line in checksum_file:
        if line.startswith("#"):
            continue
        hash_method, filename, _equal_sign, hash_value = line.split()
        filename = filename.removeprefix("(").removesuffix(")")
        if not os.path.exists(filename):
            print(f"Skipping not found file: {filename}")
            continue
        with open(filename, "rb") as file:
            computed_hash = sha256(file.read(), usedforsecurity=True).hexdigest().lower()
            if computed_hash == hash_value.lower():
                print(f"Hash match! {filename}")
            else:
                print(f"DOES NOT MATCH!!!!! {filename}")
