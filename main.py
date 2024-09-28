import uuid

import cv2
from PIL import Image, ImageOps
import imagehash
from converter import hash_to_bytearray, bytearray_to_hash, hash_bytearray_to_hashes_array
from compare import compare_hashes
w, h = 100, 200

def get_hash(path_to_file):
    capture = cv2.VideoCapture(path_to_file)
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

    result = bytearray()

    for i in range(0, int(length)):
        if i % fps != 0:
            capture.grab()
        else:
            success, frame = capture.read()

            resized_image = cv2.resize(frame, (w, h))
            gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

            img = Image.fromarray(gray)
            img_hor = ImageOps.mirror(img)

            blended_hor = Image.blend(img, img_hor, alpha=0.5)
            img_ver = ImageOps.flip(blended_hor)

            blended_ver = Image.blend(blended_hor, img_ver, alpha=0.5)
            cropped = blended_ver.crop((0, 0, w / 2, h / 2))

            hash1 = imagehash.phash(cropped, 16)
            result.extend(hash_to_bytearray(hash1))


    capture.release()
    return result



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
