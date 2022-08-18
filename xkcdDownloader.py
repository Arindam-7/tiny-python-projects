import requests, os, bs4

url = 'https://xkcd.com'

# make a directory called 'xkcd'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('2655'):
    # download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # find url of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('No comic image')
    else:
        comicUrl = comicElem[0].get('src')
        print(comicUrl)
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get('http:'+comicUrl)
        res.raise_for_status()

        # save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()


    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
