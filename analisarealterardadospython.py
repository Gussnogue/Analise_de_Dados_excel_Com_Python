import openpyxl

# Carregando arquivo
book = openpyxl.load_workbook('Planilha de Compras.xlsx')
# Selecionando uma página
frutas_page = book['Frutas']
# Imprimido os dados de cada linha
for rows in frutas_page.iter_rows(min_row=1, max_row=4):
    for cell in rows:
        if cell.value == 'Banana':
            cell.value = 'Laranja'

# Salvar as alterações e conservando a original
book.save('Planilha de Compras v2.xlsx')