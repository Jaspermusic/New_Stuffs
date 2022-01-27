# Working with real time websites

from bs4 import BeautifulSoup
import requests

# source = request.get('http://coreyms.com')
#   [will get an response object from coreyms.com]
source = requests.get('http://coreyms.com').text
#   [will get source code from the response object]

soup = BeautifulSoup(source, 'lxml')

#   [To scrap data from website -> Head over to page -> Inspect ]
#   [There you can see the elements of the page used]

article = soup.find('article')
#   [This find the first article of the page]

#   [To obtain Youtube URL]
vid_scr = article.find('iframe', class_='youtube-player')['src']
#   [Can act as an dictionary, src -> Gives the specific Youtube link]
#   [https://www.youtube.com/embed/z0gguhEmWiY?version=3&rel=1&showsearch=0&showinfo=1&iv_load_policy=1&fs=1&hl=en-US&autohide=2&wmode=transparent]
#   [Now we will parse this URL to get the ID of that video]
#   [Video ID -> z0gguhEmWiY]
vid_id = vid_scr.split('/')[4]
vid_id = vid_id.split('?')[0]
#   [vid_id -> Video ID]
yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)


#   [To obtain Headline and Youtube link of every article]
for article in soup.find('article'):
    headline = article.h2.a.Text
    print(headline)
    vid_scr = article.find('iframe', class_='youtube-player')['src']
    vid_id = vid_scr.split('/')[4]
    vid_id = vid_id.split('?')[0]
    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)
    print()

#   [For instance, if data of an article is missing]
#   [ i.e if youtube link of 2nd article is missing from the website]
#   [Then is shows errors, to avoid this]
for article in soup.find('article'):
    try:
        vid_scr = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_scr.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        pass
    print(yt_link)
#   [It enters try, if it can't find an Youtube link, it enters Execption]
