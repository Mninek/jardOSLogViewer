import sys
import os

from html_path_converter import Converter
from LogTypeHandlers.FatalLogHandler import FatalLogHandler
from LogTypeHandlers.ErrorLogHandler import ErrorLogHandler
from LogTypeHandlers.InfoLogHandler import InfoLogHandler
from LogTypeHandlers.WarnLogHandler import WarnLogHandler
from LogTypeHandlers.DebugLogHandler import DebugLogHandler
from LogTypeHandlers.DefaultHandler import DefaultHandler

def get_handlers():
    handlers = []
    handlers.append(FatalLogHandler())
    handlers.append(ErrorLogHandler())
    handlers.append(InfoLogHandler())
    handlers.append(WarnLogHandler())
    handlers.append(DebugLogHandler())
    handlers.append(DefaultHandler())

    return handlers



def convert_to_html(log_file_path):
    html_file = open('debug.html', 'w+') # change to the os.getcwd path
    log_file = open(log_file_path, 'r')

    converter = Converter()

    message = ""
    handlers = get_handlers()

    # this previous handler is used in the case where the same debug message flows to the next line
    prev_handler = None

    for line in log_file:
        handled = False
        for handler in handlers:
            if handler.can_handle(line):
                message += handler.handle(line)
                prev_handler = handler
                handled = True
                break
        if not handled:
            message += prev_handler.handle(line)

    html_file.write(message)

    openable_link = converter.convert_log_type_to_html_type(converter.convert_to_windows_path(log_file_path))
    print("HTML File generated, you can open it here: \nfile://{}".format(openable_link))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please pass in only 1 argument")
        
    log_file = sys.argv[1]

    if not log_file.endswith('.log'):
        print("Please only pass in .log files")
        
    log_file_path = os.getcwd() + '/' + log_file

    if not os.path.exists(log_file_path):
        print("Please make sure the file exists. By default, the file should be debug.log")

    convert_to_html(log_file_path)