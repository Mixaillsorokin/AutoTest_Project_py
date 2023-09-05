import logging
import requests
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    title = testdata["title"]
    dis = testdata['description']
    cont = testdata['content']


def get_my_posts(token):
    res = requests.get('https://test-stand.gb.ru/api/posts',
                       headers={'X-Auth-Token': token})
    if res:
        listres = [i['title'] for i in res.json()['data']]
        return listres
    else:
        logging.error('Not opened posts my page')


def get_not_my_posts(token):
    res = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token},
                       params={'owner': 'notMe'})
    if res:
        listres = [i['content'] for i in res.json()['data']]
        return listres
    else:
        logging.error('Not opened posts not my page')


def create_post(token):
    res = requests.post('https://test-stand.gb.ru/gateway/posts', headers={'X-Auth-Token': token},
                        data={'title': title,
                              'description': dis,
                              'content': cont})
    if res:
        return res.json()
    else:
        logging.error('Not create post ')


def find_post(token):
    d = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
    if d:
        listdescript = [i['description'] for i in d.json()['data']]
        return listdescript
    else:
        logging.error('Not find post')


def test_1(login, not_my_post):
    assert not_my_post in get_not_my_posts(login)


def test_2(login, my_post):
    assert my_post in get_my_posts(login)
