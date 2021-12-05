import csv
import datetime
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

url = "http://www.volgograd.ru/operativnyj-shtab/"

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="/home/trinity/PycharmProjects/oper_shtab/chromedriver/chromedriver",
                          options=options)

mo = ["Волгоград", "Волжский", "Алексеевский", "Быковский", "Городищенский", "Даниловский", "Дубовский", "Еланский",
      "Жирновский", "Иловлинский", "Калачевский", "Камышинский", "Киквидзенский", "Клетский", "Котельниковский",
      "Котовский", "Кумылженский", "Ленинский", "Михайловка", "Нехаевский", "Николаевский", "Новоаннинский",
      "Новониколаевский", "Октябрьский", "Ольховский", "Палласовский", "Руднянский", "Светлоярский", "Серафимовичский",
      "Среднеахтубинский", "Старополтавский", "Суровикинский", "Урюпинский", "Фроловский", "Чернышковский"]

try:
    driver.get(url)
    time.sleep(5)
    text = driver.find_elements(By.ID, "volgograd_txt")
    map_vo = driver.find_elements(By.CLASS_NAME, "interactive-map__regions")
    map_text = []
    for m in map_vo:
        map_text = m.text.split()
    date = datetime.date.today()
    with open(f"mo {date}.csv", 'w', newline='', encoding="windows-1251") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["MO", "Заразившихся", "Умерших"])
        count = 2
        for x in range(4, len(map_text), 2):
            writer.writerow([mo[count], map_text[x], map_text[x + 1]])
            count += 1
        writer.writerow([mo[1], map_text[2], map_text[3]])
        writer.writerow([mo[0], map_text[0], map_text[1]])
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
