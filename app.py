from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home():
    import pandas as pd
    df = pd.read_excel('https://github.com/PolisenoRiccardo/perilPopolo/blob/main/milano_housing_02_2_23.xlsx?raw=true')
    return render_template('home.html', lista = c)



@app.route('/esercizio1',methods = ["GET"])
def esercizio1():
   import pandas as pd
   df = pd.read_excel('https://github.com/PolisenoRiccardo/perilPopolo/blob/main/milano_housing_02_2_23.xlsx?raw=true')
   quartiere = request.args.get('quartiere')
   df[df["neighborhood"] == quartiere]

   return render_template('esercizio1.html', tabella = tabella)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)