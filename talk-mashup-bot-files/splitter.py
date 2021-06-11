#!/usr/bin/python
# -*- coding: utf-8 -*-

infile = open('ala_all-talk-titles.txt','r',encoding='UTF-8')
text = infile.readlines()
infile.close()

outfilebeg = open("ala_beginners.txt","w")
outfileend = open("ala_enders.txt","w")

beginners = []
enders = []

splitat = ['at','of','for','on','and']

needsplittingdupes = []
needsplitting = []

for line in text:
    line = line.split()
    i = -1
    for word in line:
        i += 1
        if word[-1] == ':':
            beginners.append(line[0:i+1])
            enders.append(line[i+1:])
        elif word[-1] == '?':
            beginners.append(line[0:i+1])
            enders.append(line[i+1:])
        elif word[-1] == '!':
            beginners.append(line[0:i+1])
            enders.append(line[i+1:])
        elif word.lower() in splitat:
            w = word
            beginners.append(line[0:i+1])
            enders.append(line[i+1:])
        else:
            needsplittingdupes.append(line)

for line in needsplittingdupes:
    if line in needsplitting:
        pass
    elif len(line) > 4: #short titles tend to be names, plus might split uninterestingly
        pass
    else:
        mid = len(line) / 2 #find rough halfway point in line
        mid = int(mid) #turn to integer
        beginners.append(line[:mid])
        enders.append(line[mid:])
        needsplitting.append(line)


for b in beginners:
    outfilebeg.write(' '.join(b))
    outfilebeg.write('\n')
for e in enders:
    outfileend.write(' '.join(e))
    outfileend.write('\n')


outfilebeg.close()
outfileend.close()

print(done)
