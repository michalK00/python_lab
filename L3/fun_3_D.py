import fun_3_B
import fun_A
from prettytable import PrettyTable


def print_dict_entry_dates(dict):
    table = PrettyTable()
    table.field_names = ["Address/Domain name", "No. of requests",
                         "First request", "Last request", "200 codes ratio"]

    for key in dict.keys():
        dates_list = [log['datetime'] for log in dict[key]]
        first_request = min(dates_list)
        last_request = max(dates_list)
        requests_no = len(dict[key])
        _200_requests_no = len([log['status_code']
                                for log in dict[key] if int(log['status_code']) == 200])
        request_ratio = round(_200_requests_no/requests_no, 2)

        table.add_row([key, requests_no, first_request,
                      last_request, request_ratio])
    print(table)


if __name__ == "__main__":
    print_dict_entry_dates(fun_3_B.log_to_dict(fun_A.read_logs()))
