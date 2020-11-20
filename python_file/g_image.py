from bs4 import BeautifulSoup
import requests
def get_image_links(mot_cle):
    searchUrl = "https://www.google.com/search?q={}&site=webhp&tbm=isch".format(mot_cle)
    d = requests.get(searchUrl).text
    soup = BeautifulSoup(d,'html.parser')
    img_tags = soup.find_all('img')
    imgs_urls = []
    for img in img_tags:
        if img['src'].startswith("http"):
            imgs_urls.append(img['src'])
    img_link=imgs_urls[0]
    return img_link