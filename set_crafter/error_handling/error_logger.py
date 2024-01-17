```python
import logging

class ErrorLogger:
    def __init__(self, log_file='set_crafter.log'):
        self.logger = logging.getLogger('SetCrafter')
        self.logger.setLevel(logging.ERROR)
        handler = logging.FileHandler(log_file)
        handler.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_error(self, error_message):
        self.logger.error(error_message)
```