import openpyxl
from openpyxl import Workbook
                  
def correosCliente():
    ruta='Recursos/lista.xlsx'
    excel_document = openpyxl.load_workbook(ruta)
    sheet = excel_document.get_sheet_by_name('Hoja1')

    rangoA = sheet['A']
    fila1 = sheet[1]
    columna=len(rangoA)
    fila=len(fila1)
    datosFiltrados={}
    num=1
    for row in sheet.iter_rows(min_row=2, max_col=fila, max_row=columna, values_only=True):
        if(type(row[0])==str):
            num+=1
            datosFiltrados[row[0]]=row[1]
    
    return datosFiltrados