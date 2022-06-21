import requests
import json

def get_data():
    """Функция сбора необходимой информации"""

#Формирование списка из ID товара
    cookies = {
        'HINTS_FIO_COOKIE_NAME': '1',
        'MAIN_PAGE_VARIATION': '5',
        'MVID_ABC_TEST_WIDGET': '0',
        'MVID_AB_PROMO_DAILY': '1',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_AB_TEST_COMPARE_ONBOARDING': 'true',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_PRICE_FIRST': '2',
        'MVID_PRM20_CMS': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'new',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'searchType2': '1',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        'utm_term': 'aaecb867dcae797a2390b8bf515e7410',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        '_ga': 'GA1.2.1218456126.1650881470',
        'uxs_uid': '073cb600-c480-11ec-8aaa-716bb645c2af',
        '_ym_uid': '1650881470541862738',
        '_ym_d': '1650881470',
        'afUserId': '0e175020-e27b-4e26-8b4b-e0f084775332-p',
        '__ttl__widget__ui': '1650881472055-2d8e92ee0c6f',
        '_ga_CFMZTSS5FM': 'GS1.1.1655727943.6.1.1655729248.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1655727943.6.1.1655729248.57',
        'tmr_reqNum': '156',
        'tmr_lvid': '9c9577045ca78f07c602672c03778fab',
        'tmr_lvidTS': '1650881472675',
        'flocktory-uuid': 'e152427f-3cca-4caa-b009-6682e4af973d-2',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_CRM_ID': '0025618140',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjYXJ0Ijp0cnVlfQ==',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjb21wYXJpc29uIjpmYWxzZX0=',
        'deviceType': 'desktop',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VtfmZmLRAVUhQQG0U8Vzc1FEUdIyMWT3tyElEMbWMiEHszRA9xR0lcNRE7QHB/DRdwEnQVGjhmIWZLWyJDXFUKFhoXfHAmVQsTZD9Cc3gbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS5AaCNjUFomRFVOdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRI9XypYVww0eGUQQ1h9cWsvZHtFJF8cPHVlL0FtdS5BZiVgS1kRP0cVNmdcSkI3FVlLTShyPV8/YngiD2lIXyRDXVV6KiATeG8pS3FSHAl5CDpodiZSUVElYRASSWtpYlE0XS1BR0cUdn85MHF/V2o0KlknmA==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VtfmZmLRAVUhQQG0U8Vzc1FEUdIyMWT3tyElEMbWMiEHszRA9xR0lcNRE7QHB/DRdwEnQVGjhmIWZLWyJDXFUKFhoXfHAmVQsTZD9Cc3gbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS5AaCNjUFomRFVOdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRI9XypYVww0eGUQQ1h9cWsvZHtFJF8cPHVlL0FtdS5BZiVgS1kRP0cVNmdcSkI3FVlLTShyPV8/YngiD2lIXyRDXVV6KiATeG8pS3FSHAl5CDpodiZSUVElYRASSWtpYlE0XS1BR0cUdn85MHF/V2o0KlknmA==',
        'cfidsgib-w-mvideo': '9rWdsQmm2mZAYUQWSsxZvZplng6iopCSy8D0d1f7HM1mRhXZ5wHbl89jwrx51irGyhjdpuE77IV/9cgKeRupRxrI3OOO4BBr8T1lu8oI+uLDnC0+1H9cZPG32TKMc+AobcpKbhLACUYKzlcT/wznR1PA5XYmm2mZMfnVqA==',
        'cfidsgib-w-mvideo': 'ixrZ3AECdGj3LJI2q1n4f+tQwTUHUdoFUlOEvyAhw+Jrb+nB5UepVa+CRULmSJsYfAqFF5HbaZ1Narj601ZdrSI+5U5KTqJtQDWom/XDuxDQFMd6/hWtnep6tLOIN7OmqRTlY798h0ztI8gRk38zvPYsZ0tmCGOKTawJUg==',
        'cfidsgib-w-mvideo': 'ixrZ3AECdGj3LJI2q1n4f+tQwTUHUdoFUlOEvyAhw+Jrb+nB5UepVa+CRULmSJsYfAqFF5HbaZ1Narj601ZdrSI+5U5KTqJtQDWom/XDuxDQFMd6/hWtnep6tLOIN7OmqRTlY798h0ztI8gRk38zvPYsZ0tmCGOKTawJUg==',
        'gsscgib-w-mvideo': '9fGkUX/chNNzMaCVz4H4FQrhMGGEZRIwzWwtsrqkxcjVbAWs6yrz0ieSi3zhX5UJ7civCpjTkkIZNg+AL5d1Af24Sj3+MkLDZriinPtFLKhWI58KAI3NCYOtSDRCGolkj4sdU7Jpw1XKYWv7bVOTD5NWUftCoYzhxpFN5p/6HYEg9KfsEMzA+d802xSFfxsecwUOEE5M586VnZ7X3hZCv6BwCoacViFllN7gaYGGDpLfyIGaPPFAnpLcubVc0w==',
        'gsscgib-w-mvideo': '9fGkUX/chNNzMaCVz4H4FQrhMGGEZRIwzWwtsrqkxcjVbAWs6yrz0ieSi3zhX5UJ7civCpjTkkIZNg+AL5d1Af24Sj3+MkLDZriinPtFLKhWI58KAI3NCYOtSDRCGolkj4sdU7Jpw1XKYWv7bVOTD5NWUftCoYzhxpFN5p/6HYEg9KfsEMzA+d802xSFfxsecwUOEE5M586VnZ7X3hZCv6BwCoacViFllN7gaYGGDpLfyIGaPPFAnpLcubVc0w==',
        'fgsscgib-w-mvideo': 'XnQCeeea4e05e4ef7ecd53853df81c0991bd9409',
        'fgsscgib-w-mvideo': 'XnQCeeea4e05e4ef7ecd53853df81c0991bd9409',
        '__lhash_': '334c0031815420bfc3c6d113fc66a0bc',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'MAIN_PAGE_VARIATION_1': '1',
        'MVID_2_exp_in_1': '2',
        'MVID_GUEST_ID': '20879034289',
        'MVID_LP_SOLD_VARIANTS': '0',
        'MVID_NEW_LK': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_LOGIN': 'true',
        'MVID_NEW_LK_MENU_BUTTON': 'true',
        'advcake_track_id': '4ea09249-ae1b-a1b9-4833-e025f4a77dc9',
        'advcake_session_id': '6805e889-b709-04b1-7e1c-80c2d5f2c476',
        'AF_SYNC': '1655194876097',
        'adrcid': 'AUr37YQqC8tZHuaeyYixlig',
        'admitad_uid': 'aaecb867dcae797a2390b8bf515e7410',
        '__cpatrack': 'advcake_cpa',
        '__sourceid': 'advcake',
        '__allsource': 'advcake',
        'partnerSrc': 'advcake',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2Fproducts%2Fnoutbuk-dell-vostro-5301-beige-5301-8419-1100027796944%3Futm_source%3Dadvcake%26utm_medium%3Dcpa%26utm_campaign%3D71ff78f8%26utm_content%3Daffiliate%26advcake_params%3Daaecb867dcae797a2390b8bf515e7410%26utm_term%3Daaecb867dcae797a2390b8bf515e7410%26sub1%3DDELL-Vostro-5301-8419%26sub2%3Dnoutbuki-80000-feb2022%26keyword%3DDevice',
        'advcake_utm_partner': '71ff78f8',
        'advcake_utm_webmaster': 'affiliate',
        'advcake_click_id': 'aaecb867dcae797a2390b8bf515e7410',
        'JSESSIONID': 'qK1Pvwsc3QpWCGzpvQvTCG5f2vnQSGl2nccQhTyF2Gpm5L11Rp3n!-873994709',
        'bIPs': '-1341531712',
        'flacktory': 'no',
        'SMSError': '',
        'authError': '',
        '_gid': 'GA1.2.291612674.1655727944',
        '_ym_isad': '2',
        'tmr_detect': '0%7C1655728082511',
        'ADRUM_BT': 'R:97|g:f191c5dd-8b85-43f3-ad6c-4802e2979c1c7640835',
        'MVID_ENVCLOUD': 'primary',
        'mindboxDeviceUUID': '0742f78c-f835-40b8-8f5f-1c7162a27c97',
        'directCrm-session': '%7B%22deviceGuid%22%3A%220742f78c-f835-40b8-8f5f-1c7162a27c97%22%7D',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'x-set-application-id': '76ffbbd3-2a33-406f-bf3b-7c2ab6168aad',
        'Connection': 'keep-alive',
        'Referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/skidka=da/tolko-v-nalichii=da',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'HINTS_FIO_COOKIE_NAME=1; MAIN_PAGE_VARIATION=5; MVID_ABC_TEST_WIDGET=0; MVID_AB_PROMO_DAILY=1; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_AB_TEST_COMPARE_ONBOARDING=true; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_PRICE_FIRST=2; MVID_PRM20_CMS=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=new; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; searchType2=1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; utm_term=aaecb867dcae797a2390b8bf515e7410; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; _ga=GA1.2.1218456126.1650881470; uxs_uid=073cb600-c480-11ec-8aaa-716bb645c2af; _ym_uid=1650881470541862738; _ym_d=1650881470; afUserId=0e175020-e27b-4e26-8b4b-e0f084775332-p; __ttl__widget__ui=1650881472055-2d8e92ee0c6f; _ga_CFMZTSS5FM=GS1.1.1655727943.6.1.1655729248.0; _ga_BNX5WPP3YK=GS1.1.1655727943.6.1.1655729248.57; tmr_reqNum=156; tmr_lvid=9c9577045ca78f07c602672c03778fab; tmr_lvidTS=1650881472675; flocktory-uuid=e152427f-3cca-4caa-b009-6682e4af973d-2; MVID_NEW_DESKTOP_FILTERS=true; MVID_CRM_ID=0025618140; MVID_OLD_NEW=eyJjb21wYXJpc29uIjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjYXJ0Ijp0cnVlfQ==; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjb21wYXJpc29uIjpmYWxzZX0=; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VtfmZmLRAVUhQQG0U8Vzc1FEUdIyMWT3tyElEMbWMiEHszRA9xR0lcNRE7QHB/DRdwEnQVGjhmIWZLWyJDXFUKFhoXfHAmVQsTZD9Cc3gbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS5AaCNjUFomRFVOdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRI9XypYVww0eGUQQ1h9cWsvZHtFJF8cPHVlL0FtdS5BZiVgS1kRP0cVNmdcSkI3FVlLTShyPV8/YngiD2lIXyRDXVV6KiATeG8pS3FSHAl5CDpodiZSUVElYRASSWtpYlE0XS1BR0cUdn85MHF/V2o0KlknmA==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VtfmZmLRAVUhQQG0U8Vzc1FEUdIyMWT3tyElEMbWMiEHszRA9xR0lcNRE7QHB/DRdwEnQVGjhmIWZLWyJDXFUKFhoXfHAmVQsTZD9Cc3gbN1ddHBEkWA4hPwtpW1Y0ZxUbQEgYL0tueS5AaCNjUFomRFVOdRdgSkMrNhZGRhxyM3c/awgiGVETKl94R1drZVVCODFnDE9PTRI9XypYVww0eGUQQ1h9cWsvZHtFJF8cPHVlL0FtdS5BZiVgS1kRP0cVNmdcSkI3FVlLTShyPV8/YngiD2lIXyRDXVV6KiATeG8pS3FSHAl5CDpodiZSUVElYRASSWtpYlE0XS1BR0cUdn85MHF/V2o0KlknmA==; cfidsgib-w-mvideo=9rWdsQmm2mZAYUQWSsxZvZplng6iopCSy8D0d1f7HM1mRhXZ5wHbl89jwrx51irGyhjdpuE77IV/9cgKeRupRxrI3OOO4BBr8T1lu8oI+uLDnC0+1H9cZPG32TKMc+AobcpKbhLACUYKzlcT/wznR1PA5XYmm2mZMfnVqA==; cfidsgib-w-mvideo=ixrZ3AECdGj3LJI2q1n4f+tQwTUHUdoFUlOEvyAhw+Jrb+nB5UepVa+CRULmSJsYfAqFF5HbaZ1Narj601ZdrSI+5U5KTqJtQDWom/XDuxDQFMd6/hWtnep6tLOIN7OmqRTlY798h0ztI8gRk38zvPYsZ0tmCGOKTawJUg==; cfidsgib-w-mvideo=ixrZ3AECdGj3LJI2q1n4f+tQwTUHUdoFUlOEvyAhw+Jrb+nB5UepVa+CRULmSJsYfAqFF5HbaZ1Narj601ZdrSI+5U5KTqJtQDWom/XDuxDQFMd6/hWtnep6tLOIN7OmqRTlY798h0ztI8gRk38zvPYsZ0tmCGOKTawJUg==; gsscgib-w-mvideo=9fGkUX/chNNzMaCVz4H4FQrhMGGEZRIwzWwtsrqkxcjVbAWs6yrz0ieSi3zhX5UJ7civCpjTkkIZNg+AL5d1Af24Sj3+MkLDZriinPtFLKhWI58KAI3NCYOtSDRCGolkj4sdU7Jpw1XKYWv7bVOTD5NWUftCoYzhxpFN5p/6HYEg9KfsEMzA+d802xSFfxsecwUOEE5M586VnZ7X3hZCv6BwCoacViFllN7gaYGGDpLfyIGaPPFAnpLcubVc0w==; gsscgib-w-mvideo=9fGkUX/chNNzMaCVz4H4FQrhMGGEZRIwzWwtsrqkxcjVbAWs6yrz0ieSi3zhX5UJ7civCpjTkkIZNg+AL5d1Af24Sj3+MkLDZriinPtFLKhWI58KAI3NCYOtSDRCGolkj4sdU7Jpw1XKYWv7bVOTD5NWUftCoYzhxpFN5p/6HYEg9KfsEMzA+d802xSFfxsecwUOEE5M586VnZ7X3hZCv6BwCoacViFllN7gaYGGDpLfyIGaPPFAnpLcubVc0w==; fgsscgib-w-mvideo=XnQCeeea4e05e4ef7ecd53853df81c0991bd9409; fgsscgib-w-mvideo=XnQCeeea4e05e4ef7ecd53853df81c0991bd9409; __lhash_=334c0031815420bfc3c6d113fc66a0bc; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; MAIN_PAGE_VARIATION_1=1; MVID_2_exp_in_1=2; MVID_GUEST_ID=20879034289; MVID_LP_SOLD_VARIANTS=0; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_MENU_BUTTON=true; advcake_track_id=4ea09249-ae1b-a1b9-4833-e025f4a77dc9; advcake_session_id=6805e889-b709-04b1-7e1c-80c2d5f2c476; AF_SYNC=1655194876097; adrcid=AUr37YQqC8tZHuaeyYixlig; admitad_uid=aaecb867dcae797a2390b8bf515e7410; __cpatrack=advcake_cpa; __sourceid=advcake; __allsource=advcake; partnerSrc=advcake; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2Fproducts%2Fnoutbuk-dell-vostro-5301-beige-5301-8419-1100027796944%3Futm_source%3Dadvcake%26utm_medium%3Dcpa%26utm_campaign%3D71ff78f8%26utm_content%3Daffiliate%26advcake_params%3Daaecb867dcae797a2390b8bf515e7410%26utm_term%3Daaecb867dcae797a2390b8bf515e7410%26sub1%3DDELL-Vostro-5301-8419%26sub2%3Dnoutbuki-80000-feb2022%26keyword%3DDevice; advcake_utm_partner=71ff78f8; advcake_utm_webmaster=affiliate; advcake_click_id=aaecb867dcae797a2390b8bf515e7410; JSESSIONID=qK1Pvwsc3QpWCGzpvQvTCG5f2vnQSGl2nccQhTyF2Gpm5L11Rp3n!-873994709; bIPs=-1341531712; flacktory=no; SMSError=; authError=; _gid=GA1.2.291612674.1655727944; _ym_isad=2; tmr_detect=0%7C1655728082511; ADRUM_BT=R:97|g:f191c5dd-8b85-43f3-ad6c-4802e2979c1c7640835; MVID_ENVCLOUD=primary; mindboxDeviceUUID=0742f78c-f835-40b8-8f5f-1c7162a27c97; directCrm-session=%7B%22deviceGuid%22%3A%220742f78c-f835-40b8-8f5f-1c7162a27c97%22%7D; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyLQotC+0LLQsNGA0Ysg0YHQviDRgdC60LjQtNC60L7QuSIsIi04Iiwi0JHQvtC70LXQtSA1JSJd',
            'WyLQotC+0LvRjNC60L4g0LIg0L3QsNC70LjRh9C40LgiLCItOSIsItCU0LAiXQ==',
        ],
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()



    #Запись списка ID в файл
    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w', encoding='utf-8') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)


