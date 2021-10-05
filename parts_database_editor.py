import re
from pcpartpicker import API
import json

api = API()

parts_list = ['cpu',
              'video-card',
              'memory',
              'motherboard',
              'case',
              'power-supply',
              'ssd',
              'hhd',
              'monitor',
              'cooler']


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

    def _add_new(self):
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

    def identify_category(self):
        return "cpu"

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

    def _add_new(self):
        self.brand = str(input("Brand?  "))
        self.model = str(input("Model?  "))
        self.vram = int(input("Video Memory?    "))
        self.benchmark = int(input("Benchmark %?     "))
        self.url = str(input("URL?  "))
        self.base_clock = int(input("Base Clock speed? (MHz)    "))
        self.price = int(input("Price?      "))
        self.wattage = int(input("Wattage? TDP?     "))

    def identify_category(self):
        return "gpu"

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

    def _add_new(self):
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.size = int(input("Size GB?     "))
        self.speed = int(input("Speed MHz?    "))
        self.benchmark = int(input("Benchmark %?    "))
        self.url = str(input("Pcpartpicker Link?     "))
        self.price = int(input("Price?     "))

    def identify_category(self):
        return "ram"


class Mobo:
    def __init__(self):
        #Base info Variables
        self.brand = "N/A"
        self.model = "N/A"
        #Extra info Variables
        self.form_factor = "N/A"
        self.url = "N/A"
        self.price = "N/A"

    def _add_new(self):
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?     "))
        self.form_factor = str(input("Form factor?    "))
        self.url = str(input("Pcpartpicker Link?     "))
        self.price = int(input("Price?     "))

    def identify_category(self):
        return "mobo"

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

    def _add_new(self):
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.size = int(input("Capacity? (GB)   "))
        self.speed = int(input("Speed (MB/s)    "))
        self.price = int(input("Price?    "))
        self.benchmark = int(input("Benchmark %?   "))

    def identify_category(self):
        return "ssd"

class Psu:
    def __init__(self):
        self.brand = "N/A"
        self.model = "N/A"
        self.wattage = "N/A"
        self.form_factor = "N/A"
        self.eff_rating = "N/A"
        self.price = "N/A"
        self.date = "N/A"

    def _add_new(self):
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.wattage = int(input("Wattage?   "))
        self.form_factor = str(input("Form Factor?    "))
        self.eff_rating = str(input("Efficiency rating?    "))
        self.price = int(input("Price?    "))
        self.date = str(input("Date?     "))

    def identify_category(self):
        return "psu"

class Monitor:
    def __init__(self):
        self.brand = "N/A"
        self.size = "N/A"
        self.refresh = "N/A"
        self.model = "N/A"
        self.type = "N/A"
        self.price = "N/A"
        self.date = "N/A"

    def _add_new(self):
        self.brand = str(input("Brand?    "))
        self.size = int(input("Size?     "))
        self.refresh = int(input("Refresh rate?     "))
        self.model = str(input("Model?    "))
        self.type = str(input("Type?    "))
        self.price = int(input("Price?    "))
        self.date = str(input("Date?    "))

    def identify_category(self):
        return "monitor"

class Case:
    def __init__(self):
        self.brand = "N/A"
        self.model = "N/A"
        self.type = "N/A"
        self.price = "N/A"

    def _add_new(self):
        self.brand = str(input("Brand?    "))
        self.model = str(input("Model?    "))
        self.type = str(input("Model?    "))
        self.price = int(input("Price?    "))

    def identify_category(self):
        return "case"


def append_part(part):

    category = part.identify_category()
    with open("Data/main_data/" + category + "_data.json", "a") as database:
        print ("Appending component... \n")
        json_string = json.dumps(part.__dict__)
        database.write(json_string + "\n")
        print ("Component added! \n")


def ask_for_category():
    while True:
        print("Which part to add(input number above part | 0 to exit)?\n 1  |  2  |  3  |  4   |  5  |  6  |  7  |   8\nCPU | GPU | RAM | MOBO | SSD | HDD | PSU | CASE")
        try:
            category_index = int(input()) #Ask for user to input int between 0 and number of categories in database
            if (category_index > 8 or category_index < 0):
                raise ValueError #Raise ValueError if number inputted is not between 0 and number of categories in database
        except ValueError:
            print("Error: Enter an Integer within the options.")    #Specify valueerror, reiterate to try again
        except Exception as other_error:
            print(other_error)
            with open('Logs/parts_database_errors.log', 'a') as log:    #Write to logs if different error occurs
                log.write(str(datetime.now()) + ":  " + other_error + "\n")
                log.close()
        else:
            return category_index


def manual_add_part():

    category_dict = {1: Cpu(),
                     2: Gpu(),
                     3: Ram(),
                     4: Mobo(),
                     5: Ssd(),
                     6: Hdd(),
                     7: Psu(),
                     8: Case()}

    while True:
        category_key = ask_for_category() #Function to prompt user for input corresponding to category dict key
        if (category_key != 0):  #pass and exit function if user inputs and function returns 0
            new_part = category_dict[category_key] #create instance of corresponding parts
            new_part._add_new()
            append_part(new_part)
        else:    #Hmmm, is it better to include else statement to make pass the last line in function? Or is it better to move it up as inverse of != 0 to exclude else condition?
            print("Exiting Manual Add.")
            pass





def brand_verify(part_category, part_name):
    ram_brand_list = ["Corsair", "G.Skill", "HyperX", "Crucial", "Kingston", "TeamGroup"]
    cpu_brand_list = ["AMD", "Intel"]
    gpu_brand_list = ["Nvidia", "AMD"]
    mobo_brand_list = ["Asrock", "Asus", "MSI"]
    case_brand_list = ["Corsair", "Lian Li", "NZXT", "Gigabyte", "Antec"]

    if (part_name in brand_list):
        return True

    return False


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
"""
def pcpp_data_update():

    for part in parts_list:
        print ("Retrieving " + part + " object...")
        part_object = api.retrieve(part)
        print ("Part object retrieved... \n creating JSON text"
        json_text = part_object.to_json()
        with open("Data/" + str(part) + "_Data_PCPP.json","w") as database:
            print ("Crea,ting/Writing text file...")
            database.writ,e(json_text + "\n")
            print ("Write ,successful")

    print ("PcPartPicker Parts files updated")

def ub_data_update():

    print ("coming soon")



def has_duplicates(list):
    for element in list:
        if (list.count(element) > 1):
            return True
    return False
"""

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



def main():
    manual_add_part()

main()
