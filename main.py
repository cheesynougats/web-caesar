#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2, caesar

init_page = """
<!DOCTYPE html>
<html>
<head><title>Web Caesar!</title>
</head>
"""

body_page = """
<body>
<form method="POST" action="/">
    <label>Enter some text to encrypt
        <textarea id="input">%(encrypted)s</textarea>
    </label>
    <br />
    <label>Enter number of letters to rotate
        <input type="text" value="%(number)s" />
    </label>
    <br />
    <label>Click 'Submit' to go ahead and encrypt!
        <input type="submit" />
    </label>
</form>
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("<textarea>" + caesar.encrypt("Hello, world!", 2) + "</textarea>")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
