from flask import Flask, render_template, request
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv(r"C:\Users\Konda Reddy\OneDrive\Desktop\sohel\medical_data.csv")
data.dropna(inplace=True)
X = data['Symptoms']
y = data['Disease']

vectorizer = TfidfVectorizer()
X_transformed = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)
print("Classification Report:\n", classification_report(y_test, y_pred))

with open('medical_diagnosis_model.pkl', 'wb') as f:
    pickle.dump((vectorizer, model), f)

with open('medical_diagnosis_model.pkl', 'rb') as f:
    vectorizer, model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        symptoms = request.form['symptoms']
        symptoms_transformed = vectorizer.transform([symptoms])
        prediction = model.predict(symptoms_transformed)
        return render_template('index.html', prediction_text=f'Predicted Disease: {prediction[0]}')

if __name__ == '__main__':
    app.run(debug=True)