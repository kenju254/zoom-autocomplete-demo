from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

builtin_list = list

def init_app(app):
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    db.init_app(app)


def from_sql(row):
    """
    Translates a SQLAlchemy model instance into a dictionary
    """
    data = row.__dict__.copy()
    data['id'] = row.id
    data.pop('_sa_instance_state')
    return data


class Product(db.Model):
    """
    This is the Prouduct List model.
    """
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(255))
    title = db.Column(db.String(255))
    description = db.Column(db.Text())

    def __repr__(self):
        return "<Product(title='%s') >" % (self.title)


def _create_database():
    """
    If this script is run . It creates all the tables and fields necessary to
    run the application.
    """

    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    init_app(app)
    with app.app_context():
        db.create_all()
    print "All tables are created"


if __name__ == '__main__':
    _create_database()
