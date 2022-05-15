import requests, time, sys, json

#подключаем сессию
session = requests.Session()
f = open('N:\Журналы\cookies.dat', 'r')
for line in f:
   line = line.strip()
   if line == '': continue
   pl = line.split('=',maxsplit=1)
   session.cookies.set(pl[0], pl[1])
f.close()

response = session.get('https://dnevnik.mos.ru/core/api/class_units?academic_year_id=9&pid=29396719&with_home_based=true')
if response.status_code > 400:
   print('обновите профиль')
   time.sleep(2)
   sys.exit(10)
s = json.loads(response.content)
class_list = dict()
for item in s:
    try:
        class_list[item['display_name']] = item['id']
    except KeyError:
        continue
print(class_list)
'''
for i in range(len(class_list)):
    print(i, class_list[i])'''
        


