import csv
import uuid

from database import add_video, close_session
from video_hash import get_hash

import asyncio

video_urls = []

async def get_hash_task(n, url):
    print(f"Рассчет хэша для видео {n}")
    return get_hash(url)

async def precompute_hashes():
    tasks = []

    n = 1

    for url in video_urls:
        task = asyncio.create_task(get_hash_task(n, url))
        tasks.append(task)
        n+=1

    results = await asyncio.gather(*tasks)
    return results

def add_videos_from_csv():

    file_name = "train.csv"

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        rows.pop(0)

        count_row = len(rows)

        n = 1

        print(f"Рассчет хэшей для видео из {file_name}, кол-во строк: {count_row}")
        for row in rows:
            video_urls.append(row[2])
        print("Ссылки собраны")

        loop = asyncio.get_event_loop()
        results = loop.run_until_complete(precompute_hashes())
)
        print(results[0])

        print(f"Чтение из {file_name}, кол-во строк: {count_row}")
        for row in rows:
            print(f"{n} из {count_row}")
            #print(f"uuid {row[1]}\nupload {row[0]}\ndupl {row[3]}\nhard {row[5]}")
            is_dupl = row[3] == "True"
            is_hard = row[5] == "True"
            add_video(UUID=uuid.UUID(row[1]), upload_date=row[0], is_dupl=is_dupl, is_hard=is_hard)
            n+=1

        close_session()