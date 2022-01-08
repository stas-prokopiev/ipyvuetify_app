"""class with example how router for VuaApp should look like"""
# Standard library imports
from time import sleep

# Third party imports

# Local imports

class VueAppRouter():
    """Routing for VueApp to emulate transition over pages in the app"""

    def __init__(self) -> None:
        """Initialize dictionary with all menus and their subitems"""
        self.dict_list_subitems_by_item = {}
        for item in range(5):
            list_subitems = [str(subitem) for subitem in range(item, 5 + item)]
            self.dict_list_subitems_by_item[str(item)] = list_subitems

    def get_main_content(self, item, subitem):
        """Router to get main content for clicked submenu element

        Args:
            item (str): selected menu
            subitem (str): submenu element for which to build a page

        Returns:
            ipyvuetify container or string: page content to show at main section
        """
        try:
            sleep(int(item))
            return f"{item} -> {subitem}"
        except Exception as ex:
            return self.error_page_content(str(ex))

    def error_page_content(self, str_error="Unable to get page content"):
        """Return content of error message to show when something going wrong

        Args:
            str_error (str, optional): Error message to show

        Returns:
            [str]: Error message to display
        """
        return f"ERROR: {str_error}"
