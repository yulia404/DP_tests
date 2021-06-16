import pytest
from data.login import *


# Ввод валидных данных - менеджер
@pytest.mark.parametrize("testdata1", main_login_data, ids=[repr(empty_login)])
def test_main_login(app, testdata1):
    assert app.no_authentication_error(testdata1) == None
    assert app.status_login(testdata1) == "OK"
    assert app.status_code_login(testdata1) == 200
    assert app.content_type_login(testdata1) == "application/json"
    assert app.login_api(testdata1).cookies.__contains__('csrftoken')
    assert app.login_api(testdata1).cookies.__contains__('sessionid')
    assert app.id_login(testdata1) == "2185"
    assert app.mobile_login(testdata1) == "74444444455"
    assert app.point_id_login(testdata1) == "2"
    assert app.point_name_login(testdata1) == "8 марта Уфа"
    assert app.point_cookingtime_login(testdata1) == "1 ч 15 м"


# Ввод валидных данных - панель доставки
@pytest.mark.parametrize("testdata1", delivery_panel, ids=[repr(empty_login)])
def test_delivery_panel_login(app, testdata1):
    assert app.no_authentication_error(testdata1) == None
    assert app.status_login(testdata1) == "OK"
    assert app.status_code_login(testdata1) == 200
    assert app.content_type_login(testdata1) == "application/json"
    assert app.login_api(testdata1).cookies.__contains__('csrftoken')
    assert app.login_api(testdata1).cookies.__contains__('sessionid')
    assert app.id_login(testdata1) == "2192"
    assert app.mobile_login(testdata1) == "74444444412"
    assert app.point_id_login(testdata1) == "252"
    assert app.point_name_login(testdata1) == "Айская"
    assert app.point_cookingtime_login(testdata1) == "50 м"


# Ввод валидных данных - супервизор
@pytest.mark.parametrize("testdata1", supervisor, ids=[repr(empty_login)])
def test_supervisor_login(app, testdata1):
    assert app.no_authentication_error(testdata1) == None
    assert app.status_login(testdata1) == "OK"
    assert app.status_code_login(testdata1) == 200
    assert app.content_type_login(testdata1) == "application/json"
    assert app.login_api(testdata1).cookies.__contains__('csrftoken')
    assert app.login_api(testdata1).cookies.__contains__('sessionid')
    assert app.id_login(testdata1) == "2184"
    assert app.mobile_login(testdata1) == "74444444433"
    assert app.point_id_login(testdata1) == "2"
    assert app.point_name_login(testdata1) == "8 марта Уфа"
    assert app.point_cookingtime_login(testdata1) == "1 ч 15 м"


# Ввод валидных данных - суперчеловек
@pytest.mark.parametrize("testdata1", superuser, ids=[repr(empty_login)])
def test_superuser_login(app, testdata1):
    assert app.no_authentication_error(testdata1) == None
    assert app.status_login(testdata1) == "OK"
    assert app.status_code_login(testdata1) == 200
    assert app.content_type_login(testdata1) == "application/json"
    assert app.login_api(testdata1).cookies.__contains__('csrftoken')
    assert app.login_api(testdata1).cookies.__contains__('sessionid')
    assert app.id_login(testdata1) == "2188"
    assert app.mobile_login(testdata1) == "74444444488"
    assert app.point_id_login(testdata1) == "2"
    assert app.point_name_login(testdata1) == "8 марта Уфа"
    assert app.point_cookingtime_login(testdata1) == "1 ч 15 м"


# Ввод НЕвалидных данных
@pytest.mark.parametrize("testdata1", unvalid_data, ids=[repr(empty_login)])
def test_unvalid_data(app, testdata1):
    assert app.status_login(testdata1) == "ERROR"
    assert app.status_code_login(testdata1) == 200
    assert app.content_type_login(testdata1) == "application/json"
    assert app.type_error(testdata1) == "AuthenticationError"
    assert app.authentication_error(testdata1) == "Неверный пароль или имя пользователя"
    assert app.result_login(testdata1) == None


# Ввод данных - у сотрудника нет доступа
@pytest.mark.parametrize("testdata1", user_no_access, ids=[repr(empty_login)])
def test_user_no_access(app, testdata1):
    assert app.status_login(testdata1) == "ERROR"
    assert app.status_code_login(testdata1) == 200
    assert app.content_type_login(testdata1) == "application/json"
    assert app.type_error(testdata1) == "AccessDeniedError"
    assert app.authentication_error(testdata1) == "У сотрудника недостаточно прав для работы с приложением"
    assert app.result_login(testdata1) == None


# Ввод данных - сотрудник не активен
@pytest.mark.parametrize("testdata1", user_inactive, ids=[repr(empty_login)])
def test_user_inactive(app, testdata1):
    assert app.status_login(testdata1) == "ERROR"
    assert app.status_code_login(testdata1) == 200
    assert app.content_type_login(testdata1) == "application/json"
    assert app.type_error(testdata1) == "AccessDeniedError"
    assert app.authentication_error(testdata1) == "Сотрудник не имеет доступ для работы в системе"
    assert app.result_login(testdata1) == None


# Ввод данных - у сотрудника не создана панель
@pytest.mark.parametrize("testdata1", user_no_panel, ids=[repr(empty_login)])
def test_user_no_panel(app, testdata1):
    assert app.status_login(testdata1) == "ERROR"
    assert app.status_code_login(testdata1) == 200
    assert app.content_type_login(testdata1) == "application/json"
    assert app.type_error(testdata1) == "AccessDeniedError"
    assert app.authentication_error(testdata1) == "Окружение сотрудника не настроено для работы с сервисом"
    assert app.result_login(testdata1) == None