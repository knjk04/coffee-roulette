import openpyxl


def read_first_column():
    workbook = openpyxl.load_workbook('sample_people.xlsx')
    sheet = workbook['Sheet1']
    first_column = list(sheet.columns)[0]

    values = []

    for cell in first_column:
        if cell.value is None:
            break
        values.append(cell.value)

    return values
