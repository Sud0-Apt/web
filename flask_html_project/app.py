# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
