# coding: utf8
from bs4 import BeautifulSoup
from selenium import webdriver

binary = "C:\\Program Files\\Firefox Developer Edition\\firefox.exe"
driver = webdriver.Firefox(firefox_binary=binary)
fout = open("out.dat", "a+")

for number in xrange (1, 6897):
    url = "https://www.climatempo.com.br/climatologia/"+str(number)+"/santos-sp"
    driver.get(url)
    soup_level1=BeautifulSoup(driver.page_source, 'html.parser')
    location = soup_level1.find_all("span", attrs={"class":"font18"})
    i1 = str(location[1]).index(">")
    i2 = str(location[1])[1:].index("<")
    cidade = str(location[1])[i1+1:i2-4]
    estado = str(location[1])[i2-1:i2+1]
    table_title = soup_level1.find_all("th", attrs={"class":"text-center bold font14 txt-blue"})
    colunas = len(table_title)
    title = ["Estado", "Cidade"]
    for item in table_title:
        i1 = str(item).index(">")
        i2 = str(item)[1:].index("<")
        title.append(str(item)[i1+1:i2+1])
    month = []
    table_column_month = soup_level1.find_all("td", attrs={"class":"text-center normal font14 txt-blue"})
    for item in table_column_month:
        i1 = str(item).index(">")
        i2 = str(item)[1:].index("<")
        month.append(str(item)[i1+1:i2+1])
    data = []
    table_line_data = soup_level1.find_all("td", attrs={"class":"text-center normal font14 txt-black"})
    for item in table_line_data:
        i1 = str(item).index(">")
        i2 = str(item)[1:].index("<")
        data.append (str(item)[i1+1:i2+1])
    if number == 1:
        for item in title:
            fout.write(item)
            fout.write(", ")
        fout.write("\n")
    fout.write (estado)
    fout.write (",")
    fout.write (cidade)
    fout.write(",")
    for m in range(0, len(data),3):
        fout.write(month[m/3])
        fout.write(", ")
        fout.write(data[m])
        fout.write(", ")
        fout.write(data[m+1])
        fout.write(", ")
        fout.write(data[m+2])
        fout.write(", ")
    fout.write("\n")

driver.close()
fout.close()