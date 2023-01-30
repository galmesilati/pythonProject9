import requests

response = requests.get('https://api.nationalize.io/',
                        params={'name': 'name'})
name = input("insert your name:")
if response.status_code == 200:
    my_data = response.json()
    name = sorted(my_data['country'], key=lambda x: x['probability'])[-1]
    print(name)

    response_country = requests.get('https://restcountries.com/v3.1/alpha', params={"codes": "country_id"})
    if response.status_code == 200:
        my_code = response.json()
        print(type(my_code))
        print(my_code)
        for index in range(len(my_code)):
            for key in my_code[index]:
                print(my_code[index][""])

    # response2 = requests.get('https://restcountries.com/v3.1/alpha/IL')
    # if response2.status_code == 200:
    #     my_code = response2.json()
    #     country = my_code['name']['common']
    #     print(country)









