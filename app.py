from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def root():
    story_prompts = silly_story.prompts
    print(story_prompts)
    return render_template(
        "questions.html",
        prompts=story_prompts)
        
@app.route('/results')
def story():
    return render_template(
        "story.html"
        )
