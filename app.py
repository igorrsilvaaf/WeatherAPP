import locale
import tkinter as tk
from datetime import datetime, timedelta
from tkinter import *

import pytz
import requests
import unicodedata
from PIL import Image
from PIL import ImageTk
from babel.dates import format_date
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

# Criaçao da janela
root = Tk()
root.title("Previsão App")
root.geometry("864x470+600+300")
root.configure(bg='#FFFFFF')
root.resizable(False, False)


# localização para português
locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')


def get_weather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="igorrsilvaaf")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)}°N, {round(location.longitude)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)

    # Obtenha o dia da semana atual em português formatado
    current_day = datetime.now().strftime("%A")

    # Normalize a string para lidar com caracteres acentuados e capitalize as palavras
    current_day_normalized = unicodedata.normalize('NFKD', current_day).encode('ASCII', 'ignore').decode(
        'utf-8').lower().split(" ")
    current_day = " ".join([word.capitalize() for word in current_day_normalized])

    # Atualize o texto no widget 'week'
    week.config(text=current_day)

    # Consulta API OpenWeather
    API = f"https://api.openweathermap.org/data/2.5/forecast?lat="+str(location.latitude)+"&lon="+str(
        location.longitude)+"&appid=c6ff004f7136bc2f7f55c320c823940f&lang=pt_br"
    json_data = requests.get(API).json()

    # Current
    temp = int(json_data['list'][0]['main']['temp'] - 273.15)
    humidity = json_data['list'][0]['main']['humidity']
    pressure = json_data['list'][0]['main']['pressure']
    wind = json_data['list'][0]['wind']['speed']
    description = json_data['list'][0]['weather'][0]['description']

    temperature.config(text=(temp, "ºC"))
    humidity_weather.config(text=(humidity, "%"))
    pressure_weather.config(text=(pressure, "hPa"))
    wind_speed.config(text=(wind, "m/s"))
    description_weather.config(text=description)

    # Temperatura do dia
    temp_right.config(text=(temp,"ºc"))

    # Box grande
    firstdayimage = json_data['list'][0]['weather'][0]['icon']

    # Box 2
    seconddayimage = json_data['list'][1]['weather'][0]['icon']

    img = (Image.open(f"icon/{seconddayimage}@2x.png"))
    resized_image = img.resize((60, 60))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image = photo2

    tempday2 = int(json_data['list'][1]['main']['temp'] - 273.15)
    descday2 = json_data['list'][1]['weather'][0]['description']
    city = json_data['city']['name']

    day2temp.config(text=f"\n {tempday2} ºC  \n {descday2}")

    # Box 3
    thirddayimage = json_data['list'][2]['weather'][0]['icon']

    img = (Image.open(f"icon/{thirddayimage}@2x.png"))
    resized_image = img.resize((60, 60))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3

    tempday3 = int(json_data['list'][2]['main']['temp'] - 273.15)
    descday3 = json_data['list'][2]['weather'][0]['description']
    city = json_data['city']['name']

    day3temp.config(text=f"\n {tempday3} ºC  \n {descday3}")

    # Box 4
    fourthdayimage = json_data['list'][3]['weather'][0]['icon']

    img = (Image.open(f"icon/{fourthdayimage}@2x.png"))
    resized_image = img.resize((60, 60))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    tempday4 = int(json_data['list'][3]['main']['temp'] - 273.15)
    descday4 = json_data['list'][3]['weather'][0]['description']
    city = json_data['city']['name']

    day4temp.config(text=f"\n {tempday4} ºC  \n {descday4}")

    # Box 5
    fifthdayimage = json_data['list'][4]['weather'][0]['icon']

    img = (Image.open(f"icon/{fifthdayimage}@2x.png"))
    resized_image = img.resize((60, 60))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    tempday5 = int(json_data['list'][4]['main']['temp'] - 273.15)
    descday5 = json_data['list'][4]['weather'][0]['description']
    city = json_data['city']['name']

    day5temp.config(text=f"\n {tempday5} ºC  \n {descday5}")

    # Box 6
    sixthdayimage = json_data['list'][5]['weather'][0]['icon']
    img = (Image.open(f"icon/{sixthdayimage}@2x.png"))
    resized_image = img.resize((60, 60))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    tempday6 = int(json_data['list'][5]['main']['temp'] - 273.15)
    descday6 = json_data['list'][5]['weather'][0]['description']
    city = json_data['city']['name']

    day6temp.config(text=f"\n {tempday6} ºC  \n {descday6}")

    # Box 7
    sevendayimage = json_data['list'][6]['weather'][0]['icon']
    img = (Image.open(f"icon/{sevendayimage}@2x.png"))
    resized_image = img.resize((60, 60))
    photo7 = ImageTk.PhotoImage(resized_image)
    sevenimage.config(image=photo7)
    sevenimage.image = photo7

    tempday7 = int(json_data['list'][6]['main']['temp'] - 273.15)
    descday7 = json_data['list'][6]['weather'][0]['description']
    city = json_data['city']['name']

    day7temp.config(text=f"\n {tempday7} ºC  \n {descday7}")

    # Dias da semana
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    first = datetime.now()

    # Configuração para babel
    locale_str = 'pt_BR'

    second = first+timedelta(days=1)
    day2.config(text=format_date(second, 'EEEE', locale=locale_str).capitalize())

    third = first+timedelta(days=2)
    day3.config(text=format_date(third, 'EEEE', locale=locale_str).capitalize())

    fourth = first+timedelta(days=3)
    day4.config(text=format_date(fourth, 'EEEE', locale=locale_str).capitalize())

    fifth = first+timedelta(days=4)
    day5.config(text=format_date(fifth, 'EEEE', locale=locale_str).capitalize())

    sixth = first+timedelta(days=5)
    day6.config(text=format_date(sixth, 'EEEE', locale=locale_str).capitalize())

    seven = first+timedelta(days=6)
    day7.config(text=format_date(seven, 'EEEE', locale=locale_str).capitalize())

