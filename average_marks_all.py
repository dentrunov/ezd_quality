#средние оценки для всех классов
import requests, time, sys, json
from openpyxl import Workbook

#подключаем сессию
session = requests.Session()
f = open('N:\Журналы\cookies.dat', 'r')
for line in f:
   line = line.strip()
   if line == '': continue
   pl = line.split('=',maxsplit=1)
   session.cookies.set(pl[0], pl[1])
f.close()

#список классов из скрипта рядом
classes = {'1А': 563649, '1Б': 563648, '1В': 563645, '1Г': 563644, '1Д': 563643, '1Е': 563642, '1Ж': 563647, '1З': 563646, '1И': 585135, '1К': 592068, '1Л': 591606, '2А': 434397, '2Б': 404325, '2В': 434396, '2Г': 434394, '2Д': 467730, '2Е': 467729, '2Ж': 467725, '2З': 467723, '2И': 583353, '2К': 590201, '3А': 434420, '3Б': 434419, '3В': 404324, '3Г': 404321, '3Д': 467728, '3Е': 467726, '3Ж': 467722, '3З': 467721, '3И': 514117, '3К': 552548, '3Л': 570997, '3М': 587438, '3Н': 591995, '4А': 434395, '4Б': 434393, '4В': 434392, '4Г': 434410, '4Д': 467727, '4Ж': 467717, '4З': 467716, '4И': 552550, '4К': 585214, '4М': 591717, '5А': 404323, '5Б': 434418, '5В': 434379, '5Г': 404318, '5Д': 434376, '5Е': 467719, '5Ж': 467715, '5З': 514115, '5И': 570998, '5К': 591607, '6А': 404322, '6Б': 434411, '6В': 404317, '6Г': 434408, '6Д': 467718, '6Е': 467506, '6Ж': 467712, '6З': 552549, '6И': 578817, '6К': 590867, '7А': 404320, '7Б': 404319, '7В': 404315, '7Г': 434373, '7Е': 467713, '7Ж': 467708, '7З': 578818, '7И': 592825, '8А': 404316, '8Б': 434409, '8В': 434407, '8Г': 404313, '8Д': 467711, '8Е': 467709, '8Ж': 467706, '8З': 578819, '9А': 434377, '9Б': 434374, '9В': 404314, '9Г': 404312, '9Д': 467710, '9Е': 467707, '9Ж': 574934, '10А': 434427, '10Б': 404329, '10В': 404328, '10Г': 434426, '10Д': 467705, '10Е': 467704, '10Ж': 559244, '11А': 434402, '11Б': 434401, '11В': 434400, '11Г': 434368, '11Д': 514112, '11Е': 514111}

#создаем файл эксель
wb = Workbook()
dest_filename = 'N:\Журналы\quality_book.xlsx'
ws1 = wb.active
ws1.title = "Качество знаний по классам"
ws1['A1'] = 'Класс'
ws1['B1'] = 'Предмет'
ws1['C1'] = 'Период'
ws1['D1'] = 'Отличники'
ws1['E1'] = 'Качество знаний'
ws1['F1'] = 'Уровень обученности'
ws1['G1'] = 'Неудовлетворительно'
#wb.save(dest_filename)
row = 2
for cl in classes:
    print(cl)
    response = session.get(f'https://dnevnik.mos.ru/reports/api/final_marks/json?academic_year_id=9&class_unit_id={classes[cl]}&in_string=subjects&pid=29396719&with_deleted=false')
    if response.status_code > 400:
       print('обновите профиль')
       time.sleep(3)
       sys.exit(10)
    s = json.loads(response.content)

    class_data = []
    class_name = cl
    subj = s['subjects']
    for i, s in enumerate(subj, start=1):
        subjectName = s['name']
        d = [subjectName]
        for subs in s['periods']:
            kOTL = 0
            kKZ = 0
            kUO = 0
            k2 = 0
            k = 0
            period_name = subs['name']
            for s1 in subs['final_marks']:
                try:
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
                except: continue

            if k > 0:
                d += ['%.1f' % (kOTL * 100 / k) + '%', '%.1f' % (kKZ * 100 / k) + '%', '%.1f' % (kUO * 100 / k) + '%','%.1f' % (k2 * 100 / k) + '%']
                ws1['A'+str(row)] = class_name
                ws1['B'+str(row)] = subjectName
                ws1['C'+str(row)] = period_name
                ws1['D'+str(row)] = str(kOTL * 100 / k) + '%'
                ws1['E'+str(row)] = str(kKZ * 100 / k) + '%'
                ws1['F'+str(row)] = str(kUO * 100 / k) + '%'
                ws1['G'+str(row)] = str(k2 * 100 / k) + '%'
                row += 1
        print(d)


wb.save(dest_filename)

