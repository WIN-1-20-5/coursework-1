################################################################
#   голова программы
################################################################

import csv
import modul as m

#название файла
file_name='dataset.csv'


#################################################################
#    основная программа(while)
#################################################################

while True:

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

    #удаляем лишние столбцы    
    #добавляем запятые, если их меньше требуемого
    #корректируем дату
    with open(file_name, "r") as file:
        data = file.readlines()
    
        for i in range(len(data)):        
            s = data[i]        
            s2 = s.split(',')
        #столбцы
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
        #дата
            elif len(s2[-1].split('.'))!=3 and i>0:
                s2 = s2[:-1]+['..']
                s3 = ''
                for j in range(len(s2)):
                    s3+=s2[j]
                    if j<len(s2):
                        s3+=','
                data[i]=s3
        #владельцы
            elif not('0'<=str(s2[-2])<='99') and i>0:
                s2[-2] = '0'
                s3 = ''
                for j in range(len(s2)):
                    s3+=s2[j]
                    if j<len(s2):
                        s3+=','
                data[i]=s3

        #цена
            s = data[i]        
            s2 = s.split(',')
            s3 = s2[5].replace(' ','')
            s3 = s3.replace('.','')
            s2[5] = s3
            s3 = ''
            for j in range(len(s2)):
                s3+=str(s2[j])
                if j<len(s2)-1:
                    s3+=','
            data[i]=s3

        #владельцы

            
    #записываем все данные
    with open(file_name, 'w') as file:
        file.writelines( data )

################################################################
#   Меню
################################################################

    #вызов меню
    m.menu()

    
    o = (m.inputA())


    #0. Выход из программы
    if o==0:
        break
        
    #1
    elif o==1:
        m.print_dataset(count_y)

    #2
    elif o==2:
        m.input_dataset(file_column,count_y)

    #3
    elif o==3:
        m.edit_dataset(file_column,count_y,data)
        
    #4
    elif o==4:
        m.edit_2_dataset(file_column,count_y,data)

    #5
    elif o==5:
        m.delete_dataset(file_column,count_y,data)

    #6
    elif o==6:
        import search
        break
        
##    #8
##    elif o==8:
##        m.edit_3_dataset(count_y,data,file_column)
        
    #9
    elif o==9:
        m.clear_dataset(data)

    

    
