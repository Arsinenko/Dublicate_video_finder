import csv
import uuid

from database import add_video, close_session

def add_videos_from_csv():
    with open("train.csv", "r") as file:
        reader = csv.reader(file)
        count_row = len(list(reader))
        print("чтение из train.csv")
        for row in reader:

            # print("uuid:" + row[1])
            # print("upload_date:" + row[0])
            # print("")
            print(reader.line_num + f" из {count_row}")
            add_video(UUID=uuid.UUID(row[1]), upload_date=row[0], is_duplicate=row[3], is_hard=row[5])

        close_session()