import csv
import uuid

from database import add_video, close_session

def add_videos_from_csv():

    file_name = "train.csv"

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        count_row = len(rows)
        print(f"чтение из {file_name}, кол-во строк: {count_row}")
        for row in reader:

            # print("uuid:" + row[1])
            # print("upload_date:" + row[0])
            # print("")
            print(reader.line_num + f" из {count_row}")
            add_video(UUID=uuid.UUID(row[1]), upload_date=row[0], is_duplicate=row[3], is_hard=row[5])

        close_session()