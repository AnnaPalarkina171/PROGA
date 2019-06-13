from flask import Flask
from flask import url_for, render_template, request, redirect
import markovify


# Print three randomly-generated sentences of no more than 140 characters
#for i in range(3):
#    print(text_model.make_short_sentence(140))


app = Flask(__name__)

@app.route('/')
def index():
    urls = {'главная (эта страница)': url_for('index'),
            }
    # Get raw text as string.
    with open('GP.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    # Build the model.
        text_model = markovify.Text(text, state_size=3)

    # Print five randomly-generated sentences
    for i in range(1):
        sentence = text_model.make_sentence()
        #if request.args['shft'] == '\n':
            #return render_template('index.html', urls=urls, sentence=sentence)
    return render_template('index.html', urls=urls, sentence=sentence)


if __name__ == '__main__':
    app.run(debug=False)