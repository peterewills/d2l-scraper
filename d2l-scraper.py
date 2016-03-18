from bs4 import BeautifulSoup as bs
import csv

# This function scrapes the .html file downloaded from D2L and yields a list
# of the users, in the form 'Last, First'

def get_user_strings():

    location = raw_input('Enter path of saved html file: ')
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

    name = raw_input('Enter desired path of csv file: ')
    while name[len(name)-4:] != '.csv':
        name = raw_input('Gotta end in .csv! Try again: ')

    with open(name,'wa') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',skipinitialspace=True,
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for user in user_strings:
            spamwriter.writerow(split_name(user))


# Now we run everything, and exclaim our amazement at the result.
user_strings = get_user_strings()
csv_write(user_strings)
print 'Shazam!'
