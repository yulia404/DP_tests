import pytest
import time
from data.login import *


# Шапка:
# Проверка имени точки
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_point_name_flights(app, testdata):
    app.open_flights_page(testdata)
    # assert app.point_name() == app.get_point_name(testdata1)
    assert app.point_name() == "8 марта Уфа"


# Проверка времени ожидания
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_point_time_flights(app, testdata):
    app.open_flights_page(testdata)
#    assert app.point_time() == app.get_module(testdata1)
    assert app.point_time() == "1 ч 15 м"


# Проверка кнопки домашней страницы
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_flights_button_home(app, testdata):
    app.open_flights_page(testdata)
#    assert app.point_time() == app.get_module(testdata1)
    assert app.button_home_page_icon() == 'M1.11965 11.2857L10.7957 1.53356L11.4442 0.879552C11.592 0.731519 11.7919 0.648438 12.0002 0.648438C12.2085 0.648438 12.4083 0.731519 12.5561 0.879552L22.8807 11.2857C23.0321 11.4378 23.1518 11.6189 23.2326 11.8184C23.3135 12.0179 23.3539 12.2317 23.3515 12.4472C23.3414 13.3361 22.6077 14.0457 21.7263 14.0457H20.662V22.2701H3.33832V14.0457H2.25153C1.82332 14.0457 1.42015 13.8765 1.11715 13.5709C0.967951 13.421 0.849739 13.2426 0.769358 13.0463C0.688978 12.8499 0.648026 12.6395 0.648872 12.427C0.648872 11.9978 0.81665 11.5912 1.11965 11.2857ZM10.5978 20.452H13.4025V15.3007H10.5978V20.452ZM5.14131 12.2276V20.452H8.99519V14.6946C8.99519 14.1366 9.44343 13.6846 9.99685 13.6846H14.0035C14.5569 13.6846 15.0051 14.1366 15.0051 14.6946V20.452H18.859V12.2276H21.263L11.9977 2.89209L11.4192 3.4754L2.73483 12.2276H5.14131Z'
    app.button_home_page().click()
    assert app.check_url().endswith("/")


# Проверка наличия кнопки поворота страницы
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_flights_button_rotate_screen(app, testdata):
    app.open_flights_page(testdata)
#    assert app.point_time() == app.get_module(testdata)
    assert app.button_rotate_screen_icon() == "M15.1114 2.3054C18.1043 3.72625 20.2539 6.63665 20.5793 10.0833H21.9543C21.4868 4.43665 16.766 0 11.0001 0C10.7939 0 10.5968 0.0183477 10.3905 0.0320977L13.8876 3.52915L15.1114 2.3054ZM9.37761 1.5996C8.84136 1.06335 7.97051 1.06335 7.43426 1.5996L1.59971 7.43415C1.06346 7.9704 1.06346 8.84125 1.59971 9.3775L12.6181 20.3958C13.1543 20.9321 14.0252 20.9321 14.5614 20.3958L20.396 14.5613C20.9322 14.025 20.9322 13.1542 20.396 12.6179L9.37761 1.5996ZM13.5943 19.4242L2.57136 8.40585L8.40596 2.57125L19.4243 13.5896L13.5943 19.4242ZM6.88886 19.6946C3.89596 18.2737 1.74636 15.3633 1.42096 11.9167H0.0459595C0.513459 17.5633 5.23426 22 11.0001 22C11.2064 22 11.4035 21.9817 11.6097 21.9679L8.11261 18.4708L6.88886 19.6946Z"


# Проверка наличия кнопки полноэкранного режима
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_flights_button_fullscreen(app, testdata):
    app.open_flights_page(testdata)
#    assert app.point_time() == app.get_module(testdata)
    assert app.button_fullscreen_icon() == "M0.766195 6.64963C1.18944 6.64963 1.53239 6.30658 1.53239 5.88343V2.61658L6.46719 7.55037C6.61686 7.69993 6.8129 7.77471 7.00894 7.77471C7.20509 7.77471 7.40124 7.69993 7.5508 7.55026C7.85002 7.25104 7.85002 6.76588 7.55069 6.46676L2.61569 1.53288H5.88325C6.30639 1.53288 6.64944 1.18983 6.64944 0.766683C6.64944 0.343539 6.3065 0.000488281 5.88325 0.000488281H0.766195C0.342949 0.000488281 0 0.343539 0 0.766683V5.88353C0 6.30658 0.342949 6.64963 0.766195 6.64963Z"


# Заказы "На кухне":
# Загловок "На кухне"
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_header_at_kitchen(app, testdata):
    app.open_flights_page(testdata)
#    assert app.point_time() == app.get_module(testdata)
    assert app.header_at_kitchen().text == "На кухне"


# Номер заказа
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_number_order_kitchen(app, testdata):
    app.open_flights_page(testdata)
    assert app.number_order_kitchen().text == "0365"
