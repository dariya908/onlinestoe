catalogue = {'hot-dot': 50, 'hamburger': 120, 'shaurma': 150, 'naggets': 130, 'piza': 930,
                         'boso-lagman': 250, 'plov': 190, 'giro-lagman': 240, 'mantes': 160, 'rolls': 600,
                         'garnir': 100, 'grechka': 70, 'pelmeni': 130, 'french meat': 400, 'fish': 500,
                         't-bone': 870, 'Beijing duck': 5000, 'shashlyk assorti': 50000
                         }

username='dariya0908'
password='Dariya8998'
money=1000

def register(username,password,check_password):
    if 8 < len(username) < 40:
        if password.istitle() and not password.isdigit() and not password.isalpha():
            if password == check_password:
                print('registasia')
            else:
                print('paroli ne sovpadaut')
        else:
            print('ne pravilnye znahenia')
    else:
        print('kol-vo simvolov ne sovpadaut')

register('dariya0908','Dariya8998','Dariya8998')

def counter(money,price):
    if money<price:
        return 'no money'
    else:
        result=money=price
        return result

def choise(num_of_fud):
    list1=[]
    for i in range(num_of_fud):
        new_element=input()
        if  new_element in catalogue:
            list1.append(new_element)
    return list1

def order():
    money=1000
    list1=choise(3)
    for food in list1:
        price=catalogue[food]
        if money >= price:
            money=counter(money,price)
    print(money)
order()



