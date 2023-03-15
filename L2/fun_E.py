import file_reader
import file_printer


def filter_return_code_200(line):
    words = line.split()
    code = words[-2]
    if code == "200":
        file_printer.print_to_stdout(line)


if __name__ == "__main__":
    file_reader.read_file_from_stdin(filter_return_code_200)
