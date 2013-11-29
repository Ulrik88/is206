import webapp2
import cgi
import string

def escape_html(s):
    return cgi.escape(s, quote = True)

form="""
<form method="post">
    <H1>Min rot13</h1>
    <br>
    <textarea rows="4" cols="50" name="text">%(rot13)s</textarea>
    <br>
    <br>
    <input type="submit">
</form>
"""

def rot13_function(st):
    tab1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tab2 = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    tab = string.maketrans(tab1, tab2)
    return str(st).translate(tab)

class MainPage(webapp2.RequestHandler):
	def write_form(self,message):
		self.response.out.write(form % {"rot13": escape_html(message)})

	def get(self):
		self.write_form("")

	def post(self):
		textarea_text = self.request.get('text')
		rot13 = rot13_function(textarea_text)
		self.write_form(rot13)

application = webapp2.WSGIApplication([('/', MainPage)], debug=True)