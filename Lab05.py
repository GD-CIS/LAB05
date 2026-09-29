def is_valid_part(part):
    if len(part) == 2 and part[0] == "0":
        return False
    else:
        part = int(part)
        if 0 <= part <= 255:
            return True
        else:
            return False

def is_valid_ip(ip:str):
    ip = ip.split(".")
    if len(ip) == 4:
        for part in ip:
            if not is_valid_part(part):
                return False
        return True
    else:
        return False

def decimal_to_binary(n):
    if n == 0: return 0
    if n == 1: return 1
    q, r = divmod(n , 2)
    result = decimal_to_binary(q)
    return str(result) + str(r)

def binary_to_decimal(b:str):
    if b == "":return 0
    place = len(b) - 1
    return 2 ** place * int(b[0]) + binary_to_decimal(b.removeprefix(b[0]))

def ip_to_binary(ip:str):
    ip = ip.split(".")
    new = []
    for i in ip:
        new.append(str((decimal_to_binary(int(i)))))
    print(".".join(new))







#ip = (input(f"Enter IP here: \n"))
#print(is_valid_part(ip)) #Use this to test part testing function.
#print(is_valid_ip(ip)) #Use this to test IP recognization.
#print(decimal_to_binary(int(ip))) #Put an INTEGER in here to convert to binary.
#print(binary_to_decimal(ip)) #put in a BASE 2 formatted number to have it converted to decimal.
#ip_to_binary("12.234.12.1") #EXTRA CREDIT//Uncomment this to see ip_to_binary
