import json, codecs

url = 'marks.json'

with codecs.open(url, "r", "utf_8_sig" ) as j:
    j1 = j.read()
    p = json.loads(j1)
    
subj = p['subjects']
class_data = []
for i, s in enumerate(subj, start=1):
    d = [s['name']]
    for subs in s['periods']:
        kOTL = 0
        kKZ = 0
        kUO = 0
        k2 = 0
        k = 0
        for s1 in subs['final_marks']:
            mark = int(s1['value'])
            
            if mark > 4:
                kOTL += 1
            if mark > 3:
                kKZ += 1
            if mark > 2:
                kUO += 1
            if mark < 3:
                k2 += 1
            k += 1
        if k > 0:
            d += ['%.1f' % (kOTL * 100 / k) + '%', '%.1f' % (kKZ * 100 / k) + '%', '%.1f' % (kUO * 100 / k) + '%','%.1f' % (k2 * 100 / k) + '%']
    print(d)
        

