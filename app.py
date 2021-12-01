from flask import Flask, request
import time
import statistics

app = Flask(__name__)

@app.route('/mean', methods=['GET', 'POST'])
def mean():

    liste = request.args.getlist('liste', type=int)
    result = statistics.mean(liste)
    return ("The mean of the list {}  is : {}".format(liste, result))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)