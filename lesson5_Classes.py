# class News:
#      f = open("guru99.txt", "w+")
#      def __init__(self, name):
#           self.name = name
#
# # news1 = News('News----')
#      f.write(News('News----'))
#      f.close()
# print(news1.name)


from datetime import datetime
from datetime import date
from datetime import time
# from datetime import strftime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")
print(dt_string)


class Newsblock:
    def __init__(self, intro, news1, city, time1, ending):
        self.intro = intro
        self.news1 = news1
        self.city = city
        self.time1 = time1
        self.ending = ending

    def __str__(self):
        return f"{self.intro}\n{self.news1}\n{self.city}, {self.time1}\n{self.ending}"
    def publish_smth(self):
        f = open("Newsfeed.txt", "w+")
        f.write(f"{self.intro}\n{self.news1}\n{self.city}, {self.time1}\n{self.ending}")
        f.close()

p1 = Newsblock("News -------------------------","This is news about cats", "Kyiv", "05.03.2023", "------------------------------")
p1.publish_smth()
print(p1)




def countdaysleft():
    expiredate = (date(2023, 3, 29) - date.today()).days
    return expiredate


print(str(countdaysleft())+" left")


while True:
    print("Main menu")
    print("Press 1 for News")
    print("Press 2 for Add")
    print("Press 3 for Weather")
    choice=eval(input("Choose what to publish ="))
    if (choice==1):
        choice2=input(variablefornews)
    else:
        break









