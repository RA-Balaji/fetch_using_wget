from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='c8ccff7e62552ea2dc78e61338d3054c'

posts=[
    {
        'name':'senna',
        'team':'mclaren',
        'country':'brazil',
        'date':'4/4/20'
    },
     {
        'name':'prost',
        'team':'ferrari',
        'country':'france',
        'date':'6/4/20'
    }
] 

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
   return render_template('about.html', title='chumma')

@app.route('/register', methods=['GET', 'POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
       flash(f'Account created for { form.username.data }', 'success')
       return redirect(url_for('home')) 
   return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
   form = LoginForm()
   return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)