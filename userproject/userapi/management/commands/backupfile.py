from django.core.management.base import BaseCommand, CommandError
from rest_framework.serializers import Serializer
from userapi.models import User
from userapi.api.serializers import UserSerializer
import datetime
from userapi.tools.files_tools import cria_diretorio, xlsx_file_create

principal_dir = 'userapi/'

class Command(BaseCommand):
    help = 'Faz download de todos os dados cadastrados em XLSX'

    def handle(self, *args, **options):

        #cria o diretório para salvar os arquivos...
        cria_diretorio('files')

        all_users = User.objects.all()
        serializer_user = UserSerializer(all_users, many=True)


        xlsx_file_create('files', self.cria_arquivo_xlsx(),serializer_user.data )


    def cria_arquivo_xlsx(self):
        name_file = 'usersbackup-'
        return name_file+datetime.datetime.now().isoformat().split('T')[0]

