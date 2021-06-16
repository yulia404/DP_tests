import pytest
from data.login import *


# Ввод валидных данных
@pytest.mark.parametrize("testdata1", valid_data, ids=[repr(x) for x in valid_data])
def test_valid_data(app, testdata1):
    app.login(testdata1)
    assert app.find_exit_button() == "Выход"


# Пустой логин - ошибка валидации
@pytest.mark.parametrize("testdata2", empty_login, ids=[repr(empty_login)])
def test_empty_login(app, testdata2):
    app.login(testdata2)
    assert app.check_url().endswith("/login")
    assert app.empty_login() == "Введите логин!"


# Пустой пароль - ошибка валидации
@pytest.mark.parametrize("testdata3", empty_password, ids=[repr(empty_password)])
def test_empty_password(app, testdata3):
    app.login(testdata3)
    assert app.check_url().endswith("/login")
    assert app.empty_password() == "Введите пароль!"


# Пустой логин и пароль - ошибка валидации
@pytest.mark.parametrize("testdata4", empty_login_password, ids=[repr(empty_login_password)])
def test_empty_data(app, testdata4):
    app.login(testdata4)
    assert app.check_url().endswith("/login")
    assert app.empty_login() == "Введите логин!"
    assert app.empty_password() == "Введите пароль!"


# Ввод невалидных данных - всплывающая ошибка
@pytest.mark.parametrize("testdata5", unvalid_data, ids=[repr(unvalid_data)])
def test_unvalid_data(app, testdata5):
    app.login(testdata5)
    assert app.check_url().endswith("/login")
    assert app.error_for_data() == "Неверный пароль или имя пользователя"
    assert app.error_for_data() == app.authentication_error(testdata5)


# Ввод данных -  пользователя нет доступа - заглушка
@pytest.mark.parametrize("testdata6", user_no_access, ids=[repr(user_no_access)])
def test_user_no_access(app, testdata6):
    app.login(testdata6)
    assert app.check_url().endswith("/error")
    assert app.refresh_button() == "Обновить"
    assert app.error_message() == "У сотрудника нет прав для просмотра рейсов"
    assert app.error_message() == app.authentication_error(testdata6)


# Ввод данных -  пользователь не активен - заглушка
@pytest.mark.parametrize("testdata7", user_inactive, ids=[repr(user_inactive)])
def test_user_inactive(app, testdata7):
    app.login(testdata7)
    assert app.check_url().endswith("/error")
    assert app.refresh_button() == "Обновить"
    assert app.error_message() == "Сотрудник не имеет доступ для работы в системе"
    assert app.error_message() == app.authentication_error(testdata7)


# Ввод данных -  у пользователя не настроена панель - заглушка
@pytest.mark.parametrize("testdata8", user_no_panel, ids=[repr(user_no_panel)])
def test_user_no_panel(app, testdata8):
    app.login(testdata8)
    assert app.check_url().endswith("/error")
    assert app.refresh_button() == "Обновить"
    assert app.error_message() == "Окружение сотрудника не настроено для работы с сервисом"
    assert app.error_message() == app.authentication_error(testdata8)