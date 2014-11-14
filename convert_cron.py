### NOTE: Currenlty doesn't fully work for the crontab_short.txt sample file. Getting there.

import re
from datetime import datetime

# TO DO: consider setting this up as a Class(es).
'''
def parse_file() takes a crontab file(inputfile) and returns a list of lists named 
'parsed_data'. Each line of the inputfile becomes a list, with each whitespace
delimitted item being a list element.

EXAMPLE: 
    inputfile:  line 1 of file-  #Test file
                line 2 of file- 'blank line'
                line 3 of file-  */2 15   *  * * cron/job2.php 
    result: [['#Test', 'file'], [], ['*/2', '15', '*', '*', '*', 'cron/job2.php']]
'''
def parse_file(inputfile):
    inputfile = open(inputfile)
    parsed_data = []

    for line in inputfile:
        parsed_data.append(line.split())
    # print "PARSED DATA ", parsed_data
    return parsed_data


# TO DO: This is incomplete and doesn't account for all crontab possibilities.
def interpret_crontab(parsed_data):
    values = []
    now = datetime.now()
    parsed_data = parsed_data

    if parsed_data[0] == "*":
        values.append(now.minute())
    elif "/" in parsed_data[0]:
        item = parsed_data[0]
        item = item[2:]
        values.append(item)
    else: 
        values.append(parsed_data[0])

    if parsed_data[1] == "*":
        values.append(now.hour)
    elif "/" in parsed_data[1]:
        item = parsed_data[1]
        item = item[2:]
        values.append(item)
    else: 
        values.append(parsed_data[1])

    if parsed_data[2] == "*":
        values.append(now.day)
    else: 
        values.append(parsed_data[2])

    if parsed_data[3] == "*":
        values.append(now.month)
    elif "/" in parsed_data[3]:
        item = parsed_data[3]
        item = item[2:]
        values.append(item)
    else: 
        values.append(parsed_data[3])

    if parsed_data[4] == "*":
        values.append(now.isoweekday()) # use isoweekday() instead of weekday()
    else: 
        values.append(parsed_data[4])
    print 'VALUES: ', values
       
    # last item in list contains path for job file
    job_path = parsed_data[-1]
    job_name = re.search("(job\d+).py", job_path)
    
    if job_name:
        job_name = job_name.group(1)


# TO DO: Consider breaking this next section into a separate function.
    '''
    Determine if current time is after or before cron job time by subtracting current time
    from the scheduled cron time and determining if value is positive or negative. Haven't worked this into logic.
    For example, in some cases if current time is past last cron time, 
    # then add +1 day to cron time.
    '''
    cron_time = "%s-%s-%s %s:%s" %(now.year, values[3], values[2],
        values[1], values[0])

    # converts cron_time string to datetime object.
    cron_time_obj = datetime.strptime(cron_time, "%Y-%m-%d %H:%M") 
    time_diff = cron_time_obj - now

    # print 'TIME DIFF: ', time_diff

    if time_diff.days > 0:
        #converts cron_time datetime object to a string.
        cron_time_f = datetime.strftime(cron_time_obj, "%Y-%m-%d %H:%M")
    else:
        values[2] = int(values[2]) + 1
        cron_time = "%s-%s-%s %s:%s" %(now.year, values[3], values[2],
            values[1], values[0])
        cron_time_obj = datetime.strptime(cron_time, "%Y-%m-%d %H:%M")
        cron_time_f = datetime.strftime(cron_time_obj, "%Y-%m-%d %H:%M")

    # FINAL OUTPUT. Ideally output would be formatted and written to an HTML file.
    print "JOB NAME:", job_name + '   ' + "CRON TIME: " + cron_time_f + '\n'


'''
def run_parse_interpret () runs def parse_data() and then def interpret_crontab().
For each line of the crontab file it prints the cron job name and the cron time.
''' 
def run_parse_interpret(crontab_file):
        parsed_data = parse_file(crontab_file)
   
        for item in parsed_data:
            if not item: # ignores an empty list (ie. an empty line in the crontab file)
                pass

            # Checks for items that have an empty list starting with '#' (ie. comments)
            # that have either only 1 list item ([0], line in file has no spaces) or 
            # have >1 list items (thus need to check [0][0]).   
            elif "#" in item[0] or "#" in item[0][0]:
                pass
                # print "COMMENT", item
            else:
                interpret_crontab(item)


# NOTE: Currently, can only handle crontab expressions without ranges or commas.
# so have to use crontab_small.txt file instead of crontab-1.txt.

crontab_file = 'crontab_short.txt'
run_parse_interpret(crontab_file)
