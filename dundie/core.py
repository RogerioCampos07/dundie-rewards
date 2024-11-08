'''Core module of dundie'''
from dundie.utils.log import get_logger

log = get_logger()

def load(filepath):
    """
    Load data from filepath to database
    """
    try:
        with open(filepath) as file_:
            return [line.strip() for line in file_.readlines()]
    except FileNotFoundError as e:
        log.error(str(e))
        raise e
