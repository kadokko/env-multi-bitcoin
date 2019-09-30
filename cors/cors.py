import os
import json
import requests
from flask import Flask, jsonify, make_response
from flask import request
from flask import abort
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


class RpcProxy:

  def __init__(self, url):
    self.url = url
    self.session = requests.Session()

  def post(self, auth, method, *params):
    headers = {'content-type': 'application/json', 'Authorization': auth}
    body = json.dumps({"method": method, "params": list(params), "jsonrpc": "2.0"})
    try:
      response = self.session.post(self.url, headers=headers, data=body)
    except requests.exceptions.ConnectionError:
      raise Exception('failed to connect for rpc server.')

    res = response.json()
    if response.status_code != 200:
      if 'error' in res and res['error'] is not None:
        err = res['error']
        raise RpcException(err['code'], err['message'])
      raise Exception('an error occured.')

    return res['result']


class RpcException(Exception):

  def __init__(self, code, message):
    self.code = code
    self.message = message


@app.route("/rpc", methods=['POST'])
def transfer():
  req = request.get_json()
  url = os.getenv('RPC_URL')
  auth = request.headers.get('Authorization')
  try:
    res = RpcProxy(url).post(auth, req['method'], *req['params'])
    return make_response(jsonify({ "data": res }))
  except RpcException as e:
    abort(500, {
      'code': e.code,
      'message': e.message,
    })

@app.errorhandler(500)
def errorhandler(error):
  response = jsonify({
    'code': error.description['code'],
    'message': error.description['message']
  })
  return response, 500


if __name__ == '__main__':
  app.run(
    host="0.0.0.0",
    debug=False
  )
