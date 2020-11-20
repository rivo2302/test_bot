def generic_one_button(sender_id,titles,subtitles,images,button_postback,button_name):
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