"""One Word for Your Wi-Fi — entry for make.fun.

Writes one word to /output/entry.txt.
The word is one word that describes our Wi-Fi, funny and true, and nothing else.
"""
import os

WORD = "Moody"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")

if __name__ == "__main__":
    main()
