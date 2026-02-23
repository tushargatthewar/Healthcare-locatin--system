# Healthcare Location System

An intelligent medical assistance platform that combines machine learning-based disease prediction with geolocation services to provide patients with immediate healthcare guidance.

## 🎯 Overview

The Healthcare Location System analyzes patient symptoms, predicts potential diseases using machine learning, recommends precautionary measures, and locates nearby hospitals - creating a comprehensive healthcare navigation solution.

## ✨ Key Features

- **AI-Powered Disease Prediction**: Uses 3 ML models (Decision Tree, Random Forest, Naive Bayes) to predict from 41 diseases based on symptoms
- **Hospital Locator**: Find nearby hospitals within 5km radius using Google Maps integration
- **Smart Recommendations**: Get precautionary measures and disease information
- **Government Schemes**: Access information about healthcare schemes
- **Multilingual Support**: Google Translate integration for accessibility
- **Mobile App**: React Native application for iOS and Android

## 🖼️ Screenshots

### Home Page
![Home Page](Screenshot%20(9).png)

### Symptom Selection
![Symptom Selection](Screenshot%20(10).png)

### Disease Prediction Results
![Disease Prediction](Screenshot%20(11).png)

### Hospital Locator
![Hospital Locator](Screenshot%20(13).png)

### Hospital Map View
![Hospital Map](Screenshot%20(14).png)

## 🛠️ Technology Stack

### Backend
- Python Flask Framework
- MySQL Database (with SQLite fallback)
- scikit-learn, pandas, numpy
- Flask-CORS

### Frontend
- HTML5, CSS3, JavaScript
- Google Maps API with Places Library
- Google Translate API
- Responsive Design

### Mobile
- React Native (Expo Framework)
- Python-shell integration

### Machine Learning
- Decision Tree Classifier
- Random Forest Classifier
- Naive Bayes Classifier

## 📋 Prerequisites

- Python 3.7+
- MySQL Server (or SQLite)
- Node.js and npm (for React Native app)
- Google Maps API Key

## 🚀 Installation

### Backend Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Healthcare-location-system
```

2. Install Python dependencies:
```bash
pip install Flask mysql-connector-python scikit-learn pandas numpy matplotlib flask-cors joblib
```

3. Configure database:
   - Update database credentials in `form/dbconnection.py`
   - Default configuration:
     - Host: localhost
     - User: root
     - Database: webdata

4. Run the Flask application:
```bash
cd form
python main.py
```

The server will start at `http://127.0.0.1:5000`

### Mobile App Setup

1. Install dependencies:
```bash
npm install
```

2. Start the Expo development server:
```bash
npm start
```

3. Scan QR code with Expo Go app (iOS/Android)

## 📊 Machine Learning Models

The system uses three pre-trained models located in the `form/` directory:

- `disease_classifier.pkl` - Decision Tree Classifier
- `disease_classifier_random.pkl` - Random Forest Classifier
- `disease_classifier_bayes.pkl` - Naive Bayes Classifier

### Training Your Own Models

Run the training script:
```bash
cd python
python ML_CODE.py
```

Training data: `training.csv` (132 symptoms, 41 diseases)
Testing data: `testing.csv`

## 🗄️ Database Schema

### Patient Tables
- `patient_info` - Personal details and authentication
- `patient_contact` - Contact information
- `patient_insurance` - Insurance details
- `patient_scheme` - Government scheme enrollment

### Doctor Tables
- `doctor_info` - Doctor credentials
- `doctor_contact` - Contact and department info
- `doctor_license` - License and specialization

### Hospital Tables
- `hospital_info` - Hospital registration
- `hospital_contact` - Address and contact numbers
- `hospital_legalinfo` - Legal and licensing info

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Patient home page |
| GET | `/index` | Symptom input form |
| POST | `/symptomes` | Disease prediction |
| GET | `/schemes` | Government schemes |
| GET | `/nearby_hospitals` | Hospital locator |
| POST | `/hospital_info` | Hospital data processing |
| POST | `/hospital_info1` | Hospital details |
| GET | `/prof/<hospital_name>` | Hospital profile |

## 🎨 Features in Detail

### Disease Prediction
1. Select up to 4 symptoms from 132 options
2. Three ML models analyze simultaneously
3. Ensemble prediction for accuracy
4. Get disease name, precautions, and occurrence statistics

### Hospital Locator
1. Automatic location detection
2. Manual location search with autocomplete
3. Interactive map with hospital markers
4. Hospital details with photos
5. Direct navigation support

### Supported Diseases (41 total)
- Infectious: Malaria, Dengue, Typhoid, Tuberculosis, Hepatitis (A-E)
- Chronic: Diabetes, Hypertension, Arthritis, Asthma
- Common: Cold, Migraine, Acne, Allergies
- Critical: Heart Attack, Paralysis, AIDS
- And many more...

## 🔐 Security Features

- Aadhar-based authentication
- Session management with secret keys
- Input validation and sanitization
- CORS protection
- Encrypted password storage

## 🌐 Google Maps API Setup

1. Get API key from [Google Cloud Console](https://console.cloud.google.com/)
2. Enable Maps JavaScript API and Places API
3. Update API key in `form/templates/nearby_hospitals.html`:
```javascript
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places&callback=initMap"></script>
```

## 📱 Mobile App Usage

1. Launch the app
2. Select 5 symptoms from dropdown menus
3. Tap "Submit" button
4. View predicted disease and recommendations
5. Access hospital locator

## 🔮 Future Enhancements

- [ ] Virtual consultation with doctors
- [ ] Online appointment booking
- [ ] Cloud-based health records
- [ ] Daily health checkup reminders
- [ ] AI chatbot for 24/7 assistance
- [ ] Prescription management
- [ ] Emergency ambulance calling
- [ ] Health analytics and trends

## 📄 Project Structure

```
Healthcare-location-system/
├── form/                      # Main Flask application
│   ├── main.py               # Primary application file
│   ├── dbconnection.py       # Database integration
│   ├── templates/            # HTML templates
│   ├── static/               # CSS, JS, images
│   └── *.pkl                 # ML model files
├── python/                    # ML training scripts
│   ├── ML_CODE.py            # Model training
│   ├── training.csv          # Training dataset
│   └── testing.csv           # Testing dataset
├── src/                       # React Native components
│   └── components/
├── App.js                     # React Native entry point
├── package.json              # Node dependencies
└── README.md                 # This file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available for educational purposes.

## 👥 Authors

Healthcare Location System Development Team

## 📞 Support

For technical inquiries or support, please open an issue in the repository.

## 🙏 Acknowledgments

- Google Maps API for location services
- scikit-learn for ML algorithms
- Flask framework for backend
- React Native for mobile development
- Medical datasets for training

---

**Note**: This system provides health information and guidance but should not replace professional medical consultation. Always consult with qualified healthcare providers for medical advice.
