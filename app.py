from flask import Flask, request, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story
from flask import flash, get_flashed_messages

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def ask_quesiton():
    """Generate and show from to ask words"""

    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)

@app.route("/story")
def show_story():
    """Show story results"""

    text = story.generate(request.args)

    return render_template("story.html", text=text)