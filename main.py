import cv2
import imagehash
from PIL import Image
import psycopg2
import asyncio


class DB:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname="dbname this",
                user="username this",
                password="password this",
                host="host this",
                port="port this"
            )
        except Exception as e:
            print("Connection error:" + str(e))

    def close(self):
        if self.connection is not None:
            self.cursor.close()
            self.connection.close()
        else:
            print("connection doesn't exist")

    def add_video_url(self, url: str):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute("sql query this")
            self.connection.commit()
        except Exception as e:
            print("add video url error:" + str(e))

    def add_video_hash(self, hash: str):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute("sql query this")
            self.connection.commit()
        except Exception as e:
            print("add video hash error:" + str(e))

    def get_video_hash(self, video_path):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute("sql query this")
            hash = self.cursor.fetchone()
            return hash
        except Exception as e:
            print("get video hash error:" + str(e))

    def get_video_url(self):
        # не знаю нужно ли нам это
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute("sql query this")
            url = self.cursor.fetchone()
            return url
        except Exception as e:
            print("get video url error:" + str(e))


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

            resized_image = cv2.resize(frame, (100, 200))
            gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
            img = Image.fromarray(gray)
            hash1 = imagehash.phash(img, 16)
            result.append(hash1)

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

