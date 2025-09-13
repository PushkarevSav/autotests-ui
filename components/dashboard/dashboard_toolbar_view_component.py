import allure

from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'dashboard-toolbar-title-text', 'Title toolbar')

    @allure.step('Check visible title dashboard')
    def check_visible(self):
        self.title.check_visible()