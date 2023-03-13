import requests


def url_shortener(full_link, link_names):
    API_KEY = '02e2b972c4bf1ab2b0449533440ea8232c99f'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': API_KEY, 'short': full_link, 'name': link_names}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    print('')

    try:
        title =  data['url']['title']
        short_link = data['url']['shortLink']
        print('Title:', title)
        print('Link=', short_link)

    except:
        status = data['url']['status']
        print('Error Status:', status)

link = input('Enter a link: >>')
names = input('Give your link a name: >>')

url_shortener(link, names)


