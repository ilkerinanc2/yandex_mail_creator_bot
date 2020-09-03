import os
import random
import string
import shutil
import requests
import selenium


def WaitTillElementCome(driver, selector, count=10, time=1):
    counter = 0
    driver.implicitly_wait(time)
    element = driver.find_elements_by_css_selector(selector)

    while len(element) < 0 and counter < count:
        driver.implicitly_wait(time)
        element = driver.find_elements_by_css_selector(selector)
        counter += 1


def GetRandomString(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


class RandomLoginObject:
    def __init__(self, username, password, name, surname):
        self.UserName = username
        self.Password = password
        self.Name = name
        self.Surname = surname

    def __str__(self):
        return """
        Username : {}
        Password : {}
        Name : {}
        Surname : {}
        SecurityQuestion : {}
        """.format(self.UserName, self.Password, self.Name, self.Surname, self.SecurityQuestion)

    SecurityQuestion = ""


def GetRandomLoginInfos():
    login_info = RandomLoginObject(GetRandomString(8), GetRandomString(8), GetRandomString(4), GetRandomString(4))
    return login_info


def FirstElemContains(elements, must_contain):
    elem = list(filter(lambda x: must_contain in x.text, elements))
    if len(list(elem)) > 0:
        return elem[0].text
    return False


def FillElem(driver, selector, value):
    temp = driver.find_elements_by_css_selector(selector)
    if len(temp) > 0:
        temp[0].send_keys(value)


def GetElemText(driver, selector):
    elems = driver.find_elements_by_css_selector(selector)
    if len(elems):
        return elems[0].text
    return ""


def save_image_to_file(imageUrl, name):
    if not os.path.isdir("img"):
        os.mkdir("img")

    response = requests.get(imageUrl, stream=True)

    with open('{}/{}'.format("img", name), 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)


def PressButtonWithText(driver, text):
    buttons = driver.find_elements_by_css_selector("button")
    buttons = list(filter(lambda x: text in x.text, buttons))
    if len(buttons):
        buttons[0].click()
