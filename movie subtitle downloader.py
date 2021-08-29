import webbrowser, requests, zipfile, io
from bs4 import BeautifulSoup

def subtitles_downloader():
    try:
        movie_name = input("Enter the name of the movie: ")

        #replacing spaces with hypens in movie name
        legal_movie_name = movie_name.replace(" ", "-")

        #getting the html content of the subtitle page
        url = requests.get('https://www.subscene.com/subtitles/' + legal_movie_name + '/english')
        url_soup = BeautifulSoup(url.content, 'html.parser')

        #all the urls 
        urls = [ ]
        for link in url_soup.select('.a1 a', href=True):
            urls.append(link['href'])
 
        #selecting second link from the list
        sub_link = 'https://www.subscene.com/' + urls[1]
        sub_url = requests.get(sub_link)
        sub_url_soup = BeautifulSoup(sub_url.content, 'html.parser')

        #accessing download button and getting download link
        downloadButton = sub_url_soup.select('.download a')
        dl_link = downloadButton[0]['href']
        downloadLink = 'https://www.subscene.com' + dl_link

        #getting .srt files from the link
        r = requests.get(downloadLink)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()

        print("Subtitle downloaded of " + movie_name + ". Check the folder where this program is stored.")

    except IndexError:
        print("No subtitle found for " + movie_name)


subtitles_downloader()
