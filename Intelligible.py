from flask import Flask, render_template, request
import dale
import flesch_kincaid
import gunning_fog
import smog
import sys
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')


@app.route('/hello', methods=['POST'])
def hello():
    para = request.form['para']
    d=dale.dale_chall_r(str(para))
    fks=flesch_kincaid.flesch_kincaid_score_r(str(para))
    fkg=flesch_kincaid.flesch_kincaid_grade_r(str(para))
    gf=gunning_fog.gunning_fog_grade_r(str(para))
    sm=smog.smog_grade_r(str(para))
    return render_template("result.html", d=d , fks=fks , fkg=fkg , gf=gf ,sm=sm , para=para )

if __name__ == '__main__':
    app.run(debug=True)