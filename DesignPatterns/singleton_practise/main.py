from Logger import Logger


# Függvények vagy osztályok, amelyek használják a Logger-t
def create_logger1():
    logger = Logger()
    logger.log("This is a log entry from function_one.")


def create_logger2():
    logger = Logger()
    logger.log("This is a log entry from function_two.")


# A Logger osztály tesztelése
create_logger1()
create_logger2()

logger = Logger()
print("Checking the same instance:")
print(logger is Logger())  # Should print: True

print("Checking logs collected:")
for log in logger.get_logs():
    print(log)
