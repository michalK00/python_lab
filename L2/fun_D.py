import sys
import file_printer
import line_validator


def check_percent_of_graphics_resources():
    all_resouces_count = 0
    graphical_resource_count = 0
    for line in sys.stdin:
        if line_validator.validate_and_handle_exceptions(line):
            words = line.split()
            method = words[-5].strip("\"")
            if method == "GET":
                all_resouces_count += 1
                file_extension = (words[-4].rsplit("."))[-1]
                if file_extension in ["gif", "jpg", "jpeg", "xbm"]:
                    graphical_resource_count += 1

    file_printer.print_to_stdout(
        f"Percent of graphics in all downloaded resources {graphical_resource_count / all_resouces_count:.2f}%")


if __name__ == "__main__":
    check_percent_of_graphics_resources()
