import requests
import bs4

class Build:
    def __init__(self):
        self.url = None


    def url_is_valid(self, url):
        if not ("pcpartpicker.com" in url.lower()):
            print ("URL is not from PCPartPicker")
            return False
        elif not (requests.get(url).ok):
            print ("Request Error")
            return False
        return True

    def get_url(self):
        while True:
            new_url = str(input("Input PCPartPicker Saved Parts List URL: \n\n"))
            if (url_is_valid(new_url)):
               break


new_request = requests.get(new_url)
print(f"Status Code: {new_request.status_code}")

print (new_request.text)




