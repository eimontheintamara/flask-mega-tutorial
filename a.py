from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    user={'username':'Ei Mon Theint'}
    return '''
<html>
 <head>
   <title>Home Page- Microblog</title>
 </head>
 <body>
   <h1>Hello and welcome to flask,my dear visitor:, ''' + user['username'] + '''!</h1>
 </body>
</html>'''

if __name__=="__main__":
    app.run(debug=True)

