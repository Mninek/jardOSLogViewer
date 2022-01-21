class Handler:
    def can_handle(self, line):
        #check if a message can be handled by the handler
        raise NotImplementedError("Please implement can_handle for all handling classes")

    def handle(self, line):
        #handles the message
        raise NotImplementedError("Please implement the handle function for all handling classes")