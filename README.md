# Boston House Price Prediction

## 1. Train and Export Model
- Open `MLhousepricepred.ipynb` in Jupyter or VS Code.
- Run all cells to train the model and export `regmodel.pkl` and `scaler.pkl`.

## 2. Start Backend API
- Ensure you have Flask installed:  
  `pip install flask`
- Save the provided `app.py` in this folder.
- Run the backend:  
  `python app.py`
- The API will be available at `http://127.0.0.1:5000/predict`.

## 3. Use the Frontend
- Save the provided `frontend.html` in this folder.
- Open `frontend.html` in your browser.
- Enter house features and click "Predict Price".

## Notes
- Make sure `regmodel.pkl` and `scaler.pkl` are in the same folder as `app.py`.
- The backend must be running for the frontend to work.
