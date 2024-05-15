class Logger:
    _instance = None
    _logs = []

    def __new__(cls):
        if cls._instance is None:
            print("Creating the Logger instance")
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        self._logs.append(message)
        print(f"Logged: {message}")

    def get_logs(self):
        return self._logs
