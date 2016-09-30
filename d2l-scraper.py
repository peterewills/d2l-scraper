from __future__ import print_function
import sys
from bs4 import BeautifulSoup as bs
import csv

def get_user_input(prompt):
    """
    If python3, return input(*args)
    If python2, return raw_input(*args)
    """
    if sys.version_info > (3,0): # python 3
        return input(prompt)
    else: # python 2
        return raw_input(prompt)
    
# This function scrapes the .html file downloaded from D2L and yields a list
# of the users, in the form 'Last, First'

def get_user_strings():
    
    location = get_user_input('Enter path of saved html file: ')
    html = open(location).read()

    soup = bs(html,'lxml')

    user_tags = soup.find_all('a',{'title':'Email this user'})
    user_strings = [str(user.string) for user in user_tags]

    return user_strings

# This function splits the string of the directory style name into two
# separate strings, one for last and one for first name.

def split_name(name):

    split = name.find(',')
    last = name[:split]
    first = name[split+2:]

    return [last,first]

# This function takes the list of users and writes it to a .csv file. There
# are stupid spaces 

def csv_write(user_strings):

    name = get_user_input('Enter desired path of csv file: ')
    while name[len(name)-4:] != '.csv':
        name = get_user_input('Gotta end in .csv! Try again: ')

    with open(name,'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',skipinitialspace=True,
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for user in user_strings:
            spamwriter.writerow(split_name(user))


# Now we run everything, and exclaim our amazement at the result.
if __name__ == '__main__':
    user_strings = get_user_strings()
    csv_write(user_strings)
    print('Shazam!')
