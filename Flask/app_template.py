from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/url/<argument>')
def success(argument):
   return 'welcome %s' % argument

@app.route('/')
def base_url():
    return "Base Url"

@app.route("/post_url",methods=['POST'])
def post_method():
    var1 = request.form.get('var1')

    return "From post URL"

@app.route("/get_url",methods=['GET'])
def get_method():
    var1 = request.args.get("var1")

    return "From Get URL"

if __name__ == '__main__':
   app.run(debug = True)