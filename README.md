# earnings-call-sentiment-app

This Flask app provides an easy-to-use interface for users to input an earnings call transcript and receive a sentiment score based on the VADER (Valence Aware Dictionary and sEntiment Reasoner) model, which is implemented using the NLTK Python library. The app analyzes forward-looking transcript sentences that contain keywords such as "forecast", "potential", and "next year", and highlights specific lines that are tagged as positive or negative to derive the sentiment score.

**Access demo [here](https://earnings-call-sentiment-app.onrender.com)**

Sample input:

![transcript_app_screenshot_1](https://user-images.githubusercontent.com/41703555/232328957-b5660f2f-8134-46ca-9418-39ca57bf6d45.jpg)

Sample output:

![transcript_app_screenshot_2](https://user-images.githubusercontent.com/41703555/232328960-d98e54ac-7840-4f1e-a8b2-74ddf458c9d4.jpg)
