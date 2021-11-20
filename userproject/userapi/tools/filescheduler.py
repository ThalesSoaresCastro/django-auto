from userapi.tools.files_tools import start_create_file
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
job = None

def start_job():
    global job
    #atualiza o arquivo a cada 10 minutos, em background
    job = scheduler.add_job(start_create_file, 'interval', seconds=600)
    try: 
        scheduler.start()
    except:
        pass