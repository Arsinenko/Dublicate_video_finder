import psycopg2


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
