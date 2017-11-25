print """
    ####################################################
    #####                                          #####
    #####    USB CAPDATA READER (Keyboard Data)    #####
    #####                                          #####
    ####################################################
                                        By Dr4g0v
                                        
      Mouse data converter is coming soon...


1-)Enter data manually (as hex format)
        Ex --> 3d204f
2-)Get the cap data from a file (result.txt)
        tshark -r sample.pcapng -T fields -e usb.capdata > result.txt

"""

def get_data(data):
    char_map=""
    data=data.upper()
    for i in range(0,len(data),2):
        while True:
            with open("keyboard.txt","r") as file:
                column=file.readlines()
                for j in range(79):
                    splitted=column[j].split()
                    if splitted[1]==data[i:(i+2)]:
                        char_map+=splitted[3]
            break
    return char_map

def read_file():
    char_map=""
    with open("result.txt","r") as file:
        content=file.readlines()
        for i in range(len(content)):
            splitted=content[i].split(":")
            if len(splitted)==8:
                if (splitted[2][1])+(splitted[2][3])=="00":
                    pass
                else:
                    char_map+=(splitted[2][1])+(splitted[2][3])
                    
            else:
                pass
    print "Data -->",char_map
    print "\n--------------------\n"
    return get_data(char_map)


try:
    select=raw_input("Select an option :")
    select=int(select)
    if select==1:
        data=raw_input("Enter data :")
        print "[+]",get_data(data)

    elif select==2:
        print "[+]",read_file()

    else:
        print "Select a valid option"

except ValueError:
    print "Please select first or second option (1/2)"




