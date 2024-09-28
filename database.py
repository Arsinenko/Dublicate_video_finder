from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import uuid

import models
from converter import hash_bytearray_to_hashes_array
from video_hash import get_hash
from compare import compare_hashes

engine = create_engine("postgresql://hacksai:qwerty1221777@localhost:5432/hacksdb")


Session = sessionmaker(bind=engine)
session = Session()

def is_duplicate(videohashes):
    videos = get_videos()
    for video in videos:
        hashes_to_compare = hash_bytearray_to_hashes_array(video.content_hash)
        result = compare_hashes(hashes_to_compare, videohashes)
        if result:
            return (True, video.uuid)
    return (False, None)


def add_video(UUID, upload_date: str, is_dupl: bool, is_hard: bool):
    print("hash")
    video_hash = get_hash(f"https://s3.ritm.media/yappy-db-duplicates/{UUID}.mp4")
    print("delection")
    alg_detection, duplicate_for = is_duplicate(hash_bytearray_to_hashes_array(video_hash))

    #print(alg_detection, is_dupl)
    if alg_detection != is_dupl:
        input(f"Несоответствие: алгоритм: {alg_detection} тестовые данные: {is_dupl} {UUID}")

    print("add to db")
    video = models.Video(uuid=UUID,
                         upload_date=upload_date,
                         content_hash=video_hash,
                         is_duplicate=alg_detection,
                         duplicate_for=duplicate_for,
                         is_hard=is_hard)
    session.add(video)
    session.commit()

def close_session():
    session.close()

def get_videos():
    videos = session.query(models.Video).all()
    return videos
