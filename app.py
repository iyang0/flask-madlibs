from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import STORIES


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def root():
    """base path, asks user for what story they want."""
    return render_template("story_picker.html")

@app.route('/<story>')
def prompt(story):
    """Prompts user for input text of prompts"""
    story_prompts = STORIES[story].prompts

    return render_template(
        "questions.html",
        madlib=story,
        prompts=story_prompts)
        
@app.route('/<story>/results')
def story(story):
    """Generates a story from the input and places it in the DOM"""

    story_answers = request.args
    story_template = STORIES[story].generate(story_answers)

    return render_template(
        "story.html",
        final_story = story_template
        )
