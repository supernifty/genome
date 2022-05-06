#!/usr/bin/env python

import csv

import flask

import proxy

app = flask.Flask(__name__, template_folder='templates')
app.wsgi_app = proxy.ReverseProxied(app.wsgi_app)
app.config.from_pyfile('config.py')
app.secret_key = 'ducks in space'

@app.route('/', methods=['GET'])
def main():
  return flask.render_template('main.html')

@app.route('/tx', methods=['GET', 'POST'])
def tx():
  # json
  rows = []
  for r in csv.DictReader(open('static/tx.tsv', 'rt'), delimiter='\t'):
    rows.append([r['gene'], r['tx'], r['chrom'], r['txstart'], r['txend'], r['genome']])
  return flask.jsonify(data=rows)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=4321)
