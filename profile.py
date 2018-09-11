from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def display_home():
    return render_template('home.html', the_title="Home | Chanwoo")

@app.route("/about-me")
def display_aboutMe():
	return render_template('about-me.html', the_title="About Me | Chanwoo")

@app.route("/projects")
def display_projects():
	return render_template('projects.html', the_title="Projects | Chanwoo")

if __name__ == '__main__':
	app.run()
