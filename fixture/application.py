from selenium import webdriver
import time
import requests


class Application:

    def __init__(self, base_url):
        self.wd = webdriver.Chrome()
        self.base_url = base_url

    def fixture_is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_login_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def change_fill_value(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_css_selector(field_name).click()
            wd.find_element_by_css_selector(field_name).clear()
            wd.find_element_by_css_selector(field_name).send_keys(text)

    def fill_login_form(self, testdata):
        wd = self.wd
        self.change_fill_value('[data-e2e="username"]', testdata.username)
        self.change_fill_value('[data-e2e="password"]', testdata.password)
        wd.find_element_by_css_selector('[data-e2e="login-button"]').click()
        time.sleep(1)

    def login(self, testdata):
        self.open_login_page()
        self.fill_login_form(testdata)

    def find_exit_button(self):
        wd = self.wd
        exit_button = wd.find_element_by_css_selector('[data-e2e="exit"]').text
        return exit_button

    def check_url(self):
        url_page = self.wd.current_url
        return url_page

    def empty_login(self):
        wd = self.wd
        error_for_empty_login = wd.find_element_by_css_selector('div.css-1kxonj9>div.css-c5x6ck').text
        return error_for_empty_login

    def empty_password(self):
        wd = self.wd
        error_for_empty_password = wd.find_element_by_css_selector('div.css-ahqfeo>div.css-c5x6ck').text
        return error_for_empty_password

    def error_for_data(self):
        wd = self.wd
        time.sleep(1)
        error_message = wd.find_element_by_class_name("css-zycdy9").text
        return error_message

    def error_message(self):
        wd = self.wd
        time.sleep(1)
        error_message = wd.find_element_by_class_name('css-xjm4rw').text
        return error_message

    def refresh_button(self):
        wd = self.wd
        refresh_button_text = wd.find_element_by_css_selector('[type="submit"]').text
        return refresh_button_text

    def point_name(self):
        wd = self.wd
        name = wd.find_element_by_class_name('Header_point__1_BSf').text
        return name

    def point_time(self):
        wd = self.wd
        time = wd.find_element_by_class_name('Header_eta_time__358_5').text
        return time

    def button_flights(self):
        wd = self.wd
        button_flights = wd.find_element_by_css_selector('[href="/flights"]>[type="button"]')
        return button_flights

    def open_flights_page(self, testdata):
        self.login(testdata)
        self.button_flights().click()

    def button_pickup(self):
        wd = self.wd
        button_pickup = wd.find_element_by_css_selector('[href="/pickup"]>[type="button"]')
        return button_pickup

    def button_exit(self):
        wd = self.wd
        button_exit = wd.find_element_by_css_selector('[data-e2e="exit"]')
        return button_exit

    def modal_window_exit(self):
        wd = self.wd
        modal_window_exit = wd.find_element_by_css_selector('.css-qlig70 > div')
        return modal_window_exit

    def button_exit_no(self):
        wd = self.wd
        button_exit_no = wd.find_element_by_xpath('[//*[@id="chakra-modal-70"]/footer/button]')
        return button_exit_no

    def button_exit_close(self):
        wd = self.wd
        button_exit_close = wd.find_element_by_css_selector('[aria-label="Close"]')
        return button_exit_close

    def button_exit_yes(self):
        wd = self.wd
        button_exit = wd.find_element_by_css_selector('[data-e2e="exit-yes"]')
        return button_exit

    def logout(self):
        wd = self.wd
        wd.find_element_by_xpath('//*[@id="root"]/section/aside/div/div/ul[3]/li[2]/span[2]').click()
        wd.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]/span').click()
        wd.find_element_by_id("login_username")

    def destroy(self):
        self.wd.quit()

    def button_home_page(self):
        wd = self.wd
        button_home_page = wd.find_element_by_css_selector('[href="/"]>[type="button"]')
        return button_home_page

    def button_home_page_icon(self):
        wd = self.wd
        button_home_page_icon = wd.find_element_by_css_selector('[href="/"]>[type="button"]> svg > path')
        attr_value = button_home_page_icon.get_attribute("d")
        return attr_value

    def button_fullscreen_icon(self):
        wd = self.wd
        button_fullscreen_icon = wd.find_element_by_css_selector('[aria-label="Полноэкранный режим"]> svg > path')
        button_fullscreen = button_fullscreen_icon.get_attribute("d")
        return button_fullscreen

    def button_rotate_screen_icon(self):
        wd = self.wd
        button_rotate_screen_icon = wd.find_element_by_css_selector('[aria-label="Сменить ориентацию"]> svg > path')
        button_rotate_screen = button_rotate_screen_icon.get_attribute("d")
        return button_rotate_screen

    def header_at_kitchen(self):
        wd = self.wd
        header_at_kitchen = wd.find_element_by_css_selector('.Flights_kitchen__1t0GB  > .Flights_label__25-s8')
        return header_at_kitchen

    def number_order_kitchen(self):
        wd = self.wd
        number_order_kitchen = wd.find_element_by_css_selector('.Flights_kitchen__1t0GB > .CardOrder_order__2g4AD > .CardOrder_content__3HpJT> div.css-70qvj9 > div:nth-child(1)')
        return number_order_kitchen

    def pizza_kitchen(self):
        wd = self.wd
        pizza_kitchen = wd.find_element_by_xpath("//div[./div[text()='0451']]/*[name()='svg'][1]/*[1]")
        pizza_kitchen_icon = pizza_kitchen.get_attribute("d")
        return pizza_kitchen_icon

    def icon_card_kitchen(self):
        wd = self.wd
        icon_card_kitchen = wd.find_element_by_xpath("//div[./div[text()='0451']]/*[name()='svg'][2]/*[1]")
        icon_card = icon_card_kitchen.get_attribute("d")
        return icon_card

    def icon_farfor_kitchen(self):
        wd = self.wd
        icon_farfor_kitchen = wd.find_element_by_xpath("//div[./div[text()='0451']]/*[2]/*[name()='svg'][1]/*[1]")
        icon_farfor = icon_farfor_kitchen.get_attribute("d")
        return icon_farfor

    def icon_klukwa_kitchen(self):
        wd = self.wd
        icon_klukwa_kitchen = wd.find_element_by_xpath("//div[./div[text()='0452']]/*[2]/*[name()='svg'][1]/*[2]")
        icon_klukwa = icon_klukwa_kitchen.get_attribute("d")
        return icon_klukwa

    def order_no_at_time_kitchen(self):
        wd = self.wd
        order_no_at_time_kitchen = wd.find_element_by_xpath("//div[./div[./div[text()='0451']]]/div[2]/div[2]").text
        return order_no_at_time_kitchen

    def no_at_time_kitchen(self):
        wd = self.wd
        no_at_time_kitchen = wd.find_element_by_xpath("//div[./div[./div[text()='0451']]]/div[2]/div[3]").text
        return no_at_time_kitchen

    def order_at_time_kitchen(self):
        wd = self.wd
        order_at_time_kitchen = wd.find_element_by_xpath("//div[./div[./div[text()='0452']]]/div[2]/div[2]").text
        return order_at_time_kitchen

    def at_time_kitchen(self):
        wd = self.wd
        at_time_kitchen = wd.find_element_by_xpath("//div[./div[./div[text()='0451']]]/div[2]/*[1]").text
        return at_time_kitchen

    def station_no_serving(self):
        wd = self.wd
        station_no_serving = wd.find_element_by_xpath("//div[./div[./div[text()='0451']]]/div[2]/*[1]").text[0]
        return station_no_serving



    def login_api(self, testdata):
        mutation = {
                "query": '''
                    mutation ($username:String!, $password:String!){
                        user {
                            login(payload: {username: $username, password: $password}) {
                              status
                              error {
                                __typename
                                ... on  AccessDeniedError {
                                  message
                                }
                                ... on  AuthenticationError {
                                  message
                                }
                              }
                              result {
                                id
                                mobile
                                point {
                                    id
                                    name
                                    datetime
                                    cookingTime
                                }
                              }
                            }
                        }
                     }
                ''',
                "variables": {
                    "username": testdata.username,
                    "password": testdata.password
                }
            }
        response_api = requests.post('https://api.dp.frfrstaging.pw/graphql', json=mutation)
        return response_api

    def authentication_error(self, testdata):
        resp = self.login_api(testdata).json()
        authentication_error = resp['data']['user']['login']['error']['message']
        return authentication_error

    def type_error(self, testdata):
        resp = self.login_api(testdata).json()
        type_error = resp['data']['user']['login']['error']['__typename']
        return type_error

    def no_authentication_error(self, testdata):
        resp = self.login_api(testdata).json()
        Error_text = resp['data']['user']['login']['error']
        return Error_text

    def status_login(self, testdata):
        resp = self.login_api(testdata).json()
        Error_text = resp['data']['user']['login']['status']
        return Error_text

    def status_code_login(self, testdata):
        status_code_login = self.login_api(testdata).status_code
        return status_code_login

    def content_type_login(self, testdata):
        content_type_login = self.login_api(testdata).headers['Content-Type']
        return content_type_login

    def result_login(self, testdata):
        resp = self.login_api(testdata).json()
        result_login = resp['data']['user']['login']['result']
        return result_login

    def id_login(self, testdata):
        resp = self.login_api(testdata).json()
        id_login = resp['data']['user']['login']['result']['id']
        return id_login

    def mobile_login(self, testdata):
        resp = self.login_api(testdata).json()
        mobile_login = resp['data']['user']['login']['result']['mobile']
        return mobile_login

    def point_id_login(self, testdata):
        resp = self.login_api(testdata).json()
        point_id_login = resp['data']['user']['login']['result']['point']['id']
        return point_id_login

    def point_name_login(self, testdata):
        resp = self.login_api(testdata).json()
        point_name_login = resp['data']['user']['login']['result']['point']['name']
        return point_name_login

    def point_cookingtime_login(self, testdata):
        resp = self.login_api(testdata).json()
        point_cookingtime_login = resp['data']['user']['login']['result']['point']['cookingTime']
        return point_cookingtime_login