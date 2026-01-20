class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            print("Creating new Logger instance...")
        else:
            print("Using existing Logger instance...")
        return cls._instance

    def log(self, message):
        print(f"[LOG]: {message}")

print("Interactive Logger - type 'exit' to quit\n")

logger = Logger()

while True:
    msg = input("Enter a message to log: ").strip()
    if msg.lower() == "exit":
        print("Exiting logger.")
        break
    logger.log(msg)


logger2 = Logger()
print(f"\nlogger is logger2? {logger is logger2}")
