# FlaskWebApp1.py
from flask import Flask, redirect, render_template
from flask.helpers import url_for

webapp = Flask(__name__)

@webapp.route("/<name>")
def index(name):
    # 不能干嘛冷的一条redirect语句放在py里面，那样会报错，缺少app context
    # 即前面@webapp.route("/")的声明部分
    if name=="a":
        return redirect(url_for('static', filename='staticHTMLFile.html'))
    elif name=="x":
        return redirect(url_for('xenon'))


@webapp.route("/showname/<name>")
def renderDynamicContent(name=None):
    return render_template('dynamicTemplate1.html', name=name)



@webapp.route("/static", methods=['GET'])
def showStaticFiles():
    return

@webapp.route("/xenon", methods=['GET'])
def xenon():
    #return url_for('xenon', filename='ui-widgets.html')
    return render_template("ui-widgets.html")
"""
@webapp.route("/test", methods=['GET'])

def test():
    return render_template('staticHTMLFile.html')

#redirect(url_for('static',filename='staticHTMLFile.html'))
"""
if __name__ == '__main__':
    webapp.run(debug=True)
