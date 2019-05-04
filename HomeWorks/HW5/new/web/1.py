from flask import Flask
from flask import url_for, render_template, request, redirect
import requests
import os
app = Flask(__name__)

@app.route('/')
def search():
    if request.args:
        req = request.args['request']
        with open('name.txt','w',encoding='utf-8') as f:
            f.write(req)
        os.system(r'C:\\Users\\User\\Desktop\\mystem.exe -cdgin --format xml --eng-gr {} {}'.format('name.txt', 'name.xml'))
        return redirect('/examples')
    return render_template('search.html')

@app.route('/examples')
def examples():
    return render_template('examples.html')


if __name__ == '__main__':
    app.run(debug=True)