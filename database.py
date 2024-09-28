from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

engine = create_engine("postgresql://hacksai:qwerty1221777@localhost:5432/hacksdb")


Session = sessionmaker(bind=engine)
session = Session()


def add_video(UUID, upload_date: str, content_hash: str, is_duplicate: bool, duplicate_for: str, is_hard: bool):
    video = models.Video(uuid=UUID,
                         upload_date=upload_date,
                         content_hash=content_hash,
                         is_duplicate=is_duplicate,
                         duplicate_for=duplicate_for,
                         is_hard=is_hard)
    session.add(video)
    session.commit()
    session.close()