def update_logo():
    current_time = datetime.now().strftime("%H:%M:%S %p")
    if "06:00:00" <= current_time <= "19:00:00":
        logo_image.configure(file="./assets/weather_icon_dia.png")
    else:
        logo_image.configure(file="./assets/weather_icon_noite2.png")
    root.after(60000, update_logo)


# --------------------------- Visual -----------------------------------

# Icone da tela
image_icon = PhotoImage(file="./assets/logo.png")
root.iconphoto(False, image_icon)

max_width = 90

# Caixa onde ira aparecer a temperatura
round_box = PhotoImage(file="./assets/round_box.png")
Label(root, image=round_box, bg="#FFFFFF").place(x=270, y=110)

# Label das informaçoes da round_box
label1 = Label(root, text="Temperatura:", font=('Helvetica', 10, "bold"), fg="#FBEC9A", bg="#00C3FF")
label1.place(x=276, y=124)

label2 = Label(root, text="Humidade:", font=('Helvetica', 10, "bold"), fg="#FBEC9A", bg="#00C3FF")
label2.place(x=276, y=144)

label3 = Label(root, text="Pressão:", font=('Helvetica', 10, "bold"), fg="#FBEC9A", bg="#00C3FF")
label3.place(x=276, y=164)

label4 = Label(root, text="Vento:", font=('Helvetica', 10, "bold"), fg="#FBEC9A", bg="#00C3FF")
label4.place(x=276, y=184)

label5 = Label(root, text="Descrição:", font=('Helvetica', 10, "bold"), fg="#FBEC9A", bg="#00C3FF")
label5.place(x=276, y=204)

# Temperaturas
temperature = Label(root, text="...", font=("Helvetica", 10, "bold"), fg="#FBEC9A", bg="#00C3FF")
temperature.config(anchor='e')
temperature.place(x=510, y=124, width=max_width)

humidity_weather = Label(root, text="...", font=("Helvetica", 10, "bold"), fg="#FBEC9A", bg="#00C3FF")
humidity_weather.config(anchor='e')
humidity_weather.place(x=510, y=144, width=max_width)

pressure_weather = Label(root, text="...", font=("Helvetica", 10, "bold"), fg="#FBEC9A", bg="#00C3FF")
pressure_weather.config(anchor='e')
pressure_weather.place(x=510, y=164, width=max_width)

wind_speed = Label(root, text="...", font=("Helvetica", 10, "bold"), fg="#FBEC9A", bg="#00C3FF")
wind_speed.config(anchor='e')
wind_speed.place(x=510, y=184, width=max_width)

description_weather = Label(root, text="...", font=("Helvetica", 10, "bold"), fg="#FBEC9A", bg="#00C3FF")
description_weather.config(anchor='e')
description_weather.place(x=510, y=204, width=max_width)

# Imagens ao lado da temperatura do dia
logo_image = PhotoImage(file="./assets/logo.png")
logo = Label(image=logo_image, bg="#FFFFFF")
logo.place(x=10, y=110)
update_logo()

# temperatura do dia
temp_right = Label(text="...", font=("arial", 30, "bold"), bg="#FFFFFF", fg="#FACB1B")
temp_right.place(x=160, y=120)

# Caixa de pesquisa
search_image = PhotoImage(file=r"assets/search_box.png")
myImage = Label(image=search_image, bg="#FFFFFF")
myImage.place(x=270, y=20)

# Icone esquerdo da caixa de pesquisa
weat_image = PhotoImage(file="assets/icone_search(24 x 24).png")
weather_image = Label(root, image=weat_image, bg="#00C3FF")
weather_image.place(x=275, y=24)

textfield = tk.Entry(root, justify="left", width=15, font=("poppins", 16), bg="#00C3FF", border=0, fg="white")
textfield.place(x=310, y=24)
textfield.focus()

# Icone de pesquisa do botao de pesquisa
search_icone = PhotoImage(file="./assets/search_(24 x 24).png")
image_search = Button(image=search_icone, border=0, cursor="hand2", bg="#00C3FF", command=get_weather)
image_search.place(x=570, y=24)

# Dia da semana
week = Label(root, text="...", font=("Helvetica", 22, "bold"), fg="#162228", bg="#FFFFFF")
week.place(x=30, y=20)

