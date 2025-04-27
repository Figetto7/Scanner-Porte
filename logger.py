import logging

class Logger:
    """
    Logger di Scan che registra eventi su file e console
    """
    _instance=None
    def __new__(cls, name:str="ScanLogger", filename:str="log.txt"):
        if cls._instance is None:
            cls._instance=super(Logger, cls).__new__(cls)
            cls._instance._initialize(name, filename)
        return cls._instance
    def _initialize(self, name:str, filename:str):
        self.logger=logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            file_handler=logging.FileHandler(filename)
            stream_handler=logging.StreamHandler()
            formatter=logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            self.logger.addHandler(stream_handler)
    
    def info(self, message:str):
        self.logger.info(message)
    def error(self, message:str):
        self.logger.error(message)
    def warning(self, message:str):
        self.logger.warning(message)