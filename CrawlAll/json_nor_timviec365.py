import json
import datetime
import re

from pyasn1.compat.octets import null

def fix_salary(salary):
    if not(salary):
        return []
    sals = []
    salar = []
    if len(re.findall('triệu', salary)) > 0:
        sals = re.findall('\d+(?:\,\d+)?', salary) # tìm các con số
        for sal in sals:
            if len(sal) > 5:
                sal = re.sub(',', '', sal)
                sala = int(sal)/1000
                salar.append(int(sala))
                continue
            if len(re.findall(',', sal)) > 0:
                sala = re.sub(',', '', sal)
                sala = int(sala)*100
                salar.append(int(sala))
                continue
            sala = int(sal)*1000
            salar.append(int(sala))
        return salar

    if len(re.findall('USD', salary)) > 0:
        string_sal = re.sub(',', "", salary) # loại bỏ dấu ,
        sals = re.findall('\d+', string_sal) #tìm các con số
        for sal in sals:
            sala = int(sal) * 23000 / 1000  # đổi USD sang VNĐ
            salar.append(int(sala))
        return salar
    sall = []
    sall.append(salary)
    return sall
with open('timviec365.json', encoding='utf-8') as json_file:
    datas = json.load(json_file)

for data in datas:
    data['Salary'] = fix_salary(data['Salary']) #fix salary


with open('DataAfterFix/timviec365_after_fix.json', 'w', encoding='utf-8') as json_file:
  json.dump(datas, json_file, ensure_ascii=False)
