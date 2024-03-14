#!/usr/bin/python3
for alphabets in range(ord('a'), ord('z') + 1):
    if alphabets in [ord('e'), ord('q')]:
        continue
    print("{:c}".format(alphabets), end="")
