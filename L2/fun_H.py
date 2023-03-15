import file_reader
import file_printer


def validate_polish_site(line):
    url = line.split("-")[0][:-1]
    if url[-3:] == ".pl":
        file_printer.print_to_stdout(line)


if __name__ == "__main__":
    file_reader.read_file_from_stdin(validate_polish_site)
