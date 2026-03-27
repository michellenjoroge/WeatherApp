import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "052a59748cd4433b6259f3c503e9d27f"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]

            result_label.config(
                text=f"🌡 {temp}°C\n☁ {weather}",
                fg="#333"
            )
        else:
            result_label.config(text="❌ City not found", fg="red")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# 🎨 Window setup
root = tk.Tk()
root.title("🌤 Weather App")
root.geometry("300x250")
root.config(bg="#f0f8ff")  # light blue background

# 🌟 Title
title = tk.Label(root, text="Weather App", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
title.pack(pady=10)

# 📍 City input
city_entry = tk.Entry(root, font=("Arial", 12), justify="center")
city_entry.pack(pady=5)

# 🔘 Button
get_btn = tk.Button(
    root,
    text="Get Weather",
    command=get_weather,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5
)
get_btn.pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff")
result_label.pack(pady=10)

root.mainloop()