# GSoC-Scraper
### Overview
The repository contains a python script file intended to scrap official GSoC 2021 Result and store the obtained data in a .csv file.
This script employs [requests-html](https://github.com/kennethreitz/requests-html) python library to parse **local copy** of the results page from [GSoC 2021 Results](https://summerofcode.withgoogle.com/projects/).
The script also uses the in-built [csv](https://docs.python.org/3/library/csv.html) library to read and write scrapped data. 
List of files :
- [scraper.py](https://github.com/TheTUFGuy/GSoC-Scraper/blob/main/scraper.py) -the main python code
- [gsoc.html](https://github.com/TheTUFGuy/GSoC-Scraper/blob/main/gsoc.html)  -a copy of the GSoC Results page 
- [gsoc2021.csv](https://github.com/TheTUFGuy/GSoC-Scraper/blob/main/gsoc2021.csv)  -a csv file storing scrapped data
<hr>

### Instructions
- Download the given code locally and make sure all given files are in same directory and that directory has proper read/write permissions.  
- Install requests-html library using the command 
> pip install requests-html  
- Now run the scraper.py file in python and it will write all the data into gsoc2021.csv
That's all!:grinning:
