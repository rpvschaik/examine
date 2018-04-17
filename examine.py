import xlrd, random


def readexcel():
    wb = ''

    while wb == '':
        try:
            path = input("Waar staat je bestand? ")
            wb = xlrd.open_workbook(path)
        except:
            print("Bestand niet gevonden")

    sheet=wb.sheet_by_index(0)
    my_dict={}

    for row in range(0,sheet.nrows):
        col0 = row+1
        col1 = sheet.cell_value(row, 0)
        col2 = sheet.cell_value(row, 1)
        my_dict[col0]=(col1,col2)

    return my_dict



my_dict=readexcel()
questions=max(my_dict.keys())

answer=''
count_answers=0
count_correct=0

print('ik ga je '+str(questions)+' woordjes overhoren. Type \'stop\' als je niet meer verder wilt gaan.')

while answer!='stop':
    randnr=random.sample(my_dict.keys(),1)[0]
    answer=input("vertaling voor "+my_dict[randnr][0]+": ")
    count_answers+=1

    if answer=='stop':
        print('nog te leren:')
        for e in my_dict.values():
            print(e[0],e[1],sep=" : ")
    elif answer.lower() == my_dict[randnr][1].lower():
        my_dict.pop(randnr)
        count_correct+=1
        print('goed zo!','('+str(count_correct)+' van '+str(count_answers)+' goed geantwoord)\n')
        if any(my_dict) == False:
            print('Je kent nu alle woorden!')
            break
    else:
        print('foutje, goede antwoord is: ',my_dict[randnr][1])
