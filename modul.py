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

################################################################
#   проверка соответствия базы данных
################################################################

##    #записываем названия столбцов
##    with open(file_name, "r") as file:        
##        file_column = file.read()    
##        n = file_column.find('\n')
##        file_column = file_column[:n]
##        file_column = file_column.split(',')

        
##    #измеряем кол-во строк
##    count_y = 0
##    with open(file_name, "r") as file:
##        s = file.read()
##        count_y += len(s.split('\n')) - 1

            
##    #записываем все данные
##    #удаляем лишние столбцы    
##    #добавляем запятые, если их меньше требуемого    
##    with open(file_name, "r") as file:
##        data = file.readlines()
##
##        
##    
##        for i in range(len(data)):        
##            s = data[i]        
##            s2 = s.split(',')
##            if len(s2) < len(file_column):            
##                data[i] = s[:-1:] + ',' * (len(file_column) - len(s2)) + '\n'
##            elif len(s2) > len(file_column):
##                s3 = []
##                for j in range(len(file_column)):
##                    s3.append(s2[j])
##                s = ''
##                for j in s3:
##                    s += str(j) + ','
##                s = s[:-1]
##                s += '\n'            
##                data[i] = s



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
    print("6.  Search in data")
##    print("8. !Редактировать параметры!")
    print("9. !Clean dataset!")
    print("0.  Exit")


    
#"небесячий" ввод
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
def print_dataset(count_y):
       
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
        print(f'\nTotal {count_y-1} strings in file.')
                
    
        
#ввод в базу данных
def input_dataset(file_column,count_y):
    
    d = str(count_y) + ',' 
    for i in range(1, len(file_column)):
        print(file_column[i], end='_')
        d += input() + ','
    d = d[:-1:]
    d += '\n'
    
    with open(file_name, mode="a") as file:
        file.write(d)

    
#коррекция "ненулевой строки"
def edit_dataset(file_column,count_y,data):
        
    print(f"Total {count_y-1} editable strings")
    n = 0
    while n<=0 or n>=count_y:
        print("Which string would you like to edit ?")
        n = inputA()


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
def edit_2_dataset(file_column,count_y,data):
        
    with open(file_name, "r") as file:         
        print(f"Total {count_y-1} editable strings.")
        o = 0
        while o<=0 or o>=count_y:
            print("Which string wold you like to edit ?")
            o = inputA()

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

        s = str(data[o])
        s = s.split(',')
        
        o2 = 0
        while o2<=0 or o2>=len(file_column):
            print("Which column would you like to edit ?")
            o2 = inputA()
        s[o2] = input('_')

        s2 = ''
        for i in s:
            s2 += i + ','
        s2 = s2[:-1:]


        data[o] = s2

    with open(file_name, 'w') as file:
        file.writelines( data )



#изменить параметры(нулевую строку)
def edit_3_dataset(data):
       
    s = data[0]

    print(data[0])
    print("How many parameters would you like to add ?_")
    n = inputA()
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
def delete_dataset(file_column,count_y,data):

    print(f"Total {count_y-1} editable strings")
    n = 0
    while n<=0 or n>=count_y:
        print("Which string would you like to delete ?")
        n = inputA()
    
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
def clear_dataset(data):
        
    with open(file_name, 'w') as file:
        file.write(data[0])
        


################################################################
#   конец модуля
################################################################

#говорим пользователю, что он должен запустить основную программу   
if __name__=="__main__":
   print("You are in the module. Please, go to the main programm.")
