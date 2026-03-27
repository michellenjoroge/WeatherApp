# WeatherApp
Capstone project assignment - Weather app that fetches weather conditions in different cities

# Prompt-Powered Kickstart: Building a Python Weather App with Tkinter

---

## 1.Title & Objective

**Technology Chosen:** Python with Tkinter and OpenWeather API  

**Why this technology?**  
Python is beginner-friendly and widely used in software development. Tkinter allows easy creation of graphical user interfaces (GUI), making it perfect for beginners.

**End Goal:**  
To build a simple interactive desktop application that allows users to enter a city name and view real-time weather data.

---

## 2.Quick Summary of the Technology

**What is Python?**  
Python is a high-level programming language used in web development, automation, data science, and more.

**What is Tkinter?**  
Tkinter is a built-in Python library used to create GUI applications.

**What is an API?**  
An API (Application Programming Interface) allows communication between applications and external services.

**Where is it used?**  
Used in apps like weather apps, mobile apps, and web apps.

**Real-world example:**  
Weather apps on smartphones use APIs to fetch live weather data.

---

## 3.System Requirements

- OS: Windows
- Python 3.14.3 installed
- VS Code or PyCharm

## Installation & Setup Instructions

Follow these steps to set up and run the project:

### 1. Install Python
- Download Python from: https://www.python.org/downloads/  
- Install it on your system  
- Make sure to check **"Add Python to PATH"** during installation  

---

### 2. Install VS Code
- Download from: https://code.visualstudio.com/  
- Install the application  
- Open VS Code and install the **Python Extension**

---

### 3. Create Project Folder

Open your terminal and run:

## Minimal Working Example

### Description

This example demonstrates how the application works at a basic level.

- The user enters a city name  
- The app sends a request to the OpenWeather API  
- It retrieves weather data  
- It displays the temperature and weather condition in the GUI  

---

### Example Code

```python
import requests

# Replace with your actual API key
API_KEY = "your_api_key_here"

# Ask user for city name
city = input("Enter city: ")

# API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Send request to API
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Check if request was successful
if data["cod"] == 200:
    temp = data["main"]["temp"]  # Get temperature
    weather = data["weather"][0]["description"]  # Get weather description

    # Display result
    print(f"Temperature: {temp}°C")
    print(f"Condition: {weather}")
else:
    print("City not found")
---

---

### Issue 1: pip not recognized

**Problem:**  
Running `pip install requests` returned an error:
