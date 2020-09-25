import urllib.request, json

if __name__ == '__main__':
    url = input('Enter url: ')
    print('Retrieving ', url)
    data = urllib.request.urlopen(url).read()
    js = json.loads(data)
    print(json.dumps(js['comments']))
    print('User count = ', len(js['comments']))
    sum = 0

    for user in js['comments']:
        sum = sum + user['count']
    print(sum)
