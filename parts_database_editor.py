import re
from pcpartpicker import API
import json

api = API()



class Cpu:
    def __init__(self):
        #Base info variables
        self.brand ="N/A"
        self.model ="N/A"
        self.cores ="N/A"
        self.threads ="N/A"
        self.base_clock ="N/A"
        self.boost_clock = "N/A"
        #Extra info variables
        self.release_date ="N/A"
        self.benchmark_percentage ="N/A"
        self.integrated_graphics = "N/A"
        self.url = "N/A"
        self.price = "N/A"
        self.wattage = "N/A"

    def add_cpu(self):
        self.brand = str(input("Brand?  "))
        self.model = str(input("Model?  "))
        self.cores = int(input("Number of Cores?    "))
        self.threads = int(input("Number of Threads?    "))
        self.base_clock = float(input("Base clock speed?     "))
        self.boost_clock = float(input("Boost Clock speed?     "))
        self.release_date = str(input("Release Quarter?  (Q* ****     "))
        self.benchmark_percentage = int(input("Benchmark percentage?    "))
        self.integrated_graphics = bool(input("Integrated Graphics? True or False   "))
        self.url = str(input("URL?     "))
        self.price = int(input("Price?     "))
        self.wattage = int(input("Wattage? TDP?      "))

class Gpu:
    def __init__(self):
        #Base info variables
        self.brand ="N/A"
        self.model ="N/A"
        self.vram ="N/A"
        #Extra info variables
        self.benchmark ="N/A"
        self.url = "N/A"
        self.base_clock = "N/A"
        self.price = "N/A"
        self.wattage = "N/A"

    def add_gpu(self):
        self.brand = str(input("Brand?  "))
        self.model = str(input("Model?  "))
        self.vram = int(input("Video Memory?    "))
        self.benchmark = int(input("Benchmark %?     "))
        self.url = str(input("URL?  "))
        self.base_clock = int(input("Base Clock speed? (MHz)    "))
        self.price = int(input("Price?      "))
        self.wattage = int(input("Wattage? TDP?     "))


class Ram:
    def __init__(self):
        #Base info variables
        self.brand = "N/A"
        self.model = "N/A"
        self.size ="N/A"
        self.speed = "N/A"
        #Extra info variables
        self.benchmark = "N/A"
        self.url = "N/A"
        self.price = "N/A"

    def add_ram(self):
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.size = int(input("Size GB?     "))
        self.speed = int(input("Speed MHz?    "))
        self.benchmark = int(input("Benchmark %?    "))
        self.url = str(input("Pcpartpicker Link?     "))
        self.price = int(input("Price?     "))


class Mobo:
    def __init__(self):
        #Base info Variables
        self.brand = "N/A"
        self.model = "N/A"
        #Extra info Variables
        self.form_factor = "N/A"
        self.url = "N/A"
        self.price = "N/A"

    def add_mobo(self):
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?     "))
        self.form_factor = str(input("Form factor?    "))
        self.url = str(input("Pcpartpicker Link?     "))
        self.price = int(input("Price?     "))

class Ssd:
    def __init__(self):
        #Base info Variables
        self.brand = "N/A"
        self.model = "N/A"
        self.size = "N/A"
        #Extra info variables
        self.speed = "N/A"
        self.price = "N/A"
        self.benchmark = "N/A"

    def add_ssd(self):
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.size = int(input("Capacity? (GB)   "))
        self.speed = int(input("Speed (MB/s)    "))
        self.price = int(input("Price?    "))
        self.benchmark = int(input("Benchmark %?   "))

class Psu:
    def __init__(self):
        self.brand = "N/A"
        self.model = "N/A"
        self.wattage = "N/A"
        self.form_factor = "N/A"
        self.eff_rating = "N/A"
        self.price = "N/A"
        self.date = "N/A"

    def add_psu(self):
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.wattage = int(input("Wattage?   "))
        self.form_factor = str(input("Form Factor?    "))
        self.eff_rating = str(input("Efficiency rating?    "))
        self.price = int(input("Price?    "))
        self.date = str(input("Date?     "))

