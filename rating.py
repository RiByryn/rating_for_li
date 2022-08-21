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

def get_team_by_index(response, i):
    return response[i]['value']

def get_team_name(html):
    soup = BeautifulSoup(

def get_team_city(html):
        return html['ninja_column_4']

for chunk_number in range(2):
    s = "https://ligaindigo.ru/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action" \
        "&table_id=20533" \
        "&target_action=get-all-data" \
        "&default_sorting=old_first" \
        "&ninja_table_public_nonce=ed696648d9" \
        "&chunk_number={chunk_number}"

    li_response = json.loads(requests.get(s).text)
    teams = []
    for item in li_response:
        team_data = item['value']
        name = get_team_name(get_team_by_index(li_response))
        city = get_team_city(get_team_by_index(li_response, 0))
        if city == 'Петербург':
            teams.append(name, city))

print(teams)

    li_response = json.loads(requests.get(s).text)
    chunk_teams = [filter(
        lambda team: team[1] == 'Петербург',
        map(
            lambda item: (get_team_item(item['value']), get_team_city(item['value'])),
            li_response
        )
    )]
    teams.extend(chunk_teams)
print(teams)