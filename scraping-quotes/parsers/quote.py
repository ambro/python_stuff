from locators.quote_locators import QuoteLocators


class QuoteParser:
    """
    Docs
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<QuoteParser content:{self.content}, author:{self.author}, tags:{self.tags}>'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return [tag.string for tag in self.parent.select(locator)]

