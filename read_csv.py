import csv
import uuid

from database import add_video, close_session

def add_videos_from_csv():

    file_name = "train.csv"

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        rows.pop(0)

        count_row = len(rows)

        n = 1

        print(f"Чтение из {file_name}, кол-во строк: {count_row}")
        for row in rows:
            print(f"{n} из {count_row}")
            #print(f"uuid {row[1]}\nupload {row[0]}\ndupl {row[3]}\nhard {row[5]}")
            add_video(UUID=uuid.UUID(row[1]), upload_date=row[0], is_dupl=row[3], is_hard=row[5])
            n+=1

        close_session()