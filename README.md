# 🚗 Car Price Prediction using Machine Learning & Tkinter GUI

This project is a **Machine Learning–based Car Price Prediction System** with a fully functional **Tkinter GUI**.  
Users can log in, enter car details, and instantly receive a predicted selling price.  
This system uses a trained **Random Forest Regression** model saved as `car_price_model.pkl`.

---

## 📌 Features

### 🔹 Machine Learning
- Trained using **Random Forest Regressor**
- Dataset contains:
  - Year of manufacture
  - Present price (in lakhs)
  - Driven kilometers
  - Fuel type
  - Selling type
  - Transmission type
  - Owner count
- Model trained in **Jupyter Notebook**
- Model saved using **joblib** as `car_price_model.pkl`

---

## 🔹 Graphical User Interface (Tkinter)
- Login page (username + password)
- Main prediction form with input fields
- Beautiful background image (`bg.jpg`)
- Bold, clean labels for input fields
- Predict button → shows price in lakhs
- Logout button → returns user safely
- Responsive and easy-to-use layout

---

## 📁 Project Folder Structure


---

## 🧠 Model Training Summary

The model was trained in **Jupyter Notebook** using the following steps:

1. **Load dataset**
2. **Drop Car_Name column**
3. **Encode categorical columns**
4. **Split data into train/test**
5. **Train RandomForestRegressor**
6. **Evaluate model performance**
7. **Save trained model**

### Code used to save the model:
```python
joblib.dump(model, "car_price_model.pkl")


Author

Madushi Sulakshana
Car Price Prediction System using ML & Tkinter
Python | Machine Learning | GUI Development
