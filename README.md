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
## AI Prompt Journal

This section documents how AI was used to assist in learning and building the project.

---

### Prompt 1

**Prompt Used:**  
"Give me a simple Python project using an API"

**Link to Curriculum:**  
https://ai.moringaschool.com/

**AI Response Summary:**  
The AI suggested building a weather application using an API.

**Helpful Response Extract:**  
“The AI recommended using the OpenWeather API to fetch real-time weather data.”

**Evaluation:**
 Very helpful — helped in choosing a practical and beginner-friendly project idea.

---

### Prompt 2

**Prompt Used:**  
"How to create a GUI using Tkinter in Python"

**Link to Curriculum:**  
https://ai.moringaschool.com/

**AI Response Summary:**  
Provided step-by-step guidance on creating a window, buttons, and labels.

**Helpful Response Extract:**  
“The AI showed how to use Tkinter widgets like Label, Entry, and Button.”

**Evaluation:**  
Very helpful — made it easy to build the user interface.

---

### Prompt 3

**Prompt Used:**  
"How to connect Python to an API and fetch data"

**Link to Curriculum:**  
https://ai.moringaschool.com/

**AI Response Summary:**  
Explained how to use the `requests` library and handle JSON responses.

**Helpful Response Extract:**  
“The AI explained how to send a GET request and extract data from JSON.”

**Evaluation:**  
Helpful — improved understanding of API integration.

---

### Prompt 4

**Prompt Used:**  
"Fix pip not recognized error in Python"

**Link to Curriculum:**  
https://ai.moringaschool.com/

**AI Response Summary:**  
Suggested using `python -m pip` and checking PATH settings.

**Helpful Response Extract:**  
“The AI recommended using python -m pip instead of pip directly.”

**Evaluation:**
 Very helpful — resolved installation issue quickly.



### Overall Reflection

Using AI significantly improved the development process by:
- Speeding up problem-solving  
- Providing clear step-by-step guidance  
- Helping debug errors quickly  

AI was an effective learning assistant throughout the project.

---


## Common Issues & Fixes

During development, several issues were encountered. Below are the common problems and how they were resolved.

##  References

The following resources were used to learn and build this project:

---

###  Official Documentation

- Python Documentation: https://docs.python.org/3/  
- Requests Library Documentation: https://docs.python-requests.org/  
- Tkinter Documentation: https://docs.python.org/3/library/tkinter.html  
- OpenWeather API: https://openweathermap.org/api  

---

###  Video Tutorials

- Python Tkinter Tutorial (GUI Development)  
  https://www.youtube.com/watch?v=YXPyB4XeYLA  

- Python API Tutorial (Using Requests)  
  https://www.youtube.com/watch?v=tb8gHvYlCFs  

---

### Helpful Blog Posts & Articles

- How to Use APIs in Python  
  https://realpython.com/api-integration-in-python/  

- Beginner Guide to Tkinter  
  https://www.geeksforgeeks.org/python-gui-tkinter/  

- StackOverflow (Error Fixes & Debugging)  
  https://stackoverflow.com  

---

### Summary

These resources helped in:
- Understanding Python basics  
- Learning GUI development with Tkinter  
- Integrating APIs into applications  
- Debugging common errors  

---
---

### Issue 1: pip not recognized

**Problem:**  
Running `pip install requests` returned an error:
