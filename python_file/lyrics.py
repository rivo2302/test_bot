import time
from bs4 import BeautifulSoup
import requests


from pers import url_lyrics_entranger
from generic_template import generic_one_button
from g_image import get_image_links

source_etranger= url_lyrics_entranger

def get_results (mot_cle,sender_id):
    images=[]
    titles=[]
    subtitles=[]
    page_links=[]
    params= {"q":mot_cle}
    request=requests.get(source_etranger,params=params)
    page=BeautifulSoup(request.content,'lxml')
    tds=page.findAll('td',{'class':'text-left visitedlyr','style':'cursor: pointer;'})
    nb_resutalt=9
    if nb_resutalt<len(tds):
        a=0
        while a<nb_resutalt:       
            page_links.append((tds[a].find('a'))['href'])
            sub_title=tds[a].findAll('b')
            titles.append(sub_title[0].text)
            subtitles.append(sub_title[1].text)
            images.append(get_image_links(sub_title[0].text+"-"+sub_title[1].text))
            time.sleep(0.2)
            a +=1
        resultat=generic_one_button(sender_id,titles,subtitles,images,page_links,"Voir")
    elif nb_resutalt >len(tds):
        a=0
        while a<len(tds):       
            page_links.append((tds[a].find('a'))['href'])
            sub_title=tds[a].findAll('b')
            titles.append(sub_title[0].text)
            subtitles.append(sub_title[1].text)
            images.append(get_image_links(sub_title[0].text+"-"+sub_title[1].text))
            time.sleep(0.2)
            a +=1
        resultat=generic_one_button(sender_id,titles,subtitles,images,page_links,"Voir")
    elif len(titles)==0:
        resultat={"text":"Désolé mais je ne trouve à propos de cette cette argument."}
    return resultat
def get_lyrics(link):
    request=requests.get(link)
    page=BeautifulSoup(request.content,"lxml")
    paroles=page.find('div',{'class':''}).text.split("\n\n")
    return paroles

