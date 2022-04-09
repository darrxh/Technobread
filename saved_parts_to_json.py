import requests
import bs4

class Build:
    def __init__(self, request_object):
        self.url = request_object.url

    def url_is_valid(self):
        if not ("pcpartpicker.com" in self.url):
            print ("URL is not from PCPartPicker")
            return False
        elif not (self.ok):
            print ("Request Error")
            return False
        return True

    def get_url(self):
        while True:
            new_url = str(input("Input PCPartPicker Saved Parts List URL: \n\n"))
            if (url_is_valid()):
               break

    def output(self):

        print (new_request.json)




def export_json(new_build):
    pass




new_build = Build(requests.get(new_url))








