from flask import Flask, request, render_template
from api_service import fetch_video_data
from utils import preprocess_data, analyze_keywords
from ml_model import suggest_title

app = Flask(__name__)

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/suggest', methods=['POST'])
def suggest():
    """Handle the suggestion form submission."""
    query = request.form['query']
    video_data, error_message = fetch_video_data(query)

    if error_message:
        # If there was an API error, render the home page with the error
        return render_template('index.html', error=error_message)

    df = preprocess_data(video_data)
    keywords = analyze_keywords(df)

    # Example placeholder user input for ML model
    title_suggestion = suggest_title(user_input1=3, user_input2=5)  


    return render_template(
        'result.html',
        suggestion=title_suggestion,
        keywords=keywords
    )

if __name__ == '__main__':
    app.run(debug=True)
