import time
from bs4 import BeautifulSoup


from pers import url_lyrics_entranger

class lyrics :
    def __init__(self):
        self.source_etranger= url_lyrics_entranger
    def generic_one_button(self,sender_id,titles,subtitles,images,button_postback,button_name):
        a=0
        liste_resultat=[]
        while a<len(titles):
            liste_resultat.append({
                "title":titles[a],
                "image_url":images[a],
                "subtitle":subtitles[a],
                "buttons":[
                    {
                        "type":"postback",
                        "title":button_name,
                        "payload":button_postback[a]
                    }                   
                ]
            })
            a +=1
        result={
            "recipient":{"id":sender_id},
            "message":{
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"generic",
                    "elements":liste_resultat
                }
            }
            }
        }
        return result
    def get_image_links(self,mot_cle):
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
    def get_results (self,mot_cle,sender_id):
        images=[]
        titles=[]
        page_links=[]
        params= {"q":mot_cle}
        request=requests.get(self.source_etranger,params=params)
        page=BeautifulSoup(request.content,'lxml')
        tds=page.findAll('td',{'class':'text-left visitedlyr','style':'cursor: pointer;'})
        nb_resutalt=6
        #Il faut vérifier comment on résout le maximum içi
        if nb_resutalt<len(tds):
            a=0
            while a<nb_resutalt:       
                page_links.append((tds[a].find('a'))['href'])
                titles.append((tds[a].find('b')).text)
                images.append(self.get_image_links(mot_cle))
                time.sleep(1)
                a +=1
            resultat=self.generic_one_button(sender_id,titles,titles,images,page_links,"Voir en entier")
        elif nb_resutalt >len(tds):
            a=0
            while a<len(tds):       
                page_links.append((tds[a].find('a'))['href'])
                titles.append((tds[a].find('b')).text)
                images.append(self.get_image_links(mot_cle))
                time.sleep(1)
                a +=1
            resultat=self.generic_one_button(sender_id,titles,titles,images,page_links,"voir")
        elif len(titles)==0:
            resultat={"text":"Désolé mais je ne trouve à propos de cette cette argument."}
        return resultat
    def get_lyrics(self,link):
        request=requests.get(link)
        page=BeautifulSoup(request.content,"lxml")
        paroles=page.find('div',{'class':''}).text.split("\n\n")
        return paroles