from . import LogTypeHandlerBase

class FatalLogHandler(LogTypeHandlerBase.Handler):
    def can_handle(self, line):
        if line.startswith('[FATAL]'):
            return True
        return False

    def handle(self, line):
        return "<span style=\"background-color:red;color:white\">{}</span><br>".format(line)