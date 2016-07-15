
# coding: utf-8

# In[1]:

import requests
import json
import time
from datetime import datetime
from collections  import  OrderedDict
from prettytable import PrettyTable  


Taiwan = ['TPE','KHH']
Japan = ['NRT', 'KIX', 'OKA', 'CTS']

search_date = input("搜尋航班日期(YYYYMMDD):")
print ("機場代號: TPE(桃園), KHH(高雄), NRT(成田), KIX(關西), OKA(沖繩), CTS(新千歲)")
search_origin = input("出發地:")
search_destination = input("目的地:")

if search_origin in Taiwan:
    search_currency = "TWD"
else:
    search_currency = "JPY"


search_month = datetime.strptime(search_date, "%Y%m%d").strftime("%Y%m")
url = "https://www.vanilla-air.com/api/booking/flight-fare/list.json?__ts=1467903532538&adultCount=1&channel=pc&childCount=0&couponCode=&currency="+search_currency+"&destination="+search_destination+"&infantCount=0&origin="+search_origin+"&targetMonth="+search_month+"&version=1.0"


res = requests.get(url)
data = json.loads(res.text, object_pairs_hook = OrderedDict)

for FlightDetailOfDays, FlightDetailOfDays_value in (data['Result']['FlightDetailOfDays'].items()):
    # 使用PrettyTable製作表格
    x = PrettyTable(["Date", "Flight", "KomiKomi", "Simple", "Seat"])  
    #x = PrettyTable(["Date", "Flight", "KomiKomi", "Simple", "WakuWaku", "Seat", "Waku Seat"])  
    x.align["Date"] = "l" # Left align city names
    x.padding_width = 1 # One space between column edges and contents (default)
    
    for i in range(len(FlightDetailOfDays_value['FlightDetails'])):
        date = FlightDetailOfDays
        flightnum = "JW" + FlightDetailOfDays_value['FlightDetails'][i]['FltNumber']
        komikomi_price = (FlightDetailOfDays_value['FlightDetails'][i]['InclusiveFare']['AdultFare']).split('#')[2]
        simple_price = (FlightDetailOfDays_value['FlightDetails'][i]['SimpleFare']['AdultFare']).split('#')[2]
        #wakuwaku_price = (FlightDetailOfDays_value['FlightDetails'][i]['CampaignFare']['AdultFare']).split('#')[2]
        seat = FlightDetailOfDays_value['FlightDetails'][i]['InclusiveFare']['AdultSeats']
        #waku_seat = FlightDetailOfDays_value['FlightDetails'][i]['CampaignFare']['AdultSeats']
        
        x.add_row([date, flightnum, komikomi_price, simple_price, seat]) 
        #x.add_row([date, flightnum, komikomi_price, simple_price, wakuwaku_price, seat, waku_seat]) 
        
    print (x)   


# In[ ]:




# In[ ]:



