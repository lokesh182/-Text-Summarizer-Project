import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
log_dir = "logs"
log_file_path = os.path.join(log_dir,"Logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format = logging_str,
    
    handlers = [
        logging.FileHandler(log_file_path), # log to file
        logging.StreamHandler(sys.stdout) # log to console
    ]
    
)
logger = logging.getLogger("Text Summarizer Logger")