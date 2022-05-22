from . import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    text = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Запись: {self.title}'