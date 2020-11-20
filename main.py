#! python3.8

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
import sys
import requests
import json


class WeatherApp(QMainWindow):
	def __init__(self):
		super(WeatherApp, self).__init__()
		self.setFixedSize(400, 400)
		self.setWindowTitle("Weather App")
		self.ui()

	def ui(self):
		self.label = QtWidgets.QLabel("Country", self)
		self.label.move(100, 150)

		self.label_1 = QtWidgets.QLabel("Country:", self)
		self.label_1.move(30, 150)


		self.label2 = QtWidgets.QLabel("City", self)
		self.label2.move(100, 200)

		self.label2_1 = QtWidgets.QLabel("City:", self)
		self.label2_1.move(30, 200)


		self.label3 = QtWidgets.QLabel("Temperature", self)
		self.label3.move(100, 250)

		self.label3_1 = QtWidgets.QLabel("Temperature:", self)
		self.label3_1.move(30, 250)


		self.label4 = QtWidgets.QLabel("Feels like", self)
		self.label4.move(100, 300)

		self.label4_1 = QtWidgets.QLabel("Feels like:", self)
		self.label4_1.move(30, 300)


		self.label5 = QtWidgets.QLabel("Clouds", self)
		self.label5.move(100, 350)

		self.label5_1 = QtWidgets.QLabel("Clouds:", self)
		self.label5_1.move(30, 350)


		self.label6 = QtWidgets.QLabel("Pressure", self)
		self.label6.move(300, 150)

		self.label6_1 = QtWidgets.QLabel("Pressure:", self)
		self.label6_1.move(230, 150)


		self.label7 = QtWidgets.QLabel("Humidity", self)
		self.label7.move(300, 200)

		self.label7_1 = QtWidgets.QLabel("Humidity:", self)
		self.label7_1.move(230, 200)


		self.label8 = QtWidgets.QLabel("Longitude", self)
		self.label8.move(300, 300)

		self.label8_1 = QtWidgets.QLabel("Longitude:", self)
		self.label8_1.move(230, 300)


		self.label9 = QtWidgets.QLabel("Latitude", self)
		self.label9.move(300, 250)

		self.label9_1 = QtWidgets.QLabel("Latitude:", self)
		self.label9_1.move(230, 250)


		self.b1 = QtWidgets.QPushButton("Find", self)
		self.b1.clicked.connect(self.clicked)
		self.b1.resize(80, 29)
		self.b1.move(50, 50)

		self.b2 = QtWidgets.QPushButton("Exit", self)
		self.b2.clicked.connect(QApplication.instance().quit)
		self.b2.resize(130, 29)
		self.b2.move(230, 350)

		self.city_edit = QLineEdit("Kyiv", self)
		self.city_edit.move(250, 50)
		self.city_edit.resize(80, 29)

	def clicked(self):
		longitude, latitude, clouds, temp, feels_like, pressure, \
			humidity, country, city_name = self.weather()
            
		self.label.setText(country)
		self.label2.setText(city_name)
		self.label3.setText(str(temp))
		self.label4.setText(str(feels_like))
		self.label5.setText(clouds)
		self.label6.setText(str(pressure))
		self.label7.setText(str(humidity))
		self.label8.setText(str(longitude))
		self.label9.setText(str(latitude))

	def weather(self):
		api_key = ""
       # API key can be register on https://openweathermap.org/
		city = self.city_edit.text()

		w_result = requests.get("https://api.openweathermap.org/data/2.5/" + 
			"weather?q=" + city + "&units=metric&appid=" + api_key).json()
		l = w_result["coord"]["lon"]
		l2 = w_result["coord"]["lat"]
		c = w_result["weather"][0]["description"]
		t = w_result["main"]["temp"]
		f = w_result["main"]["feels_like"]
		p = w_result["main"]["pressure"]
		h = w_result["main"]["humidity"]
		c2 = w_result["sys"]["country"]
		c3 = w_result["name"]

		return (l, l2, c, t, f, p, h, c2, c3)



def window():
	app = QApplication(sys.argv)
	wnd = WeatherApp()
	wnd.show()
	sys.exit(app.exec_())

window()
