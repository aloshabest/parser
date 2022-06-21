import csv, json


def create_csv():

    with open('mvideo_notebook.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                'Название',
                'Диагональ/разрешение',
                'Процессор',
                'Оперативная память (RAM)',
                'Графический контроллер',
                'Объем SSD',
                'Операционная система',
                'Обычная цена',
                'Скидочная цена',
                'Сумма скидки',
                'Бонус',
            )

        )

    with open('mvideo_scrap/5_result.json', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:

        with open('mvideo_notebook.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow(
                (
                    data[item].get('name'),
                    data[item].get('Диагональ/разрешение'),
                    data[item].get('Процессор'),
                    data[item].get('Оперативная память (RAM)'),
                    data[item].get('Графический контроллер'),
                    data[item].get('Объем SSD'),
                    data[item].get('Операционная система'),
                    data[item].get('basePrice'),
                    data[item].get('salePrice'),
                    data[item].get('sale'),
                    data[item].get('bonus'),
                )

            )


def main():
    create_csv()


if __name__ == '__main__':
    main()