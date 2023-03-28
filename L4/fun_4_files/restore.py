import os
import shutil
import sys
import dotenv
import json
from backup import json_path

dotenv.load_dotenv()  # wczytuje zmienne środowiskowe


def list_all_changes():
    amount_of_lines = 0
    with open(json_path, 'r') as json_file:
        file_data = json.load(json_file)

        for elem in file_data:
            print(f"{amount_of_lines} = {elem}")
            amount_of_lines += 1

    return amount_of_lines


def bring_backup(number_of_backup, directory, amount_of_lines):
    if number_of_backup > amount_of_lines or number_of_backup < 0:
        raise Exception("Input correct number!")

    with open(json_path, 'r') as json_file:
        file_data = json.load(json_file)

    shutil.rmtree(file_path)
    shutil.unpack_archive(os.path.abspath(file_data[number_of_backup]["name_of_file"]) + ".zip", directory)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        # przyjęty ten katalog, aby nie pogubić plików! Katalog robotczy to ../Laboratoria
        file_path = "./TEST"

    amount = list_all_changes()

    bring_backup(int(input("Input number of backup: ")), file_path, amount)

    # zczytuje wartość zmiennej środowiskowej i ustawia w pliku .env na nową wartość
    dotenv.set_key(dotenv.find_dotenv(), "BACKUPS_DIR", os.environ["BACKUPS_DIR"])
