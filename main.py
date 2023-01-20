from flask import Flask, render_template,request, url_for, flash, redirect

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def main():
    if request.method == 'POST':
       query = request.form['query']
       answer = generateAnswer(query)
       return render_template('dashboard.html',answer=answer)
    else:
        return render_template('home.html')
