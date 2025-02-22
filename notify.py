import datetime #for reading present date
import time 
import requests #for retreiving coronavirus data from web
from plyer import notification #for getting notification on your PC


#Retrieving the data from the web
covidData = None    
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    #if the data is not fetched due to lack of internet
    print("Please! Check your internet connection")

#Crearting a notification 
if (covidData != None):
    #converting data into JSON format
    data = covidData.json()['Success']
    
    #repeating the loop for multiple times
    while(True):
        notification.notify(
            #title of the notification,
            title = "COVID19 Stats on {}".format(datetime.date.today()),
            #the body of the notification
            message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}\n Recovered : {recoveredCase}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data['active'],  
                        recoveredCase = data["recovered"]),
            #creating icon for the notification
            #we need to download a icon of ico file format
            app_icon = "bell-Icon.ico",
            # the notification stays for 50sec
            timeout  = 50
        )
        #sleep for 4 hrs => 60*60*4 sec
        #notification repeats after every 4hrs
        time.sleep(60*60*4)
