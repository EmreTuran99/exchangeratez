import requests
from datetime import date
from datetime import datetime
from bs4 import BeautifulSoup
import time
import tweepy

CONSUMER_KEY = 'QynIrY7A2cTlcETQqPMypQK5u'
CONSUMER_SECRET = 'Qv9ZzCRHgvClhtDX1XLJdIy70w8kVUagfiFCa6gVMuhuK8aRAN'
ACCESS_KEY = '465027258-PMmnsWdHxOJCuDbDPkKr2pXdDP7R8l2SUslepr2A'
ACCESS_SECRET = 'KNYMS90DRebxkZyORQekxq4AI4GVdAiTvZErZkJS7Dsuq'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

delay = 65
i = 0

URL = 'https://www.sozcu.com.tr'

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
amount_Dollar = soup.find_all("span", {"class": "f-value"})[0].text.replace("\n", "").strip()
amount_Euro = soup.find_all("span", {"class": "f-value"})[1].text.replace("\n", "").strip()
amount_AUX = soup.find_all("span", {"class": "f-value"})[2].text.replace("\n", "").strip()

while i == 0: 
    
    current = datetime.now()
    exact_time = current.strftime("%H:%M:%S")
    minute = current.strftime("%M")

    if(minute == '00' or minute == '15' or minute == '45' or minute == '30'):
        print('Time: {}' .format(exact_time))
        print('Dolar Rate: {}' .format(amount_Dollar))
        print('Euro Rate: {}' .format(amount_Euro))
        print('AUX Rate: {}\n' .format(amount_AUX))
        time.sleep(delay)
