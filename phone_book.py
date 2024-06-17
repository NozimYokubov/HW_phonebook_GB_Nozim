

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phon.txt')
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            number=input('number ')
            print(find_by_number(phone_book,number))    	
        elif choice==4:
            user_data=input('new data ')
            add_user(phone_book,user_data)
        elif choice==5:
            last_name=input('lastname ')
            new_number=input('new  number ')
            a = change_number(phone_book,last_name,new_number)
            print(*a)
        elif choice==6:
            write_txt('phon.txt', phone_book)
            print('done')
        choice=show_menu()



def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить данные\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу")
    choice = int(input())
    return choice


# Иванов, Иван, 111, описание Иванова
# Петров, Петр, 222, описание Петрова
# Васичкина, Василиса, 333, описание Васичкиной
# Питонов, Антон, 777, умеет в Питон



def read_txt(filename): 
    phone_book=[]
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    line = ['Питонов,Антон,777,умеет в Питон']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
			#dict(( (фамилия, Иванов), (имя, Точка), (номер, 8928) ))
            phone_book.append(record)	
    return phone_book


def print_result(phone_book):
    # for i in phone_book:
    #     print(*i.values())   # надо доработать табуляцию
    print('\n'.join(' '.join(map(str, i.values())) for i in filter(lambda x: 1, phone_book)))

def find_by_lastname(phone_book,last_name):
    # a = list(filter(lambda x: x['Фамилия'] == last_name, phone_book))
    # for i in a:
    #     print(*i.values())
    a = ('\n'.join(' '.join(map(str, i.values())) for i in filter(lambda x: x['Фамилия'] == last_name, phone_book)))
    return a

def find_by_number(phone_book,number):
    a = ('\n'.join(' '.join(map(str, i.values())) for i in filter(lambda x: x['Телефон'] == number, phone_book)))
    return a

def add_user(phone_book,user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data.split(',')))
	#dict(( (фамилия, Иванов), (имя, Точка), (номер, 8928) ))
    phone_book.append(record)	
    return phone_book

def change_number(phone_book,last_name,new_number):
    # print(list(filter(lambda x: x['Фамилия'] == last_name, phone_book)))
    for i in phone_book:
        if i['Фамилия']==last_name:
            i['Телефон'] = new_number
            return i.values()



def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

 

work_with_phonebook()

