# 🌦️ AI Weather Prediction Engine

This repository contains the backend engine and model training code for an AI weather prediction project. The website/dashboard UI is not developed yet — the focus is on data processing, model training, and backend weather analysis.

---

## 🚀 Current Project Scope

- ✅ Backend weather data engine
- ✅ Data loading and analysis
- ✅ Model training and prediction pipeline
- ✅ Notebook experimentation
- ⛔ Frontend dashboard / website not developed yet

---

## 🛠️ Tech Stack

### Backend / Engine

```txt
Python
FastAPI
Requests
```

### Data Analysis

```txt
Pandas
NumPy
Matplotlib
```

### Machine Learning

```txt
Scikit-learn
```

### Notebooks

```txt
Jupyter / Python scripts for exploration and training
```

---

## 📁 Project Structure

```bash
Ai-weather-Prediction-Model-/
├── backend/
│   ├── analyze.py
│   ├── main.py
│   ├── test.py
│   └── weather.py
├── charts/
│   ├── Temp__Analyze.py
│   └── Weather_Analyze.py
├── data/
│   └── Weather__data__.csv
├── models/
├── notebooks/
│   ├── main.py
│   ├── train.py
│   └── Weather__analysis.py
├── LICENSE
└── README.md
```

---

## 🔍 What This Project Does

- Loads weather data from CSV and live API calls
- Analyzes temperature and humidity trends
- Trains machine learning models for temperature prediction
- Provides a FastAPI backend engine for weather services
- Includes notebooks for experiment tracking and model training

---

## 🚫 What This Project Does Not Do Yet

- No production-ready frontend website
- No complete dashboard UI
- No deployed web app
- No full end-user interface

---

## 🌍 API Used

This project can use OpenWeatherMap API for weather data.

Get a free API key at:

```txt
https://openweathermap.org/api
```

---

## ⚙️ Installation & Setup

### Step 1 — Clone Repository

```bash
git clone https://github.com/devidutta3/Ai-weather-Prediction-Model-.git
```

### Step 2 — Open Project Folder

```bash
cd "c:\Users\dasde\OneDrive\Desktop\Ai-weather-Prediction-Model-"
```

### Step 3 — Create Virtual Environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Expected Libraries

```txt
pandas
numpy
matplotlib
scikit-learn
fastapi
uvicorn
requests
```

---

## ▶️ Run Backend Engine

```bash
cd backend
uvicorn main:app --reload
```

Then open:

```txt
http://127.0.0.1:8000
```

---

## 📌 Licensing

This project is licensed under the Apache License 2.0. Users must comply with the terms of the license when using, modifying, or distributing this code.

- Do not remove the `LICENSE` file.
- Keep the license notice intact in redistributed source code.
- Give credit to the original developer when sharing or reusing this project.
- Follow Apache 2.0 requirements for attribution, modifications, and redistribution.

For full terms, see `LICENSE`.

---

## 🧠 Notes

- The repository currently implements the backend and model training flow only.
- Frontend/dashboard development is planned for a later stage.
- Use the notebooks in `notebooks/` for training and analysis workflows.

---

## 🚨 Common Errors & Fixes

### Error: `ModuleNotFoundError`

Fix:

```bash
pip install package_name
```

### Error: `401 Invalid API Key`

Fix:

Check your OpenWeatherMap API key.

### Error: `404 city not found`

Fix:

Verify the city name and spelling in the API request.


Check city spelling carefully.

---

## 💡 Future Improvements

- 🌙 Dark Mode
- 📍 Geo-location Weather
- 📈 7-Day Forecast
- 🤖 AI Weather Assistant
- 🔐 User Authentication
- 🗄️ Database Integration

---

## 🤝 Contributing

Pull requests are welcome.

For major changes, open an issue first to discuss what you would like to change.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

```txt
Krishna
B.Tech Student | Frontend Developer | AI/ML Learner
```

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub.
