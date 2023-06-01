from flask import Flask, jsonify, render_template
from flask import request
from video_downlode import *
from summarizer import *

app = Flask(__name__)
temp = ""
i=0


@app.route('/',methods = ['POST', 'GET'])
def hello():
    if request.method == 'POST':
      global i
      if i==1:
        result = temp  #link
        Download(result)
      else:
        result = request.form['vd']
        Download(result)
      
      i=0
      return render_template("index.html", name="hey")
    
    else:
        return render_template("index.html", name="hey")


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      global i
      i=1
      result = request.form['link'] #link
      global temp
      temp = result
      
      top_n = request.form['top_n'] #top_n

      result = result.split("=", 1)[1] #video id
      summary_and_subs = generate_summary(result, int(top_n))
      return render_template("result.html", result=summary_and_subs)
   



if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8081, debug=True)