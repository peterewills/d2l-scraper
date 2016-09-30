from __future__ import print_function
import sys # for python2/3
from bs4 import BeautifulSoup as bs
import csv
import string, random # for TA names
import os # detect if CSV file exists


def get_user_input(prompt):
    """
    If python3, return input(*args)
    If python2, return raw_input(*args)
    """
    if sys.version_info > (3,0): # python 3
        return input(prompt)
    else: # python 2
        return raw_input(prompt)
    
def get_user_strings():
    """
    This function scrapes the .html file downloaded from D2L and yields a list
    of the users, in the form 'Last, First'.  You can use the prompt multiple times
    to specify multiple HTML files.
    """
    def get_user_strings_from_file(location):
        with open(location) as f:
            html = f.read()
            soup = bs(html, 'lxml')
            user_tags = soup.find_all('a',{'title':'Email this user'})
            return [str(user.string) for user in user_tags]

    user_strings = []
    location = get_user_input('Enter path of saved html file: ')
    #location = get_user_input('Enter path of saved html file                : ')
    user_strings += get_user_strings_from_file(location)
    while location:
        location = get_user_input('Enter path of saved html file (blank to continue): ')
        if location:
            user_strings += get_user_strings_from_file(location)
        else: return user_strings
    
def get_TA_names():
    """
    Prompt the user for a list of TA names.
    For example,
        Enter TA names (blank to skip): Peter James
    or
        Enter TA names (blank to skip): ["Peter", "James"]
    """
    ls = get_user_input('Enter TA names (blank to skip): ')
    try:
        return eval(ls)
    except SyntaxError: # not formatted as Python list
        return list(map(str, ls.split()))

def split_name(name):
    """
    This function splits the string of the directory style name into two
    separate strings, one for last and one for first name.
    """

    split = name.find(',')
    last = name[:split]
    first = name[split+2:]

    return [last,first]

def csv_write(user_strings, TA_names):
    """
    This function takes the list of users and writes it to a .csv file. There
    are stupid spaces 
    """

    name = get_user_input('Enter desired path of csv file: ')
    while name[len(name)-4:] != '.csv':
        name = get_user_input('Gotta end in .csv! Try again: ')
    
    if os.path.exists(name):
        print('Appending list of users to existing file `{}`.'.format(name))
    else:
        print('Writing list of users to new file `{}`.'.format(name))
    
    # if we want to distribute the projects amongts the TAs
    if TA_names:
        random.shuffle(TA_names)
        
        # try to distributed the number of projects to grade fairly
        n_base = len(user_strings)//len(TA_names)
        TA_num_list = [[ta, n_base] for ta in TA_names]
        for i in range(len(user_strings)-len(TA_names)*n_base):
            ind = i%len(TA_names)
            TA_num_list[ind][1] += 1
        
        if len(user_strings) != sum(map(lambda x: x[1], TA_num_list)):
            raise RuntimeError("We didn't distribute the projects correctly.  This is a bug.")

        with open(name,'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',skipinitialspace=True,
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
            ind=0
            for ta, num in TA_num_list:
                spamwriter.writerow([ta])
                for user in user_strings[ind:ind+num]:
                    spamwriter.writerow(split_name(user))
                spamwriter.writerow(['',''])
                ind += num
    
    # write the CSV of all users
    else:
        with open(name,'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',skipinitialspace=True,
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for user in user_strings:
                spamwriter.writerow(split_name(user))


# Now we run everything, and exclaim our amazement at the result.
if __name__ == '__main__':
    user_strings = get_user_strings()
    TA_names = get_TA_names()
    csv_write(user_strings, TA_names)
    print('Shazam!')
