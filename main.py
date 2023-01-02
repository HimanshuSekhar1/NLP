from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
# __name__ is the module where flask will look for templates and instances
app = Flask(__name__)
app.config['SECRET_KEY'] = 'aca09cd8b623490e5e8ef906b5072c6e'

# These will be the data inside the website
projects = [
  {
    'title': 'Marine Bioplastics',
    'content': 'This is a project for marine bioplastics in the ocean.',
    'date_posted': '29 December 2022',
    'link': 'https://github.com/HimanshuSekhar1/Marine-Microplastics'
  },

  {
    'title': 'The Sharpe Ratio',
    'content': 'This is a project for sharpe ratio for the stocks of Facebook and Amazon.',
    'date_posted': '30 December 2022'
  },
]

# Routes to different pages of the site
# Here two app routes will help in going to the same page with two links 
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = projects)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

# Routes to the registration from and login form
@app.route('/register', methods = ['GET', 'POST'])
def register():
  form = RegistrationForm()
  # validate on submit will check the validity of the requests we send in registration form
  if form.validate_on_submit():
    # This will give a flash message that a user is created or not
    # f is for the f string
    flash(f'Account created for {form.username.data}!','success')
    return redirect(url_for('home'))
  return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'abc@q.com' and form.password.data == '12345':
      flash('You have been logged in!','success')
      return redirect(url_for('home'))
    else:
      flash('Login unsuccessful. Please check email and password.', 'danger')
  return render_template('login.html', title = 'Log In', form = form)
  
# Used to run the app
app.run(host='0.0.0.0', port=81, debug=True)