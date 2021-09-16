import json
from pcpartpicker import API

api = API()

parts_list = ['cpu',
              'video-card',
              'memory',
              'motherboard',
              'case',
              'power-supply'
              ]


def pcpp_data_update():

    for part in parts_list:
        print ("Retrieving " + part + " object...")
        part_object = api.retrieve(part)
        print ("Part object retrieved... \n creating JSON text")
        json_text = part_object.to_json()
        with open("PCPP_" + part + ".json","w") as database:
            print ("Creating/Writing text file...")
            database.write(json_text + "\n")
            print ("Write successful")

    print ("PcPartPicker Parts files updated")

def ub_data_update():

    print ("coming soon")

def create_json():

    





