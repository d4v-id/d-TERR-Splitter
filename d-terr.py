
# by d4v.id
from tqdm import tqdm
import sys
from colorama import Fore,Style
import os


bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW

def ket_file(ket):
    words = 0
    with open(ket, "r") as kata_file:
        for line in kata_file:
            num_kata = line.split(";"or","or":"or".")
            words += len(num_kata)

        return str(words)


def split_line():
    os.system("cls")
    print(f"{gr}\n//{res}{yl} D-TERR by d4v.id{res}")
    print(f"{gr}//{res}{yl} Splitter Lines {res}")

    #File Input
    print(f"{red}\n[{res}?{red}]{res} Enter Filename (.txt):")
    nama = str(input(f"{gr}>>{res} "))

    nama_file = open(nama, "r")
    read_file = nama_file.read()
    print("\nFile: {}".format(nama))
    print("Lines: {}".format(all_line(nama)))
    lines = read_file.split()
    print(f"{red}[{res}#{red}]{res} Splitter Lines({yl}Ex: 34000 - end{res})")
    print(f"{red}[{res}?{red}]{res} Enter Number To Split ({yl}Ex: 34000{res}):")
    num = int(input(f"{gr}>>{res} "))
    print(f"{red}\n[{res}?{red}]{res} Enter Output Filename (.txt):")
    outFile = str(input(f"{gr}>>{res} "))

    print("\n\nProcessing: {} - {} lines".format(int(all_line(nama)), num))
    print("Result: {} copyied".format(int(all_line(nama)) - num))
    
    if int(all_line(nama)) - num < 0:
        print(f"{red}Failed Input{res}")
        exit()

    num_line = lines[(num-1):]
    with open(outFile,"w") as nama_file:
        for all_in in tqdm(num_line):
            nama_file.write("{}\n".format(all_in))
 
        print(f"{gr} SUCCESS SAVE {res}[{gr}{outFile}{res}]")


def all_line(file_line):
    baris = 0
    with open(file_line, "r") as file:
        for line in file:
            baris += 1
            line = baris

        return str(line)


def typeSplit(sign):
    if sign == 1:
        split = ":"
    elif sign == 2:
        split = ","
    elif sign == 3:
        split = ";"
    elif sign == 4:
        split = "|"
    elif sign == 5:
        split = "#"
    else:
        print(f"{red}Wrong input..")

    return str(split)


def name_file():
    print(f"{red}\n[{res}?{red}]{res} Enter Filename (.txt) >")
    nama = str(input(f"{gr}>>{res} "))
    print("File: {}\nLine: {}\nWords: {}".format(nama, all_line(nama), ket_file(nama)))


def split_text():
    os.system("cls")
    print(f"{gr}\n//{res}{yl} D-TERR by d4v.id{res}")
    print(f"{gr}//{res}{yl} Splitter Text {gr}--> {yl}: , ; | #{res}")

    # File Input
    print(f"{red}\n[{res}?{red}]{res} Enter Filename (.txt) >")
    nama = str(input(f"{gr}>>{res} "))
    nama_file = open(nama, "r")
    print(f"{red}\n[{res}#{red}]{res} List Splitter{yl} (; : , | #) {res}")
    print(f"{red}[{res}#{red}]{res} Ex: [ admin{yl};{res}pa213ss{yl};{res}sada@gmail.com ]") 
    
    # Type Input
    print(f"{red}\n[{res}?{red}]{res} Split Type\t1.) {yl}:{res}     2.) {yl},{res}      3.) {yl};{res}     4.) {yl}|{res}     5.) {yl}#{res}")
    numType = int(input(f"{gr}>>{res} "))
    
    # Select Input
    print(f"{red}\n[{res}#{red}]{res} Ex: [ admin{yl};{res}pa213ss{yl};{res}sada@gmail.com ]") 
    print(f"{red}[{res}?{red}]{res}     [   0  {yl};{res}   1   {yl};{res}       2       ] \nChoose number (ex: 0): ")
    num = int(input(f"{gr}>>{res} "))

    # Output Input
    print(f"{red}\n[{res}?{red}]{res} Enter Output Filename  (.txt) >")
    outFile = str(input(f"{gr}>>{res} "))
    
    inputType = typeSplit(numType)
    read_file = nama_file.readlines()
    with open(outFile, "w") as nama_file:
        for line in tqdm(read_file):
            if inputType in line:
                action = line.split(inputType)
                input_action = action
                nama_file.write("{}\n".format(input_action[num]))
            else:
                pass
        
        print(f"{gr} SUCCESS SAVE {res}[{gr}{outFile}{res}]")
         


# MAIN
os.system("cls")
print(f"{gr}\n//{res}{yl} D-TERR by d4v.id{res}")
type_tools = [f"File Checker", "Splitter Text(: , ; | #)", "Splitter Lines"]
print(f"{gr}//{res}{yl} Multiple For Splitter{res}")
try:
    print(f"{red}\n[{res}?{red}]{res} Choose Methode: ")
    print("\t(1) {}\t(2) {}\t(3). {}".format(type_tools[0], type_tools[1], type_tools[2]))
    put_number =int(input(f"{gr}\t>>{res} "))
    if put_number == 1:
        name_file()
    elif put_number == 2:
        split_text()
    elif put_number == 3:
        split_line()

except ValueError:
    print(f"{red}\nFailed Input..{res}")
except FileNotFoundError:
    print(f"{red}\nFile Notfound..{res}")
except IndexError:
    print(f"{red}\nFailed Split Type / Input..{res}")
except KeyboardInterrupt:
    print(f"{red}\nExiting...{res}")

    
