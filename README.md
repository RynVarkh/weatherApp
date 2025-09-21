# ☀️ Weather App (Python)

A simple **command-line weather application** in Python that fetches the current weather and daily temperature range for any city using the **Open-Meteo API**.

---

## 🚀 Features
- Get current temperature and wind speed 🌡💨
- Get today's minimum and maximum temperatures 📅
- Displays country and approximate city population
- Simple CLI interface

---

## 🛠️ Requirements
- Python 3.x
- Packages listed in `requirements.txt` (mainly `requests`)


## 📂 Project Structure

```bash 
weatherApp/
├── venv/               # Python virtual environment (optional)
├── requirements.txt    # Dependencies
├── weather.py          # Main script
└── README.md           # Project documentation
```

---

## Usage

1. Clone the repository:
```bash
git clone https://github.com/your-username/weatherApp.git
cd weatherApp
```

2. Activate your virtual environment (optional but recommended):
```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the script:
```bash
python weather.py
```

5. Enter a city name when prompted:
```bash
City: Bangalore
```