"""Program:     AutoPhotoReducer
    Author:      rehab-robotics
      Date:        3/28/2015

Description: To access the NSF GRFP website periodically (via cron or other)
                so you can sleep. If you win the award, it will wake you up to
                celebrate by opening the youtube URL you provide below.

Usage:       Enter your desired URL and first and last name in the url_name and
                name variables below. You should hook this up to cron (or another
                automating service capable of calling terminal programs) so it
                will run on its own.
"""

from BeautifulSoup import BeautifulSoup
import urllib2
import webbrowser
import re
''' Your info. I recommend using only your first and last name, unless you
   have a very common name and are worried about false-positives. Use the smallest
   identifiable school name. ie, if you go to UCSB, use 'Barbara'.

   You need to leave a blank string if you choose not to use a parameter.
   ex, with only a first and last name the dictionary looks like:

   name = {'first': 'rehab',
           'last': 'robotics',
            'school': ''}

   '''
name = {'first': 'Your_First_Name',
        'last': 'Your_Last_Name',
         'school': 'Your_School_Name'}

''' The url of the YouTube video you want to hear in case of victory. (you should
        leave Joey Bada$$ here, but change it if you want, I guess)'''
url_yay = 'https://www.youtube.com/watch?v=DSlNvg18MKc'

'''Leave the rest of the code alone'''
grfp_site = "https://www.fastlane.nsf.gov/grfp/"
html_page = urllib2.urlopen(
    grfp_site + "AwardeeList.do?method=loadAwardeeList")
soup = BeautifulSoup(html_page)

dl_link = ''

for link in soup.findAll('a'):
  if 'export' in link.get('href'):
    dl_link = link.get('href')

awardee_list = urllib2.urlopen(grfp_site + dl_link)
awardee_list1 = awardee_list.read()


success = False
terms = [name['first'], name['last'], name['school']]

'''Using both methods because I'm not sure how to handle this file. Currently the
    returned AwardeeList.do file is blank, so I tested with a local file from
    last year's AwardeeList.do and used python to open it. Either way, one of these
    methods should work'''
for thing in awardee_list1:
  if all(x in thing for x in terms):
    print "Congrats!!!"
    success = True
    webbrowser.open(url_yay)

if not success:
    for thing in awardee_list:
      if all(x in thing for x in terms):
        print "Congrats!!!"
        webbrowser.open(url_yay)
