# from flask import Flask, request, render_template
from flask import Flask, render_template,request
import requests

def blackbox(method, url, json=None):
    #input must be generalized to pass `n` inputs to method
    res = requests.request(method=method, url=url, json=json)
    return res.text

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/')
@app.route('/')
def root():
    return render_template("index.html")
    # return app.send_static_file('index.html')

@app.route('/exec', methods=["POST"])
def amin():
    args = request.form
    if args.get("payload")== None:
        res =  blackbox(request.args.get("method"), request.args.get("url"))
    else:
        res =  blackbox(args["method"], args["url"],args["payload"]), 200
    print(res)
    return str(res[0]),int(res[1])

        
if __name__ == "__main__":
    app.run(debug=True)
# tests
# url exist
# method exiron
# method dne
# json dne
# json e
# url ne