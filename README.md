# Climate-Change-Modeling

This project uses machine learning to model climate change indicators and predict CO₂ emissions based on key environmental factors like temperature, CO₂ concentration, and sea level. It includes a trained model, a Streamlit app for real-time prediction, and a data preprocessing and modeling notebook.

## 📁 Project Structure

```
.
├── climate.ipynb            # Jupyter notebook for EDA, preprocessing, modeling
├── climate_data.csv         # Cleaned climate dataset
├── streamlit_app.py         # Streamlit app for prediction
├── rf_model.pkl             # Trained Random Forest model
├── scaler.pkl               # StandardScaler used during training
├── requirement.txt          # List of required Python libraries
└── README.md                # Project documentation
```

## 🚀 Features

- Data preprocessing and feature engineering on climate datasets.
- Machine learning pipeline using Random Forest Regressor.
- Scaler saved for inference consistency.
- Deployed with an interactive Streamlit interface.
- Predict CO₂ emissions from temperature, CO₂ ppm, and sea level.

## 🧪 Tech Stack

- **Python**, **pandas**, **NumPy**
- **scikit-learn**, **matplotlib**, **seaborn**
- **nltk**, **textblob**, **WordCloud**
- **Streamlit** *(for live web app)*

## 🔍 Streamlit App

To run the CO₂ Emission Predictor web app:

```bash
streamlit run streamlit_app.py
```

### Inputs:
- Temperature (°C)
- CO₂ Concentration (ppm)
- Sea Level Deviation (mm)

The model uses default/mid values for other climate features behind the scenes.

## 🧠 Model Info

- **Algorithm:** Random Forest Regressor
- **Features Used:**
  - Year, Week No, Latitude, Longitude
  - Temperature, CO₂ ppm, Sea Level
  - CO₂ rolling mean, Sea level diff, Temp lag
- **Scaler:** StandardScaler from `scikit-learn`
- **Output:** Estimated CO₂ emission (unitless score)

## 🛠 Installation

Install required dependencies:

```bash
pip install -r requirement.txt
```

## 📊 Dataset

- Source: `climate_data.csv` (preprocessed)
- Contains numerical climate indicators suitable for regression modeling.

## ✍️ Authors

- **Shivtej Jad**   
  📧 shivtej0907@gmail.com

## 📌 Future Improvements

- Incorporate real-time data API (e.g., NASA, NOAA).
- Add sentiment analysis from climate-related texts.
- Use advanced models like LSTM/GRU for temporal dependencies.
- Deploy as a hosted web app on platforms like Heroku or Hugging Face.