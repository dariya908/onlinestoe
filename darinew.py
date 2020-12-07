def register(username,password,check_password):
    if password == check_password:
        if 8 < len(username) < 40 and 8 < len(password) < 14:
            print('успешно!')
            with open('database.txt','w') as db1:
                db1.write(username+'\n'+password)
            code = 1234
            return code
        else:
            print('Неправильная длина!')
    else:
        print('Пароли не совпадают!')


answer = register('superprogrammer228','12345678aa','12345678aa')
def check_code(guess,answer):
    if answer == guess:
        print('Все успешно!Можете входить!')
    else:
        print('Неверный код')
check_code(1234,answer)
def auth():
    pass
def sort():
    pass

products = ['Acer','ASUS razer','HP','hp zenbook','acer aspire','ihpone x','Iphone PRO MAX','samsung galaxy','samsung TAB515',
            'Sony Ericson','nokia 3310', 'Nokia WIN','adata hdd1tb','ADATA SSD','Kingston 1tb','kiNGston ssd','GeForce RTX',
            'AMD','amd rx760','Intel HD','MacbOOk PRO','iMac','macbook air','lenovo','AMD','aMd ryzen'
            ]