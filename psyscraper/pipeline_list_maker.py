#!/usr/bin/python

import re
from titlecase import titlecase

def abbreviations(word, **kwargs):
    if word.upper() in ('ADD', 'ADHD', 'CJD', 'NOS', 'MDMA', 'LSD', 'BZP', 'GABA', 'NMDA', 'HPA', 'P300', 'AIMS', 'GAF', 'PANSS', 'BPRS', 'MAOI', 'SSRI', 'MRI', 'DTI', 'NMR', 'THC', 'HAM-A', 'HAM-D', 'CGI', '5-HT', 'OCD', 'PTSD', 'ADNI'):
        return word.upper()

with open('/home/james/Desktop/psyscraper/psyscraper/pipeline_keyword_doc', 'rb') as f:
    mylist = map(str.strip, f)

with open('/home/james/Desktop/psyscraper/psyscraper/pipeline_keyword_list', 'w') as g:
    for item in mylist:
        item = titlecase(item, callback=abbreviations)
        #item  = "'%s',"%(item)
        print >> g, item
    
with open('/home/james/Desktop/psyscraper/psyscraper/pipeline_keyword_list', 'rb') as h:
    mylist2 = map(str.strip, h)
    mylist2.sort()
    
with open('/home/james/Desktop/psyscraper/psyscraper/pipeline_keyword_list', 'w') as i:
    for item in mylist2:
        print >> i, item

with open('/home/james/Desktop/psyscraper/psyscraper/pipeline_keyword_list', 'rb') as j:
    mylist3 = map(str.strip, j)   
    
with open('/home/james/Desktop/psyscraper/psyscraper/pipeline_keyword_list_lower', 'w') as k:
    for item in mylist3:
        item = item[:].lower()
        print >> k, item
