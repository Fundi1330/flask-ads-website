from flask import Flask, render_template
from app.models import db, Ads
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.app_context().push()

db.init_app(app)

migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html', title='Home')

@app.route('/pop-corners', methods=['GET'])
def popcorners():
    popcorners = Ads.query.filter_by(id=1).first()
    return render_template('pop-corners.html', title='Pop Corners', popcorners=popcorners)

@app.route('/heinz-ketchup', methods=['GET'])
def heinz():
    heinz = Ads.query.filter_by(id=2).first()
    return render_template('heinz.html', title='Heinz Ketchup', heinz=heinz)

@app.route('/monobank', methods=['GET'])
def monobank():
    monobank = Ads.query.filter_by(id=3).first()
    return render_template('mono-bank.html', title='Mono bank', monobank=monobank)