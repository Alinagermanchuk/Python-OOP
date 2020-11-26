from PyQt5 import QtWidgets
from scene import CompositeScene, Placeholder


class UIScene(QtWidgets.QMainWindow, CompositeScene):
    def __init__(self, path):
        CompositeScene.__init__(self, path)

        self.addPlaceholder(Placeholder('inner-content', self.InnerContent, self.getScene('UI/Feed')))
        self.connectButtons()

    def connectButtons(self):
        self.onclick(self.FeedBtn, lambda: self.changePlaceholdersScene('inner-content', 'UI/Feed'))
        self.onclick(from PyQt5 import QtWidgets
from scene import CompositeScene, Placeholder


class UIScene(QtWidgets.QMainWindow, CompositeScene):
    def __init__(self, path):
        CompositeScene.__init__(self, path)

        self.addPlaceholder(Placeholder('inner-content', self.InnerContent, self.getScene('UI/Feed')))
        self.connectButtons()

    def connectButtons(self):
        self.onclick(self.FeedBtn, lambda: self.changePlaceholdersScene('inner-content', 'UI/Feed'))
        self.onclick(self.NotificationsBtn, lambda: self.changePlaceholdersScene('inner-content', 'UI/Notifications'))
        # self.onclick(self.SearchBtn, lambda: self.changePlaceholdersScene('inner-content', 'UI/Search'))
        self.onclick(self.SettingsBtn, lambda: self.changePlaceholdersScene('inner-content', 'UI/Settings'))
