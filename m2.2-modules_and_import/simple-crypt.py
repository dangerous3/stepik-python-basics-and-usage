'''Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог
понять какой из паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей
служит ключом для расшифровки файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.'''

import simplecrypt
import urllib.request

# Файл с информацией
url_info = "https://stepik.org/media/attachments/lesson/24466/encrypted.bin"
info_file = './crypt-examples/encrypted.bin'
# Файл с паролями
url_passwd = "https://stepik.org/media/attachments/lesson/24466/passwords.txt"
passwd_file = './crypt-examples/passwords.txt'

urllib.request.urlretrieve(url_info, info_file)
urllib.request.urlretrieve(url_passwd, passwd_file)

with open(info_file, "rb") as inp, open(passwd_file, "r") as pwd:
    encrypted = inp.read()
    for line in pwd:
        try:
            line = line.strip()
            message = simplecrypt.decrypt(line, encrypted)
            print(message)
        except simplecrypt.DecryptionException:
            print("Bad password")




