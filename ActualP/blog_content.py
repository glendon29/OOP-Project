import datetime


class Blog():
    def __init__(self, title, subtitle, content, author):
        self.__title = title
        self.__subtitle = subtitle
        self.__content = content
        self.__author = author

    def get_title(self):
        return self.__title

    def get_subtitle(self):
        return self.__subtitle

    def get_content(self):
        return self.__content

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_subtitle(self, subtitle):
        self.__subtitle = subtitle

    def set_content(self, content):
        self.__content = content

    def set_author(self, author):
        self.__author = author


