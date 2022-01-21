from . import LogTypeHandlerBase

class InfoLogHandler(LogTypeHandlerBase.Handler):
    def can_handle(self, line):
        if line.startswith('[INFO]'):
            return True
        return False

    def handle(self, line):
        return "<span style=\"color:blue\">{}</span><br>".format(line)