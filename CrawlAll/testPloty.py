import pandas as pd
import plotly.express as px
import math
import json
import numpy as np

def create_data_city():
    # Mở file việc làm
    job_all = pd.read_csv('C:/Users/Admin/Desktop/CSV-THDL/allcr1/all_dup.csv')

    #Tạo bản sao
    df2 = job_all.copy()

    # Chuẩn hóa tên tỉnh/ thành
    df2['Address'] = df2['Address'].replace("[\[\'\]]", "", regex=True)
    cities = df2['Address'].replace("Hồ Chí Minh", "TP. Hồ Chí Minh")

    #Lấy ra tên tỉnh/ thành độc nhất
    unique = cities.unique()

    s = np.zeros(unique.shape[0], dtype=int)
    # Đếm số lần xuất hiện ở mỗi thành phố
    for i in range(cities.shape[0]):
        for j in range(unique.shape[0]):
            if cities.loc[i] == unique[j]:
                s[j] += 1

    #Chuyển sang Logarit
    log = []
    for i in range(len(s)):
        log.append(math.log10(s[i] + 1))

    # Tạo data 2 cột: tên tỉnh/ thành & log10(số job mỗi tỉnh + 1)
    data = {'City': unique, 'Log': log, 'Num of Job': s}
    df3 = pd.DataFrame(data)
    return df3

# Vẽ lên map
def map(data):
    #Mở file GeoJson của Việt Nam
    with open('C:/Users/Admin/Desktop/vn_iso_province.geojson', 'r', encoding='utf-8') as f:
        vn = json.load(f)
    # fig = px.choropleth(data, geojson=vn, locations='City', color='Log',
    #                     featureidkey='properties.Name_VI',
    #                     color_continuous_scale="Viridis",
    #                     range_color=(0, 3.5),
    #                     hover_name = 'Num of Job',
    #                     hover_data = ['Num of Job'],
    #                     scope="asia",
    #                     )
    # fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    # fig.write_html("C:/Users/Admin/PycharmProjects/OpenCV1/CrawlAll/job_vn.html")
    fig = px.choropleth_mapbox(data, geojson=vn, locations='City', color='Log',
                               featureidkey='properties.Name_VI',
                               color_continuous_scale="Viridis",
                               range_color=(0, 3.5),
                               hover_name='Num of Job',
                               hover_data=['Num of Job'],
                               mapbox_style='carto-positron',
                               center={'lat': 24, 'lon': 78},
                               zoom=3,
                               opacity=0.5
                               )
    fig.write_html("C:/Users/Admin/PycharmProjects/OpenCV1/CrawlAll/job_vn.html")

data = create_data_city()
map(data)