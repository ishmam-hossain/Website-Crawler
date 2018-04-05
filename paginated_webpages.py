from bs4 import BeautifulSoup
import requests


def get_singles_links(url):
    
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')

    for link in soup.findAll('a'):       
        hrf = link.get('href')
        
        if url == str(hrf):
            continue
        
        elif check_url(hrf) and ( kwrd in str(hrf) or kwrd in link.get_text() ) :
            unq_links.add(hrf)
            # and str(hrf).startswith(base_url)


def check_url(hrf):
    
    if 'javascript' in hrf or str(hrf).startswith('#'):
        return False
    else:
        return True 



n = int(input("Enter number of pages: "))
kwrd = input("Enter Keyword: ").strip()
base_url = input("Enter URL: ").strip()


pg = 1
unq_links = set()


while pg <= n:

    url = base_url + str(pg)

    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'lxml')

    for link in soup.findAll('a'):       
        hrf = link.get('href')
        
        if url == str(hrf):
            continue
        
        elif check_url(hrf) and ( kwrd in str(hrf) or kwrd in link.get_text() ) :
            unq_links.add(hrf)
            get_singles_links(hrf)
            #and str(hrf).startswith(base_url) 
        
    
    pg += 1
    
    
print('\n\n'+str(len(unq_links)))
print('\n\n'.join(unq_links))