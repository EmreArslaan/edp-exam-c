class Event:
    def _init_(self, payload: dict):
        self.payload = payload
        print(f"Debug: Event created with payload: {self.payload}")

class ApplicationSentEvent(Event):
    def _init_(self, payload: dict):
        super()._init_(payload)
        print(f"Event: Application submitted for {payload['student']}.")

class ApplicationAcceptedEvent(Event):
    def _init_(self, payload: dict):
        super()._init_(payload)
        print(f"Event: Application accepted for {payload['student']}.")

class ApplicationRejectedEvent(Event):
    def _init_(self, payload: dict):
        super()._init_(payload)
        print(f"Event: Application rejected for {payload['student']}.")
