from bs4 import BeautifulSoup
import requests
import datetime as dt

#birth = dt.datetime(2002,2,6)
#print(dt.datetime.today() - birth)
page_num = 0
while True:
    try:
        result = requests.get(f"https://wuzzuf.net/search/jobs/?a=navbl%7Cspbl&q=trainer&start={page_num}")
        src = result.content
        #print(src)
        soup = BeautifulSoup(src, "html.parser")
        page_limit =int(soup.find("strong").text)
        if (page_num > page_limit // 15):
            print("pages ended")
            break


        tato = soup.find_all("h2", {"class" : "css-m604qf"})
        #print(tato)

        #tato = soup.find_all("a", {"class" : "css-nw354e"})
        tatto = []
        for i in range(len(tato)):
            tatto.append(tato[i].text)
        print(tatto)
        page_num +=1

        print("page "+str(page_num)+ " out of " +str(page_limit))
    except:
        print("pages ended")
        break
