# parkrun-parse

parkrun-parse will parse multiple park run results, and generate two output files:
* parkrun.csv - A CSV file containing multiple columns of results
* parkrun.png - a line graph graphical representation of the results

Park Run results are aggregated on a per-minute finish time. This allows you to see the bell curve of finishers for a particular park run, and how it compares to other runs. 

## Running the code
You can pass as many arguments as you look, with each argument pointing to a particular Park Run's latest results page:
```
python3 parkrun.py 'https://www.parkrun.org.uk/chelmsfordcentral/results/latestresults/' 'https://www.parkrun.co.za/goldenharvest/results/latestresults/' 'https://www.parkrun.org.uk/brentwood/results/latestresults/'

-- Complete --
I have created two output files: parkrun.csv and parkrun.png
```

## Output
The output image will look like:
![alt text](https://github.com/willie-engelbrecht/parkrun-parse/blob/master/parkrun.png "Line Graph")

In addition, there is also parkrun.csv which contains the raw data that can be imported into your favourite tool like Excel for further analyses. 
