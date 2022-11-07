from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request,'Helloapp/home.html')


from django.shortcuts import render
import pandas as pd

# sheet_url = "https://docs.google.com/spreadsheets/d/1hyKMSMfkWXtPDisZ8uCXOtTpGx0JjeVDnvnHdadWhiY/edit#gid=0"
# url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

# df = pd.read_csv(url_1)
def index(request):
    """ view function for sales app """

    # read data                                                                                                  
	
    df = pd.read_csv(r"C:\\Users\\Parmeet.bhatia\\OneDrive - Incedo Technology Solutions Ltd\\Desktop\\Car_sales.csv")
    rs = df.groupby("Engine size")["Sales in thousands"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories, 'values': values, 'table_data':table_content}
    return render(request, 'Helloapp/home.html', context=context)    

def bar(request):
    """ view function for sales app """

    # read data                                                                                                  
	
    df = pd.read_csv(r"C:\\Users\\Parmeet.bhatia\\OneDrive - Incedo Technology Solutions Ltd\\Desktop\\Car_sales.csv")
    rs = df.groupby("Engine size")["Sales in thousands"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories, 'values': values, 'table_data':table_content}
    return render(request, 'Helloapp/home2.html', context=context)  

def spider(request):
    """ view function for sales app """

    # read data                                                                                                  
	
    df = pd.read_csv(r"C:\\Users\\Parmeet.bhatia\\OneDrive - Incedo Technology Solutions Ltd\\Desktop\\Population.csv")
    ID = list(df["ID"])
    Parent = list(df["Parent"])
    Name = list(df["Name"])
    Value = list(df["Value"])


    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"ID": ID, 'Parent': Parent,'Name':Name,'Value':Value, 'table_data':table_content}
    return render(request, 'Helloapp/spider.html', context=context)   

def convert(request):
    return render(request,'Helloapp/ExceltoJson.html')    