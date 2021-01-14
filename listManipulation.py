#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 02:05:35 2020

@author: TheDongBringer
"""

import pandas as pd
from collections import Counter




taglist = [['thatracingchannel', 'trc'], 'thatracingchannel', 'trc', ['Silvia', 'nissansilvia', 's13', '180sx', '240sx', 'boost', 'stance', 'stancenation', 'nissan', 'nismo', 's14', 's15', 'schassis', 'drift', 'turbo', 'jdm', '2jzgte', 'schassissocialclub', 'stanced', 'kouki', '2jz', '2jztheworld', 'rb26', 'rb26dett', 'jdmgoodness', '240sxcoupe', '240sxhatch', 'rps13', '240sxgram'], 'Silvia', 'nissansilvia', 's13', '180sx', '240sx', 'boost', 'stance', 'stancenation', 'nissan', 'nismo', 's14', 's15', 'schassis', 'drift', 'turbo', 'jdm', '2jzgte', 'schassissocialclub', 'stanced', 'kouki', '2jz', '2jztheworld', 'rb26', 'rb26dett', 'jdmgoodness', '240sxcoupe', '240sxhatch', 'rps13', '240sxgram', ['subarusti', 'subaruwrx', 'subie', 'subiegang', 'subie001', 'subieflow', 'eatsleepsubaru', 'subieaddicts', 'subielove', 'subieculture', 'subiecity', 'subielicious', 'subaru', 'wrx', 'sti', 'subispeedme'], 'subarusti', 'subaruwrx', 'subie', 'subiegang', 'subie001', 'subieflow', 'eatsleepsubaru', 'subieaddicts', 'subielove', 'subieculture', 'subiecity', 'subielicious', 'subaru', 'wrx', 'sti', 'subispeedme']

flat_list = []
_ = [flat_list.extend(item) if isinstance(item, list) else flat_list.append(item) for item in taglist if item]
count = Counter(flat_list)
print(count)
##### or
count2 = dict((x,flat_list.count(x)) for x in set(flat_list))
print(count2)
#df = pd.DataFrame(flatten)
# flatList = [ item for elem in taglist for item in elem]


#def single_list(list,ignore_types=(str)): 
# for item in list:
#      if isinstance(item, Iterable) and not isinstance(item, ignore_types):
#          yield from single_list(item,ignore_types=(str))
#      else:
#          yield item
#
#items_single=single_list(taglist)
#dict((x,items_single.count(x)) for x in set(items_single))
#for item in items_single:
#    print(item)
