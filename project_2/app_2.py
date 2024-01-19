from flask import Flask, request, Response, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Отключаем отслеживание изменений
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(12), nullable=False)

@app.route('/')
def index():
    # Рендерим шаблон вместо чтения файла
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    name = request.form.get('name')
    phone = request.form.get('phone')

    user = User(name=name, phone=phone)
    db.session.add(user)
    db.session.commit()

    # Используем render_template для отображения сообщения
    return render_template('message.html', message=f'Спасибо, {name}! Ваш номер телефона ({phone}) сохранен в базе данных.')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000, host='0.0.0.0')





