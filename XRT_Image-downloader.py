import requests
from bs4 import BeautifulSoup
import urllib.request

num = ['01','02','03','04','05','06','07','08','09','10','11','12']
save_dir = 'D:\\Internship\\Solar_astronomy\\Project_3-Sigmoid\\2015\\'
for nums in num:
  url = "http://solar.physics.montana.edu/HINODE/XRT/SCIA/synop_images/syncmp_PNG/2015/"+ nums + '/'
  r = requests.get(url)
  htmlContent = r.content 
  soup = BeautifulSoup(htmlContent,'html.parser' )
  anchors = soup.find_all('a')
  all_link = []
  for link in anchors:
    if (link.get('href')[-3:] == 'png') and (link.get('href')[-11:-7] == '1024') and (link.get('href')[-6:-4] == '10'):
      all_link.append(url+link.get('href'))
  for i in range(len(all_link)):
    f = open(save_dir +nums + str(i)+'.png','wb')
    f.write(urllib.request.urlopen(all_link[i]).read())
    f.close()

