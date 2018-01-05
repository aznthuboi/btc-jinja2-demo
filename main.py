from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=['GET'])
def btc():
    r = requests.get(
        'https://api.coindesk.com/v1/bpi/currentprice.json')
    # dictionary
    s = r.json()['bpi']['USD']['rate']
    # render #1
    return render_template('index.html', s=s)

@app.route("/history", methods=['GET'])
def btc_history():
    r1 = requests.get(
        'https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-12-0')
    # dictionary
    history = r1.json()['bpi']
    # render #1
    r2 = (['Date {}, Price {}'.format(i, history.get(i)) for i in history])
    return render_template('index.html', r2=r2)



if __name__ == '__main__':
    app.run()
