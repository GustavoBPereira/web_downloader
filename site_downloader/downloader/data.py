import os


class Link:
    def __init__(self, link):
        self.link = link


    # @cached_property
    # def prefix_static_dir(self):
    #     return os.path.join(self.gustavo.prefix_path + "/staticfiles/img")
    #
    # @cached_property
    # def origin_url(self):
    #     return self.link
    #
    # @cached_property
    # def relative_path(self):
    #     return os.path.relativeurl(self.gustavo.prefix_path, self.absolute_path)
    #
    # @cached_property
    # def absolute_path(self):
    #     instanciaurl = urllib.request(self.link)
    #     a = os.path.join(self.prefix_static_dir, instanciaurl.path)
    #     return os.path.normalize(a)
    #
    # def save(self):
    #     if not os.file.exists(self.path):
    #         os.makedirs(self.path)
    #         urllib.retrieve(self.path)


class Img:
    def __init__(self, link):
        self.link = link


class Js:
    def __init__(self, link):
        self.link = link


class Css:
    def __init__(self, link):
        self.link = link
