from bs4 import BeautifulSoup
import requests

def get_url_kwrd():
    
    #u = input("Enter URL: ").strip()
    kwrd = input("Enter Key-word: ")
    u = 'http://bdjobs.com/sitemap.xml'
    keys = kwrd.split(' ')
    
    return u, keys


url, kwrds = get_url_kwrd()    

unq_links = set()

source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'lxml')


for link in soup.findAll('loc'):
    '''
    src_code = requests.get(link.text)
    plain_txt = src_code.text
    sp = BeautifulSoup(plain_txt,'lxml')
     
    for news in sp.findAll('a'):
        
        hrf = news.get('href')
        
        if kwrd in str(hrf):
            unq_links.add(hrf)
    '''
    
    if all(kwrd in link.text for kwrd in kwrds):
        unq_links.add(link.text)
        
        
        src_code = requests.get(link.text)
        plain_txt = src_code.text
        sp = BeautifulSoup(plain_txt,'lxml')
     
        for news in sp.findAll('a'):
        
            hrf = news.get('href')
        
            if 'macbook' in str(hrf):
                unq_links.add(hrf)
    
print()
print('\n'.join(unq_links))
print('\n'+str(len(unq_links)))

    
    
    
    
    