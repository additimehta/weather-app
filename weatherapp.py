#weatherapp
import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/en-CA/weather/today/l/584018bec07ce9573837c14fa59da031fa6fcdeb1c3c9e3b2b27cb79ce254b5a?Goto=Redirected"

root = Tk()
root.title("Weather App")
root.configure(bg = "white")

img = Image.open("C:/Users/suman/Desktop/PycharmProjects/weatherapp/weathericon.png")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

locationLabel = Label(root, font=("Calibri bold",20),bg="white")
locationLabel.grid(row=0,sticky="N",padx=100)

temperatureLabel = Label(root, font=("Calibri bold",70),bg="white")
temperatureLabel.grid(row=1,sticky="W",padx=40)
Label(root, image=img, bg="white").grid(row=1,sticky="E")
weatherPredictionLabel = Label(root,font=("Calibri bold", 15), bg="white")
weatherPredictionLabel.grid(row=2, sticky="W", padx=40)

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1', class_="CurrentConditions--location--1YWj_").text
    temperature = soup.find('span', class_="CurrentConditions--tempValue--MHmYY").text
    weather_prediction = soup.find('div',class_="CurrentConditions--phraseValue--mZC_p").text

    locationLabel.config(text=location)
    temperatureLabel.config(text=temperature)
    weatherPredictionLabel.config(text=weather_prediction)

    temperatureLabel.after(60000,getWeather)
    root.update()
getWeather()
root.mainloop()