from flask import render_template, Blueprint, request, redirect
from .models import Item
from . import db

from cloudipsp import Api, Checkout

home = Blueprint('home', __name__)


@home.route('/')
def index():
    items = Item.query.order_by(Item.price).all()

    return render_template('index.html', items=items)


@home.route('/buy/<int:id>')
def item_buy(id):
    item = Item.query.get(id)

    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "RUB",
        "amount": str(item.price) + '00'
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)



@home.route('/about')
def about():
    return render_template('about.html')


@home.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        price = request.form.get('price')
        text = request.form.get('text')

        item = Item(title=title, price=price, text=text)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error'
    else:
        return render_template('create.html')
