import json

import requests
import re
from bs4 import BeautifulSoup

# li = "https://ligaindigo.ru/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=20533&target_action=get-all-data&default_sorting=old_first&ninja_table_public_nonce=ed696648d9&chunk_number=0"
# # print(requests.get(li).text)
# a = json.loads(requests.get(li).text)[0]['value']
# # print(a)
# soup = BeautifulSoup(a['ninja_column_3'], 'lxml')
# city = a['ninja_column_4']
# # print(soup.text.strip())
# # print(city)
# print((soup.text.strip(), city))

ranks = {
    "Новички": range(0),
    "Жители": range(1, 4),
    "Активисты": range(4, 7),
    "Авторитеты": range(7, 10),
    "Депутаты": range(10, 13),
    "Министры": range(13, 16),
    "Премьер-министры": range(16, 19),
    "Президенты": range(19, 22),
    "Начальники планеты": range(22, 25),
    "Лунные атаманы": range(25, 28),
    "Солнечные стражи": range(28, 31),
    "Звёздные воины": range(31, 34),
    "Космические рейнджеры": range(34, 37),
    "Короли галактики": range(37, 40),
    "Императоры Вселенной": range(40, 43)
}

def get_team_name(meow):
    soup = BeautifulSoup(meow['ninja_column_3'], 'lxml')
    return soup.text.strip()

def get_team_city(html):
    return html['ninja_column_4']

def get_team_rank(html):
    rank_link = BeautifulSoup(html['ninja_column_5'], 'html')
    link = rank_link.contents[0].next.contents[0].next.attrs['src'].split('/')[-1]
    rank_num = int(re.findall(r'\d+', link)[0])
    for key, value in ranks.items():
        if rank_num in value:
            return key

teams = []

for chunk_number in range(2):
    s = "https://ligaindigo.ru/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action" \
        "&table_id=20533" \
        "&target_action=get-all-data" \
        "&default_sorting=old_first" \
        "&ninja_table_public_nonce=ed696648d9" \
        "&chunk_number={chunk_number}"

    li_response = json.loads(requests.get(s).text)

    for i, item in enumerate(li_response):
        table_data = li_response[i]['value']
        name = get_team_name(table_data)
        city = get_team_city(table_data)
        rank = get_team_rank(table_data)
        if city == 'Петербург':
            teams.append((name, city, rank))

print(teams)

#     li_response = json.loads(requests.get(s).text)
#     chunk_teams = [filter(
#         lambda team: team[1] == 'Петербург',
#         map(
#             lambda item: (get_team_item(item['value']), get_team_city(item['value'])),
#             li_response
#         )
#     )]
#     teams.extend(chunk_teams)
# print(teams)