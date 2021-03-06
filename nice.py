from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
		'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
		'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
		"""Home page."""

		return """
		<!doctype html>
		<html>
			<head>
				<title>Hi There!</title>
			</head>
			<body>
				<h1>Hi! This is the home page.</h1>
				<a href="/hello">Hello link</a>

			</body>
		</html>
		"""

@app.route('/hello')
def say_hello():
		"""Say hello and prompt for user's name."""

		command_list = []
		for each in AWESOMENESS:
				line = "<input type='radio' name= 'comp_radio' value='" + each + "'>" + each
				command_list.append(line)
		middle_part_html = "".join(command_list)        
			

		return """
		<!doctype html>
		<html>
			<head>
				<title>Hi There!</title>
			</head>
			<body>
				<h1>Hi There!</h1>
				<form action="/greet">
					<label>What's your name? <input type="text" name="person"></label>
					<input type="submit">
			 </form>
       <form>
       {}
       </form>
			</body>
		</html>
		""".format(middle_part_html)


@app.route('/greet')
def greet_person():
		"""Get user by name."""

		player = request.args.get("person")

		compliment = choice(AWESOMENESS)

		return """
		<!doctype html>
		<html>
			<head>
				<title>A Compliment</title>
			</head>
			<body>
				Hi %s I think you're %s!
			</body>
		</html>
		""" % (player, compliment)


if __name__ == '__main__':
		# debug=True gives us error messages in the browser and also "reloads"
		# our web app if we change the code.
		app.run(debug=True)
