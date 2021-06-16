

class Login:

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return "%s:%s" % (self.username, self.password)


valid_data = [
    # доступ: панель доставки
    Login(username="74444444412", password="74444444412"),
    # доступ: менеджер
    Login(username="74444444455", password="74444444455"),
    # доступ: супервизор
    Login(username="74444444433", password="74444444433"),
    # доступ: суперчеловек + курьер
    Login(username="74444444488", password="74444444488")
]

empty_login = [
    Login(username="", password="74444444412"),
]

empty_password = [
    Login(username="74444444412", password=""),
]

empty_login_password = [
    Login(username="", password=""),
]

unvalid_data = [
    Login(username="48538450456", password="4400088877")
]

user_no_access = [
    # у пользователя нет доступа - оператор
    Login(username="74444444466", password="74444444466")
]

user_inactive = [
    # пользователь неактивен
    Login(username="74444444400", password="74444444400")
]

user_no_panel = [
    # у пользователя нет настроенной панели
    Login(username="74444444413", password="74444444413")
]

main_login_data = [
    # доступ: менеджер
    Login(username="74444444455", password="74444444455"),
]

delivery_panel = [
    # доступ: панель доставки
    Login(username="74444444412", password="74444444412"),
]

supervisor = [
    # доступ: супервизор
    Login(username="74444444433", password="74444444433")
]

superuser = [
    # доступ: суперчеловек + курьер
    Login(username="74444444488", password="74444444488")
]

