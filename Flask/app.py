from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def base_url():
    return "Base Url"

if __name__ == '__main__':
   app.run(debug = True)