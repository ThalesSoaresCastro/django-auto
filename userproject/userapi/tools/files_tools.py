from pathlib import Path
import xlsxwriter

principal_dir = 'userapi/'

def cria_diretorio(name):
    if not Path(principal_dir+name).is_dir():
        Path(principal_dir+name).mkdir(exist_ok=True)


def verifica_arquivo(file):
    return Path(file).is_file()


def xlsx_file_create(dirname,namefile,data):
    
    name_complete = principal_dir+dirname+'/'+namefile+'.xlsx'
    
    workbook = xlsxwriter.Workbook(name_complete)

    worksheet = workbook.add_worksheet('users_info')

    row = 1
    col = 0

    worksheet.write(0, 0, 'ID')
    worksheet.write(0, 1, 'Login')
    worksheet.write(0, 2, 'Senha')
    worksheet.write(0, 3, 'Data Nascimento')
    
    col=0

    for user in data:
        #voltando a coluna para zero e adicionado os dados...
        if col>0:
            col=0
        worksheet.write(row, col, user.get('id'))
        worksheet.write(row, col+1, user.get('login'))
        worksheet.write(row, col+2, user.get('senha'))
        worksheet.write(row, col+3, user.get('data_nascimento'))
        row+=1
    
    workbook.close()



