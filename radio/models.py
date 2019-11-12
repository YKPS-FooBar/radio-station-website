from radio import db


class Song(db.Model):
    """The database for songs."""

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    song = db.Column(db.String(80), nullable=False)
    slot = db.Column(db.DateTime, nullable=False)
    file_name = db.Column(db.String(80), nullable=True)

    def __init__(self, song, slot, file_name=None):
        self.song = song
        self.slot = slot
        self.file_name = file_name


db.create_all()
