from flask import Flask, render_template, redirect, url_for, request

from wtforms import Form,validators,StringField


import Process

app = Flask(__name__)

class UploadBlog(Form):
    title = StringField('Title', [validators.Length(min=1, max=150), validators.DataRequired()])
    subtitle = StringField('Subtitle', [validators.Length(min=1, max=150), validators.DataRequired()])
    content = StringField('Content', [validators.Length(min=1, max=150), validators.DataRequired()])
    author=StringField('Author', [validators.Length(min=1, max=150), validators.DataRequired()])

@app.route('/login', methods=['GET', 'POST'])
def loginpage():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/home'))
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/profiling')
def profiling():
    return render_template('profiling.html')

@app.route('/blog_content')
def blogcontent():
    blogList = Process.processBlog()
    return render_template('blog_content.html',contents=blogList, count=len(blogList))

@app.route('/add_content')
def addcontent():
    form = UploadBlog(request.form)
    if request.method == 'POST' and form.validate():
        Process.uploadBlog(form.title.data, form.subtitle.data, form.content.data,form.author.data)
        print(" Successfully Post Blog")
    return render_template('add_content.html')


if __name__ == '__main__':
    app.run()
