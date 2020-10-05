#!/usr/bin/env python3

import re
import operator

errorcount = {}
usercount = {}
file = open('syslog.log')
for i in file.readlines():
    m = re.search(r"ERROR ([\w ']*) ", i)
    if m !=None:
        if m.group(1).strip() not in errorcount:
            errorcount[m.group(1).strip()] = 1
        else:
            errorcount[m.group(1).strip()] += 1
file.close()
errorcount=sorted(errorcount.items(), key = operator.itemgetter(1), reverse=True)
file = open('syslog.log')
for i in file.readlines():
    state = re.search(r"ticky: ([\w]+).*\(([\w.]+)", i)
    if state != None:
        if state.group(2) not in usercount:
            if state.group(1) == "INFO":
                usercount[state.group(2)] = {"INFO":1, "ERROR":0}
            elif state.group(1) == "ERROR":
                usercount[state.group(2)] = {"INFO":0, "ERROR":1}
        else:
            if state.group(1) == "INFO":
                usercount[state.group(2)]["INFO"] += 1
            elif state.group(1) == "ERROR":
                usercount[state.group(2)]["ERROR"] += 1
file.close()
usercount=sorted(usercount.items(), key = operator.itemgetter(0))
with open('error_message.csv','w+') as f:
    f.write('ERROR'+','+'COUNT'+'\n')
    for k,v in errorcount:
        f.write(k+','+str(v)+'\n')
with open('user_statistics.csv','w+') as f:
    f.write("Username"+','+ "INFO"+','+ "ERROR"+'\n')
    for k,v in usercount:
        f.write(k+','+str(v["INFO"])+','+str(v["ERROR"])+'\n')
