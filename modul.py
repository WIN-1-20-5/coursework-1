################################################################
#   голова программы
################################################################

#обьявляем библиотеку(-и)
import csv






################################################################
#   ввод данных
################################################################

#задаем переменные здесь, ради сокращения кода
#потом ради производительности можем переместить в сответствующие функции

#название файла
file_name='dataset.csv'

#####измеряем кол-во строк
####count_y = 0
####with open(file_name, "r") as file:
####    s = file.read()
####    count_y += len(s.split('\n')) - 1
##    
###записываем названия столбцов
##with open(file_name, "r") as file:        
##    file_column = file.read()    
##    n = file_column.find('\n')
##    file_column = file_column[:n]
##    file_column = file_column.split(',')


################################################################
#   проверка соответствия базы данных
################################################################



################################################################
#   сами функции
################################################################

#вызов меню
def menu():
    print("################################################################################")
    print("Menu")
    print("1.  Show dataset")
    print("2.  Write new data")
    print("3.  Edit data")
    print("4.  Edit template")
    print("5.  Delete data")
##    print("8. !Редактировать параметры!")
    print("9. !Clean dataset!")
    print("0.  Exit")


    
#"небесячий" ввод
def inputO():
    o=""
    while o=="":
        o=input("_")
    return int(o)

def inputA():
    o=""
    while o=="":
        o=input("_")
        if not('0'<=o<='9'):
            o = ""
            continue
    return int(o)

def inputB():
    o=""
    while o=="":
        o=input("_")
    return o


    
#вывод базы данных
def print_dataset(count_y,data,file_column):
    with open(file_name,'r') as file:
        print('File contains:\n')
       
        s = file.read()
        s = s.split('\n')
        
        d = []
        for i in s:
            a = i.split(',')
            d.append(a)
        d = d[:-1:]
        
        maxs = [0]*len(d[0])
        
        for j in range(len(d[0])):
            for i in range(len(d)):
                if maxs[j] < len(d[i][j]):
                    maxs[j] = len(d[i][j])
        
        b = []
        c = ''
        
        for j in range(len(d)):
            for i in range(len(d[0])):
                
                a = maxs[i] - len(d[j][i])
                b.append(d[j][i] + ' '*(a))
            for i in b:
                c += i + ' | '
            print(c)
            c = ''
            b = []
        print(f'\nTotal {count_y} strings in file.')
                
    
        
#ввод в базу данных
def input_dataset(count_y,data,file_column):

    d = str(count_y) + ',' 
    for i in range(1, len(file_column)):
        print(file_column[i], end='_')
        d += input() + ','
    d = d[:-1:]
    d += '\n'
    
    with open(file_name, mode="a") as file:
        file.write(d)

    
#коррекция "ненулевой строки"
def edit_dataset(count_y,data,file_column):

    print(f"Total {count_y-1} editable strings")
    n = 0
    while n<=0 or n>=count_y:
        n = int(input("Which string would you like to edit ?"))


    with open(file_name,'r') as file:
        s = file.read()
        s = s.split('\n')
        
        d = []
        for i in [s[0],s[n]]:
            a = i.split(',')
            d.append(a)
        
        maxs = [0]*len(d[0])
        
        for j in range(len(d[0])):
            for i in range(len(d)):
                if maxs[j] < len(d[i][j]):
                    maxs[j] = len(d[i][j])
        
        b = []
        c = ''


        for j in range(len(d)):
            for i in range(len(d[0])):
                
                a = maxs[i] - len(d[j][i])
                b.append(d[j][i] + ' '*(a))
            for i in b:
                c += i + ' | '
            print(c)
            c = ''
            b = []
##    for i in file_column:
##        print(i, end='\t')
##    print()
##    s = data[n]
##    s = s.split(',')
##    for i in s:
##        print(i, end='\t')
##    print()
    d = str(n) + ',' 
    for i in range(1, len(file_column)):
        print(file_column[i], end='_')
        d += input() + ','
    d = d[:-1:]
    d += '\n'
    data[n] = d

    with open(file_name, 'w') as file:
        file.writelines( data )

#изменить конкретный параметр
def edit_2_dataset(count_y,data,file_column):

    with open(file_name, "r") as file:         
        print(f"Total {count_y-1} editable strings.")
        o = 0
        while o<=0 or o>=count_y:
            o = int(input("Which string wold you like to edit ?"))

    with open(file_name,'r') as file:
        s = file.read()
        s = s.split('\n')
        
        ll = ''
        for i in range(len(s[0].split(','))):
            ll += str(i) + '),'
        ll = ll[:-1:]
        
        d = []
        for i in [ll,s[0],s[o]]:
            a = i.split(',')
            d.append(a)
        
        maxs = [0]*len(d[0])
        
        for j in range(len(d[0])):
            for i in range(len(d)):
                if maxs[j] < len(d[i][j]):
                    maxs[j] = len(d[i][j])
        
        b = []
        c = ''


        for j in range(len(d)):
            for i in range(len(d[0])):
                
                a = maxs[i] - len(d[j][i])
                b.append(d[j][i] + ' '*(a))
            for i in b:
                c += i + ' | '
            print(c)
            c = ''
            b = []
##    with open(file_name, "r"):
##        print()
##        for i in range(len(file_column)):
##            print(i, end = '\t')
##        print()
##        for i in file_column:
##            print(i, end = '\t')
##        print('\n')
##        for i in s:
##            print(i, end = '\t')
##        print()

        s = str(data[o])
        s = s.split(',')
        
        o2 = 0
        while o2<=0 or o2>=len(file_column):
            o2 = int(input("Which column would you like to edit ?"))
        s[o2] = input('_')

        s2 = ''
        for i in s:
            s2 += i + ','
        s2 = s2[:-1:]


        data[o] = s2

    with open(file_name, 'w') as file:
        file.writelines( data )



#изменить параметры(нулевую строку)
def edit_3_dataset(count_y,data,file_column):
    s = data[0]

    print(data[0])
    print("How many parameters would you like to add ?_")
    n = int(inputO())
    d = 'id,' 
    for i in range(1,n+1):
        print(i, end='_')
        d += input() + ','
    d = d[:-1:]
    d += '\n'
    data[0] = d

    with open(file_name, 'w') as file:
        file.writelines( data )



#Удалить строку
def delete_dataset(count_y,data,file_column):
    print(f"Total {count_y-1} editable strings")
    n = 0
    while n<=0 or n>=count_y:
        n = int(input("Which string would you like to delete ?"))
    
    data[n] = ""
    with open(file_name, 'w') as file:
        file.writelines( data )
        
    with open(file_name, 'r') as file:
        data = file.readlines()
        for i in range(1,len(data)):
            a = data[i].split(',')
            a[0] = str(i)
            s = ','.join(a)
            data[i] = s

    with open(file_name, 'w') as file:
        file.writelines( data )



#Удалить данные(кроме нулевой строки)
def clear_dataset(count_y,data,file_column):    
    with open(file_name, 'w') as file:
        file.write(data[0])



################################################################
#   проверка соответствия базы данных
################################################################
        


################################################################
#   конец модуля
################################################################

#говорим пользователю, что он должен запустить основную программу   
if __name__=="__main__":
   print("You are in the module. Please, go to the main programm.")
