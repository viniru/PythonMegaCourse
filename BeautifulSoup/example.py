import wget
import requests
from bs4 import BeautifulSoup

def download(link,item):
    requests.get(link)
    print(link)

episodes=[1,52,54,128,129,176,177,178,230,231,272,286,287,288,289,290,307,308,309,310,311,345,425,435,462,463,464,465,491,492,493,494,495,496,497,498,499,500,501,502,503,504,579,580,581,667,668,671,672,673,674,675,681,683,700,701,702,703,704,705,706,723,734,741,751,770,771,779,780,781,782,783,792,813,863,864,866,867]
i=0
for item in episodes:
  
    url1 = "https://gogoanimes.co/detective-conan-episode-"+str(item)
    r = requests.get(url1)
    c=r.content
    url2 = BeautifulSoup(c,"html.parser").find("div",{"class":"download-anime"}).find('a').get('href')
    r = requests.get(url2)
    c=r.content
    soup2 = BeautifulSoup(c,"html.parser")
    down2 = soup2.find_all("div",{"class":"mirror_link"})
    down3 = down2[0].find("div",{"class":"dowload"})
    if down3 is None:
        url3 = down2[1].find("div",{"class":"dowload"}).find('a').get('href')
        if(str(url3).__contains__("rapidvideo") is False):
            continue
        r = requests.get(url3)
        c = r.content
        soup3 = BeautifulSoup(c,"html.parser")
        downx5 = soup3.find_all("div",{"class":"video"})
        if ((downx5 is None) or (len(downx5) != 2)):
            print("cancelled : "+str(item))
            continue
        down5 = downx5[1]
        url3 = down5.find("a").get("href")
        download(url3)
        continue
    down4 = down3.find('a')
    url2 = down4.get('href')
    download(url2,item)