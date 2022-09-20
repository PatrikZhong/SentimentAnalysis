#Copyright (c) Microsoft Corporation. All rights reserved.
#Licensed under the MIT License.

# -*- coding: utf-8 -*-

import json
import os 
from pprint import pprint
import requests
import array

'''
This sample makes a call to the Bing Web Search API with a query and returns relevant web search.
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
'''

# Add your Bing Search V7 subscription key and endpoint to your environment variables.

endpoint = "https://api.nytimes.com/svc/archive/v1/2019/1.json?fq=web_url&api-key=ITSlccGJGygYCcGzGl9asNmpjIfs2hjR"

try:
    response = requests.get(endpoint)
    response.raise_for_status()

    # print("Headers:")
    # print(response.headers)

    json_data = response.json() #dictionary
    # print(json_data['response'])
    # docs = json_data["response"]["docs"]
    documents = json_data["response"]["docs"]
    amountOfArticles = len(documents)

    print(amountOfArticles)
    print(type(documents))

    for x in range(amountOfArticles):
        
        headline = json_data["response"]["docs"][x]["headline"]["main"]
        lead_paragraph = json_data["response"]["docs"][x]["lead_paragraph"]
        pub_date = json_data["response"]["docs"][x]["pub_date"]
        with open('json.txt', 'a') as f:
            json.dump(headline + "*", f, indent=4)
            json.dump(lead_paragraph + "*", f, indent=4)
            json.dump(pub_date + "*", f, indent=4)
        
    

    # with open('testfil.txt', 'w') as f:
    #     (json.dump(lead_paragraph, f, indent=4))

    # stringified_json = json.dumps(json_data)
    # copyright = pyjq.all('.copyright', json_data)
    # print(copyright)
    # jq_query = '.response .docs [] | {{the_snippet: .snippet, the_headline: .headline .main, the_date: .pub_date, the_news_desk: .news_desk}}' 
    # open("testfil.txt", "w")
    # output = pyjq.all(jq_query, json_data)



except Exception as ex:
    raise ex