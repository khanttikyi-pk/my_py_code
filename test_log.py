import logging
import sys
import os

date = os.system("date /t")

logging.basicConfig(filename='test.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

logging.debug("This is DEBGUG message")
logging.info("This is INFO message.")
logging.warning(date)
logging.error("This is ERROR message.")
logging.critical("This is CRITICAL message.")

