import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # file name we craete
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # part that file should be create
os.makedirs(logs_path,exist_ok=True) ## make dirs

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) # 

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,)



