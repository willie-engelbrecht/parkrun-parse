from bs4 import BeautifulSoup
import csv
import sys
import datetime
from urllib.parse import urlparse

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))

try:
    from urllib.request import Request, urlopen  # Python 3
except ImportError:
    from urllib2 import Request, urlopen  # Python 2

if len(sys.argv) < 2:
    print("Please supply at least one Park Run URL, up to as many as you want")
    exit(0)

# Prep the dictionary
csvrows = {}
for i in range(0, 90):
    csvrows[i] = 0

# Main loop, loop through each url given
for url in sys.argv:
    try:
        req = Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
        html = urlopen(req).read()
        soup = BeautifulSoup(html, features="html.parser")
        table = soup.find("table")

        # Parse the URL, and extract the run name
        o = urlparse(url)
        splits = o.path.split("/")
        

        # Extract the data out of each row (<tr>) into different elemnts (<td>)
        output_rows = []
        for table_row in table.findAll('tr'):
            columns = table_row.findAll('td')
            output_row = []
            for column in columns:
                output_row.append(column.text)
            output_rows.append(output_row)


        # Remove the first row, as that contains the headers
        output_rows.pop(0)

        # Prep the dictionary
        rows = {}
        for i in range(0, 90):
            rows[i] = 0

        # Take the minute portion of the time, and increment the counter by 1
        for t in output_rows:
            if t[2]:
                pos = int(t[2].split(":")[0])
                rows[pos] += 1

        # Reset pos[1] to 0. This counts wrong times captured
        rows[1] = 0

        # Flip the structure around, and prep the data for matplotlib
        x = []
        y = []
        for i in range(0,90):
            if not csvrows[i]:
                csvrows[i] = [rows[i]]
            else:
                csvrows[i].append(rows[i])            
            x.append(i)
            y.append(rows[i])

        # Draw the plot for this run
        plt.plot(x, y, marker='.', label=splits[1])
    except ValueError:
        pass

# Save to CSV file
with open('parkrun.csv', 'w') as f:
     for i in range(0,90):
        v = csvrows[i]
        s = ''
        for v2 in v:
            s += str(v2) + ","
        f.write(str(s[:-1]) + "\r\n")


# Generate the output image
plt.xticks(np.arange(min(x), max(x)+1, 2.0))
plt.title('Comparing Park Run times  -  ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
plt.xlabel('Time')
plt.ylabel('Number of runners')
plt.legend(loc='best')
plt.savefig('parkrun.png')

print("\n-- Complete --")
print("I have created two output files: parkrun.csv and parkrun.png")
