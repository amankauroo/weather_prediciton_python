import requests
import tkinter as tk
from tkinter import ttk
from datetime import datetime

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hourly Weather Report")
        self.root.geometry("600x450")

        # API Key and Location (Replace with your OpenWeatherMap API key and location)
        self.api_key = "e425f66c6b62eeaed73752101386b685"
        self.city = "Port Louis"
        self.country_code = "MU"  # Optional, use if needed

        self.create_widgets()

    def create_widgets(self):
        self.weather_label = ttk.Label(self.root, text="Hourly Weather Report", font=("Helvetica", 16))
        self.weather_label.pack(pady=10)

        self.text_area = tk.Text(self.root, height=20, width=70)
        self.text_area.pack(pady=10)

        self.get_weather_button = ttk.Button(self.root, text="Get Hourly Weather", command=self.get_hourly_weather)
        self.get_weather_button.pack(pady=10)

    def get_hourly_weather(self):
        base_url = "http://api.openweathermap.org/data/2.5/forecast"
        params = {
            "q": f"{self.city},{self.country_code}",
            "appid": self.api_key,
            "units": "metric",  # You can change this to "imperial" for Fahrenheit
        }

        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                # Clear previous text in the text area
                self.text_area.delete(1.0, tk.END)

                # Extract and display hourly weather information
                for entry in data["list"]:
                    timestamp = entry["dt"]
                    date_time = datetime.utcfromtimestamp(timestamp)
                    temperature = entry["main"]["temp"]
                    description = entry["weather"][0]["description"]
                    weather_info = f"{date_time}: Temperature {temperature}°C, {description}\n"
                    self.text_area.insert(tk.END, weather_info)
            else:
                error_message = f"Error: {data['message']}"
                self.text_area.insert(tk.END, error_message)

        except requests.RequestException as e:
            error_message = f"Error: {e}"
            self.text_area.insert(tk.END, error_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