#    assert app.number_order_kitchen() == app.get_number_order(testdata)


# Бренд Фарфор
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_icon_farfor_kitchen(app, testdata):
    app.open_flights_page(testdata)
    time.sleep(1)
    assert app.icon_farfor_kitchen() == "M27.2346 15.6153C26.3453 22.9069 19.6762 28.1237 12.3845 27.2344C5.09291 26.3452 -0.123857 19.676 0.765365 12.3844C1.65459 5.09279 8.32376 -0.123979 15.6154 0.765243C22.907 1.68411 28.1238 8.32363 27.2346 15.6153ZM20.5357 4.61854C19.5872 5.86345 19.528 7.6419 20.5357 8.94609C21.3953 10.0428 22.7884 10.4874 24.063 10.2206C24.1519 10.191 24.2408 10.1614 24.3298 10.1614C24.4483 10.1317 24.5965 10.0724 24.7151 10.0132C23.8851 7.81974 22.4328 5.92273 20.5357 4.61854ZM25.2486 11.9102C25.1004 11.9102 24.9819 11.9398 24.8337 11.9694C24.7447 11.9991 24.6558 12.0287 24.5669 12.0287C23.2923 12.4141 22.2845 13.5404 22.1067 14.9632C21.9289 16.297 22.5513 17.5715 23.5887 18.2829C23.7962 18.3718 24.0333 18.4904 24.2408 18.6386C24.3001 18.6683 24.3594 18.6979 24.4187 18.7275C24.8929 17.6901 25.219 16.5638 25.3672 15.4078C25.5154 14.1925 25.4561 13.0365 25.2486 11.9102ZM17.957 18.935C18.7869 18.2829 19.7651 17.9272 20.7432 17.8087C20.2986 16.8898 20.0911 15.8227 20.2097 14.726C20.3579 13.6293 20.8025 12.6512 21.4842 11.8509C20.5357 11.5248 19.6762 10.932 19.0241 10.0724C18.3127 9.18322 17.957 8.14579 17.8977 7.07872C16.9789 7.52333 15.9414 7.73082 14.8744 7.58261C13.8073 7.46405 12.8291 7.01944 12.0585 6.36734C11.7324 7.37513 11.11 8.29399 10.2208 9.00537C9.36118 9.68711 8.3534 10.0428 7.34561 10.1317C7.81986 11.0506 7.99771 12.1176 7.87914 13.2144C7.76058 14.3111 7.28633 15.2596 6.63423 16.0599C7.58274 16.3859 8.47196 16.9787 9.12406 17.8383C9.83543 18.7275 10.1911 19.765 10.2504 20.832C11.1693 20.3874 12.2067 20.1799 13.2738 20.3281C14.3408 20.4467 15.319 20.8913 16.0896 21.5434C16.4453 20.5653 17.0381 19.6464 17.957 18.935ZM12.0288 2.72153C12.266 4.26285 13.4812 5.50776 15.0818 5.71525C16.6824 5.92273 18.1645 5.00387 18.7573 3.61075C17.7199 3.1365 16.5935 2.81045 15.3783 2.66225C14.2519 2.51405 13.1256 2.54369 12.0288 2.72153ZM4.61866 7.46405C5.86357 8.50148 7.7013 8.56076 9.03513 7.52333C10.3393 6.48591 10.7247 4.7371 10.0726 3.28471C7.87914 4.08501 5.9525 5.5374 4.61866 7.46405ZM2.7513 16.0895C2.92914 16.0599 3.13662 16.0302 3.31447 16.0006C3.37375 15.9709 3.46267 15.9709 3.52195 15.9413C4.79651 15.5263 5.80429 14.4296 5.98214 13.0069C6.18962 11.3173 5.1522 9.77603 3.61088 9.2425C3.13662 10.2799 2.81058 11.4063 2.66237 12.6215C2.51417 13.8072 2.54381 14.9632 2.7513 16.0895ZM7.5531 23.4404C8.59052 22.1955 8.6498 20.3578 7.61238 19.0239C6.7528 17.8976 5.33004 17.453 4.02585 17.779C3.96657 17.8087 3.87764 17.8087 3.81836 17.8383C3.64052 17.8976 3.46267 17.9569 3.31447 18.0458C4.14441 20.2392 5.62645 22.1362 7.5531 23.4404ZM16.1193 25.2485C15.9118 23.7072 14.6669 22.4623 13.0663 22.2548C11.436 22.0473 9.92436 22.9958 9.36118 24.4778C10.369 24.9225 11.4657 25.2485 12.6217 25.3671C13.8073 25.5153 14.9929 25.456 16.1193 25.2485ZM23.4405 20.4467C23.4109 20.4171 23.3516 20.3874 23.322 20.3578C23.0848 20.2392 22.8774 20.1206 22.6699 20.0021C21.5139 19.5278 20.1801 19.6464 19.113 20.4763C17.8088 21.4841 17.4235 23.2626 18.0756 24.715C20.269 23.8554 22.1363 22.3733 23.4405 20.4467Z"
