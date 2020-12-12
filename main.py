################################################################
#   голова программы
################################################################

import csv
import modul as m

#название файла
file_name='dataset.csv'



#################################################################
#    регистрация
#################################################################

#import register


#################################################################
#    основная программа(while)
#################################################################

while True:
    #вызов меню
    m.menu()

################################################################
#   проверка соответствия базы данных
################################################################


    #записываем названия столбцов
    with open(file_name, "r") as file:        
        file_column = file.read()    
        n = file_column.find('\n')
        file_column = file_column[:n]
        file_column = file_column.split(',')
        
    #измеряем кол-во строк
    count_y = 0
    with open(file_name, "r") as file:
        s = file.read()
        count_y += len(s.split('\n')) - 1
            
    #записываем все данные
    #удаляем лишние столбцы    
    #добавляем запятые, если их меньше требуемого    
    with open(file_name, "r") as file:
        data = file.readlines()

        
    
        for i in range(len(data)):        
            s = data[i]        
            s2 = s.split(',')
            if len(s2) < len(file_column):            
                data[i] = s[:-1:] + ',' * (len(file_column) - len(s2)) + '\n'
            elif len(s2) > len(file_column):
                s3 = []
                for j in range(len(file_column)):
                    s3.append(s2[j])
                s = ''
                for j in s3:
                    s += str(j) + ','
                s = s[:-1]
                s += '\n'            
                data[i] = s
    
################################################################
#   Меню
################################################################

    o = (m.inputA())


    #0. Выход из программы
    if o==0:
        break
        
    #1
    elif o==1:
        m.print_dataset(count_y,data,file_column)

    #2
    elif o==2:
        m.input_dataset(count_y,data,file_column)

    #3
    elif o==3:
        m.edit_dataset(count_y,data,file_column)

    #4
    elif o==4:
        m.edit_2_dataset(count_y,data,file_column)

    #5
    elif o==5:
        m.delete_dataset(count_y,data,file_column)
        
##    #8
##    elif o==8:
##        m.edit_3_dataset(count_y,data,file_column)
        
    #9
    elif o==9:
        m.clear_dataset(count_y,data,file_column)

    

    
