import requests
def uptofb(link,mes):
    page_ID='110331861785733'
    access_TOKEN='&access_token='
    print('Working on Photo ')      
    photo_Link='/photos?url='+link
    message=mes
    post='https://graph.facebook.com/'+page_ID+photo_Link+'&message='+message+access_TOKEN
    response=requests.post(post)
    return response.json()