#    assert app.number_order_kitchen() == app.get_number_order(testdata)


# Бренд Клюква
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_icon_klukwa_kitchen(app, testdata):
    app.open_flights_page(testdata)
    time.sleep(1)
    assert app.icon_klukwa_kitchen() == "M22.0949 8.70916C20.2571 8.57337 18.4345 9.12588 16.9814 10.2593C15.5283 11.3927 14.5487 13.0259 14.2329 14.8415H6.18916V10.6747C6.18916 10.2324 6.05649 9.20054 4.83297 9.20054C3.60945 9.20054 3.48169 10.2324 3.48169 10.6747V21.7306C3.48169 22.1826 3.61436 23.2293 4.83297 23.2293C6.05157 23.2293 6.18916 22.1826 6.18916 21.7306V17.4114H14.2329C14.5353 19.1322 15.4336 20.6916 16.7705 21.8165C18.1073 22.9413 19.7975 23.5597 21.5446 23.5634C21.7264 23.5634 21.9131 23.5634 22.0949 23.5634C24.0316 23.5136 25.8723 22.7092 27.2245 21.3218C28.5767 19.9344 29.3334 18.0736 29.3334 16.1363C29.3334 14.1989 28.5767 12.3382 27.2245 10.9508C25.8723 9.56334 24.0316 8.75898 22.0949 8.70916V8.70916ZM26.4239 17.0625C26.2406 17.9853 25.799 18.837 25.1506 19.5186C24.5021 20.2003 23.6734 20.6837 22.7609 20.9128C21.8485 21.1419 20.8897 21.1071 19.9962 20.8126C19.1027 20.5181 18.3112 19.9759 17.7137 19.2491C17.1163 18.5223 16.7376 17.6409 16.6215 16.7073C16.5055 15.7736 16.6569 14.8263 17.0582 13.9754C17.4596 13.1245 18.0943 12.405 18.8885 11.9007C19.6827 11.3964 20.6038 11.128 21.5446 11.1267V11.1267C22.2796 11.1257 23.0057 11.2878 23.6705 11.6014C24.3353 11.9149 24.9222 12.3721 25.389 12.9399C25.8557 13.5077 26.1907 14.172 26.3696 14.8849C26.5486 15.5978 26.5672 16.3416 26.4239 17.0625V17.0625Z"
#    assert app.number_order_kitchen() == app.get_number_order(testdata)


# Иконка пиццы
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_pizza_kitchen(app, testdata):
    app.open_flights_page(testdata)
    time.sleep(1)
    assert app.pizza_kitchen() == "M30.2861 20.0363C27.5656 11.2834 20.7167 4.43454 11.9614 1.71333C10.6196 1.30512 9.24914 2.09712 8.85291 3.38823C8.42401 4.69998 9.12325 6.09402 10.4027 6.52799C10.434 6.542 10.4661 6.55353 10.4982 6.56427C17.6157 8.80021 23.1999 14.3844 25.4359 21.5019C25.4458 21.5332 25.4582 21.5646 25.4714 21.5951C25.9151 22.9068 27.3382 23.5647 28.5939 23.153C29.981 22.7342 30.6934 21.2437 30.2861 20.0363Z"
#    assert app.number_order_kitchen() == app.get_number_order(testdata)


# Иконка карты
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_icon_card_kitchen(app, testdata):
    app.open_flights_page(testdata)
    time.sleep(1)
    assert app.icon_card_kitchen() == "M32 10.1875V8.5C32 6.567 30.433 5 28.5 5H3.5C1.567 5 0 6.567 0 8.5V10.1875C0 10.3601 0.139938 10.5 0.3125 10.5H31.6875C31.8601 10.5 32 10.3601 32 10.1875Z"
#    assert app.number_order_kitchen() == app.get_number_order(testdata)


# Заказ ко времени
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_order_at_time_kitchen(app, testdata):
    app.open_flights_page(testdata)
    time.sleep(1)
    assert app.order_at_time_kitchen() == 'ДО'
    assert app.at_time_kitchen() == '02:09'
#    assert app.number_order_kitchen() == app.get_number_order(testdata)


# Заказ как можно скорее
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_order_no_at_time_kitchen(app, testdata):
    app.open_flights_page(testdata)
    time.sleep(1)
    assert app.order_no_at_time_kitchen() == 'К'
    assert app.no_at_time_kitchen() == '01:50'
#    assert app.number_order_kitchen() == app.get_number_order(testdata)


# Станции, Несервированный заказ:
@pytest.mark.parametrize("testdata", main_login_data, ids=[repr(main_login_data)])
def test_station_no_serving(app, testdata):
    app.open_flights_page(testdata)
    time.sleep(1)
    assert app.station_no_serving() == '0'
#    assert app.number_order_kitchen() == app.get_number_order(testdata)