
# Lead Scoring System

This project implements a lead scoring system to prioritize and evaluate potential leads based on their likelihood of conversion. The system uses machine learning models to assign scores to leads, helping sales teams focus on high-potential prospects.

## Features

- **Lead Scoring**: Predict the likelihood of a lead converting into a customer.
- **Data Analysis**: Explore and analyze lead data to identify key factors influencing conversion.
- **Predictive Modeling**: Build and evaluate machine learning models for lead scoring.
- **Visualization**: Visualize lead scores and model performance metrics.
- **Web Interface**: Provide a Flask-based web interface to input lead data and view scores.

## Prerequisites

- Python 3.x
- Flask (for web application interface)
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook (for exploratory data analysis)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/lead-scoring-system.git
   cd lead-scoring-system
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Set up environment variables if needed.

## Usage

### Data Analysis

1. **Load and Explore Data**:
   - Load lead data and perform exploratory data analysis to understand conversion factors.
   - Analyze distributions of key features such as lead source, industry, company size, and engagement level.

2. **Preprocess Data**:
   - Clean the data by handling missing values, encoding categorical variables, and scaling numerical features.

### Predictive Modeling

1. **Train Models**:
   - Implement and train various classification algorithms (e.g., Logistic Regression, Random Forest, Gradient Boosting) to score leads.

2. **Evaluate Models**:
   - Evaluate model performance using metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.

3. **Optimize Models**:
   - Tune hyperparameters to improve model performance and avoid overfitting.

### Running the Flask Application

1. Start the Flask server:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to access the web interface for inputting lead data and viewing lead scores.

## Code Overview

- **app.py**: Main Flask application script.
  - **index()**: Renders the main page.
  - **score()**: Handles scoring of leads based on user input.

- **model.py**: Contains machine learning model implementation and evaluation.
  - **train_models()**: Trains different classification models.
  - **evaluate_models()**: Evaluates model performance.
  - **predict_lead_score()**: Predicts lead scores based on input features.

- **data_preprocessing.py**: Handles data loading, cleaning, and preprocessing.

- **requirements.txt**: Lists the Python packages required for the project.

- **notebooks/**: Contains Jupyter Notebooks for exploratory data analysis and model training.

## Configuration

- **MODEL_PATH**: Path to the trained model file if loading from disk.
- **FLASK_APP_PORT**: Port for the Flask application (default: 5000).

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Scikit-learn](https://scikit-learn.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

---
[coding4vinayak](https://vinayakss.vercel.app/)
