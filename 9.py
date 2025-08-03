import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', encoding = 'utf-8', filemode='w') 

class Counter():
    try:
        logging.info("Инициализация класса")
        def __init__(self):
            self.count = 0
        def increment(self):
            self.count += 1
            logging.info(f"Инкремент {self.count}")
        def decrement(self):
            self.count -= 1
            logging.info(f"Декремент {self.count}")
        def getcount(self):
            self.count
            logging.info(f"Получение значения {self.count}")
    except Exception as e:
        logging.error(f"Ошибка: {e}")


counter = Counter()
counter.increment()
counter.decrement()
counter.getcount()
