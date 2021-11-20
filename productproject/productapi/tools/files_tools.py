from pathlib import Path
import xlsxwriter
import datetime

from productapi.models import Product
from productapi.api.serializers import ProductSerializer

principal_dir = 'productapi/'

def start_create_file():
    
    cria_diretorio('files')
    all_products = Product.objects.all()
    serializer_product = ProductSerializer(all_products, many=True)
 
    xlsx_file_create('files', cria_arquivo_xlsx(),serializer_product.data )

def cria_arquivo_xlsx():
        name_file = 'productsbackup-'
        return name_file+datetime.datetime.now().isoformat().split('T')[0]

def cria_diretorio(name):
    if not Path(principal_dir+name).is_dir():
        Path(principal_dir+name).mkdir(exist_ok=True)


def verifica_arquivo(file):
    return Path(file).is_file()


def xlsx_file_create(dirname,namefile,data):
    
    name_complete = principal_dir+dirname+'/'+namefile+'.xlsx'
    
    workbook = xlsxwriter.Workbook(name_complete)

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
    
    workbook.close()



