#!/usr/bin/env python3
# Never Say It Out Loud — u-pucuys-never-say-it-out-loud-8198c3cd
"""Never Say It Out Loud — one line, printed and written to /output/entry.txt."""
import os

LINE = "I know exactly what you meant. I just like watching you rephrase it three times."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
