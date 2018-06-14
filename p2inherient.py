from flask import Flask,render_template

app=Flask(__name__,template_folder='template')

@app.route("/")

def index():
    user={'username':'Ei Mon Theint'}
    posts=[
            {
                'author':{'username':'ChitNaing(Psycho)'},
                'body':'Beautiful day in Yangon!'
            },
            {
                'author':{'username':'MgAyeKo(PaungTi)'},
                'body':'Shoud read book-TaMeLayPhatPho'
            }
    ]

    return render_template('p2base.html',title='sweetHome',user=user,posts=posts)

if __name__=="__main__":
    app.run(debug=True)