class Monitor:
    def __init__(self):
        self.brand = "N/A"
        self.size = "N/A"
        self.refresh = "N/A"
        self.model = "N/A"
        self.type = "N/A"
        self.price = "N/A"
        self.date = "N/A"

    def add_monitor(self):
        self.brand = str(input("Brand?    "))
        self.size = int(input("Size?     "))
        self.refresh = int(input("Refresh rate?     "))
        self.model = str(input("Model?    "))
        self.type = str(input("Type?    "))
        self.price = int(input("Price?    "))
        self.date = str(input("Date?    "))

class Case:
    def __init__(self):
        self.brand = "N/A"
        self.model = "N/A"
        self.type = "N/A"
        self.price = "N/A"

    def add_case(self):
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.type = str(input("Model?    "))
        self.price = int(input("Price?    "))

parts_list = ['cpu',
              'video-card',
              'memory',
              'motherboard',
              'case',
              'power-supply',
              'ssd',
              'hhd',
              'monitor']



def append_component(new_part):
    print ("Adding component...")
    with open('Data/', 'a') as database:
        json_string = json.dumps(new_part.__dict__)
        database.write(json_string + "\n")
    print ("Component added! \n")


#Takes string, removes all spaces and special characters/returns all letters in uppercase
def simplify_string(part_name):
    part_name = part_name.upper()
    simple_name = re.sub("[ -().]", "", part_name)
    return simple_name

def threadripper_match(cpu_name):

    cpu_name = simplify_string(cpu_name)
    if ("THREADRIPPER" in cpu_name):
        model_number = cpu_name.replace("THREADRIPPER", "")
    elif ("RYZENTR" in cpu_name):
        model_number = cpu_name.replace("RYZENTR", "")

    cpu_name = "Ryzen Threadripper" + model_number
    return cpu_name

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





def has_duplicates(list):
    for element in list:
        if (list.count(element) > 1):
            return True
    return False


def common_part_counter():

    with open("Data/cpu_Data_PCPP.json","r") as pcpp_data:
        json_string_pcpp = pcpp_data.read()
        data_list_pcpp = json.loads(json_string_pcpp)
    with open("Data/cpu_Data_UB.json","r") as ub_data:
        json_string_ub = ub_data.read()
        data_list_ub = json.loads(json_string_ub)

    ub_list = []
    pcpp_list = []
    common_list = []
    ub_remainders_list = []
    pcpp_remainders_list = []

    for pcpp_index in data_list_pcpp:
        pcpp_list.append(str(pcpp_index['model']))
    for ub_index in data_list_ub:
        ub_list.append(str(ub_index['Model']))

    #Sort and remove duplicates
    ub_list.sort()
    pcpp_list.sort()
    ub_list = list(dict.fromkeys(ub_list))
    pcpp_list = list(dict.fromkeys(pcpp_list))


    print("Number of Elements in UB List:  " + str(len(ub_list)))
    print("Number of Elements in PCPP List:   " + str(len(pcpp_list)))

    for ub_index in ub_list:
        for pcpp_index in pcpp_list:
            if (ub_index.lower() == pcpp_index.lower()):
                common_list.append(str(ub_index))


    print (has_duplicates(common_list))

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

def manual_add_part():
    while True:
        print("Which part to add(input x to exit)? CPU | GPU | RAM | MOBO | SSD | HDD | PSU | CASE \n")
        part_category = str(input()).lower()
        if (part_category == 'x'):
            print ("Program exited.")
            break

        elif (part_category == 'cpu'):
            new_cpu = Cpu()
            new_cpu.add_cpu()
            append_component(new_cpu)

        elif (part_category == 'gpu'):
            new_gpu = Gpu()
            new_gpu.add_gpu()
            append_component(new_gpu)

        elif (part_category == 'ram'):
            new_ram = Ram()
            new_ram.add_ram()
            append_component(new_ram)

        elif (part_category == 'mobo'):
            new_mobo = Mobo()
            new_mobo.add_mobo()
            append_component(new_mobo)

        elif (part_category == 'ssd'):
            add_ssd()
        elif (part_category == 'hdd'):
            add_hdd()
        elif (part_category == 'psu'):
            add_psu()
        elif (part_category == 'case'):
            add_case()
        elif (part_category == 'monitor'):
            add_monitor()
        elif (part_category == '')

        else:
            print ("Invalid entry")
            with open('Logs/database_adder_error_log.txt','a') as log:
                now = datetime.now()
                now = str(now)
                log.write(now + ":  Error \n")





common_part_counter()



