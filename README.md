# 🏥 AI-Powered Medical Diagnosis System  

An **AI-driven Medical Diagnosis System** built using **Flask, Python, and Scikit-learn**, designed to predict diseases based on user-input symptoms.  

![Screenshot 2025-03-19 211056](https://github.com/user-attachments/assets/43ea5cb6-68b8-4407-a821-2e3c21d9c543)


## 📖 Table of Contents  
1. Introduction  
2. Features  
3. Technologies Used  
4. Setup and Installation  
5. How It Works  
6. Project Structure  
7. Sample Inputs  
8. CSS Styling  
9. Live Demo  
10. Future Enhancements  
11. Development  
12. License  

## 🎯 Introduction  
This project leverages **Machine Learning (ML)** techniques to assist users in predicting potential diseases based on symptoms. It employs **Natural Language Processing (NLP)** for symptom recognition and classification using **Random Forest Classifier**.  

## ✨ Features  
- AI-based disease prediction using **Random Forest**  
- User-friendly **Flask-based web interface**  
- **TfidfVectorizer** for symptom processing  
- Interactive and responsive UI  
- Secure and scalable  

## 🔧 Technologies Used  
- **Backend:** Flask (Python)  
- **Frontend:** HTML5, CSS3  
- **Machine Learning:** Scikit-learn, Pandas, NumPy  
- **Model:** Random Forest Classifier  
- **Hosting:** Flask built-in server  

## 🛠️ Setup and Installation  
### Prerequisites  
- Python 3.7+  
- Virtual environment (optional but recommended)  
- Install necessary dependencies  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/ai-medical-diagnosis.git  
   cd ai-medical-diagnosis  
   ```  
2. Install required dependencies:  
   ```bash  
   pip install -r requirements.txt
   ```  
3. Run the application:  
   ```bash  
   python app.py  
   ```  
   Open **http://127.0.0.1:5000/** in your browser.  

## 🚀 How It Works  
1. **Input:** User enters symptoms in a text box.  
2. **Processing:**  
   - Symptoms are converted into numerical representations.  
   - **Random Forest Classifier** processes the data and predicts the disease.  
3. **Output:** The predicted disease is displayed on the UI.  

## 📂 Project Structure  
```
ai-medical-diagnosis/  
│  
├── app.py                 # Main Flask application  
├── templates/  
│   └── index.html         # Frontend HTML  
├── static/  
│   └── styles.css         # CSS for styling  
├── medical_data.csv       # Dataset containing symptoms and diseases  
├── medical_diagnosis_model.pkl  # Trained model  
├── requirements.txt       # Dependencies  
├── README.md              # Documentation  
└── LICENSE                # Project license  
```

## 📝 Sample Inputs  
- **Example Input:**  
  `fever, cough, sore throat`  
- **Example Output:**  
  `Predicted Disease: Flu`  

## 🎨 CSS Styling  
The web application includes an interactive UI with a **gradient background, stylish buttons, and responsive design**.

## 🌐 Live Demo  
[Live Demo](#)  
(*Replace with the deployed link or keep as a placeholder.*)  

## 🔮 Future Enhancements  
- Improve model accuracy with **Deep Learning**  
- Integrate **Real-time API** for live symptom analysis  
- Deploy on **Cloud Platforms** (AWS, GCP)  

## 🛠️ Development  
1. Fork the repository:  
   ```bash  
   git fork https://github.com/your-username/ai-medical-diagnosis.git  
   ```  
2. Create a new branch:  
   ```bash  
   git checkout -b feature-name  
   ```  
3. Commit changes:  
   ```bash  
   git commit -m "Added a new feature"  
   ```  
4. Push the branch:  
   ```bash  
   git push origin feature-name  
   ```  
5. Open a **Pull Request**.  

## ⚖️ License  
This project is licensed under the **MIT License**.  

---  

**💚 THANK YOU!** 🚀  
