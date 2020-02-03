#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# [START gae_python37_app]
from flask import Flask, request
from flask import jsonify, render_template, url_for
app = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')
@app.route('/')
def root():
    return render_template('index.html')
# def hello():
#     """Return a friendly HTTP greeting."""
#     return 'Hello I like to make AI Apps'
@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)
@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
