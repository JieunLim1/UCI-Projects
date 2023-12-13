############ IMPORT HERE #############
import sys
from datetime import datetime 

############## IMPLEMENT FUNCTIONS HERE ############
def command_lb(lst):
    print(f'Number of bedrooms in service:  {len(lst)}')
    print('------------------------------------')
    for i in lst:
        print(i)

def command_pl(command_script):
    print(command_script[3:])

def command_nb(command_script):
    nospace_item = command_script[3:].strip()
    if nospace_item in bedrooms:
        print(f'Sorry, can\'t add room {nospace_item} again; it\'s already on the list.')
    bedrooms.append(nospace_item)

def cancel_reservation(roomnum,rrcount):
    index = 0
    while index != len(reservationlst):
        if reservationlst[index][0] == roomnum:
            print(f'Deleting room {reservationlst[index][0]} forces cancellation of this reservation:')
            print(f'{reservationlst[index][3]} arriving {reservationlst[index][1]} and departing {reservationlst[index][2]} (Conf. #{reservationlst[index][4]})')
            reservationlst.remove(reservationlst[index])
            index -= 1
        index += 1
    rrcount = (reservationlst[len(reservationlst)-1][4])
    return rrcount
        
def command_db(command_script,rrcount):
    num = command_script[3:].strip()
    index = 0
    found = False
    while index != len(bedrooms):
        if bedrooms[index] == num:
            bedrooms.remove(num)
            found = True
            break
        index += 1
    if found is True and num in reservationrooms:
        rrcount = cancel_reservation(num,rrcount)
    if found is False:
        print(f'Sorry, can\'t delete room {num}; it is not in service now') 
    return rrcount


def compare_date(arrival, depart):
    arrivallst = arrival.split('/')
    arrivalyear = int(arrivallst[2])
    arrivalmonth = int(arrivallst[0])
    arrivaldate = int(arrivallst[1])

    departlst = depart.split('/')
    departyear = int(departlst[2])
    departmonth = int(departlst[0])
    departdate = int(departlst[1])
    first = datetime(arrivalyear,arrivalmonth, arrivaldate)
    second = datetime(departyear,departmonth,departdate)
    diff = first - second
    return diff.days


def command_rr(command_script,rrcount):
    splitted = command_script.split(' ')
    i = 0
    while i < len(splitted):
        if splitted[i] == "":
            splitted.remove(splitted[i])
            i-=1
        i += 1
    reservationroom = splitted[1]
    arrival = splitted[2]
    departure = splitted[3]
    #date check
    if compare_date(arrival, departure) >= 0:
        print(f'Sorry, can\'t reserve room {reservationroom}  ({arrival} to {departure});')
        if compare_date(arrival, departure) > 0:
            print('can\'t leave before you arrive.')
        elif compare_date(arrival, departure) == 0:
            print('can\'t arrive and leave on the same day.')
        rrcount -= 1
        return rrcount
    
    name = ""
    for index in range(4,len(splitted)):
        name += splitted[index] + " "
    name = name.strip()

    if reservationroom not in bedrooms:
        print(f'Sorry; can\'t reserve room {reservationroom}; room not in service')
        rrcount -= 1
        return rrcount

    for i in range(len(reservationlst)):
        if reservationroom == reservationlst[i][0]:
            first = reservationlst[i][1].split('/')
            first = datetime(int(first[2]), int(first[0]), int(first[1]))
            second = reservationlst[i][2].split('/')
            second = datetime(int(second[2]), int(second[0]), int(second[1]))
            arrivallst = arrival.split('/')
            arrival1 = datetime(int(arrivallst[2]), int(arrivallst[0]), int(arrivallst[1]))
            departurelst = departure.split('/')
            departure1 = datetime(int(departurelst[2]), int(departurelst[0]), int(departurelst[1]))
            if first <= arrival1 < second or first < departure1 < second:
                print(f'Sorry, can\'t reserve room {reservationroom}  ({arrival} to {departure});')
                for i in range(len(reservationlst)):
                    if reservationlst[i][0] == reservationroom:
                        existroomconfirmnum = reservationlst[i][4]
                        break
                print(f'it\'s already booked (Conf. #{existroomconfirmnum})')
                rrcount -= 1
                return rrcount
    reservationitem = [reservationroom,arrival,departure,name, rrcount]
    print(f'Reserving room {reservationitem[0]} for {reservationitem[3]} -- Confirmation #{reservationitem[4]}')
    print(f'(arriving {reservationitem[1]}, departing {reservationitem[2]})')
    reservationlst.append(reservationitem)
    reservationrooms.append(reservationitem[0])
    confirmationnumlst.append(reservationitem[4])
    return rrcount

def command_lr():
    print(f'Number of reservations:  {len(reservationlst)}')
    print('No.\tRm.\tArrive\t\tDepart\t\tGuest')
    print('------------------------------------------------')
    for i in reservationlst:
        print(f'{i[4]}\t{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}')

