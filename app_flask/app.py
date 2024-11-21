from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import psycopg2
import random

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class Article(db.Model):
    """создаем класс модель базы данных."""
    id = db.Column(db.Integer, primary_key=True)
    name_car = db.Column(db.String(100), nullable=True)
    age_car = db.Column(db.String(300), nullable=True)
    mileage_car = db.Column(db.String(300), nullable=True)
    price_car = db.Column(db.INT(), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        # то как обьект будет отоброжаться
        return f"{self.id}: {self.name_car},{self.age}"


@app.route('/')
@app.route('/home')
def index():
    """переход на домашнюю страницу"""
    return render_template('index.html')


@app.route('/create-article', methods=['POST', 'GET'])
def create_article() -> None:
    """получаем данные от пользователя и заносим в БД.
       создаем запись"""
    if request.method == "POST":
        name_car = request.form['name_car']
        age_car = request.form['age_car']
        mileage_car = request.form['mileage_car']
        price_car = request.form['price_car']
        article = Article(name_car=name_car, age_car=age_car,
                          mileage_car=mileage_car, price_car=price_car)

        try:
            print('вход в sesion')
            db.session.add(article)
            print('session good !!!!!!!!!!!!!!!!')
            db.session.commit()
            return redirect('/')
        except:
            return 'ошибка при добавлении статьи'
    else:
        return render_template('creaete-arcticle.html')


@app.route('/posts/<int:id>/update', methods=['POST', 'GET'])
def post_update(id):
    """обновляем данные записи"""
    article = Article.query.get(id)
    if request.method == "POST":
        article.name_car = request.form['name_car']
        article.age_car = request.form['age_car']
        article.mileage_car = request.form['mileage_car']
        article.price_car = request.form['price_car']

        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return 'ошибка при добавлении статьи'
    else:
        return render_template('posts_update.html', article=article)




@app.route('/posts')
def posts():
    """инофрмация о всех постах"""
    articles = Article.query.order_by(Article.date.desc()).all()
    return render_template('posts.html', articles=articles)


@app.route('/posts/<int:id>')
def posts_detail(id):
    """карточка обьявления со всей информацией """
    articles = Article.query.get(id)
    return render_template('posts_detail.html', articles=articles)


@app.route('/posts/<int:id>/delete')
def posts_delete(id):
    """удаляем пост"""
    articles = Article.query.get_or_404(id)

    try:
        db.session.delete(articles)
        db.session.commit()
        return redirect('/posts')
    except:
        return 'ошибка при удалении поста'


if __name__ == "__main__":
    random_port = random.randint(5000, 9999)
    app.run(debug=True, port=random_port)
