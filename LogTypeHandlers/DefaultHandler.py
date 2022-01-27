from . import LogTypeHandlerBase

class DefaultHandler(LogTypeHandlerBase.Handler):
    def can_handle(self, line):
        prefixes = ['[DEBUG]', '[WARN]', '[FATAL]', '[LOG]', '[ERROR]']
        for prefix in prefixes:
            if line.startswith(prefix):
                return False
        return True

    def handle(self, line):
        return "<span style=\"color:black\">{}</span><br>".format(line)