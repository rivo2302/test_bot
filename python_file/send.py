import requests
from pers import page_access_token
def envoyer(donnee):
    link="https://graph.facebook.com/v2.6/me/messages"
    params={'access_token':page_access_token}
    headers={"Content-Type": "application/json"}     
    req=requests.post(link,params=params,headers=headers,data=donnee)