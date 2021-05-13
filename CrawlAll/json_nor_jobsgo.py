import json
import datetime
import re
import datetime


def fix_deadline(deadline):
    cooldown = int(re.sub('\D', '', deadline))
    date = datetime.date.today() + datetime.timedelta(days=cooldown)
    dead = date.strftime("%d/%m/%Y")
    return dead
def fix_salary(salary):
    if not(salary):
        return []
    sals = []
    salar = []
    if len(re.findall('VNĐ', salary)) > 0 or len(re.findall('triệu', salary)) > 0:
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
with open('Jobsgo.json', encoding='utf-8') as json_file:
    datas = json.load(json_file)


for data in datas:
    data['Salary'] = fix_salary(data['Salary']) #fix salary
    data['Deadline'] = fix_deadline(data['Deadline'])

# with open('jobsgo_after_fix.json', 'w', encoding='utf-8') as json_file:
#   json.dump(datas, json_file, ensure_ascii=False)
