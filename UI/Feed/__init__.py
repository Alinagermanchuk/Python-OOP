from scene import CompositeScene, Placeholder


class FeedScene(CompositeScene):
    def __init__(self, path):
        CompositeScene.__init__(self, path)

        self.addPlaceholder(Placeholder('graphics', self.Graphics, self.getScene('UI/Feed/Graphics')))
        self.addPlaceholder(Placeholder('companies', self.Companies, self.getScene('UI/Feed/Companies')))
                                                                                                                                       from scene import CompositeScene, Placeholder


class FeedScene(CompositeScene):
    def __init__(self, path):
        CompositeScene.__init__(self, path)

        self.addPlaceholder(Placeholder('graphics', self.Graphics, self.getScene('UI/Feed/Graphics')))
        self.addPlaceholder(Placeholder('companies', self.Companies, self.getScene('UI/Feed/Companies')))
