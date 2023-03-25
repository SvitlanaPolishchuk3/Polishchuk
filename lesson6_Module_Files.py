from datetime import datetime
from datetime import date
import os


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")


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
        f.write(f"{self.intro}\n{self.news1}\n{self.city}, {self.time1}\n{self.ending}")
        f.close()


class Ad:
    def __init__(self, intro, adtext, ending, year, month, day):
        self.intro = intro
        self.adtext = adtext
        self.ending = ending
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
        p2 = Ad("\n\nPrivate Ad ------------------", self.getad(), "------------------------------", self.getyear(), self.getmonth(), self.getday())
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


with open('Newsfeed.txt', 'w') as file:
    pass


while True:
    print("Main menu")
    print("Press 1 for News")
    print("Press 2 for Ad")
    print("Press 3 for Weather forecast")
    print("Press 4 for import from files")
    # print("Press 5 for Ad_import")
    # print("Press 6 for Weather forecast_import")
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
        # d.publish_news()


    elif (choice==9):
        break
    else:
        print("invalid user input")
        continue

