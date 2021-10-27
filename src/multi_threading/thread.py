import logging
import threading
import time


# logging.basicConfig(filename='app.log', filemode='w',
#                     format='%(name)s - %(levelname)s - %(message)s')

logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')
logging.warning("This will get logged to a file")

