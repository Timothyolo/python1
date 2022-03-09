#!/usr/bin/python3
"""Alta3 Research | <your name here>
   Using an HTTP GET to determine when the ISS will pass over head"""

# python3 -m pip install requests
import requests

import time

time_API="http://api.open-notify.org/iss-pass.json?lat=47.6&lon=-122.3"

def main():
       gotresp = requests.get(time_API)

       got_time = gotresp.json()
       
       print(got_dj)



if __name__ == "__main__":
    main()
i
