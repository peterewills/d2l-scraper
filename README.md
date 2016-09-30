# d2l-scraper
A web scraper to build .csv file of names in a D2L dropbox

This script allows you to use Python to scrape a D2L dropbox and build a .csv file of the names of students who have contributed to that dropbox. This script should run in both Python 2 and 3, and it **requires the [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) module**, which comes preinstalled with [Anaconda](https://anaconda.org) (which I strongly recommend for anyone using python for scientific computing).

To use the script, perform the following steps:

1. Download the .html file of the dropbox you wish to scrape. (Go to File -> Save As in your browser.) Give it a simple name, e.g. `dropbox.html`.
   If all users cannot be displayed on one page in D2L, download the pages separately, and see the example below
2. Download `d2l_scraper.py` (or clone this repository!).
3. Open your terminal, and navigate to the directory containing `d2l-scraper.py` (help for [Mac](http://computers.tutsplus.com/tutorials/navigating-the-terminal-a-gentle-introduction--mac-3855), and [Windows](http://www.computerhope.com/issues/chusedos.htm)).
4. Run `python d2l_scraper.py` from the terminal.
5. Follow the onscreen instructions.
6. Shazam!

Note that the `.html` file need not be in the same folder as the python script. However, if this is the case, you'll need to enter the full path of the `.html` file. Similarly, you can designate an arbitrary path for your `.csv` file; no path designation will place it in the current working directory.

You can optionally specify TA names.  d2l_scraper.py will shuffle the TA names and fairly distribute users to each TA.

## Example session with d2l-scraper
```
james@folberjm-2: d2l-scraper$ python d2l_scraper.py 
Enter path of saved html file: /path/to/d2l_1.html
Enter path of saved html file (blank to continue): /path/to/d2l_2.html
Enter path of saved html file (blank to continue): 
Enter TA names (blank to skip): Peter James
Enter desired path of csv file: d2l.csv
Writing list of users to new file `d2l.csv`.
Shazam!
```
