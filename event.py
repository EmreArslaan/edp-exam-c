import logging

# Configure the logging system
logging.basicConfig(level=logging.DEBUG,  # Log messages of DEBUG level and above
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Event:
    def __init__(self, payload: dict):
        self.payload = payload
        logging.debug(f"Event created with payload: {self.payload}")

class ApplicationSentEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)
        logging.info(f"Application submitted for {payload['student']}.")

class ApplicationAcceptedEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)
        logging.info(f"Application accepted for {payload['student']}.")

class ApplicationRejectedEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)
        logging.info(f"Application rejected for {payload['student']}.")