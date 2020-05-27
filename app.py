import flask
from flask import jsonify

app = flask.Flask(__name__)

@app.route('/api/feature_flags/', methods=['GET'])
def feature_flags():
  feature_flags = {
      "restful_response": True,
      "block_info": True,
  }
  return jsonify(feature_flags)

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
  app.run()