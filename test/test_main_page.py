import pytest
import time
from data.login import *


# Проверка имени точки
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_point_name(app, testdata):
    app.login(testdata)
    assert app.point_name() == app.point_name_login(testdata)
    assert app.point_name() == "8 марта Уфа"


# Проверка времени ожидания
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_point_time(app, testdata):
    app.login(testdata)
    assert app.point_time() == app.point_cookingtime_login(testdata)
    assert app.point_time() == "1 ч 15 м"


# Проверка кнопки "Рейсы", переход на страницу рейсов
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_button_flight(app, testdata):
    app.login(testdata)
    assert app.button_flights().text == "Рейсы"
    app.button_flights().click()
    assert app.check_url().endswith("/flights")


# Проверка кнопки "Самовывоз", переход на страницу самовывоза
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_button_pickup(app, testdata):
    app.login(testdata)
    assert app.button_pickup().text == "Самовывоз"
    app.button_pickup().click()
    assert app.check_url().endswith("/pickup")


# Проверка кнопки "Выход"
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_button_exit(app, testdata):
    app.login(testdata)
    assert app.button_exit().text == "Выход"
    app.button_exit().click()
    assert app.modal_window_exit().text == "Вы действительно хотите выйти?"


# Проверка кнопки "Выход" - нет
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_button_exit_no(app, testdata):
    app.login(testdata)
    app.button_exit().click()
    time.sleep(1)
    assert app.button_exit_no().text == "Нет"
    app.button_exit_no().click()
    time.sleep(1)
    assert app.check_url().endswith("/")


# Проверка кнопки "Выход" - крестик
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_button_exit_close(app, testdata):
    app.login(testdata)
    app.button_exit().click()
    app.button_exit_close().click()
    assert app.check_url().endswith("/")


# Проверка кнопки "Выход" - подтверждение
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_button_exit_yes(app, testdata):
    app.login(testdata)
    app.button_exit().click()
    time.sleep(1)
    assert app.button_exit_yes().text == "Да"
    app.button_exit_yes().click()
    time.sleep(1)
    assert app.check_url().endswith("/login")

