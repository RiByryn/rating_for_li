import json

import requests
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


# "Z0": "Новички"
# "Z1-3": "Жители"
# "Z4-6": "Активисты"
# "Z7-9": "Авторитеты"
# "Z10-12": "Депутаты"
# "Z13-15": "Министры"
# "Z16-18": "Премьер-министры"
# "Z19-21": "Президенты"
# "Z22-24": "Начальники планеты"
# "Z25-27": "Лунные атаманы"
# "Z28-30": "Солнечные стражи"
# "Z31-33": "Звёздные воины"
# "Z34-36": "Космические рейнджеры"
# "Z37-39": "Короли галактики"
# "Z40-42": "Императоры Вселенной"

def get_team_name(meow):
    soup = BeautifulSoup(meow['ninja_column_3'], 'lxml')
    return soup.text.strip()

def get_team_city(html):
    return html['ninja_column_4']

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
        if city == 'Петербург':
            teams.append((name, city))

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