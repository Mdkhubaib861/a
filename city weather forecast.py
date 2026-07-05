import requests
from tkinter import *
import csv
from tkinter import filedialog
import pyscreenshot as ImageGrab
from reportlab.pdfgen import canvas
'''
city = input("Enter city: ")

# Get lat & lon
url1 = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
data1 = requests.get(url1, headers={"User-Agent": "app"}).json()

if not data1:
    print("City not found")
    exit()

lat = data1[0]['lat']
lon = data1[0]['lon']

# Get weather
API_KEY = "YOUR_API_KEY"
url2 = f"https://weather.googleapis.com/v1/currentConditions:lookup?location.latitude={lat}&location.longitude={lon}&key=AIzaSyBkcmchhtQh8z-7tLV76T4_t9bSGxbWCWk"
data2 = requests.get(url2).json()

if 'error' in data2:
    print("API Error:", data2['error']['message'])
    exit()



# Extract data
temp = data2['temperature']['degrees']
condition = data2['weatherCondition']['description']['text']
humidity = data2['relativeHumidity']
wind = data2['wind']['speed']['value']

# Output
print(f"\nWeather in {city}:")
print(f"Temp: {temp}°C")
print(f"Condition: {condition}")
print(f"Humidity: {humidity}%")
print(f"Wind: {wind} km/h")

'''

window=Tk()
window.title("Weather API")
window.resizable(width=False, height=False)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)


ct=StringVar()
lat_val=StringVar()
lon_val=StringVar()
timezone =StringVar()
temp=StringVar()
max_temp=StringVar()
min_temp=StringVar()
humidity=StringVar()
condition=StringVar()

def getLatLong():
    city=ct.get()
    url1 = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
    data1 = requests.get(url1, headers={"User-Agent": "app"}).json()
    print(data1[0]['lat'],data1[0]['lon'])
    lat_val.set(data1[0]['lat'])
    lon_val.set(data1[0]['lon'])

    url2 = f"https://weather.googleapis.com/v1/currentConditions:lookup?location.latitude={lat_val.get()}&location.longitude={lon_val.get()}&key=AIzaSyBkcmchhtQh8z-7tLV76T4_t9bSGxbWCWk"
    data2 = requests.get(url2).json()
    timezone.set(data2['timeZone']['id'])
    temp.set(f"{data2['temperature']['degrees']} °C")
    max_temp.set(f"{data2['currentConditionsHistory']['maxTemperature']['degrees']} °C")
    min_temp.set(f"{data2['currentConditionsHistory']['minTemperature']['degrees']} °C")
    humidity.set(f"{data2['relativeHumidity']}%")
    condition.set(data2['weatherCondition']['description']['text'])

