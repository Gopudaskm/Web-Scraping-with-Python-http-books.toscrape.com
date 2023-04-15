import requests
import lxml
from bs4 import BeautifulSoup 
import json
z=1
book_list=[]
books_dict={}
website_url="http://books.toscrape.com/"
response=requests.get(website_url)
soup=BeautifulSoup(response.text,'lxml')
books=soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
for book in books:
    book_dict={}
    book_title_dict={}
    book_url="http://books.toscrape.com/"+(book.find('a')["href"])
    response2=requests.get(book_url)
    soup2=BeautifulSoup(response2.text,'lxml')
    book_details=soup2.find('article',{'class':'product_page'})
    book_details1=book_details.find('div',{'class':'col-sm-6 product_main'})
    title=book_details1.findChild('h1').text
    stock=book_details1.findChildren('p')[1].text.strip().replace("In stock (","").replace(" available)","")
    description=str(book_details.findChildren('p')[3].text).encode('latin-1').decode('utf-8')
    upc=book_details.find_all('tr')[0].find_all('td')[0].text
    product_type=book_details.find_all('tr')[1].find_all('td')[0].text
    price_excl_tax=str(book_details.find_all('tr')[2].find_all('td')[0].text).encode('latin-1').decode('utf-8')
    price_inc_tax=str(book_details.find_all('tr')[3].find_all('td')[0].text).encode('latin-1').decode('utf-8')
    tax=str(book_details.find_all('tr')[4].find_all('td')[0].text).encode('latin-1').decode('utf-8')
    # number_of_reviews=book_details.find_all('tr')[6].find_all('td')[0].text
    book_dict['Stock']=stock
    book_dict['Description']=description
    book_dict['UPC']=upc
    book_dict['Product type']=product_type
    book_dict['Price (incl. tax)']=price_inc_tax
    book_dict['Price (excl. tax)']=price_excl_tax
    book_dict['Tax']=tax
    book_title_dict[title]=book_dict
    book_list.append(book_title_dict)
    print(str(z)+"/1000")
    z+=1




for page_no in range(2,51):
    books_dict={}
    website_url="http://books.toscrape.com/catalogue/page-"+str(page_no) +'.html'
    response=requests.get(website_url)
    soup=BeautifulSoup(response.text,'lxml')
    books=soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    for book in books:
        book_dict={}
        book_title_dict={}
        book_url="http://books.toscrape.com/catalogue/"+(book.find('a')["href"])
        response2=requests.get(book_url)
        soup2=BeautifulSoup(response2.text,'lxml')
        book_details=soup2.find('article',{'class':'product_page'})
        book_details1=book_details.find('div',{'class':'col-sm-6 product_main'})
        title=book_details1.findChild('h1').text
        stock=book_details1.findChildren('p')[1].text.strip().replace("In stock (","").replace(" available)","")
        description=str(book_details.findChildren('p')[3].text).encode('latin-1').decode('utf-8')
        upc=book_details.find_all('tr')[0].find_all('td')[0].text
        product_type=book_details.find_all('tr')[1].find_all('td')[0].text
        price_excl_tax=str(book_details.find_all('tr')[2].find_all('td')[0].text).encode('latin-1').decode('utf-8')
        price_inc_tax=str(book_details.find_all('tr')[3].find_all('td')[0].text).encode('latin-1').decode('utf-8')
        tax=str(book_details.find_all('tr')[4].find_all('td')[0].text).encode('latin-1').decode('utf-8')
        # number_of_reviews=book_details.find_all('tr')[6].find_all('td')[0].text
        book_dict['Stock']=stock
        book_dict['Description']=description
        book_dict['UPC']=upc
        book_dict['Product type']=product_type
        book_dict['Price (incl. tax)']=price_inc_tax
        book_dict['Price (excl. tax)']=price_excl_tax
        book_dict['Tax']=tax
        book_title_dict[title]=book_dict
        book_list.append(book_title_dict)
        print(str(z)+"/1000")
        z+=1
books_dict['Books']=book_list


with open('Books.json','w',encoding='utf-8') as write_file:
    json.dump(books_dict,write_file,indent=2,ensure_ascii=False)

    
