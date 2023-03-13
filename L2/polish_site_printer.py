import line_validator


def validate_polish_site(line, line_num):

    url = line_validator.validate_line_to_standard(line, line_num).split("-")[0][:-1]
    if url[-3:] == ".pl":
        print(line)
