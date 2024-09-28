import cv2
import imagehash
from PIL import Image, ImageOps
import asyncio
from database import DB

base = DB()

w = 100
h = 200

async def get_hash(path_to_file):
    capture = cv2.VideoCapture(path_to_file)
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

    result = []

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
            cropped = blended_ver.crop((0, 0, w/2, h/2))
            
            hash1 = imagehash.phash(cropped, 16)
            result.append(hash1)
            # base.connect()
            # base.add_video_hash(hash1)
            #


    capture.release()
    return result


async def main():
    paths_to_files = ["videos/original.mp4", "videos/dublicate_video.mp4", "videos/video3.mp4"]
    tasks = []

    for path in paths_to_files:
        task = asyncio.create_task(get_hash(path))
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    return results


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main())
    print(results)

# for i in range(0,len(data1)):
#     print(data2[i]-data1[i])

