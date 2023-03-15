import file_reader
import file_printer


def filter_hour_between_22_and_6(line):
    words = line.split()
    time_stamp = words[3]
    hour = int((time_stamp.split(":"))[1])
    if hour > 22 or hour < 6:
        file_printer.print_to_stdout(line)


if __name__ == "__main__":
    file_reader.read_file_from_stdin(filter_hour_between_22_and_6)
