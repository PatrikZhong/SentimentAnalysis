#Copyright (c) Microsoft Corporation. All rights reserved.
#Licensed under the MIT License.

# -*- coding: utf-8 -*-

import json
import os 
from pprint import pprint
import requests
import pyjq

'''
This sample makes a call to the Bing Web Search API with a query and returns relevant web search.
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
'''

# Add your Bing Search V7 subscription key and endpoint to your environment variables.

subscription_key = "85e4ba1ea3b14be291c4047c46bd56f8"
endpoint = "https://api.nytimes.com/svc/archive/v1/2019/1.json?fq=web_url&api-key=ITSlccGJGygYCcGzGl9asNmpjIfs2hjR"


# Query term(s) to search for. 

# query = ""

# Construct a request
# mkt = 'en-US'
# params = { 'q': query, 'mkt': mkt }
# headers = { 'Ocp-Apim-Subscription-Key': subscription_key }


# Call the API
try:
    response = requests.get(endpoint)
    response.raise_for_status()

    print("Headers:")
    print(response.headers)


    print("JSON Response:")
    x_dict = response.json() #dictionarys
    # pprint(x_dict)
    # xDump = json.dumps(x) #dict to string
    # print("===========================================================================================")
    # y = json.loads(xDump) #string to dict
    # print(y["main"])
    # pprint(response.json())
    xDump = json.dumps(x_dict);
    file = open("testfil.txt", "a")
    file.write(xDump)

except Exception as ex:
    raise ex