#Формирование полного описания товара через ID  и запись в файл
    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('2_items.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)


#Формирование списка цен, скидок и бонусов и запись в файл
    products_ids_str = ','.join(products_ids)
    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_prices.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)



#Формирование словаря: ключ-ID, значение-цена, скидочная цена и бонус и запись в файл
    item_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        item_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items__prices.json', 'w', encoding='utf-8') as file:
        json.dump(item_prices, file, indent=4, ensure_ascii=False)



def get_result():
    """Функция формирования итогового списка скидочных товаров путем чтения из файлов с полным описанием и ценой и формированием более краткого описания через ID  и добавление к этому описанию цены и скидок"""

    with open('2_items.json', encoding='utf-8') as file:
        products_data = json.load(file)

    with open('4_items__prices.json', encoding='utf-8') as file:
        products_prices = json.load(file)

    data = products_data.get('body').get('products')

    item_result = {}

    for item in data:
        product_id = item.get('productId')
        product_name = item.get('name')
        product_properties = item.get('propertiesPortion')
        list_properties = {i.get('name'): i.get('value') for i in product_properties}

        if product_id in products_prices:
            prices = products_prices[product_id]

        item_result[product_id] = {
            'name': product_name,
        }
        for k, v in list_properties.items():
            item_result[product_id][k] = v

        item_result[product_id]['basePrice'] = prices.get('item_basePrice')
        item_result[product_id]['salePrice'] = prices.get('item_salePrice')
        item_result[product_id]['sale'] = (prices.get('item_basePrice') - prices.get('item_salePrice'))
        item_result[product_id]['bonus'] = prices.get('item_bonus')


    with open('5_result.json', 'w', encoding='utf-8') as file:
        json.dump(item_result, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()

