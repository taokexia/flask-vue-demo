#coding: utf-8
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
	return jsonify(ok=True, data='hello, world')
	
if __name__ == '__main__':
	app.run()