Convert Crontab Project
=======================

This project involves working with crontab files (a list of cron jobs). For info about crontab see: https://help.ubuntu.com/community/CronHowto

The primary goal was to produce output that tells the user when the next run time, relative to the current time, will be for each cron job in the crontable. Interpreting Cron expressions isn't very user friendly thus a secondary goal was to take each cron job expression and convert it to a human readable form. 

The impetus for this project was based on a tech test that I took for a potential job. It was great practice for parsing data, converting data, and working with dates.


**Here's a simple example:**

crontab file with 4 lines: one comment, 1 blank line, and 2 cron jobs.  
  line 1-  #Test file  
  line 2- 'blank line'  
  line 3-  2 15 * * * app/site/cron/job1.py  
  line 4-  0 0 1 *  * app/site/cron/job2.py   

RESULT 1 Next Run Time (assuming current time is 2014-11-14 8:00):  
&nbsp;&nbsp; JOB NAME: job1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; NEXT RUN TIME: 2014-11-14 15:02  
&nbsp;&nbsp; JOB NAME: job2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; NEXT RUN TIME: 2014-12-01 00:00

RESULT 2 Human Readable (assuming current time is 2014-11-14 8:00):  
&nbsp;&nbsp; JOB NAME: job1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Runs at 02:15 on every day.  
&nbsp;&nbsp; JOB NAME: job2 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Runs at 00:00 on the 1st day of every month.   

                     