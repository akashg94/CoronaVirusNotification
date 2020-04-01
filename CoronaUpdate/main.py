import pync
import os
import requests
from plyer import notification
from bs4 import BeautifulSoup

# fucntion to get the url
def getData(url):
    req = requests.get(url)
    return req.text
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

#function to get the data
if __name__ == "__main__":

    timeout = 5
    #getting the data from the website

    myhtmlData = getData("https://www.worldometers.info/coronavirus/country/us/")

    #using the soup api to parse the data

    soup = BeautifulSoup(myhtmlData,'html.parser')
    name_box = soup.find('div', attrs = {'class' : 'maincounter-number'})
    name = name_box.text.strip()

    notify(title = 'Corona virus alert',
            subtitle= 'With python',
            message= 'corona visu cases in usa ' + name)



