from flask import Flask
from flask import url_for, render_template, request, redirect
import markovify
import os
import nltk
import json

#Чисто теоретически, можно сохранить модель в json и каждый раз использовать уже сгенерированную модель,
#но на практике оказалось, что доставать фразы из уже сохраненной модели дольше, чем генерировать каждый раз.

#corpus = open("GP.txt").read()
#text_model = markovify.Text(text, state_size=3)
#model_json = text_model.to_json()

#with open('model.json','w', encoding='utf-8') as outfile:
#    json.dump(model_json ,outfile)
#with open('model.json') as file_json:
#    model_json = json.load(file_json)
#    reconstituted_model = markovify.Text.from_json(model_json)


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
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



#можно еще улучшить качество генерируемых предложений
#но это ОЧЕНЬ долго

#class POSifiedText(markovify.Text):
#   def word_split(self, sentence):
#        words = re.split(self.word_split_pattern, sentence)
#        words = [ "::".join(tag) for tag in nltk.pos_tag(words) ]
#        return words
#   def word_join(self, words):
#        sentence = " ".join(word.split("::")[0] for word in words)
#        return sentence