def command_dr(command_script):
    num = int(command_script[3:].strip())
    num = num - 1
    if num+1 not in confirmationnumlst:
        print(f'Sorry, can\'t cancel reservation; no confirmation number {num+1}')
    else:
        reservationlst.remove(reservationlst[num])
        confirmationnumlst.remove(confirmationnumlst[num])

def command_rb(command_script):
    roomnum = command_script[3:].strip()
    print(f'Reservations for room {roomnum}:')
    for i in range(len(reservationlst)):
        if reservationlst[i][0] == roomnum:
            print(f'{reservationlst[i][1]} to {reservationlst[i][2]}: {reservationlst[i][3]}')

def command_rg(command_script):
    name = command_script[3:].strip()
    print(f'Reservations for {name}:')
    for i in range(len(reservationlst)):
        if reservationlst[i][3] == name:
            print(f'{reservationlst[i][1]} to {reservationlst[i][2]}: room {reservationlst[i][0]}')

def command_la(command_script):
    date = command_script[3:].strip()
    print(f'Guests arriving on {date}:')
    for i in range(len(reservationlst)):
        if reservationlst[i][1] == date:
            print(f'{reservationlst[i][3]} (room {reservationlst[i][0]})')

def command_ld(command_script):
    date = command_script[3:].strip()
    print(f'Guests departing on {date}:')
    for i in range(len(reservationlst)):
        if reservationlst[i][2] == date:
            print(f'{reservationlst[i][3]} (room {reservationlst[i][0]})')

def datecalc(command_script):
    first_date = command_script[3:13]
    first_datelst = first_date.split('/')
    arrival = datetime(int(first_datelst[2]), int(first_datelst[0]), int(first_datelst[1]))
    second_date = command_script[14:].strip()
    second_datelst = second_date.split('/')
    departure = datetime(int(second_datelst[2]), int(second_datelst[0]), int(second_datelst[1]))
    notavailablerooms = []
    for i in range(len(reservationlst)):
        first = reservationlst[i][1].split('/')
        first = datetime(int(first[2]), int(first[0]), int(first[1]))
        second = reservationlst[i][2].split('/')
        second = datetime(int(second[2]), int(second[0]), int(second[1]))
        if (arrival <= first <= departure and arrival <= second < departure) or ( first <= arrival <= second < departure) or (arrival <= first <= departure and second < departure) or (arrival >= first and departure < second):
            notavailablerooms.append(reservationlst[i][0])
    return notavailablerooms
    
def command_lf(command_script):
    first_date = command_script[3:13]
    second_date = command_script[14:].strip()
    print(f'Bedrooms free between {first_date} to {second_date}:')
    notavailablerooms = datecalc(command_script)
    availablerooms = []
    for i in bedrooms:
        if i not in notavailablerooms:
            availablerooms.append(i)
    for i in availablerooms:
        print(i)
    return notavailablerooms

def command_lo(command_script):
    first_date = command_script[3:13]
    second_date = command_script[14:].strip()
    print(f'Bedrooms occupied between {first_date} to {second_date}:')
    notavailablerooms = datecalc(command_script)
    notavailablerooms.sort()
    for i in notavailablerooms:
        print(i)
        
    

def anteaterbnb(lines, rrcount):
    for i in range(len(lines)):
        if lines[i][:2].upper() == "PL":
            command_pl(lines[i])
        elif lines[i][:2].upper() == "LB":
            command_lb(bedrooms)
        elif lines[i][:2].upper() == 'NB':
            command_nb(lines[i])
        elif lines[i][:2].upper() == 'DB':
            rrcount = command_db(lines[i],rrcount)
        elif lines[i][:2].upper() == 'RR':
            rrcount += 1
            rrcount = command_rr(lines[i],rrcount)
        elif lines[i][:2].upper() == 'LR':
            command_lr()
        elif lines[i][:2].upper() == 'DR':
            command_dr(lines[i])
        elif lines[i][:2].upper() == 'RB':
            command_rb(lines[i])
        elif lines[i][:2].upper() == 'RG':
            command_rg(lines[i])
        elif lines[i][:2].upper() == 'LA':
            command_la(lines[i])
        elif lines[i][:2].upper() == 'LD':
            command_ld(lines[i])
        elif lines[i][:2].upper() == 'LF':
            command_lf(lines[i])
        elif lines[i][:2].upper() == 'LO':
            command_lo(lines[i])


if __name__ == "__main__": 
    # HINT: Read all sections of the Chapter 9 Zybooks chapter before beginning. Stuff from chapter 10 may be helpful as well.
    filename = sys.argv[1]
    with open(filename, encoding = "utf-8") as f:
        lines1 = f.readlines()
    #strip line
    for a in range(len(lines1)):
        lines1[a] = lines1[a].strip()

    #initialize global variables
    bedrooms = [] #available rooms
    reservationrooms = []
    reservationlst = [] #list in list
    confirmationnumlst = [] #confirmation numbers
    rr  = 0
    anteaterbnb(lines1, rr)
    