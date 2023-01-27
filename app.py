from flask import Flask, render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
import requests
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///avengers.sqlite3'
db = SQLAlchemy()
db.init_app(app)

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    history = db.Column(db.String)
    picture = db.Column(db.String)
    
    def __init__ (self,name,history,picture):
        self.name = name
        self.history = history
        self.picture = picture


class Heros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    heros = db.Column(db.String,default='Você ainda não selecionou nenhum herói')
    
    def __init__ (self,username,heros):
        self.username = username
        self.heros = heros


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    def __init__ (self,username):
        self.username = username


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    heros = Hero.query.all()
    return render_template('index.html',hero=heros)


@app.route("/<string:username>",methods=['GET','POST'])
def logado(username):
    heros = Hero.query.all()
    if request.method == 'POST':
        perfil = request.form['name']
        if perfil == 'Perfil':
            return redirect(f'/user/{username}')

        else:
            select= Heros(username,request.form['name'])
            print(type(perfil))
            db.session.add(select)
            db.session.commit()
    return render_template('indexlog.html',hero=heros,username=username)


@app.route("/user/login")
def login():
    return render_template('login.html')


@app.route("/user/<string:username>",methods=['GET','POST'])
def usertemple(username):
    if request.method == 'POST':
        name = request.form['apagar']
        apagar = db.session.query(Heros).filter(Heros.heros==name).filter(Heros.username==username).first()
        db.session.delete(apagar)
        db.session.commit()

    heros = db.session.query(Heros).filter(Heros.username==username).all()
    heroi = []
    if len(heros) < 0:
        heroi.append('Você ainda não selecionou nenhum heroi')
    for hero in heros:
        heroi.append(db.session.query(Hero).filter(Hero.name==hero.heros).first())
    return render_template('user.html',user=username,heros=heroi)



@app.route("/user",methods=['POST','GET'])
def usertempl():
    if request.method == 'POST':
        name=request.form['username']
        comp = db.session.query(User).filter(User.username==name).first()
        comp2 = comp.username
        if (name in comp2):
            return redirect(f'/user/{name}')

    return redirect('/')


@app.route('/edit/<string:username>/<int:id>',methods=['GET','POST'])
def edit(username,id):
    heroedit = Hero.query.get(id)
    if request.method == 'POST':
        heroedit.history= request.form['history']
        db.session.commit()
        return redirect(f'/{username}')
    return render_template('edit.html',edit=id,hero=heroedit)


@app.route("/<string:username>/add",methods=['GET','POST'])
def add(username):
    if request.method == 'POST':
        name = request.form["name"]
        busca = db.session.query(Hero).filter(Hero.name==search).all()
        print(name)
        return redirect(f'/{username}')
    
    
    else:
         return redirect(f'/{username}')


@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        verificar = User.query.all()
        for name in verificar:
            nome = name.username
            if user == nome:
                status='Usuario já existe'
                return render_template('register.html',status=status)
        add = User(user)
        db.session.add(add)
        db.session.commit()
        return redirect(f'/{user}')


    else:
        status = ''
        return render_template('register.html',status=status)


@app.route('/busca/<string:username>',methods=["POST"])
def Search(username):
    search = request.form["name"]
    busca = db.session.query(Hero).filter(Hero.name==search).all()
    return render_template('results.html',username=username,hero = busca)


if __name__ == '__main__':
    app.run()