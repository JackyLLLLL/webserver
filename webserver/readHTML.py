import bs4

path = '/home/pi/Jacky/webserver/static/index.html'

with open(path,'a') as f:

    Soup = bs4.BeautifulSoup(f.read(),'lxml')

    titles = Soup.select('p')
    print(len(titles))
    print(titles[6])
    print(titles[7])
    
    temp="26.5*C"
    RH  = "80%"
    titles.insert(6,"<p>目前溫度:%s</p>"%temp)
    titles.insert(7,"<p>目前濕度:%s</p>"%RH)

