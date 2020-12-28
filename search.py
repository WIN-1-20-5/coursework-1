################################################################
#   голова программы
################################################################

import csv
import modul as m

#название файла
file_name='dataset.csv'

s_st = [0]*5
mark = []
color = []
mark_on = []
color_on = []

s_data = []

################################################################
#   сами функции
################################################################

#меню поиска
def search_menu(s_st,mark_on,color_on):
    s_s = ['']*5
    
    if s_st[0] == 1:
        s_s[0] = 'Mark'
    elif s_st[0] == 2:
        s_s[0] = 'Color'
    else:
        s_s[0] = 'None'
    for i in range(1,3):
        if s_st[i] == 0:
            s_s[i] = 'OFF'
        else:
            s_s[i] = 'ON'
    for i in range(3,4+1):
        if s_st[i] == 0:
            s_s[i] = 'NO'
        elif s_st[i] == 1:
            s_s[i] = 'DOWN'
        else:
            s_s[i] = 'UP'
    print('0)Status:{0};\t\t1)Mark:{1};\t2)Color:{2};\t3)Cost:{3};\t4)Old:{4}'.format(*s_s))

#выбор фильтра
    if s_st[0] == 1:
        for i in range(len(mark)):
            print(mark_on[i],'|',mark[i])
    if s_st[0] == 2:
        for i in range(len(color)):
            print(color_on[i],'|',color[i])

#применение фильтра
    with open(file_name, "r") as file:
        data = file.readlines()

    s_data = [data[0]]
    for i in range(1,len(data)):
        s = data[i].split(',')
        a = s[3].upper()
        b = s[6].upper()
        if mark_on[mark.index(a)]=='ON' and color_on[color.index(b)]=='ON':
            s_data.append(data[i])
            
#сортировка
    i_data = []

    #cost
    if s_st[3]==1 or s_st[3]==2:
        q_cost = []
        i_cost = []
        for i in range(1,len(s_data)):
            a = s_data[i].split(',')
            q_cost.append(a[5])
            i_cost.append(a[0])

        for i in range(len(i_cost)):
            a = max(q_cost)
            i_data.append(i_cost[q_cost.index(a)])
            i_cost.pop(q_cost.index(a))
            q_cost.remove(a)
        if s_st[3]==2:
            i_data.reverse()

        e = []
        for i in s_data:
            e.extend(i.split(','))

        q_data = []
        for i in i_data:
            c = e.index(i)//len(s_data[0].split(','))
            b = s_data[c]
            q_data.append(b)
        q = s_data[0]
        s_data = q_data
        s_data.insert(0, q)

    #old
    elif s_st[4]==1 or s_st[4]==2:
        q_old = []
        i_old = []
        for i in range(1,len(s_data)):
            a = s_data[i].split(',')
            b = a[8].split('.')
            c = int(b[2])*365 + int(b[1])*30 + int(b[0])
            q_old.append(c)
            i_old.append(a[0])

        for i in range(len(i_old)):
            a = max(q_old)
            i_data.append(i_old[q_old.index(a)])
            i_old.pop(q_old.index(a))
            q_old.remove(a)
        if s_st[4]==2:
            i_data.reverse()

        e = []
        for i in s_data:
            e.extend(i.split(','))

        q_data = []
        for i in i_data:
            c = e.index(i)//len(s_data[0].split(','))
            b = s_data[c]
            q_data.append(b)
        q = s_data[0]
        s_data = q_data
        s_data.insert(0, q)
  

#отображение
    if len(s_data)>1:
        d = []
        for i in s_data:
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
                a = i.replace('\n','')
                c += a + ' | '
            print(c[:])
            c = ''
            b = []
            
    return mark_on,color_on

#функции для фильтра
def mark_reverse(mark_on):
    for i in range(len(mark)):
        if mark_on[i]=='ON':
            mark_on[i]='OFF'
        else:
            mark_on[i]='ON'
    return mark_on

def color_reverse(color_on):
    for i in range(len(color)):
        if color_on[i]=='ON':
            color_on[i]='OFF'
        else:
            color_on[i]='ON'
    return color_on

################################################################
#   проверка соответствия базы данных
################################################################

for i in range(1):
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
            data[i] = data[i].upper()

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
                
    #записываем марки и цвет
    s = []
    for i in range(count_y):    
        s.append(data[i].split(','))
    for i in range(1,len(s)):
        a = s[i]
        if not(a[3] in mark):
            mark.append(a[3])
            mark_on.append('ON')
        if not(a[6] in color):
            color.append(a[6])
            color_on.append('ON')
                
#################################################################
#    основная программа(while)
#################################################################

while True:
    #вызов меню    
    mark_on,color_on = search_menu(s_st,mark_on,color_on)

    if s_st[0]==0:
        o = m.inputA()
    elif s_st[0]==1:
        o = m.inputB()
    elif s_st[0]==2:
        o = m.inputB()

    #0. Выход из программы
    if o==0 and s_st[0]==0:
        break
    elif o=='0' and s_st[0]!=0:
        s_st[0] = 0


    #3
    elif o==3 or o=='3':
        if s_st[3]!=2:
            s_st[3]+=1
            s_st[4]=0
        else:
            s_st[3]=0
    #4
    elif o==4 or o=='4':
        if s_st[4]!=2:
            s_st[4]+=1
            s_st[3]=0
        else:
            s_st[4]=0
        
    #1
    elif o==1 or o=='1':
        if s_st[1] == 0:
            s_st[1] = 1
            s_st[0] = 1
            mark_on = mark_reverse(mark_on)   
        else:
            s_st[1] = 0
            mark_on = mark_reverse(mark_on)

    #2
    elif o==2 or o=='2':
        if s_st[2] == 0:
            s_st[2] = 1
            s_st[0] = 2
            color_on = color_reverse(color_on)
        else:
            s_st[2] = 0
            color_on = color_reverse(color_on)

    elif type(o)==type(0):
        continue
    
    elif o.upper() in mark and s_st[0]==1:
        o = o.upper()
        if mark_on[mark.index(o)] == 'ON':
            mark_on[mark.index(o)] = 'OFF'
        elif mark_on[mark.index(o)] == 'OFF':
            mark_on[mark.index(o)] = 'ON'
            
    elif o.upper() in color and s_st[0]==2:
        o = o.upper()
        if color_on[color.index(o)] == 'ON':
            color_on[color.index(o)] = 'OFF'
        elif color_on[color.index(o)] == 'OFF':
            color_on[color.index(o)] = 'ON'
        

    print()    
            


