import os
import sys
from hashlib import md5


# https://stackoverflow.com/a/14981125/8094047
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        eprint("Expected 1 argument: /path/to/msd5sum.txt")
        eprint("Example md5sum.txt:")
        eprint("sum1  filename1")
        eprint("sum2  filename2")
        eprint("sum3  filename3")
        eprint("sum4  filename4")
        exit(1)
    with open(sys.argv[1]) as md5sum_file:
        for line in md5sum_file:
            md5sum, file_name = line.split()
            if os.path.exists(file_name):
                with open(file_name, "rb") as file:
                    computed_md5 = (
                        md5(file.read(), usedforsecurity=False).hexdigest().lower()
                    )
                    if computed_md5 == md5sum.lower():
                        print(f"Hash match! {file_name}")
                    else:
                        print(f"DOES NOT MATCH!!!!! {file_name}, {computed_md5}")
            else:
                print(f"File not found {file_name}")
