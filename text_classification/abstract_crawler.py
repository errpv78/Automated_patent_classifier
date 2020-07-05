import requests
import bs4 as bs
import urllib.request
import csv

# field names 
fields = ['URL', 'Abstract']

filename = "sample_test_data_live.csv"

f = open('test_link2.txt')


with open(filename, 'w') as csvfile:
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile)

    # writing the fields 
    csvwriter.writerow(fields)

    # writing the data rows 

mydict = []

count = 0

for i in f:
    url = i [:-1]
    print(url,count)
    row = []
    row.append(url)
    try:
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source, 'lxml')
        count += 1
    except:
        row.append("Not Found\n")


    for tag in soup.find_all("meta"):
        if tag.get("name", None) == "description":
            # print(tag.get("content", None))
            row.append(tag.get("content", None))

        company = soup.find_next('h1', 'id:title')
        print(company)
        # for i in (soup.find_all("h1")):
        #     print(i.get('id'))
    mydict.append(row)
    if len(mydict) > 5:
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            #     print(row)
            csvwriter.writerows(mydict)
        mydict = []
if len(mydict) > 0:
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        #     print(row)
        csvwriter.writerows(mydict)
