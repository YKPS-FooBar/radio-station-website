from radio import db


class Song(db.Model):
    """The database for songs."""

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    file_name = db.Column(db.String(80), nullable=True)

    def __init__(self, name, start_time, file_name=None):
        self.name = name
        self.start_time = start_time
        self.file_name = file_name


db.create_all()
