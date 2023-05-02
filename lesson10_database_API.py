from datetime import datetime
from datetime import date
import os
import csv
import re


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")


def count_w():
    file = open("Newsfeed.txt", "rt")
    text = file.read()

    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    print(words)
    unique_words = set(words)

    with open('csv_words.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='-')
        for i in unique_words:
            if str(i).isdigit():
                continue

            writer.writerow([i, words.count(i)])

def count_l():
    file = open("Newsfeed.txt", "rt")
    text = file.read()
    letters = []
    for i in text:
        if str(i).isalpha():
            letters.append(i)

    letters_low = []
    for i in letters:
        letters_low.append(i.lower())
    unique_letters = set(letters_low)


    with open('csv_letters.csv', 'w', newline='') as csvfile:
        headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
        writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter=',')
        writer.writeheader()
        for i in unique_letters:
            writer.writerow({'letter':i, 'count_all':letters_low.count(i), 'count_uppercase':letters.count(i.upper()), 'percentage':round((letters_low.count(i)/len(letters_low)*100),2)})


class Newsblock:
    def __init__(self, news1, city):
        self.intro = "\nNews -------------------------"
        self.news1 = news1
        self.city = city
        self.time1 = dt_string
        self.ending = "------------------------------"

    def __str__(self):
        return f"{self.intro}\n{self.news1}\n{self.city}, {self.time1}\n{self.ending}"
    def publish_smth(self):
        f = open("Newsfeed.txt", "a")
        # f.write(func_capitalize_sentences(f"{self.intro}\n{self.news1}\n{self.city}, {self.time1}\n{self.ending}"))
        m = NewsfeedImporter()
        m.import_news(title=self.news1, city=self.city)

        f.write(f"{self.intro}\n{self.news1}\n{self.city}, {self.time1}\n{self.ending}")
        f.close()


class Ad:
    def __init__(self,  adtext, year, month, day):
        self.intro = "\nAd-------------"
        self.adtext = adtext
        self.ending = "------------------------------"
        self.year = year
        self.month = month
        self.day = day

    def countdaysleft(self):
        expiredate = (date(self.year, self.month, self.day) - date.today()).days
        return expiredate

    def __str__(self):
        return f"{self.intro}\n{self.adtext}\n{self.countdaysleft()}\n{self.ending}"

    def publish_smth(self):
        f = open("Newsfeed.txt", "a")
        m = NewsfeedImporter()
        m.import_ad(text=self.adtext, actual_day=self.day, actual_month=self.month, actual_year=self.year)

        f.write(f"{self.intro}\n{self.adtext}\nActual until: {self.day}/{self.month}/{self.year}, {self.countdaysleft()} days left \n{self.ending}")
        f.close()


class Weather:
    def __init__(self, weather1, weather2, weather3):
        self.intro = "\nWeather forecast-------------"
        self.weather1 = weather1
        self.weather2 = weather2
        self.weather3 = weather3
        self.ending = "------------------------------"

    def __str__(self):
        return f"{self.intro}\n{self.weather1}\n{self.weather2}{self.weather3}\n{self.ending}"

    def publish_smth(self):
        f = open("Newsfeed.txt", "a")
        m = NewsfeedImporter()
        m.import_weather(text_one=self.weather1, text_two=self.weather2, text_three=self.weather3)

        f.write(f"{self.intro}\n{self.weather1}\n{self.weather2}\n{self.weather3}\n{self.ending}")
        f.close()


class Dir:
    def __init__(self):
        self.news = ""
        self.city = ""
        self.ad = ""
        self.year = ""
        self.month = ""
        self.day = ""
        self.path1 = ""
        self.weather1 = ""
        self.weather2 = ""
        self.weather3 = ""
        directory = os.path.join(path1)
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith("news.txt"):
                    f = open(os.path.join(subdir, file), 'r')
                    a = f.readline()
                    self.news = a
                    b = f.readline()
                    self.city = b
                    print(a)
                    f.close()
                    self.publish_news()
                    path_to_file = os.path.join(path1+"\\"+str(file))
                    os.remove(path_to_file)


        #path1 = ""
        directory = os.path.join(path1)
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith("ad.txt"):
                    f = open(os.path.join(subdir, file), 'r')
                    a = f.readline()
                    self.ad = a
                    b = f.readline()
                    self.year = b
                    c = f.readline()
                    self.month = c
                    d = f.readline()
                    self.day = d
                    print(a)
                    f.close()
                    self.publish_ad()
                    path_to_file = os.path.join(path1 + "\\" + str(file))
                    os.remove(path_to_file)


        directory = os.path.join(path1)
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith("weather.txt"):
                    f = open(os.path.join(subdir, file), 'r')
                    a = f.readline()
                    self.weather1 = a
                    b = f.readline()
                    self.weather2 = b
                    c = f.readline()
                    self.weather3 = c
                    print(a)
                    f.close()
                    self.publish_weather()
                    path_to_file = os.path.join(path1 + "\\" + str(file))
                    os.remove(path_to_file)

    def getcity(self):
        return self.city

    def getnews(self):
        return self.news

    def getad(self):
        return self.ad

    def getyear(self):
        return int(self.year)

    def getmonth(self):
        return int(self.month)

    def getday(self):
        return int(self.day)

    def publish_news(self):
        p1 = Newsblock(self.getnews(), self.getcity())
        p1.publish_smth()

    def publish_ad(self):
        p2 = Ad(self.getad(), self.getyear(), self.getmonth(), self.getday())
        p2.publish_smth()


    def publish_weather(self):
        p1 = Weather(self.getweather1(), self.getweather2(), self.getweather3())
        p1.publish_smth()


    def getweather1(self):
        return self.weather1

    def getweather2(self):
        return self.weather2

    def getweather3(self):
        return self.weather3


