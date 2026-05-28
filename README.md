# 🌦️ AI Weather Analysis Dashboard

A complete AI + Data Science + Full Stack project that fetches live weather data, analyzes it using Pandas, visualizes trends using charts, predicts future temperature using Machine Learning, and displays everything in a modern dashboard UI.

---

## 🚀 Features

- ✅ Live weather data using OpenWeatherMap API
- ✅ Search weather by city
- ✅ Data analysis using Pandas
- ✅ Temperature & humidity charts
- ✅ Machine learning temperature prediction
- ✅ FastAPI backend
- ✅ Responsive frontend dashboard
- ✅ Deployment ready

---

## 🛠️ Tech Stack

### Backend

```txt
Python
FastAPI
Requests
```

### Data Analysis

```txt
Pandas
NumPy
```

### Data Visualization

```txt
Matplotlib
```

### Machine Learning

```txt
Scikit-learn
```

### Frontend

```txt
HTML
CSS
JavaScript
```

---

## 📁 Project Structure

```bash
AI-Weather-Dashboard/
│
├── backend/
│   ├── main.py
│   ├── weather.py
│   ├── analysis.py
│   ├── prediction.py
│   ├── utils.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│
├── data/
│   ├── weather_data.csv
│
├── charts/
│   ├── temperature_chart.png
│
├── model/
│   ├── weather_model.pkl
│
├── requirements.txt
├── README.md
```

---

## 🌍 API Used

We are using:

```txt
OpenWeatherMap API
```

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
cd AI-Weather-Dashboard
```

### Step 3 — Create Virtual Environment

#### Windows

```bash
python -m venv venv
```

#### Activate Environment

```bash
venv\Scripts\activate
```

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📦 Required Libraries

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

## ▶️ Run Backend Server

```bash
cd backend
uvicorn main:app --reload
```

Server URL:

```txt
http://127.0.0.1:8000
```

---

## 🌦️ Weather API Example

### API Request

```python
https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=YOUR_API_KEY
```

### Example Response

```json
{
  "city": "Delhi",
  "temperature": 32,
  "humidity": 70,
  "condition": "Clouds"
}
```

---

## 📊 Project Modules

### 1. Weather API Integration

- Fetch live weather data
- Search city weather
- Handle API responses

### 2. Data Analysis

- Store weather data in CSV
- Analyze temperature trends
- Humidity analysis

### 3. Data Visualization

- Temperature charts
- Humidity charts
- Trend analysis

### 4. Machine Learning

- Train prediction model
- Predict future temperature
- Save trained model

### 5. Frontend Dashboard

- Search weather
- Display charts
- Responsive UI

---

## 🧠 Learning Objectives

This project helps you learn:

- API handling
- JSON processing
- Data analysis
- Data visualization
- Machine learning workflow
- Backend API development
- Frontend integration
- Real-world project architecture

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
