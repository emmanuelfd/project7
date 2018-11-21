#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask,request,url_for, redirect, render_template, abort
import module
import json
from flask_cors import CORS
import os
#import logging as lg

#lg.basicConfig(level=lg.DEBUG)

app = Flask(__name__)
CORS(app)




@app.route('/GrandPy', methods=['GET', 'POST'])

def message():
    if request.method == 'POST':

        msg = request.form['msg']#get msg from the POST

        question = module.parsing(msg)

        print("la quest est : " + msg)
        #below question with stopwords removed.
        print(question.new_sentence)

        url_google = question.google()
        print(url_google)
        url_wiki = question.wiki()
        print(url_wiki)
        #lg.warning(url_wiki)
        wiki_description = module.wikipedia(url_wiki)
        print(wiki_description.Pageid)


        dico = {"google": url_google, "wiki": wiki_description.wikiword()}
        json_data = json.dumps(dico)

        return json_data



@app.route('/')
def ajax():
    return render_template('accueil.html', titre="Bienvenue chez GrandPy !")



#############################


if __name__ == '__main__':
    port = int(os.environ.get("PORT",8080))
    app.run(host='0.0.0.0',port=port)
    #app.run(debug=True)