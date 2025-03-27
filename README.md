# 🏨 Hotel Booking Cancellation Predictor (ML + Flask)

This web application predicts whether a hotel booking is likely to be **canceled** based on booking details.  
It integrates a **machine learning model (Random Forest Classifier)** with a **Flask-based web interface** for real-time predictions.

---

## 📚 Table of Contents

- [🎥 Demo](#-demo)
- [✅ What the App Does](#-what-the-app-does)
- [📊 Features Used in the Model](#-features-used-in-the-model)
- [📁 Project Structure](#-project-structure)
- [🧼 Data Preprocessing](#-data-preprocessing)
- [📈 Model Training](#-model-training)
- [🌐 Web App with Flask](#-web-app-with-flask)
- [🚀 How to Run the Project](#-how-to-run-the-project)

---

## 🎥 Demo

[Click to Watch Demo](https://github.com/sarakhataam/BookingCancelPredictor/blob/main/Demo/Demo.mp4)
---

## ✅ What the App Does

1. 🎯 **Predicts Booking Cancellation**
   - Based on input features like:
     - Lead time
     - Number of adults/children
     - Type of room reserved
     - Booking source (market segment)
     - Meal plan
     - Arrival date

2. 🧠 **Uses a Machine Learning Model**
   - Random Forest Classifier trained on a real hotel booking dataset

3. 🌐 **Provides a Web Interface**
   - Users input booking details via a form
   - Instantly shows whether the booking is likely to be canceled

---

## 📊 Features Used in the Model

- `lead_time`
- `arrival_date`
- `meal_plan`
- `room_type_reserved`
- `market_segment_type`
- `repeated_guest`
- `no_of_adults`
- `no_of_children`
- `no_of_weekend_nights`
- `no_of_week_nights`
- `type_of_meal_plan` (encoded)
- `room_type_reserved` (encoded)
- `market_segment_type` (encoded)

---

## 📁 Project Structure
[Image](https://github.com/user-attachments/assets/835f1e3c-c880-4021-868c-b11afd985878)

---

## 🧼 Data Preprocessing

- Categorical features like meal plan, room type, and market segment were label-encoded.
- Numerical features were scaled using `StandardScaler`.

---

## 📈 Model Training

- **Model used**: Random Forest Classifier
- **Metrics**: Accuracy, Precision, Recall
- The model was trained using `scikit-learn` and saved with `pickle`.

---

## 🌐 Web App with Flask

- User fills out a form with booking details.
- Flask processes the input, encodes/scales features.
- Prediction is made and result shown on the same page.






