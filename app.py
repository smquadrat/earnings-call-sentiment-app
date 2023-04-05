import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, render_template, request, send_from_directory

# Download the vader lexicon if it's not already downloaded
nltk.downloader.download('vader_lexicon')

# Download the punkt tokenizer if it's not already downloaded
nltk.download('punkt')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define keywords that indicate forward-looking language
keywords = ['forward-looking', 'outlook', 'forecast', 'expectations', 'guidance',
            'anticipated', 'planned', 'projected', 'predicted', 'potential', 'upcoming',
            'next quarter', 'next year', 'long-term', 'short-term', 'strategic', 'vision']

# Get the path to the sample transcript file
sample_transcript_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample_transcript.txt')


# Read the sample transcript file
with open(sample_transcript_path, 'r') as f:
    sample_transcript = f.read()

# Create a Flask app
app = Flask(__name__)

# Set up the app routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sentiment', methods=['POST'])
def sentiment():
        # Get the user-entered transcript from the form
        transcript = request.form['transcript']

        # Tokenize the transcript into sentences
        sentences = nltk.sent_tokenize(transcript)

        # Set up lists to hold the sentiment scores and highlighted sentences
        sentiment_scores = []
        positive_sentences = []
        negative_sentences = []

        # Loop through each sentence in the transcript
        for sentence in sentences:
            # Check if the sentence contains any of the forward-looking keywords
            if any(keyword in sentence.lower() for keyword in keywords):
                # Use the sentiment analyzer to get the sentiment score for the sentence
                score = sia.polarity_scores(sentence)['compound']
                # Add the sentiment score to the list
                sentiment_scores.append(score)
                # Highlight the sentence based on the sentiment score
                if score > 0:
                    highlighted_sentence = f'<span style="color:green">{sentence}</span>'
                    positive_sentences.append(highlighted_sentence)
                elif score < 0:
                    highlighted_sentence = f'<span style="color:red">{sentence}</span>'
                    negative_sentences.append(highlighted_sentence)
                else:
                    highlighted_sentence = sentence

        # Calculate the average sentiment score for all forward-looking sentences
        if sentiment_scores:
            avg_score = sum(sentiment_scores) / len(sentiment_scores)
        else:
            avg_score = 0.0

        # Render the sentiment analysis results template with the average score and highlighted sentences
        return render_template('sentiment.html', score=avg_score, positive_sentences=positive_sentences, negative_sentences=negative_sentences)

@app.route('/sample_transcript')
def sample_transcript():
    return send_from_directory('.', 'sample_transcript.txt')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)