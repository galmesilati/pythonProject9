import json

import requests

if __name__ == '__main__':
    board_url = "https://www.boredapi.com/api/activity"
    response = requests.get(board_url)
    if response.status_code == 200:
        my_data = response.json()
        print(my_data)
    print(f"the type of response.text: {type(response.text)}")
    response_as_dict = json.loads(response.text)
    print(f"the type of response_as_dict: {type(response_as_dict)}")
    print(f"activity: {response_as_dict['activity']}")

if __name__ == '__main__':
    bored_url = 'https://www.boredapi.com/api/activity'
    response = requests.get(bored_url)
    print(json.loads(response.text)['activity'])
    print(type(json.loads(response.text)))

    # option 2
    my_data = response.json()
    print(my_data['activity'])

    # 200 code:
    if response.status_code == 200:
        pass

if __name__ == '__main__':
    genderize_url = 'https://api.genderize.io'
    response = requests.get(genderize_url,
                            params={'name': 'gal'})
    if response.status_code == 200:
        print(response.json()['gender'])



