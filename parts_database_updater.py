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

    ub_list = []
    pcpp_list = []
    common_list = []

    ub_remainders_list = []
    pcpp_remainders_list = []

    for pcpp_index in data_list_pcpp:
        pcpp_list.append(str(pcpp_index['model']))
    for ub_index in data_list_ub:
        ub_list.append(str(ub_index['Model']))
    ub_list.sort()
    pcpp_list.sort()

    for ub_index in ub_list:
        for pcpp_index in pcpp_list:
            if (ub_index == pcpp_index):
                common_list.append(str(ub_index))

    print ("Elements in common: " + str(len(common_list)))

    with open("Data/common_cpu_list.txt","w") as common_cpu_list:
        for part in common_list:
            common_cpu_list.write(str(part) + "\n")


    for pcpp_index in pcpp_list:
        is_different = True
        for common_index in common_list:
            if (common_index == pcpp_index):
                is_different = False
        if (is_different):
            pcpp_remainders_list.append(pcpp_index)


    for ub_index in ub_list:
        is_different = True
        for common_index in common_list:
            if (common_index == ub_index):
                is_different = False
        if (is_different):
            ub_remainders_list.append(ub_index)


    print ("Remaining elements in UB file:  " + str(len(ub_remainders_list)))
    with open ("Data/remainders_ub.txt", "w") as remainders_ub:
        for part in ub_remainders_list:
            remainders_ub.write(str(part) + "\n")

    print ("Remaining elements in PCPP file: " + str(len(pcpp_remainders_list)))
    with open("Data/remainders_pcpp.txt", "w") as remainders_pcpp:
        for part in pcpp_remainders_list:
            remainders_pcpp.write(str(part) + "\n")





common_part_counter()



