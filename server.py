from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import date, datetime

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)


class Orders(db.Model):
    __table__ = db.Model.metadata.tables['orders']


@app.route('/')
def score():
    first_unfinish = Orders.query.filter(Orders.confirmed.is_(None)).first()
    seconds = round(
        (datetime.now() - first_unfinish.created).total_seconds())
    unfinish_amount = Orders.query.filter(Orders.confirmed.is_(None)).count()
    today_finished = Orders.query.filter(
        func.date(Orders.created) == date.today(),
        Orders.confirmed.isnot(None)).count()
    return render_template('score.html',
                           seconds=seconds,
                           unfinish=unfinish_amount,
                           finished=today_finished)


if __name__ == "__main__":
    app.run()
