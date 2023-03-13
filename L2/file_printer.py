import line_validator


def print_to_stdin(line, line_num):
    print(line_validator.validate_line_to_standard(line, line_num))
