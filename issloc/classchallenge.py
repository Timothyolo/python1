#!/usr/bin/python3
"""Alta3 Research | <your name here>
   Using an HTTP GET to determine when the ISS will pass over head"""

# python3 -m pip install requests
import requests

import time

time_api="http://api.open-notify.org/iss-pass.json?lat=47.6&lon=-122.3"

def main():
     latitude = float(input("enter your latitude\n"))
     if(latitude >80.8 or latitude<-80):
         latitude = 0
         print("The maximum and the minimum latitude is between 80.8 and -80")

         longitude = float(input("enter your latitude\n"))
     if(longitude >70.7 or longitude<-70.5):
         longitude = 0
         print("The maximum and the minimum longitude is between 70.7 and -70.5")

         seattle = requests.get(f"{time_api}?lat={latitude}&1on={longitude}")
         seattle = seattle.json()

         newtime = time.ctime(seattle["risetime"])
         print(newtime)

    





if __name__ == "__main__":
    main()

