from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)