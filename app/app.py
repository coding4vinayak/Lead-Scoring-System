from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and label encoders
with open('lead_scoring_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)

def encode_new_data(new_data, label_encoders):
    for column in new_data.columns:
        if column in label_encoders:
            le = label_encoders[column]
            new_data[column] = new_data[column].map(lambda s: le.transform([s])[0] 
                                                    if s in le.classes_ 
                                                    else -1)  # Handle unseen labels
    return new_data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input
        data = {
            'Job Title': request.form.get('job_title'),
            'Years of Experience': int(request.form.get('experience')),
            'Company Size': request.form.get('company_size'),
            'Industry': request.form.get('industry'),
            'Location': request.form.get('location'),
            'Website Visits': int(request.form.get('website_visits')),
            'Resources Downloaded': int(request.form.get('resources_downloaded')),
            'Attended Webinar': int(request.form.get('attended_webinar')),
            'Email Open Rate': float(request.form.get('email_open_rate')),
            'Email Click Rate': float(request.form.get('email_click_rate')),
            'Responded to Survey': int(request.form.get('responded_survey')),
            'Days Since Last Interaction': int(request.form.get('days_since_interaction'))
        }

        # Convert to DataFrame
        new_data = pd.DataFrame([data])

        # Encode the new data
        encoded_new_data = encode_new_data(new_data, label_encoders)

        # Make prediction
        prediction = model.predict(encoded_new_data)[0]

        # Redirect to the result page
        return render_template('result.html', prediction=prediction)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
