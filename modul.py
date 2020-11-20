################################################################
#   голова программы
################################################################

#обьявляем библиотеку(-и)







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

###записываем все данные
###удаляем лишние столбцы    
###добавляем запятые, если их меньше требуемого    
##with open(file_name, "r") as file:
##    data = file.readlines()
##    
##    for i in range(len(data)):        
##        s = data[i]        
##        s2 = s.split(',')
##        if len(s2) < len(file_column):            
##            data[i] = s[:-1:] + ',' * (len(file_column) - len(s2)) + '\n'
##        elif len(s2) > len(file_column):
##            s3 = []
##            for j in range(len(file_column)):
##                s3.append(s2[j])
##            s = ''
##            for j in s3:
##                s += str(j) + ','
##            s = s[:-1]
##            s += '\n'            
##            data[i] = s
##        
##with open(file_name, 'w') as file:
##    file.writelines( data )





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
    print("5. !Редактировать параметры!")
    #print("6. !Добавить параметр!")
    print("9. !Очистить данные!")
    print("0.  Выйти из прогрпммы")

#"небесячий" ввод
def inputO():
    o=""
    while o=="":
        o=input("_")
    return int(o)

#вывод базы данных
def print_dataset(count_y,data,file_column):
    with open(file_name,'r') as file:
        print('Файл содержит:\n')
        s = file.read()
        s = s.split(',')
        for i in s:
            print(i, end='\t')
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


def clear_dataset(count_y,data,file_column):    
    with open(file_name, 'w') as file:
        file.write(data[0])



################################################################
#   проверка соответствия базы данных
################################################################
        
###опять делаем проверку на правильность составления базы данных 
##with open(file_name, "r") as file:
##    data = file.readlines()
##    
##    for i in range(len(data)):        
##        s = data[i]        
##        s2 = s.split(',')
##        if len(s2) < len(file_column):            
##            data[i] = s[:-1:] + ',' * (len(file_column) - len(s2)) + '\n'
##        
##with open(file_name, 'w') as file:
##    file.writelines( data )





################################################################
#   конец модуля
################################################################

#говорим пользователю, что он должен запустить основную программу   
if __name__=="__main__":
   print("вы в модуле, пожалуйста перейдите в основную программу")
