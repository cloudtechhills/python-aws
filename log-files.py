import logging

#BASIC PYTHON LOGGING TUTORIAL

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG,  format='%(asctime)s :: %(levelname)s :: %(message)s :: %(filename)s :: %(created)s')


logging.debug('This is a Debug Message')
logging.warning("THis is a Warning Message!")
logging.info("THis is an Info Message")
logging.error("This is an Error Message")