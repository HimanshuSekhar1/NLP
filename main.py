from flask import Flask, render_template, url_for
# __name__ is the module where flask will look for templates and instances
app = Flask(__name__)

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
  
# Used to run the app
app.run(host='0.0.0.0', port=81, debug=True)