from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

import requests

def get_country_by_name(name:str):
    response = requests.get('https://api.nationalize.io/', params={'name': name})
    if response.status_code == 200:
        my_data = response.json()
        name = sorted(my_data['country'], key=lambda x: x['probability'])[-1]
        print(name)
    response_country = requests.get('https://restcountries.com/v3.1/alpha', params={"codes": "country_id"})
    if response.status_code == 200:
        my_code = response.json()
        print(my_code)
        for index in range(len(my_code)):
            for key in my_code[index]:
                print(my_code[index][""])

if __name__ == '__main__':
    get_country_by_name('gal')
    with ThreadPoolExecutor(3) as executor:
        names = []
        for name in names:
            name = executor.submit(get_country_by_name, name)
            names.append(name)
        print("All name submitted")
        results = []
        for name in as_completed(names):
            if name.exception():
                print("error", name.exception())
            result = name.result()
            results.append(result)









    # response2 = requests.get('https://restcountries.com/v3.1/alpha/IL')
    # if response2.status_code == 200:
    #     my_code = response2.json()
    #     country = my_code['name']['common']
    #     print(country)
    #test to delete








