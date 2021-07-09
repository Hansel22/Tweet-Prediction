from flask import Flask, escape, request, render_template
import pickle


model = pickle.load(open("disaster.sav", 'rb'))

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method =="POST":
        
        lis = []
        lis.append(request.form['text'])
        ans = model.predict([lis[0].lower()])
        result='Not Disaster'
        if ans==1:
            result='Disaster'
        else:
            result='Not Disaster'
        for i in lis:        
            return render_template("result.html",ans="{}".format(result),text="{}".format(i))
    else:
        return render_template("index.html")
    

if __name__ == "__main__":
    app.run(debug=True)