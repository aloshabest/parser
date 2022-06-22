import xlsxwriter, json

def create_mvideo_excel():
    """Функция создания таблицы полученных данных в формате excel"""

    with xlsxwriter.Workbook('mvideo_notebooks.xlsx') as workbook:
        ws = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})

        headers = [
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
        ]

        for col, h in enumerate(headers):
            ws.write_string(0, col, h, cell_format=bold)

        with open('mvideo_scrap/5_result.json', encoding='utf-8') as file:
            data = json.load(file)

        for row, item in enumerate(data, start=1):
            ws.write_string(row, 0, data[item].get('name'))
            ws.write_string(row, 1, data[item].get('Диагональ/разрешение'))
            ws.write_string(row, 2, data[item].get('Процессор'))
            ws.write_string(row, 3, data[item].get('Оперативная память (RAM)'))
            ws.write_string(row, 4, data[item].get('Графический контроллер'))
            if data[item].get('Объем SSD'):
                ws.write_string(row, 5, data[item].get('Объем SSD'))
                ws.write_string(row, 6, '')
            elif data[item].get('Операционная система'):
                ws.write_string(row, 5, '')
                ws.write_string(row, 6, data[item].get('Операционная система'))
            ws.write_string(row, 7, str(data[item].get('basePrice')))
            ws.write_string(row, 8, str(data[item].get('salePrice')))
            ws.write_string(row, 9, str(data[item].get('sale')))
            ws.write_string(row, 10, str(data[item].get('bonus')))



def create_eldo_excel():
    """Функция создания таблицы полученных данных в формате excel"""

    with xlsxwriter.Workbook('eldo_notebooks.xlsx') as workbook:
        ws = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})

        headers = [
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
        ]

        for col, h in enumerate(headers):
            ws.write_string(0, col, h, cell_format=bold)


        with open('eldo_scrap/products.json', encoding='utf-8') as file:
            data = json.load(file)

        for row, item in enumerate(data, start=1):
            ws.write_string(row, 0, data[item].get('name'))
            if data[item].get('price'):
                ws.write_string(row, 1, str(data[item].get('price')))
            if data[item].get('Операционная система'):
                ws.write_string(row, 2, str(data[item].get('Операционная система')))
            if data[item].get('Диагональ экрана'):
                ws.write_string(row, 3, data[item].get('Диагональ экрана'))
            if data[item].get('Разрешение экрана'):
                ws.write_string(row, 4, data[item].get('Разрешение экрана'))
            if data[item].get('Производитель процессора'):
                ws.write_string(row, 5, data[item].get('Производитель процессора'))
            if data[item].get('Модель процессора'):
                ws.write_string(row, 6, data[item].get('Модель процессора'))
            if data[item].get('Тактовая частота'):
                ws.write_string(row, 7, data[item].get('Тактовая частота'))
            if data[item].get('Объем оперативной памяти'):
                ws.write_string(row, 8, data[item].get('Объем оперативной памяти'))
            if data[item].get('Тип оперативной памяти'):
                ws.write_string(row, 9, data[item].get('Тип оперативной памяти'))
            if data[item].get('Тип накопителя'):
                ws.write_string(row, 10, data[item].get('Тип накопителя'))
            if data[item].get('Объем накопителя'):
                ws.write_string(row, 11, data[item].get('Объем накопителя'))
            if data[item].get('Производитель видеокарты'):
                ws.write_string(row, 12, data[item].get('Производитель видеокарты'))
            if data[item].get('Модель видеокарты'):
                ws.write_string(row, 13, data[item].get('Модель видеокарты'))
            if data[item].get('Объем видеопамяти'):
                ws.write_string(row, 14, str(data[item].get('Объем видеопамяти')))
            ws.write_string(row, 15, str(data[item].get('Цвет')))



def main():
    create_mvideo_excel()
    create_eldo_excel()


if __name__ == '__main__':
    main()