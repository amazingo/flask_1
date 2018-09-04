from app import create_app

hello_app = create_app()


@hello_app.route('/',methods=['GET','POST'])
def index():
    return '<h1>hello</h1>'





#from flask import Flask

#app = Flask(__name__)

#@app.route('/',methods=['GET','POST'])
#def index():
 #   return render_template('index.html')



#@app.route('/hello')
#def hello_world():
#    return 'Hello World!'

if __name__ == '__main__':
    hello_app.run(debug=True)
