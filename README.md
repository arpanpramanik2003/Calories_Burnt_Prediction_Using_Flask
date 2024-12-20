# Calories Burnt Prediction Using Flask and Machine Learning

This project is a web-based application that predicts the calories burnt based on user inputs using a machine learning model trained with `XGBRegressor`. The application is built with Python, Flask, and scikit-learn, providing an interactive and user-friendly experience.

## Overview
The **Calories Burnt Prediction** application enables users to calculate their calorie expenditure by inputting details such as age, gender, weight, height, and activity level. The backend uses a machine learning model trained on real-world data to make accurate predictions. 

This project demonstrates how machine learning models can be deployed in a lightweight web application using Flask, making it ideal for learning and practical usage.

---

## Features
- **Accurate Predictions**: Utilizes `XGBRegressor` for reliable calorie prediction.
- **Interactive User Interface**: HTML and CSS ensure a responsive and visually appealing design.
- **Machine Learning Backend**: Integrates a pre-trained model (`model.pkl`) for predictions.
- **Flask Framework**: Provides a lightweight and fast backend framework.
- **Scalable Deployment**: Configured for deployment on Render using Gunicorn.

---

## Machine Learning Model
- **Algorithm**: `XGBRegressor` (Extreme Gradient Boosting)
- **Data Preprocessing**: Used techniques like normalization and imputation for clean and efficient data handling.
- **Training**: The model was trained using scikit-learn and XGBoost to ensure high accuracy.
- **Saved Model**: The trained model is saved in `model.pkl` for quick loading and inference.

---
