import json

import kwargs as kwargs
import requests

#2

response = requests.get('https://restcountries.com/v3.1/alpha/', params={co})
if response.status_code == 200:
    my_code = response.json()
    print(type(my_code))
    print(my_code)
    for index in range(len(my_code)):
        for key in my_code[index]:
            print(my_code[index][""])


    # common = list(map(lambda x: "{} {}".format(x["name"], my_code))
    # # common = my_code['name']['common']
    # # print(common)