# Time zone
timezone = Label(root, text="...", font=("Helvetica", 18), fg="#162228", bg="#FFFFFF")
timezone.place(x=620, y=20)

long_lat = Label(root, font=("Helvetica", 10), fg="#162228", bg="#FFFFFF")
long_lat.place(x=620, y=50)

# frame da parte de baixo da tela
frame = Frame(root, width=890, height=160, bg="#FFFFFF")
frame.pack(side=BOTTOM)

# Bottom boxes
firstbox = PhotoImage(file="./assets/box_pequeno2.png")
secondbox = PhotoImage(file="./assets/box_pequeno2.png")

# as FRAME que fica dentro das box
Label(frame, image=secondbox, bg="#FFFFFF").place(x=20, y=20) # 2 box
Label(frame, image=secondbox, bg="#FFFFFF").place(x=160, y=20) # 3 box
Label(frame, image=secondbox, bg="#FFFFFF").place(x=300, y=20) # 4 box
Label(frame, image=secondbox, bg="#FFFFFF").place(x=440, y=20) # 5 box
Label(frame, image=secondbox, bg="#FFFFFF").place(x=580, y=20) # 6 box
Label(frame, image=secondbox, bg="#FFFFFF").place(x=720, y=20) # 7 box

# 2 box
secondFrame = Frame(root, width=90, height=118, bg="#00C3FF")
secondFrame.place(x=30, y=336)

day2 = Label(secondFrame, bg="#00C3FF", fg="white", font="poppins 10 bold")
day2.place(relx=0.5, rely=0.09, anchor="center")

secondimage = Label(secondFrame, bg="#00C3FF")
secondimage.place(relx=0.5, rely=0.43, anchor="center")

day2temp = Label(secondFrame, bg="#00C3FF", fg="#fff", text="...",  font="poppins 10 bold")
day2temp.place(relx=0.5, rely=0.75, anchor="center")

# 3 box
thirdFrame = Frame(root, width=90, height=118, bg="#00C3FF")
thirdFrame.place(x=170, y=336)

day3 = Label(thirdFrame, bg="#00C3FF", fg="white", font="poppins 10 bold")
day3.place(relx=0.5, rely=0.09, anchor="center")

thirdimage = Label(thirdFrame, bg="#00C3FF")
thirdimage.place(relx=0.5, rely=0.43, anchor="center")

day3temp = Label(thirdFrame, bg="#00C3FF", fg="#fff", text="...", font="poppins 10 bold")
day3temp.place(relx=0.5, rely=0.75, anchor="center")

# 4 box
fourthFrame = Frame(root, width=90, height=118, bg="#00C3FF")
fourthFrame.place(x=310, y=336)

day4 = Label(fourthFrame, bg="#00C3FF", fg="white", font="poppins 10 bold")
day4.place(relx=0.5, rely=0.09, anchor="center")

fourthimage = Label(fourthFrame, bg="#00C3FF")
fourthimage.place(relx=0.5, rely=0.43, anchor="center")

day4temp = Label(fourthFrame, bg="#00C3FF", fg="#fff", text="...", font="poppins 10 bold")
day4temp.place(relx=0.5, rely=0.75, anchor="center")

# 5 box
fifthFrame = Frame(root, width=90, height=118, bg="#00C3FF")
fifthFrame.place(x=450, y=336)

day5 = Label(fifthFrame, bg="#00C3FF", fg="white", font="poppins 10 bold")
day5.place(relx=0.5, rely=0.09, anchor="center")

fifthimage = Label(fifthFrame, bg="#00C3FF")
fifthimage.place(relx=0.5, rely=0.43, anchor="center")

day5temp = Label(fifthFrame, bg="#00C3FF", fg="#fff", text="...", font="poppins 10 bold")
day5temp.place(relx=0.5, rely=0.75, anchor="center")

# 6 box
sixthFrame = Frame(root, width=90, height=118, bg="#00C3FF")
sixthFrame.place(x=590, y=336)

day6 = Label(sixthFrame, bg="#00C3FF", fg="white", font="poppins 10 bold")
day6.place(relx=0.5, rely=0.09, anchor="center")

sixthimage = Label(sixthFrame, bg="#00C3FF")
sixthimage.place(relx=0.5, rely=0.43, anchor="center")

day6temp = Label(sixthFrame, bg="#00C3FF", fg="#fff", text="...", font="poppins 10 bold")
day6temp.place(relx=0.5, rely=0.75, anchor="center")

# 7 box
sevenFrame = Frame(root, width=100, height=118, bg="#00C3FF")
sevenFrame.place(x=730, y=336)

day7 = Label(sevenFrame, bg="#00C3FF", fg="white", font="poppins 10 bold")
day7.place(relx=0.5, rely=0.09, anchor="center")

sevenimage = Label(sevenFrame, bg="#00C3FF")
sevenimage.place(relx=0.5, rely=0.43, anchor="center")

day7temp = Label(sevenFrame, bg="#00C3FF", fg="#fff", text="...", font="poppins 9 bold")
day7temp.place(relx=0.5, rely=0.75, anchor="center")

root.mainloop()