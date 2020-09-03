from selenium import webdriver
import os
import time
import ikoLib
import pytesseract

driver = webdriver.Firefox()
driver.get("https://passport.yandex.com.tr/registration")

login_infos = ikoLib.GetRandomLoginInfos()

# Filling Login Informations
ikoLib.FillElem(driver, "[name='firstname']", login_infos.Name)
ikoLib.FillElem(driver, "[name='lastname']", login_infos.Surname)
ikoLib.FillElem(driver, "[name='login']", login_infos.UserName)
ikoLib.FillElem(driver, "[name='password']", login_infos.Password)
ikoLib.FillElem(driver, "[name='password_confirm']", login_infos.Password)

# Clicking 'I don't have a mobile phone' option is clicking
elements = driver.find_elements_by_css_selector("span[class*='Link_pseudo']")
for elem in elements:
    if "phone" in elem.text or "Telefon" in elem.text:
        element = elem
        element.click()
        break

login_infos.SecurityQuestion = ikoLib.GetRandomString(5)

ikoLib.FillElem(driver, "[name='hint_answer']", login_infos.SecurityQuestion)

pytesseract.pytesseract.tesseract_cmd = r'https://ext.captcha.yandex.net/image?key=00AFDOhthf2LWBFmwlPwZ755hNDwOsbl'

time.sleep(2)

captchaLink = driver.find_elements_by_css_selector("[class='captcha__image']")[0].get_attribute("src")

path_of_image = ikoLib.GetRandomString(4) + ".jpg"

# Saves the picture
ikoLib.save_image_to_file(captchaLink, path_of_image)

# Takes root path of applicaton
root = os.path.dirname(os.path.abspath(__file__))

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Or you can use any of captcha service
captcha = pytesseract.image_to_string("img/" + path_of_image)

ikoLib.FillElem(driver, "[name='captcha']", captcha)

ikoLib.PressButtonWithText(driver, "Kayıt ol")

print(login_infos)

exit()