from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# getting the data

result_dict = dict()
for i in range(20, 28):
    key = i
    data_list = list()
    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        link = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-" + str(i) + "-ianuarie-ora-13-00/"
        browser.get(link)
        table = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/main/article/div/div/table[1]")
        table_text = table.text
        lista = table_text.split('\n')
        for j in range(2, len(lista)):
            x_path = "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[" + str(j) + "]/td[3]"
            data = browser.find_element_by_xpath(x_path)
            data_list.append(data.text)
        browser.close()
    except:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
        table = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/main/article/div/div/table[1]")
        table_text = table.text
        lista = table_text.split('\n')
        browser.close()
        for k in range(2, len(lista)):
            data_list.append("No data available")
    finally:
        result_dict[key] = data_list


# getting the indexes

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
table = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/main/article/div/div/table[1]")
table_text = table.text
lista = table_text.split('\n')
index_list = list()
for j in range(2, len(lista)):
    x_path = "/html/body/div[3]/div/div[1]/main/article/div/div/table[1]/tbody/tr[" + str(j) + "]/td[2]"
    index = browser.find_element_by_xpath(x_path)
    index_list.append(index.text)
browser.close()

df = pd.DataFrame(result_dict, index=index_list)
df.to_csv("tema_selenium.xls")
