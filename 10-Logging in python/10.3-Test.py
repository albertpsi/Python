import logging

# create a logger
logger = logging.getLogger('arthematicLogger')

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app.log"), # log messages to a file
        logging.StreamHandler() # log messages to the console
    ] # handlers allow us to log messages to multiple destinations (file and console in this case), 
    # and prevents overwriting the log file each time the program runs 
    # (by appending to the file instead of overwriting it)
)

def add(x, y):
    logger.debug(f'Adding {x} and {y}')
    return x + y

def subtract(x, y):
    logger.info(f'Subtracting {y} from {x}')
    return x - y

def multiply(x, y):
    logger.warning(f'Multiplying {x} and {y}')
    return x * y

def divide(x, y):
    try:
        logger.info(f'Dividing {x} by {y}')
        return x / y
    except ZeroDivisionError:
        logger.error(f'Attempted to divide {x} by zero')
        return None
print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))
print(divide(10, 0))