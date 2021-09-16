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
        with open("Data/" + part + "_Data_PCPP.json","w") as database:
            print ("Creating/Writing text file...")
            database.write(json_text + "\n")
            print ("Write successful")

    print ("PcPartPicker Parts files updated")

def ub_data_update():

    print ("coming soon")

def create_json():

    print ("coming soon")

def common_part_counter():

    with open("Data/cpu_Data_PCPP.json","r") as pcpp_data:
        json_string_pcpp = pcpp_data.read()
        data_list_pcpp = json.loads(json_string_pcpp)
    with open("Data/cpu_Data_UB.json","r") as ub_data:
        json_string_ub = ub_data.read()
        data_list_ub = json.loads(json_string_ub)

    print ("Number of elements in UB: " + str(len(data_list_ub)))
    print ("Number of elements in PCPP: " + str(len(data_list_pcpp)))




    counter = 0
    common_list = []
    uncommon_list = []

    for pcpp_index in data_list_pcpp:
        condition = False
        for ub_index in data_list_ub:
            if (ub_index['Model'] == pcpp_index['model']):
                counter = counter + 1
                common_list.append(ub_index['Model'])
                condition = True
        if (not(condition)):
            uncommon_element = pcpp_index['model']
            uncommon_list.append(uncommon_element)

    print ("Elements in common: " + str(counter))
    with open("Data/common_cpu_list.txt","w") as finish_data:
        for part in common_list:
            finish_data.write(part + "\n")

    with open("Data/uncommon_cpu_list.txt","w") as uncommon_data:
        for uncommon in uncommon_list:
            uncommon_data.write(uncommon + "\n")

common_part_counter()



