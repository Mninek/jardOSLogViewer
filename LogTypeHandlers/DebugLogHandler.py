from . import LogTypeHandlerBase

class DebugLogHandler(LogTypeHandlerBase.Handler):
    def can_handle(self, line):
        if line.startswith('[DEBUG]'):
            return True
        return False

    def handle(self, line):
        return "<span style=\"color:black\">{}</span><br>".format(line)