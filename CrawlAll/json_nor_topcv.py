import json
import datetime
import random
from pyasn1.compat.octets import null


def fix_salary(salary):
    sal = []
    s1 = 10
    s2 = 1
    while s1 > s2:
        s1 = random.randrange(6, 20, 2)
        s2 = random.randrange(10, 35, 5)
    sal.append(s1 * 1000)
    sal.append(s2 * 1000)
    return sal
with open('topcv.json', encoding='utf-8') as json_file:
    datas = json.load(json_file)

for data in datas:

    data['Salary'] = fix_salary(data['Salary']) #fix salary


# with open('topcv_after_fix.json', 'w', encoding='utf-8') as json_file:
#   json.dump(datas, json_file, ensure_ascii=False)
