"""Count English words in a UTF-8 text file."""

import argparse
from collections import Counter
from pathlib import Path
import re
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="path to a UTF-8 text file")
    args = parser.parse_args()

    try:
        text = args.file.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: file not found: {args.file}", file=sys.stderr)
        return 1
    except UnicodeDecodeError:
        print(f"Error: file is not valid UTF-8: {args.file}", file=sys.stderr)
        return 1
    except OSError as error:
        print(f"Error: cannot read file: {args.file}: {error}", file=sys.stderr)
        return 1

    counts = Counter(word.lower() for word in re.findall(r"[A-Za-z]+", text))
    print(f"Total words: {sum(counts.values())}")
    print(f"Unique words: {len(counts)}")
    print("Word counts:")
    if not counts:
        print("(none)")
    else:
        for word, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
            print(f"{word}: {count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
