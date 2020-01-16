import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    filename="logs.txt"
)
logger = logging.getLogger(__name__)
# logger = logging.getLogger("books")
# logger = logging.getLogger("books.database") #child logger of books logger, inherits settings
logger.info("test info message")
logger.warning("test warning")