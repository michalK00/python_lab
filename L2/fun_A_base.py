def count_code_base(line, searched_code, number_of_codes):
    words = line.split()
    code = words[-2]
    if code == searched_code:
        number_of_codes += 1

    return number_of_codes
