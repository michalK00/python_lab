import line_validator
import file_printer
import friday_printer
import polish_site_printer
import sys

if __name__ == '__main__':
    i = 0
    for line in sys.stdin:
        polish_site_printer.validate_polish_site(line, i)
        i += 1
