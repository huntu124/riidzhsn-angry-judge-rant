"""One-line entry for Angry Judge Rant: writes the line the judge reads to /output/entry.txt."""

import os

LINE = (
    "WHO PUT 'temp_final_v2_REAL.js' IN PRODUCTION WITH A VARIABLE CALLED data2?! I want a name, a reason, and a time machine — in that order."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