import json
import os


class JSONProcessor:
    def __init__(self, filepath=''):
        self.filepath = filepath

    def setpath(self, filepath):
        self.filepath = filepath

    def process(self):
        try:
            with open(self.filepath) as f:
                data = json.load(f)
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Invalid JSON format.")
        for i in data["objects"]:
            if i["type"] == "news":
                element = Newsblock(i["text"], i["city"])
                element.publish_smth()
            elif i["type"] == "ad":
                element = Ad(i["text"], int(i["expire_year"]), int(i["expire_month"]), int(i["expire_date"]))
                element.publish_smth()
            elif i["type"] == "weather":
                element = Weather(i["text1"], i["text2"], i["text3"])
                element.publish_smth()
        os.remove(self.filepath)
        print("File successfully processed and removed.")


import os
import xml.etree.ElementTree as ET

class XMLRecordProvider:
    def __init__(self, filepath=''):
        self.filepath = filepath

    def setpath(self, filepath):
        self.filepath = filepath


    def process(self):
        tree = ET.parse(self.filepath)
        root = tree.getroot()
        for i in root:
            if i.find("TYPE").text == "News":
                element = Newsblock(i.find("TEXT").text, i.find("CITY").text)
                element.publish_smth()
            elif i.find("TYPE").text == "Ad":
                element = Ad(i.find("TEXT").text, int(i.find("EXPIREYEAR").text), int(i.find("EXPIREMONTH").text), int(i.find("EXPIREDATE").text))
                element.publish_smth()
            elif i.find("TYPE").text == "Weather":
                element = Weather(i.find("TEXT1").text, i.find("TEXT2").text, i.find("TEXT3").text)
                element.publish_smth()
        os.remove(self.filepath)
        print("File successfully processed and removed.")

import pyodbc
import sqlite3
class NewsfeedImporter:
    def __init__(self):
        # self.db_file = 'db_newsfeed.db'
        self.conn = pyodbc.connect(f"Driver=SQLite3 ODBC Driver;Database=db_newsfeed.db;")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS news (title TEXT, city TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS ads (text TEXT, actual_day TEXT, actual_month TEXT, actual_year TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS weather (text_one TEXT, text_two TEXT, text_three TEXT)")

    def import_news(self, title, city):
        self.cursor.execute(f"SELECT title, city FROM news WHERE title = '{title}' and city= '{city}'")
        duplicate = self.cursor.fetchall()
        if len(duplicate)==0:
            self.cursor.execute(f"INSERT INTO news (title, city) VALUES ('{title}', '{city}')")
            print('added to db')
        else:
            print('value not added')


    def import_ad(self, text, actual_day, actual_month, actual_year):
        self.cursor.execute(f"SELECT text, actual_day, actual_month, actual_year FROM ads WHERE text = '{text}' and actual_day= '{actual_day}' and actual_month= '{actual_month}' and actual_year= '{actual_year}'")
        duplicate = self.cursor.fetchall()
        if len(duplicate)==0:
            self.cursor.execute(f"INSERT INTO ads (text, actual_day, actual_month, actual_year) VALUES ('{text}', '{actual_day}', {actual_month}, {actual_year})")
            print('added to db')
        else:
            print('value not added')

    def import_weather(self, text_one, text_two, text_three):
        self.cursor.execute(f"SELECT text_one, text_two, text_three FROM weather WHERE text_one = '{text_one}' and text_two= '{text_two}' and text_three= '{text_three}'")
        duplicate = self.cursor.fetchall()
        if len(duplicate)==0:
            self.cursor.execute(f"INSERT INTO weather (text_one, text_two, text_three) VALUES ('{text_one}', '{text_two}', '{text_three}')")
            print('added to db')
        else:
            print('value not added')


    def __del__(self):
        self.cursor.commit()
        self.cursor.close()
        self.conn.close()


with open('Newsfeed.txt', 'w') as file:
    pass


while True:
    print("Main menu")
    print("Press 1 for News")
    print("Press 2 for Ad")
    print("Press 3 for Weather forecast")
    print("Press 4 for News_import")
    print("Press 5 for JSON_input")
    print("Press 6 for xml_input")
    print("Press 9 to exit program")
    choice=eval(input("Choose what to publish ="))
    if (choice==1):
        print("Write news in console")
        news1=input("Print news here =")
        city1=input("Print city here =")
        p1 = Newsblock(news1, city1)
        p1.publish_smth()


    elif (choice==2):
        print("Write an ad in console:")
        ad1=input("Print ad here =")
        year=int(input("Print expire year here ="))
        month = int(input("Print expire month here ="))
        day = int(input("Print expire day here ="))
        p2 = Ad("\n\nPrivate Ad ------------------", ad1, "------------------------------", year, month, day)
        p2.publish_smth()


    elif (choice==3):
        print("Write a weather forecast in console:")
        weath1 = input("Print weather for today in Ukraine =")
        weath2 = input("Print weather for 7 days in Ukraine =")
        weath3 = input("Print weather for other countries =")
        r = Weather(weath1, weath2, weath3)
        r.publish_smth()

    elif (choice==4):
        path1 = input("Print path to the file =")
        d = Dir()
        p1 = Newsblock(d.getnews(), d.getcity())
        p1.publish_smth()

    elif (choice==5):
        path1 = input("Print path to the file =")
        d = JSONProcessor()
        d.setpath(path1)
        d.process()
        # p1 = Newsblock(d.getnews(), d.getcity())
        # p1.publish_smth()

    elif (choice==6):
        path1 = input("Print path to the file =")
        d = XMLRecordProvider()
        d.setpath(path1)
        d.process()


    elif (choice==9):
        break
    else:
        print("invalid user input")
        continue
    count_w()
    count_l()