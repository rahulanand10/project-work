from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/malaria')
def malaria():
    return render_template('malaria.html')

@app.route('/glaucoma')
def glaucoma():
    return render_template('glaucoma.html')

@app.route('/cancer')
def cancer():
    return render_template('cancer.html')

@app.route('/mp',methods=["GET","POST"])
def positive():
    return render_template('malaria_positive.html')

@app.route('/mn',methods=["GET","POST"])
def negative():
    return render_template('malaria_negative.html')

@app.route('/city',methods=["GET","POST"])
def city():
    return render_template('city.html')

@app.route('/cd',methods=["GET","POST"])
def city_delhi():
    return render_template('delhi_malaria.html')

app.run(debug=True)