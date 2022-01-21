# converts from WSL path to a windows path that I can open up on my PC

class Converter():
    def convert_to_windows_path(self, path):
        if path.startswith("/mnt/"):
            sliced_path = path[5:]
            sliced_path = sliced_path[0].upper() + ':' + sliced_path[1:]
            return sliced_path

    def convert_log_type_to_html_type(self,path):
        if (path.endswith(".log")):
            size = len(path)
            path = path[:size-4] + ".html"

            return path