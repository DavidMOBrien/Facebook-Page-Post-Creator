import json
import facebook
import requests

def main():

    #Requires a Page Access Token from the Facebook Graph Explorer API.
    #I commented this part out for myself personally because of privacy reasons,
    #so you will need to obtain a Page Access Token and enter it in the line below

    #token = ENTER YOUR TOKEN HERE
    data = requests.get("https://graph.facebook.com/v9.0/548156981882661/published_posts?access_token=" + token)
    data = json.loads(data.text)

    proceed = True

    #Write each post's message to its own file according to its ID
    #Each JSON also has a 'paging' field that can contain a 'next' which is an address
    #To another page of post data for the corresponding Facebook Page, we want to keep jumping
    #from JSON page to JSON page as long as a 'next' exists and grab all the post's messages.
    while proceed:
        for item in data['data']:
            if 'message' in item:
                try:
                    with open(item['id'] + '.txt', "w") as writeFile:
                        writeFile.write(item['message'])
                except:
                    print("found error")
        
        if 'next' in data['paging']:
            data = requests.get(data['paging']['next'])
            data = json.loads(data.text)
            print("NEW PAGE FOUND")
        else:
            proceed = False


if __name__ == '__main__':
    main()