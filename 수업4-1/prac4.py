from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/yourpage')
def yourpage():
   return 'This is your page!'

if __name__ == '__main__':
   app.run('localhost',port=5000,debug=True)