import csv, json


def create_mvideo_csv():
    """Функция создания таблицы полученных данных в формате csv"""

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


def create_eldo_csv():
    """Функция создания таблицы полученных данных в формате csv"""

    with open('eldo_notebook.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                "Название",
                "Цена",
                "Операционная система",
                "Диагональ экрана",
                "Разрешение экрана",
                "Производитель процессора",
                "Модель процессора",
                "Тактовая частота",
                "Объем оперативной памяти",
                "Тип оперативной памяти",
                "Тип накопителя",
                "Объем накопителя",
                "Производитель видеокарты",
                "Модель видеокарты",
                "Объем видеопамяти",
                "Цвет",
            )

        )

    with open('eldo_scrap/products.json', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:

        with open('eldo_notebook.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)

            writer.writerow(
                (
                    data[item].get('name'),
                    data[item].get('price'),
                    data[item].get('Операционная система'),
                    data[item].get('Диагональ экрана'),
                    data[item].get('Разрешение экрана'),
                    data[item].get('Производитель процессора'),
                    data[item].get('Модель процессора'),
                    data[item].get('Тактовая частота'),
                    data[item].get('Объем оперативной памяти'),
                    data[item].get('Тип оперативной памяти'),
                    data[item].get('Тип накопителя'),
                    data[item].get('Объем накопителя'),
                    data[item].get('Производитель видеокарты'),
                    data[item].get('Модель видеокарты'),
                    data[item].get('Объем видеопамяти'),
                    data[item].get('Цвет'),
                )

            )



def main():
    create_mvideo_csv()
    create_eldo_csv()


if __name__ == '__main__':
    main()