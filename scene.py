from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
import os
import importlib


class Scene(QWidget):
    def __init__(self, scenePath):
        QWidget.__init__(self)

        self.path = scenePath
        uic.loadUi(scefrom PyQt5 import uic
from PyQt5.QtWidgets import QWidget
import os
import importlib


class Scene(QWidget):
    def __init__(self, scenePath):
        QWidget.__init__(self)

        self.path = scenePath
        uic.loadUi(scenePath, self)

    @staticmethod
    def onclick(btnObject, func):
        btnObject.clicked.connect(func)


class Placeholder:
    def __init__(self, name, object_, initScene):
        self.name = name
        self.object = object_
        self.changeScene(initScene)

    def clear(self):
        for i in reversed(range(self.object.count())):
            self.object.itemAt(i).widget().setParent(None)

    def changeScene(self, scene):
        self.clear()
        self.object.addWidget(scene)
        self.scene = scene


class CompositeScene(Scene):
    def __init__(self, scenePath):
        Scene.__init__(self, scenePath + '/__init__.ui')

        self._scenes = []
        self._placeholders = []
        self.loadScenes()

    def addScene(self, scenePath, composite=False):
        importPath = scenePath.replace('/', '.')
        if not composite:
            importPath = importPath[:-3]

        scene = importlib.import_module(importPath)
        className = importPath[importPath.rfind('.') + 1:] + 'Scene'
        sceneClass = getattr(scene, className)
        self._scenes.append(sceneClass(scenePath))

    def removeScene(self, scenePath):
        pass

    def getScene(self, scenePath):
        if not scenePath.endswith('.ui'):  # If folder
            scenePath += '/__init__.ui'

        for scene in self._scenes:
            if scene.path == scenePath:
                return scene
        return None

    def loadScenes(self):
        sceneDir = self.path[:self.path.rfind('/')]
        dirContent = os.listdir(sceneDir)
        for object_ in dirContent:
            objectPath = f'{sceneDir}/{object_}'
            if os.path.isdir(objectPath) and object_ != '__pycache__':
                self.addScene(objectPath, True)
            elif object_.endswith('.py') and object_ != '__init__.py':
                self.addScene(objectPath[:-3] + '.ui')

    def addPlaceholder(self, placeholder):
        self._placeholders.append(placeholder)

    def removePlaceholder(self, name):
        pass

    def getPlaceholder(self, name):
        for placeholder in self._placeholders:
            if placeholder.name == name:
                return placeholder
        return None

    def changePlaceholdersScene(self, placeholderName, scenePath):
        placeholder = self.getPlaceholder(placeholderName)
        scene = self.getScene(scenePath)
        placeholder.changeScene(scene)


class LeafScene(Scene):
    def __init__(self, scenePath):
        Scene.__init__(self, scenePath)
