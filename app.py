from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def root():
    """Prompts user for input text"""
    story_prompts = silly_story.prompts

    return render_template(
        "questions.html",
        prompts=story_prompts)
        
@app.route('/results')
def story():
    """Generates a story from the input and places it in the DOM"""

    story_answers = request.args

    story_template = silly_story.generate(story_answers)

    return render_template(
        "story.html",
        final_story = story_template
        )
