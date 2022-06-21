import xlsxwriter, json

def create_excel():

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


def main():
    create_excel()


if __name__ == '__main__':
    main()