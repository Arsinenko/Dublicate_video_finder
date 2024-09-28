from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import uuid

import models
from converter import hash_bytearray_to_hashes_array
from main import get_hash

engine = create_engine("postgresql://hacksai:qwerty1221777@localhost:5432/hacksdb")


Session = sessionmaker(bind=engine)
session = Session()


def add_video(UUID, upload_date: str, content_hash: str, is_duplicate: bool, is_hard: bool):
    video_hash = hash_bytearray_to_hashes_array(
        get_hash(f"https://s3.ritm.media/yappy-db-duplicates/{UUID}.mp4")
    )
    _is_duplicate, duplicate_for = is_duplicate(video_hash)

    print(_is_duplicate, is_duplicate)
    if is_duplicate != is_duplicate:
        input(f"{UUID}")
    video = models.Video(uuid=UUID,
                         upload_date=upload_date,
                         content_hash=content_hash,
                         is_duplicate=is_duplicate,
                         duplicate_for=duplicate_for,
                         is_hard=is_hard)
    session.add(video)
    session.commit()

def close_session():
    session.close()

def get_videos():
    videos = session.query(models.Video).all()
    for elem in videos:
        print(elem.content_hash)
    return videos


def add_videos_from_csv():
    with open("train.csv", "r") as file:
        reader = csv.reader(file)
        count_row = list(reader)
        for row in reader:
            # print("uuid:" + row[1])
            # print("upload_date:" + row[0])
            # print("")
            print(reader.line_num + f" из {count_row}")
            add_video(UUID=uuid.UUID(row[1]), upload_date=row[0], is_duplicate=row[3], is_hard=row[5])

        session.close()


add_videos_from_csv()


