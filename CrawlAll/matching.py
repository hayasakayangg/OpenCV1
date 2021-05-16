import pandas as pd
from pathlib import Path
import fuzzymatcher

cb_path = r'C:/Users/Admin/PycharmProjects/OpenCV1/CrawlAll/Data_after_fix/CareerBuilder_after_fix.json'
jg_path = r'C:/Users/Admin/PycharmProjects/OpenCV1/CrawlAll/Data_after_fix/jobsgo_after_fix.json'
tv365 = r'C:/Users/Admin/PycharmProjects/OpenCV1/CrawlAll/Data_after_fix/timviec365_after_fix.json'
tcv = r'C:/Users/Admin/PycharmProjects/OpenCV1/CrawlAll/Data_after_fix/topcv_after_fix.json'
career_builder = pd.read_json(cb_path, encoding='utf-8')
jobsgo = pd.read_json(jg_path, encoding='utf-8')
timviec365 = pd.read_json(tv365, encoding='utf-8')
topcv = pd.read_json(tcv, encoding='utf-8')

left_timviec365 = ["Job_Name", "Company_Name", "Address", "Salary"]

right_topcv = ["Job_Name", "Company_Name", "Address", "Salary"]

matched_results = fuzzymatcher.fuzzy_left_join(
    timviec365, topcv, left_timviec365, right_topcv,
    left_id_col="Job_Name", right_id_col="Job_Name")

cols = [
    "best_match_score", "Job_Name_left", "Job_Name_right", "Company_Name_left",
    "Company_Name_right", "Address_left", "Address_right", "Salary_left", "Salary_right"
]

matchedd = matched_results[cols].sort_values(
    by=['best_match_score'], ascending=False).head(5)

pd.set_option('display.max_columns', 10)

print(matchedd)
