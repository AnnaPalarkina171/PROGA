from flask import Flask
import csv
import os
import json
from flask import url_for, render_template, request, redirect

app = Flask(__name__)

colors = ["coral", "aqua", "blueviolet", "deepskyblue", "hotpink", "blue", "chartreuse", "tomato", "brown"]
cwd = os.getcwd()
names_files = []

@app.route('/main')
def main():
    urls = {
        'Main': url_for('main'),
        'Form': url_for('form'),
        'Statistics': url_for('stats'),
        'Json': url_for('json'),
        'Search': url_for('search')
    }
    return render_template('main.html', urls=urls)


@app.route('/')
def form():
    urls = {
        'Main': url_for('main'),
        'Form': url_for('form'),
        'Statistics': url_for('stats'),
        'Json': url_for('json'),
        'Search': url_for('search')
    }
    if request.args:
        language = request.args['language']
        gender = request.args['gender']
        lg = '\\' + language + '.' + gender + '.csv'
        name = cwd + lg
        if os.path.exists(cwd + '\\' + 'names.csv') is True:
            with open('names.csv', 'a', encoding='utf-8') as n:
                text = n.read()
                text = text.split(',')
                for file in text:
                    if file != '':
                        if file != name:
                            n.write(name)
                            n.write(',')
        else:
            with open('names.csv', 'a', encoding='utf-8') as n:
                n.write(name)
        with open(name, 'a', encoding='utf-8') as f:
            for c in colors:
                color = request.args[c]
                f.write(color)
                f.write(',')
            f.write('\n')
        return redirect('/main')
    return render_template('form.html', urls=urls)


@app.route('/stats')
def stats():
    content = []
    urls = {
        'Main': url_for('main'),
        'Form': url_for('form'),
        'Statistics': url_for('stats'),
        'Json': url_for('json'),
        'Search': url_for('search')
    }
    with open('names.csv', 'r', encoding='utf-8') as n:
        n = n.read()
        names = n.split(',')
        for name in names:
            if name != '':
                with open(name, 'r', encoding='utf-8') as f:
                    cont = f.read().split('\n')
                    content.append(cont)
    return render_template('stats.html', urls=urls, content=content)


@app.route('/json')
def json():
    urls = {
        'Main': url_for('main'),
        'Form': url_for('form'),
        'Statistics': url_for('stats'),
        'Json': url_for('json'),
        'Search': url_for('search')
    }

    return render_template('json.html', urls=urls)


@app.route('/search')
def search():
    urls = {
        'Main': url_for('main'),
        'Form': url_for('form'),
        'Statistics': url_for('stats'),
        'Json': url_for('json'),
        'Search': url_for('search')
    }
    return render_template('search.html', urls=urls)


if __name__ == '__main__':
    app.run(debug=True)

