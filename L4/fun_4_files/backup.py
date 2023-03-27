import os
import shutil
from datetime import datetime
import json

# dst_path = os.path.join(os.environ["HOMEPATH"], "Desktop") + "/test" pulpit
if os.getenv("BACKUPS_DIR") is None:
    os.environ["BACKUPS_DIR"] = "./.backups"


def file_name(backup_path):
    return f"{os.getenv('BACKUPS_DIR')}/{datetime.timestamp(datetime.now())}-"f"{os.path.basename(os.path.abspath(backup_path))}"


def create_json_for_backup(backup_path):
    json_path = f"{os.getenv('BACKUPS_DIR')}/backups_history.json"

    if not os.path.exists(json_path):
        with open(json_path, 'w') as json_file:
            json.dump([], json_file)

    with open(json_path, 'r') as json_file:
        file_data = json.load(json_file)

    with open(json_path, 'w') as json_file:
        file_data.append({
            "data": str(datetime.now()),
            "localization": os.path.abspath(backup_path),
            "name_of_file": file_name(backup_path)
        })

        json.dump(file_data, json_file, indent=4)


def copy_files_to_zip(src_path):
    shutil.make_archive(file_name(src_path), 'zip', src_path)
    create_json_for_backup(src_path)


if __name__ == "__main__":
    copy_files_to_zip("./fun_4_files/TEST")
    # print(dst_path)
    # if len(sys.argv) == 2:
    #    sys.argv[1]
