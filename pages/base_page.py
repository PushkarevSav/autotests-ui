from playwright.sync_api import Page

class BasePage(Page):

    def  __init__(self, page: Page):
        self.page = page
        super().__init__(page)

    def visit(self, url: str):
        self.page.goto(url, wait_until='networkidle')

    def reload(self):
        self.page.reload(wait_until='networkidle')

