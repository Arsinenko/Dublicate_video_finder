from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


import models

engine = create_engine("postgresql://hacksai:qwerty1221777@localhost:5432/hacksdb")


Session = sessionmaker(bind=engine)
session = Session()


def add_video(UUID, upload_date: str, content_hash, is_duplicate_fromcsv, is_hard: bool):
    videohash = hash_bytearray_to_hashes_array(get_hash(f"https://s3.ritm.media/yappy-db-duplicates/{UUID}.mp4"))
    is_dup, dup_for = is_duplicate(videohash)

    print(str(is_dup) + " " + str(is_duplicate_fromcsv))

    video = models.Video(uuid=UUID,
                         upload_date=upload_date,
                         content_hash=content_hash,
                         is_duplicate=is_dup,
                         duplicate_for=dup_for,
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



