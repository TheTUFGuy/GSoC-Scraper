import csv

filename='data.csv'
with open(filename,'w',encoding='utf8') as csvfile:
    csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\n',
    quoting = csv.QUOTE_MINIMAL)
    csvwriter=csv.writer(csvfile,dialect='mydialect')
    csvwriter.writerow(['Name','Organisation','Project'])

    from requests_html import HTML
    with open('gsoc.html',encoding='utf8') as html_file:
        source=html_file.read()
        r=HTML(html=source)

    lists=r.find('li.project-card')
    for list in lists:
        data=list.find('div.pos-rel',first=True)
        name=data.find('h2',first=True).text
        project=data.find('a.md-soc-theme')
        csvwriter.writerow([name,project[1].text,project[0].text])


csvfile.close()