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
    print("Меню")
    print("1.  Вывести данные")
    print("2.  Ввести данные")
    print("3.  Редактировать строку")
    print("4.  Редактировать параметр строки")
    print("5.  Удалить строку")
##    print("8. !Редактировать параметры!")
    print("9. !Очистить данные!")
    print("0.  Выйти из прогрпммы")


    
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
        print('Файл содержит:\n')
       
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
        print(f'\nВсего в файле {count_y} строк.')
                
    
        
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
    print(f"Всего {count_y-1} редактируемых строк")
    n = 0
    while n<=0 or n>=count_y:
        n = int(input("Какую строку вы хотите изменить?"))
    
    for i in file_column:
        print(i, end='\t')
    print()
    s = data[n]
    s = s.split(',')
    for i in s:
        print(i, end='\t')
    print()
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
        print(f"Всего {count_y-1} редактируемых строк")
        o = 0
        while o<=0 or o>=count_y:
            o = int(input("Какую строку вы хотите изменить?"))

        s = str(data[o])
        s = s.split(',')

    with open(file_name, "r"):
        print()
        for i in range(len(file_column)):
            print(i, end = '\t')
        print()
        for i in file_column:
            print(i, end = '\t')
        print('\n')
        for i in s:
            print(i, end = '\t')
        print()

        o2 = 0
        while o2<=0 or o2>=len(file_column):
            o2 = int(input("Какой столбец вы хотите изменить?"))
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
    print("Cколько параметров вы хотите добавить?_")
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
    print(f"Всего {count_y-1} редактируемых строк")
    n = 0
    while n<=0 or n>=count_y:
        n = int(input("Какую строку вы хотите удалить?"))
    
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
   print("вы в модуле, пожалуйста перейдите в основную программу")
