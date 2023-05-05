import requests
from bs4 import BeautifulSoup
import config

## setup 
url = 'https://eu4.paradoxwikis.com/Achievements'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table')

def scrape():
    table_dict = {}
    headers = config.headers
    url = 'https://eu4.paradoxwikis.com/Achievements'
    page = requests.get(url,headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table')
    for i,val in enumerate(table.find_all('tr')):
        ## first table row is the headings of table
        if i == 0:
            continue
        ## Traversing html tags for data and adding to dictionary
        table_dict[i]={}
        table_dict[i]['dlc'] = []
        td = val.find_all('td')
        div_a = td[0].find_all('div')
        li = td[4].find_all('li')
        div_b = td[4].find_all('a')
        
        for e in td[4].find_all('a'):
            y = e.attrs
            if len(y) == 0:
                table_dict[i]['dlc'] = 'None'
            elif len(y)== 10 or len(y) == 9:
                pass
            else:
                table_dict[i]['dlc'].append(y['title'])
        
        table_dict[i]['achievement'] = div_a[2].text.rstrip()
        table_dict[i]['description'] = div_a[3].text.rstrip()
        table_dict[i]['starting'] = td[1].text.rstrip()
        table_dict[i]['requirements'] = td[2].text.rstrip()
        table_dict[i]['version'] = td[5].text.rstrip()
        table_dict[i]['difficulty'] = td[6].text.rstrip()
    return table_dict





    
