#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys

total_size = 0
status_counts = {}
valid_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
line_count = 0


def print_stats():
    """Print total file size and number of lines by status code."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


try:
    for line in sys.stdin:
        parts = line.split()
        try:
            total_size += int(parts[-1])
            code = parts[-2]
            if code in valid_codes:
                status_counts[code] = status_counts.get(code, 0) + 1
        except (IndexError, ValueError):
            pass
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    raise

print_stats()
