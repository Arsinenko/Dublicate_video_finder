import csv
import uuid

from database import add_video, close_session

def add_videos_from_csv():

    file_name = "train.csv"

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        count_row = len(rows)
        print(f"Чтение из {file_name}, кол-во строк: {count_row}")
        for row in rows:
            print(f"{reader.line_num} из {count_row}")
            add_video(UUID=uuid.UUID(row[1]), upload_date=row[0], is_duplicate=row[3], is_hard=row[5])

        close_session()