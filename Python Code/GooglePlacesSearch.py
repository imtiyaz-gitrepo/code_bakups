import requests, json

# enter your api key here
api_key = 'GOOGLE_API_KEY'
base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
query: str = 'Indian shops in harris park'
next_page_token = None
next_page_available = True
while next_page_available is True:
    url = None;
    if next_page_token is None:
        print('token is Null')
        url = base_url + 'location=harris park&radius=500&type=restaurant&keyword=Indian&key=' + api_key
        print(url)
    else:
        print('token is Not Null')
        url = base_url + 'location=harris park&radius=500&type=restaurant&keyword=Indian&key=' + api_key + '&pagetoken=' + next_page_token
        print(url)

    r = requests.get(url)
    x = r.json()
    y = x['results']
    print('Total objects: ' + str(len(y)))
    if 'next_page_token' in x.keys():
        next_page_token = x['next_page_token']
        next_page_available = True
    else:
        next_page_available = False

    print(next_page_token)
