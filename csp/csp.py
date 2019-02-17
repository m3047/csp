#!/usr/bin/python3
# Copyright (c) 2019 by Fred Morris Tacoma WA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Content Security Policy (CSP) Proof of Concept

Demonstrates abuse of CSP to audit web browser behavior.
"""

import json
from flask import Flask, request, render_template, Response
from werkzeug import Headers

app = Flask(__name__)

@app.route('/',methods=['GET'])
def page():
    """This is the web page enforcing the security policy."""
    # Add a Content-Security-Policy-Report-Only: header.
    resp = Response()
    resp.headers.add('Content-Security-Policy-Report-Only',
                     'default-src does-not-exist.m3047; report-uri /csp/report'
                    )
    resp.set_data(render_template('csp.html'))
    return resp
  
@app.route('/report',methods=['POST'])
def report():
    """This is where the report gets posted."""
    # Open the logfile and append the data to it.
    f = open('../data/log.json','a')
    # force= is necessary because the mime type is application/csp-report
    f.write(json.dumps(request.get_json(force=True)) + "\n")
    f.close()
    # Ok, good to go! Really no way to report anything anyway.
    resp = Response()
    resp.status = 'No content'
    resp.status_code = 204
    return resp

if __name__ == "__main__":
    app.run()

