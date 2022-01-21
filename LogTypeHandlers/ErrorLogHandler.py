from . import LogTypeHandlerBase

class ErrorLogHandler(LogTypeHandlerBase.Handler):
    def can_handle(self, line):
        if line.startswith('[ERROR]'):
            return True
        return False

    def handle(self, line):
        return "<span style=\"color:red\">{}</span><br>".format(line)