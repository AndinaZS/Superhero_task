import requests

def get_intelligence(hero_name):
    url = 'https://superheroapi.com/api/2619421814940190/search/' + hero_name
    response = requests.get(url)
    if 'error' in response.text:
        print(f'Героя {hero_name} не существует или имя написано неверно')
        return 0
    else:
        hero_info = response.json()
        for el in hero_info['results']:
            if el['name'] == hero_name:
                intelligence = el['powerstats']['intelligence']
                break
        return int(intelligence)


def max_int(hero_list):
    max_int, smartest_hero = 0, []
    for hero in hero_list:
        res = get_intelligence(hero)
        if res == max_int:
            smartest_hero.append(hero)
        elif res > max_int:
            max_int = res
            smartest_hero = []
            smartest_hero.append(hero)
    if max_int == 0:
        return 'Ваши герои из другой вселенной'
    else:
        return f"Максимальный интелект у {'и'.join(smartest_hero)} равен {max_int}"


if __name__ == '__main__':
    print(max_int(['Hulk', 'Hulk', 'Captain America', 'Thanos', 'Spider-Man', 'SpiderMan']))