def save_csv():

    file = "weather_report.csv"

    with open(file, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if f.tell() == 0:
            writer.writerow([
                "City",
                "Latitude",
                "Longitude",
                "Time Zone",
                "Current Temperature",
                "Max Temp",
                "Min Temp",
                "Condition",
                "Humidity"
            ])

        writer.writerow([
            ct.get(),
            lat_val.get(),
            lon_val.get(),
            timezone.get(),
            temp.get(),
            max_temp.get(),
            min_temp.get(),
            condition.get(),
            humidity.get()
        ])

def save_gui_pdf():

    # Window position
    x = window.winfo_rootx()
    y = window.winfo_rooty()

    # Window size
    width = window.winfo_width()
    height = window.winfo_height()

    # Take screenshot
    img = ImageGrab.grab(bbox=(x, y, x + width, y + height))

    # Save temporary image
    img.save("weather_gui.png")

    # Create PDF
    pdf = canvas.Canvas("Weather_GUI_Report.pdf")

    # Insert image into PDF
    pdf.drawImage("weather_gui.png", 30, 300, width=520, height=350)

    pdf.save()

topbar = Frame(window, bg="#1e3d59", height=70)
topbar.grid(row=0, column=0, columnspan=4, sticky="ew")

topbar.grid_columnconfigure(0, weight=1)

title = Label(
    topbar,
    text="Weather Forecast Dashboard",
    bg="#1e3d59",
    fg="white",
    font=("Inter", 24, "bold")
)

title.grid(row=0, column=0, pady=15)

Label(window, text="City Name:",font=("Inter",16,"bold")).grid(row=1, column=0,padx=10, pady=10, sticky="w")

c1=Entry(window, textvariable=ct,width=30,font=("Robota",14))
c1.grid(row=1, column=1,padx=10, pady=10, sticky="w")

b1=Button(window,text="Go",command=getLatLong,font=("Inter",15,"bold"),bg="#a9a9a9",fg="black")
b1.grid(row=1, column=2, pady=10)

lat=Label(window, text="Latitude",font=("Inter",15,"bold"))
lat.grid(row=3, column=0,padx=10, pady=10, sticky="w")

lat1=Label(window, text="Latitude",textvariable=lat_val,font=("Inter",12))
lat1.grid(row=3, column=1,padx=10, pady=10, sticky="w")

lon=Label(window, text="Longitude",font=("Inter",15,"bold"))
lon.grid(row=4, column=0,padx=10, pady=10, sticky="w")

lon1=Label(window, text="Longitude",textvariable=lon_val,font=("Inter",12))
lon1.grid(row=4, column=1,padx=10, pady=10, sticky="w")

t_zone=Label(window, text="Time Zone",font=("Inter",15,"bold"))
t_zone.grid(row=5, column=0,padx=10, pady=10, sticky="w")

t_zone1=Label(window, text="Time Zone",textvariable=timezone,font=("Inter",12))
t_zone1.grid(row=5, column=1,padx=10, pady=10, sticky="w")

c_temp=Label(window, text="Current Temperature",font=("Inter",15,"bold"))
c_temp.grid(row=6, column=0,padx=10, pady=10, sticky="w")

c_temp1=Label(window, text="Current Temperature",textvariable=temp,font=("Inter",12),bg="Skyblue")
c_temp1.grid(row=6, column=1,padx=10, pady=10, sticky="w")

maxi_temp=Label(window, text="Max Temperature",font=("Inter",15,"bold"))
maxi_temp.grid(row=7, column=0,padx=10, pady=10, sticky="w")

maxi_temp1=Label(window, text="Max Temperature",textvariable=max_temp,font=("Inter",12))
maxi_temp1.grid(row=7, column=1,padx=10, pady=10, sticky="w")

mini_temp=Label(window, text="Min Temperature",font=("Inter",15,"bold"))
mini_temp.grid(row=8, column=0,padx=10, pady=10, sticky="w")

mini_temp1=Label(window, text="Min Temperature",textvariable=min_temp,font=("Inter",12))
mini_temp1.grid(row=8, column=1,padx=10, pady=10, sticky="w")

Humid=Label(window, text="Humidity",font=("Inter",15,"bold"))
Humid.grid(row=10, column=0,padx=10, pady=10, sticky="w")

Humid1=Label(window, text="Humidity",textvariable=humidity,font=("Inter",12))
Humid1.grid(row=10, column=1,padx=10, pady=10, sticky="w")

con=Label(window, text="Condition",font=("Inter",15,"bold"))
con.grid(row=9, column=0,padx=10, pady=10, sticky="w")

con1=Label(window, text="Condition",textvariable=condition,font=("Inter",12))
con1.grid(row=9, column=1,padx=10, pady=10, sticky="w")

b2=Button(window,text="Exit",font=("Inter",15,"bold"),
          bg="#ff3030",fg="black", width=15)

b2.grid(row=11, column=0, pady=15)


b3=Button(window,text="Save as PDF",font=("Inter",15,"bold"),
          bg="#7ac5cd",fg="black", width=15,command=save_gui_pdf)

b3.grid(row=11, column=1, pady=15)


b4=Button(window,text="Save as CSV file",font=("Inter",15,"bold"),
          bg="#66cd00",fg="black", width=15,command=save_csv)

b4.grid(row=11, column=2, pady=15)



window.mainloop()
