import requests
import json

def get_data(i):
    """Функция сбора необходимой информации"""

#Формирование списка из ID товара
    import requests

    cookies = {
        '__lhash_': '0423e00b65250babbee0f9dbb2bbc544',
        'iRegionSectionId': '11324',
        'ABT_test': 'B',
        'ek_ab_test': 'B',
        'AUTORIZZ': '0',
        'AC': '1',
        'lv_user_org': '0',
        'el_group_user_org': '0',
        'bonus_cobrand_showed': '0',
        'USER_AUTH_GTM': '0',
        'BITRIX_SM_ELD_TZ_OFFSET': '-180',
        'cfidsgib-w-eldorado': 'Lj8km+pePCLM/AEX1iVHEBDvDUWPysO9NdzvPXKUO8kj7yas8AL3L05HbCvmrmvKTxEgYSKmUC6PQUgAyJs0H1mF0IIBefH+qUCbVpyGJN36NQcljlAy9NZzGbXjoSZod0uL5BGpGbIiww60Gvb9D9E8nQ2ap/Ito8Zf+OU=',
        'flocktory-uuid': '30b175a6-89b6-4139-94fd-ef958737c701-7',
        '_dy_c_exps': '',
        '_dy_soct': '1009413.1015421.1655363427.eazqgnwzk3bih9lkcxfq410o8usd066p*1091396.1267618.1655363443.eazqgnwzk3bih9lkcxfq410o8usd066p*1026395.1049240.1655365124.eazqgnwzk3bih9lkcxfq410o8usd066p*1052902.1130394.1655366922.eazqgnwzk3bih9lkcxfq410o8usd066p*1020255.1036208.1655727667.eazqgnwzk3bih9lkcxfq410o8usd066p*1024759.1045344.1655810321',
        'rrpvid': '72',
        'digi-SearchVisitor': '10%3A6',
        '_gcl_au': '1.1.1030975575.1655194845',
        'utm_campaign': 'google',
        '__utma': '267034714.1941448371.1655194845.1655802914.1655808057.6',
        '__utmz': '267034714.1655802914.5.4.utmcsr=google|utmccn=google|utmcmd=organic',
        '_ga_4P3TZK55KZ': 'GS1.1.1655808059.6.1.1655810321.0',
        '_ga': 'GA1.2.1461500219.1655194845',
        '_dycnst': 'dg',
        '_dyid': '-9173831576010079011',
        '_dycst': 'dk.w.f.ws.',
        '_dy_geo': 'RU.EU.RU_.RU__',
        '_dy_df_geo': 'Russia..',
        '_dy_toffset': '-1',
        'advcake_trackid': '5fc5e259-1e9e-a1f3-8fc7-7a3e9b16fc1d',
        'advcake_session_id': 'df4ac387-3dcb-d12d-a591-b93d598721ec',
        'advcake_track_url': 'https%3A%2F%2Fwww.eldorado.ru%2F%3Futm_source%3Dgoogle%26utm_medium%3Dorganic%26utm_campaign%3Dgoogle%26utm_referrer%3Dgoogle',
        'advcake_utm_partner': 'google',
        'advcake_utm_webmaster': '',
        'advcake_click_id': '',
        'clickcake_total': '133',
        'clickcake_current': '8',
        'clickcake_max': '123',
        'clickcake_sid': '03379682-ca65-cc40-ef7d-21389df30c79',
        'clickcake_clicks_history': '%7B%2220220614%22%3A3%2C%2220220616%22%3A119%2C%2220220620%22%3A3%2C%2220220621%22%3A8%7D',
        'clickcake_sessions_history': '%7B%2220220614%22%3A2%2C%2220220616%22%3A38%2C%2220220620%22%3A3%2C%2220220621%22%3A4%7D',
        'clickcake_sessions_depth': '%7B%226a48e7a3-0486-b131-27fe-43a83c4d653a%22%3A3%7D',
        'clickcake_id': '5a6087eb-8e89-ba0a-d650-af88d8189c7a',
        '_userGUID': '0:l4dw9ws0:VfnuIZekgczCniIrR0YCNQnX27RPZXnY',
        'tmr_reqNum': '695',
        'tmr_lvid': 'f29c7d91ada34782967757748c9ea2d2',
        'tmr_lvidTS': '1655194846550',
        '_ym_uid': '1655194847787336357',
        '_ym_d': '1655194847',
        'rcuid': '62a844dd82847c000189c548',
        'adrcid': 'A3nj6u_gW0gByXpIYBtLeNg',
        'uxs_uid': 'e541c560-ebba-11ec-bd70-133fdc635bda',
        'unauthorizedId': 'v1mridatcabsj4kiohpp8afj4ygyc7bina5ai19foa53grg408izg3uilt3ziqh244rzftetqoi0kae184p23ln1qqwcyac75qk16nfjsevkyue82vknyguuktpcm57u6bcv05il13qmq7u6twbaexohjadyc32zv1kap5ig4klskqjkexf9w6fgw370ahcol1fug7x0tco62oao4f6dblzjfaz8kzms4wb0iyifl8uwsew3mv91a6p8afqtahhz',
        '_dy_c_att_exps': '',
        'last_source': 'yandex.ru',
        'ab_user': '7884722240100',
        'ab_segment': '78',
        'BITRIX_SM_SALE_UID': '30978651691',
        '_dyjsession': 'eazqgnwzk3bih9lkcxfq410o8usd066p',
        'clickcake_clid_history': '%5B%2250311b16%22%5D',
        'lvBasket': '71614418',
        '__ttl__widget__ui': '1655367210085-0478b090176b',
        'bCNT': '0%3A0',
        'show_region_popup': '0',
        '_gid': 'GA1.2.1222124704.1655727669',
        'tmr_detect': '0%7C1655810321607',
        '__js_p_': '195,7200,0,1,0',
        'dt': '1',
        'PHPSESSID': 'd6d1q1eguq8ojda49ceavmr6ea',
        '__utmc': '267034714',
        '_ym_isad': '2',
        '_dyid_server': '-9173831576010079011',
        '__utmb': '267034714.8.10.1655808057',
        '_dyjsession': 'eazqgnwzk3bih9lkcxfq410o8usd066p',
        '_dy_csc_ses': 'eazqgnwzk3bih9lkcxfq410o8usd066p',
        'clickcake_rsid': '6a48e7a3-0486-b131-27fe-43a83c4d653a',
        'dSesn': '4863dff0-4516-fafc-979b-19867dfa8034',
        '_dvs': '0:l4o208uz:2xcilbpIh8SqtD5n6LRAwwYH1c5tTAFH',
        '__utmt': '1',
        '__hash_': '25e06eb4cf5d3a4ff40043bed0b51017',
        '__jhash_': '53',
        '__jua_': 'Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A101.0%29%20Gecko%2F20100101%20Firefox%2F101.0',
        '__utmt_icc': '1',
        'gsscgib-w-eldorado': 'wPgsMvHEQXg9ZYqi/YtEHawFNzsW9A7YDyvbNBqkADOnW935mEujk/buNBqwGmlAuzQxr/HhUbKwwXh7ZHaPcYjkF6wziSTtuPdFIPHOp307zndsJLF+KN8vJApI5Q4g1E/nj+XLrQX/ghbjRRFuDDA/hH20EeVLqIbuOM+7xJIXNtppD5W8824g3+wkT85RaLpUJn7Ya8ZmZlhbasIxBekdFAiVmBO0VML1h0MgsWMkEQstyQtzeNpj4v2VRQ==',
        'cfidsgib-w-eldorado': 'Lj8km+pePCLM/AEX1iVHEBDvDUWPysO9NdzvPXKUO8kj7yas8AL3L05HbCvmrmvKTxEgYSKmUC6PQUgAyJs0H1mF0IIBefH+qUCbVpyGJN36NQcljlAy9NZzGbXjoSZod0uL5BGpGbIiww60Gvb9D9E8nQ2ap/Ito8Zf+OU=',
        '__zzatgib-w-eldorado': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VdQSEeKEgWVhAeVUBfTUJ7dFYMOFEgf0cqLBs3V10cESRYDiE/C2lbVjRnFRtASBgvS255LkBtHl9KWiVLWU51F2BKQys2FkZGHHIzdz9rCCIZURMqX3hHV2tlVUI4MWcMT09NOTMyMGZaK1kwOWNVdBkYNnIVey4iP24eJHlsZQojTS1vaFEVElsQEj8LF1ZGQSZYFThNLD5RMixid2NfLDlVEQsSF0ReXFVpdWcZTEBXLw0uOF4tbx5lTF4iSV1WeyUfGH9nFR5ATxtQCDQ2YnBXJysRJlQ/RxlKZU57CV1jEzhEIQl2PT8bEDo=360s0A==',
        '__utmt_~1': '1',
        '_dc_gtm_UA-44012634-4': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'https://www.eldorado.ru/d/',
        'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7IlNJRCI6ImQ2ZDFxMWVndXE4b2pkYTQ5Y2Vhdm1yNmVhIn0sImV4cCI6MTY1NTgxMjExM30.Ul7wdd75Z4_AYyC5Z_RUeKYz0zDd8TuNOjP3lFF0C4_vuDxv3RRcnzuSzUJ7SpjWXhn_VUfgAFvd-j-eoVwLrQ',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    params = {
        'limit': '36',
        'offset': '0',
        'orderField': 'popular',
        'orderDirection': 'DESC',
        'smallFacetValues': '[]',
        'tags': '[]',
    }



    items = {}
    x = -36
    for j in range(i):
        x += 36
        params['offset'] = x


        response = requests.get('https://www.eldorado.ru/sem/v3/A408/categories/noutbuki/products', params=params,
                                cookies=cookies, headers=headers).json()


        products = response.get('data')
        for item in products:
            product_id = item.get('id')
            name = item.get('name')
            price = item.get('price')
            lst = item.get('listingDescription')
            properties = {i.get('name'): i.get('attributeNameToValueMap') for i in lst}
            items[product_id] = {}
            items[product_id]['name'] = name
            items[product_id]['price'] = price

            for v in properties.values():
                for key, value in v.items():
                    items[product_id][key] = value


    with open('products.json', 'w', encoding='utf-8') as file:
        json.dump(items, file, indent=4, ensure_ascii=False)



def main():
    #количество страниц в поиске
    i = 5
    get_data(i)

if __name__ == '__main__':
    main()
