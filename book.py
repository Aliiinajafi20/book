from pandas import excelwriter, read_exel
df = read_exel('book1.xlsx')
df['value 4'] = df['value 1'] + df['value 2'] + df['value 3']

def doube_num(num):
    return num * 2

df['dubled'] = df['value 4'].apply(doube_num)

wrtier = excelwriter('new_book.xlsx')
df.to_excel(wrtier,'new_sheet')
wrtier.save()
