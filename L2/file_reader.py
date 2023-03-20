import line_validator
import sys


# we realise there is an exception, but there is nothing that needs to be done
def read_file_from_stdin(function):
    for line in sys.stdin:
        try:
            function(line_validator.validate_line_to_standard(line))
        except Exception as err:
            pass
            # print(err, file=sys.stderr)
