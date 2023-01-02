from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
# __name__ is the module where flask will look for templates and instances
app = Flask(__name__)
app.config['SECRET_KEY'] = 'aca09cd8b623490e5e8ef906b5072c6e'

# These will be the data inside the website
projects = [
  {
    'title': 'Marine Bioplastics',
    'content': 'This is an exploratory data analysis of National Oceanic and Atmospheric Adminstration\'s (NOAA) marine microplastics data to know and understand microplastics, their growth rate with respect to various ocean bodies in our planet earth. It involves data cleaning and EDA.',
    'date_posted': '15 December 2022',
    'link': 'https://github.com/HimanshuSekhar1/Marine-Microplastics'
  },

  {
    'title': 'Risk and Returns: The Sharpe Ratio',
    'content': 'This is a project about "The Sharpe Ratio" by calculating it for the stocks of the two tech giants Facebook and Amazon. As benchmark S&P 500 was used that measures the performance of the 500 largest stocks in the US.',
    'date_posted': '5 December 2022',
    'link': 'https://github.com/HimanshuSekhar1/Risk-and-Returns-The-Sharpe-Ratio'
  },

  {
    'title': 'World Developement Indicator',
    'content': 'This is an analysis done for countries on the basis of World Developement Indicator which involves data cleaning and visualization.',
    'date_posted': '13 December 2022',
    'link': 'https://github.com/HimanshuSekhar1/World-Development-Indicator'
  },
  {
    'title': 'CO2 Emissions Canada',
    'content': 'This is a data analysis of Vehicles make in Canada by their CO2 emissions into the environment using python in Jupyter notebooks. Later in the notebook, it consists of bicycle sales data using Microsoft SQL server integretion.',
    'date_posted': '5 December 2022',
    'link': 'https://github.com/HimanshuSekhar1/CO2-emissions-Canada'
  },
  {
    'title': 'Age of Abalone',
    'content': 'This project is about abalone, how their age changes with various physical characteristics and mortality.',
    'date_posted': '7 December 2022',
    'link': 'https://github.com/HimanshuSekhar1/Age-of-Abalone'
  },
  {
    'title': 'Flipkart Web Scraper',
    'content': 'In this project, the web data is scraped from flipkart ecommerce site for a book data. It\'s product name, price and ratings were only scraped out of the web.',
    'date_posted': '10 December 2022',
    'link': 'https://github.com/HimanshuSekhar1/Flipkart-web-scraper'
  },
  {
    'title': 'OYO Rooms Web Scraper',
    'content': 'This is a project to scraped the data of OYO rooms for a particular city and a list of hotels having major popularity.',
    'date_posted': '11 December 2022',
    'link': 'https://github.com/HimanshuSekhar1/OYO-Rooms-Web-scraper'}
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