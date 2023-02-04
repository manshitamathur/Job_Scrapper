
def scrap(job,loc):
    import requests
    from bs4 import BeautifulSoup
    title=[]
    company=[]
    location=[]
    link=[]

    try:
        
        for i in range(25,170,25):
            url="https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords="+job+"&location="+loc+"&geoId=&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0&start="+str(i)

        
            r = requests.get(url).text
            soup=BeautifulSoup(r,'html.parser')
            
            #spans_title=soup.find_all('span', {"class": "screen-reader-text"})
            spans_title=soup.find_all('h3',{"class":"base-search-card__title"})
            
            for span in spans_title:
                title.append(span.text.strip())

        
            span_location=soup.find_all('span',"job-search-card__location")
            for span in span_location:
                location.append(span.text.strip())



            span_company=soup.find_all('h4',"base-search-card__subtitle")
            for span in span_company:
                company.append(span.text.strip())


            for a in soup.find_all('a', href=True):
                if(a['href'].find('view')!=-1):
                    link.append(a['href'])
                    
        res=[title,company,location,link]
        return res
    except Exception as e:
        print(e)    
   

