from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://www.pazaruvaj.com/tripod-stativ-za-fotoaparat-i-kamera-c4192/?sgst=1'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')
containers = page_soup.findAll('div', {'class' : 'product-box-container'})

#print(containers)
for container in containers:
    brand = container.div.div.a['title']

    price_container = container.findAll('a', {'class' : 'price'})
    product_price = price_container[0].text
    
    maketrans = str.maketrans
    product_string = product_price.translate(maketrans(',.' , '.,'))
    #product_leva = ''.join(c for c in product_price if c.isdigit())

    print(f'Model name: {brand}')
    print(f'Prize: {product_price}')
    #print(f'cena v leva: {product_leva}')