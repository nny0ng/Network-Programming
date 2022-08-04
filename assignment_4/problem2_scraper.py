import re
import csv
import requests
from bs4 import BeautifulSoup

def GET():
    response = requests.get('https://sites.google.com/view/davidchoi/home/members') # get url
    soup = BeautifulSoup(response.text, 'html.parser') # use beautifulsoup

    file = open('problem2_csv.csv', 'w', newline='') # csv file open
    w = csv.writer(file, delimiter=',') # open with write mode

    result = [] # list of final result

    ### profile picture url
    tmp = ['profile_pic_url'] # list that start is category
    profile_pic_url = soup.select('div.t3iYD > img') # find class
    for std in profile_pic_url:
        a, b = str(std).split('src="', 2) # parsing url
        tmp.append((b.split('"'))[0])
    result.append(tmp) # add to list

    ### name, start year, end year
    start_end_year = soup.select('p.CDt4Ke.zfr3Q') # find class
    std = ['start_year'] # list that start is category
    std2 = ['end_year'] # list that start is category
    name = ['name'] # list that start is category

    ## name
    for i in range(0, len(start_end_year), 2): # even range
        start_end_year[i] = re.sub('<(.+?)>', '', str(start_end_year[i])) # parsing text
        a = start_end_year[i].split('(', 2)
        a[-1] = re.sub(r'[^0-9]', '', a[-1])
        if not a[0] == '': # non blank
            a[0] = a[0].rstrip()
            name.append(a[0])
        if not a[-1] == '': std.append(a[-1]) # non blank
    result.append(name) # add to list

    ## start year
    for i in range(1, len(std)):
        if len(std[i]) == 4: # end year is not exist
            std2.append('NA')
        elif len(std) > 4: # end year is exist
            start = std[i][:len(std[i])//2] # parsing start year
            end = std[i][len(std[i])//2:] # parsing start year
            std[i] = start
            std2.append(end)
    result.append(std) # add to list
    result.append(std2) # add to list

    ### research_interest(for Current Members), current_job_role (for Alumnies)
    # num of current mem = 9
    # num of aluminies mem = 9
    start_end_year = soup.select('p.CDt4Ke.zfr3Q') # find class
    new_array = []
    current = ['research_interest(for Current Members)'] # list that start is category
    alumnies = ['current_job_role(for Alumnies)', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'] # list that start is category, blank is 'NA'

    for i in range(1, len(start_end_year), 2): # odd range
        new_array.append(re.sub('<(.+?)>', '', str(start_end_year[i]))) # parsing text

    for i in range(0, 18): # num of entire member
        if i < 9: # separate list to research interest
            new_array[i] = new_array[i].replace('Research Interests:', '') # delete category of all
            new_array[i] = new_array[i].lstrip() # no blank
            if new_array[i] == '': new_array[i] = 'NA' # blank = 'NA'
            current.append(new_array[i])
        else:
            current.append('NA') # blank = 'NA'

    for i in range(9, len(new_array)): # separate list to current job role
        if not new_array[i] == '': # no blank at front
            alumnies.append(new_array[i])
    result.append(current) # add to list
    result.append(alumnies) # add to list

    ### job role => current not exist
    current_job = ['job_role', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA']
    current_job = current_job + alumnies[10:] # predict alumnies job role is same with current job role
    result.append(current_job) # add to list

    ### write csv
    w.writerows(result)

if __name__ == '__main__':
    GET()