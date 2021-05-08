import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/global/in-en/p/pl?d=graphics+card'
#opening the connection,grabbing the page
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
#page_soup.h1
#grabs ech product
containers=page_soup.find_all("div",{"class":"item-container"})
#len(containers)#prints number of dics/containers found
#contain.div.div.a.img["title"]
filename="product.csv"
f=open(filename,"w")
headers="brand,product_name,shipping"
f.write(headers)


for contain in containers:
	brand=contain.div.div.a.img["title"]
	title_container=contain.find_all("a",{"class":"item-title"})
	product_name=title_container[0].text
	shipping_container=contain.find_all("li",{"class":"price-ship"})
	shipping=shipping_container[0].text.strip()

	print("brand:"+brand)
	print("product_name:"+product_name)
	print("shipping:"+shipping)

	f.write(brand + ","+ product_name.replace(",","|") +","+ shipping+"\n")

f.close()

