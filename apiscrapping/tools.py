from pathlib import Path
import xlsxwriter
import datetime

principal_dir = './'

def start_create_file(nomearq, data, tp):
    
    cria_diretorio('files')

    xlsx_file_create('files', cria_nome_arquivo_xlsx(nomearq), data, tp)

def cria_nome_arquivo_xlsx(nome):
        name_file = nome+'backup-'
        return name_file+datetime.datetime.now().isoformat().split('T')[0]

def cria_diretorio(name):
    if not Path(principal_dir+name).is_dir():
        Path(principal_dir+name).mkdir(exist_ok=True)


def verifica_arquivo(file):
    return Path(file).is_file()


def xlsx_file_create(dirname,namefile,data, typearq):
    
    name_complete = principal_dir+dirname+'/'+namefile+'.xlsx'    
    workbook = xlsxwriter.Workbook(name_complete)

    if typearq != 'prod' and typearq != 'usr' or not typearq:
        print('Opção Inválida!!')
        return

    if typearq == 'prod':
        worksheet = workbook.add_worksheet('products_info')
        row = 1
        col = 0

        worksheet.write(0, 0, 'ID')
        worksheet.write(0, 1, 'Nome')
        worksheet.write(0, 2, 'Descrição')
        worksheet.write(0, 3, 'Quantidade')
        worksheet.write(0, 4, 'Preço')
        
        col=0

        for product in data:
            #voltando a coluna para zero e adicionado os dados...
            if col>0:
                col=0
            worksheet.write(row, col, product.get('id'))
            worksheet.write(row, col+1, product.get('nome'))
            worksheet.write(row, col+2, product.get('descricao'))
            worksheet.write(row, col+3, product.get('quantidade'))
            worksheet.write(row, col+4, product.get('preco'))
            row+=1

    if typearq == 'usr':
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



