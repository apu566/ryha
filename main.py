import requests
from bs4 import BeautifulSoup as bs
main_list = []

file_data = open("new.txt", "r")
list1 = file_data.readlines()

for li in list1:
    li1 = li.replace("/n", "")
    r = requests.get(li1)
    #print(r.content)
    soup = bs(r.content, "html5lib")

    try:
        addr = soup.find("div" , {"class": "K4nuhf"})
        main_list.append(addr.text)
    except:
        main_list.append("None")

    try:
        web = soup.find("a" , {"class": "FKF6mc TpQm9d"})
        main_list.append(web.get("href"))
    except:
        main_list.append("None")
    
    a = open("a.txt" , "a", encoding="utf-8")
    for ma in main_list:
        a.write(ma + "**")
        
    a.write("\n")
    a.close()
    
    main_list.clear()
