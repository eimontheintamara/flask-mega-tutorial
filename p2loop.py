from flask import Flask,render_template

app=Flask(__name__,template_folder='template')

@app.route("/")
def index():
    user={'username':'Ei Mon Theint'}
    posts=[
            {
                'author':{'username':'Jue'},
                'body':'Beautiful day in Myanmar!'
            },
            {
                'author':{'username':'La Min Mo Mo'},
                'body':'The Advengers movie was so cool!'
            }
        ]

    return render_template('p2loop.html',title='Home',user=user,posts=posts)

if __name__ == "__main__":
    app.run(debug=True)


