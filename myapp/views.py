from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
import csv
from .import newjob

import requests
from bs4 import BeautifulSoup
import ssl

from csv import writer
import random
import string
# Create your views here.
#allinfo=[]

def home(request):

    if request.method=='POST':
        job=request.POST.get('job')
        location=request.POST.get('location')
        print(job,location)
        try:
            global allinfo 
            allinfo =newjob.scrap(job,location)
            
            res=[]
            #print(allinfo)
            if(len(allinfo[0])==0):
                return render(request,'index.html',{"error":True})
            for i in range(len(allinfo[0])):
                d={}
                d['title']=allinfo[0][i]
                d['company']=allinfo[1][i]
                d['location']=allinfo[2][i]
                d['link']=allinfo[3][i]
                #print(d)
                res.append(d)
                
            #print(res)
                
            dic={'data':res}
            print(len(res))
            request.session['data']=res
            request.session['title']=job+" jobs in "+location+".csv"
            return render(request,'index.html',dic)

        except():
            print("error")
            return render(request,'home.html')
    
    return render(request,'home.html')



def save_file(request):
        # Importing the required modules
    import os
    import sys
    import pandas as pd
    from bs4 import BeautifulSoup

    import requests
    
    import ssl
    import csv
    from csv import writer
    import random
    import string
    from django.http import HttpResponse
    #print("------------------------------")
    temp=request.session['data']
    fname=request.session['title']
    
    #print(fname)
    

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']= 'attachment; filename={t}'.format(t=fname)
    

    
    csv_writer=csv.writer(response)
    
    
    headers = ['Title', 'Location', 'Company','Link']
    csv_writer.writerow(headers)
    
    for element in temp:
        title=element['title']
        location=element['location']
        link=element['link']
        company=element['company']
        my_fields=[title,location,company,link]
                                                               
        csv_writer.writerow([title, location, company,link])

    return response

# def my_view(request, exportCSV):
#     # ... Figure out `queryset` here ...

#     if exportCSV:
#         response = HttpResponse(mimetype='text/csv')
#         response['Content-Disposition'] = 'attachment;filename=export.csv'
#         writer = csv.writer(response)
#         for cdr in queryset:
#             writer.writerow([cdr['calldate'], cdr['src'], cdr['dst'], ])
#         return response
#     else:
#         return render_to_response('index.html', {'queryset': queryset,
#             'filter_form': filter_form, 'validated': validated},
#             context_instance = RequestContext(request))


# def download1(request):
#     import os
#     import sys
#     import pandas as pd
#     from bs4 import BeautifulSoup

#     import requests
    
#     import ssl
#     import csv
#     from csv import writer
#     import random
#     import string
#     from django.http import HttpResponse

#     temp=[]
#     temp=allinfo
#     # Storing the data into Pandas
#     # DataFrame
#     # dataFrame = pd.DataFrame(data = allinfo, columns = list_header)
    
#     print(temp)
    
#     # Converting Pandas DataFrame
#     # into CSV file
#     #dataFrame.to_csv('Results.csv')


#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition']= 'attachment; filename=Res.csv'
#     #dictionaries = [{"column_1": 1, "column_2": 2, "column_3": 3},{"column_1": 4, "column_2": 5, "column_3": 6}]
#     keys = temp[0].keys()
#     print(keys)
#     a_file = open("Res.csv", "w")
#     dict_writer = csv.DictWriter(a_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(temp)
#     a_file.close()

    

#     return response