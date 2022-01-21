from . import LogTypeHandlerBase

class WarnLogHandler(LogTypeHandlerBase.Handler):
    def can_handle(self, line):
        if line.startswith('[WARN]'):
            return True
        return False

    def handle(self, line):
        return "<span style=\"color:olive\">{}</span><br>".format(line)