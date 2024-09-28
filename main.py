import uuid

from converter import  hash_bytearray_to_hashes_array
from compare import compare_hashes


from database import add_video, get_videos
from read_csv import add_videos_from_csv
# add_video(UUID=uuid.UUID('45e3ed7b-dc38-4717-8262-1fee5f8fb263'),
#           upload_date='2024-07-30 00:45:36',
#           content_hash=get_hash("https://s3.ritm.media/yappy-db-duplicates/45e3ed7b-dc38-4717-8262-1fee5f8fb263.mp4"),
#           is_duplicate=False,
#           duplicate_for=None,
#           is_hard=False,)

def is_duplicate(videohashes):
    videos = get_videos()
    for video in videos:
        hashes_to_compare = hash_bytearray_to_hashes_array(video.content_hash)
        result = compare_hashes(hashes_to_compare, videohashes)
        if result:
            return (True, video.uuid)
    return (False, None)

if __name__ == "__main__":
    add_videos_from_csv()

# testhash = hash_bytearray_to_hashes_array(get_hash("https://s3.ritm.media/yappy-db-duplicates/34502a8b-b45a-46e0-a3d6-a8561615f48b.mp4"))
# print(is_duplicate(testhash))
