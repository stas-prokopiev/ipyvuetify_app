""""""
# Standard library imports
from functools import partial

# Third party imports
import ipyvuetify as v
from IPython.display import display
from IPython.display import HTML

# Local imports


# Contants
# background-color: black !important;
CSS_DELETE_MARGINS = """
<style>
    .jp-Notebook {margin: 0px !important; padding: 0px !important;}
    .jp-Cell {margin: 0px !important; padding: 0px !important;}
    .jupyter-widgets {margin: 0px !important;}
</style>
"""


class VueApp(v.App):
    """"""

    def __init__(
            self,
            d_d_main_by_subitem_by_item,
            list_app_bar_left_fab_widgets=None,
            list_app_bar_right_fab_widgets=None,
            list_footer_children=None,
    ):

        display(HTML(CSS_DELETE_MARGINS))
        super().__init__(
            class_="ma-0 pa-2",
            style_="height:99vh; width:99vw; "
        )
        self.d_d_main_by_subitem_by_item = d_d_main_by_subitem_by_item
        # 1) Init basic widgets
        self.init_basic_widgets()
        # 2) Init containers
        # 2.1) Prepare AppBar container
        self.vw_appbar = v.AppBar(
            app=True,
            dense=True,
        )
        list_app_bar_children = [self.vw_fab_show_drawer]
        if list_app_bar_left_fab_widgets:
            list_app_bar_children += list_app_bar_left_fab_widgets
        list_app_bar_children += [
            v.Divider(vertical=True),
            v.Spacer(),
            self.vw_tabs_menu,
            v.Spacer(),
            v.Divider(vertical=True),
        ]
        if list_app_bar_right_fab_widgets:
            list_app_bar_children += list_app_bar_right_fab_widgets
        list_app_bar_children += [self.vw_fab_night_mode]
        self.vw_appbar.children = list_app_bar_children
        # 2.2) Prepare NavigationDrawer container
        self.vw_navigation_drawer = v.NavigationDrawer(
            v_model=False,
            app=True,
            temporary=True,
            left=True,
            class_="px-2",
        )
        list_first_row = []
        if list_app_bar_left_fab_widgets:
            list_first_row += list_app_bar_left_fab_widgets
            list_first_row.append(v.Divider(vertical=True))
        list_first_row.append(v.Spacer())
        if list_app_bar_right_fab_widgets:
            list_first_row += list_app_bar_right_fab_widgets
        # list_first_row.append(self.vw_fab_night_mode)
        self.vw_row_nav_drawer_first_row = v.Row(children=list_first_row)
        # 2.3) Prepare Main container
        self.vw_app_main = v.Content(children=["TEST"])
        # 2.4) Prepare Footer
        self.vw_footer = v.Footer(app=True,)
        if list_footer_children:
            self.vw_footer.children = [
                v.Row(justify="center", children=list_footer_children)]
        # 2.5) Fill App container with all elements
        self.children = [
            self.vw_appbar,
            self.vw_navigation_drawer,
            self.vw_app_main,
            self.vw_footer,
            self.vw_dialog_page_loading
        ]
        # 3) Build App
        self.build_app()

    def init_basic_widgets(self):
        """"""
        self.vw_fab_night_mode = v.Btn(
            fab=True,
            small=True,
            icon=True,
            children=[v.Icon(children=["mdi-weather-night"])],
            color="blue darken",
        )
        self.vw_fab_night_mode.on_event("click", self.change_theme)
        self.vw_fab_show_drawer = v.Btn(
            fab=True,
            left=True,
            small=True,
            icon=True,
            children=[v.AppBarNavIcon()]
        )
        self.vw_fab_show_drawer.on_event("click", self.show_drawer)
        self.vw_tabs_menu = v.Tabs(
            show_arrows=True,
            # center_active=True,
            align_with_title=True,
            centered=True,
            style_="width:90%;",
            active_class="",
        )
        self.vw_dialog_page_loading = v.Dialog(
            v_model=False,
            persistent=True,
            fullscreen=True,
            children=[
                v.Row(justify="center", children=[
                    v.ProgressCircular(
                        size="150",
                        color="primary",
                        indeterminate=True
                    )
                ])
            ],
        )

    def change_theme(self, *_):
        """"""
        v.theme.dark = not v.theme.dark
        if v.theme.dark:
            but_icon = "mdi-weather-sunny"
            self.vw_fab_night_mode.color = "yellow"
        else:
            but_icon = "mdi-weather-night"
            self.vw_fab_night_mode.color = "blue darken"
        self.vw_fab_night_mode.children = [v.Icon(children=[but_icon])]

    def show_drawer(self, *_):
        """"""
        self.vw_navigation_drawer.v_model = True

    def build_app(self, ):
        """"""
        self.build_appbar()
        self.build_navigation_drawer()


    def update_menu_items(self):
        """"""



    def change_main_content(self, func_to_call, str_menu_1, *_):
        """"""
        self.vw_navigation_drawer.v_model = False
        # self.vw_dialog_page_loading.v_model = True


        # self.vw_tabs_menu.v_model = ""
        # self.vw_tabs_menu.value = ""


        self.vw_app_main.children = [func_to_call() + str(str_menu_1)]



        from time import sleep
        sleep(2)
        self.vw_dialog_page_loading.v_model = False



    def build_appbar(self):
        """"""
        list_tabs_children = []
        for str_menu_1 in self.d_d_main_by_subitem_by_item:
            d_main_by_subitem = self.d_d_main_by_subitem_by_item[str_menu_1]
            vw_menu = v.Menu(
                offset_x=False,
                offset_y=True,
                class_="ma-0 pa-0",
                open_on_hover=True,
                v_slots=[{
                    "name": "activator",
                    "variable": "menuData",
                    "children": v.Btn(
                        v_on="menuData.on",
                        text=True,
                        color="primary",
                        class_="ma-0 pa-0",
                        disabled=False,
                        rounded=True,
                        children=[str(str_menu_1)]
                    )
                }]
            )
            list_menu_subitems = []
            for str_subitem in d_main_by_subitem:
                vw_item = v.ListItem(children=[
                    v.ListItemTitle(children=[str(str_subitem)])
                ])
                func_main_content = d_main_by_subitem[str_subitem]
                vw_item.on_event(
                    "click",
                    partial(self.change_main_content, func_main_content, str_menu_1)
                )
                list_menu_subitems.append(vw_item)
            vw_menu.children = list_menu_subitems
            list_tabs_children.append(
                v.Tab(children=[vw_menu],
                ref=f"{str_menu_1}")
            )





        self.vw_tabs_menu.children = list_tabs_children
        self.vw_tabs_menu.v_model = "1"



    def build_navigation_drawer(self):
        """"""



        list_drawer_rows = [self.vw_row_nav_drawer_first_row]



        for str_menu_1 in self.d_d_main_by_subitem_by_item:
            d_main_by_subitem = self.d_d_main_by_subitem_by_item[str_menu_1]
            vw_menu = v.Menu(
                offset_x=True,
                offset_y=False,
                open_on_hover=True,
                # bottom=True,
                v_slots=[{
                    "name": "activator",
                    "variable": "menuData",
                    "children": v.Btn(
                        v_on="menuData.on",
                        text=True,
                        rounded=True,
                        children=[str(str_menu_1)]
                    )
                }]
            )
            list_menu_subitems = []
            for str_subitem in d_main_by_subitem:
                vw_item = v.ListItem(children=[
                    v.ListItemTitle(children=[str(str_subitem)])
                ])
                func_main_content = d_main_by_subitem[str_subitem]
                vw_item.on_event(
                    "click",
                    partial(self.change_main_content, func_main_content, str_menu_1)
                )
                list_menu_subitems.append(vw_item)
            vw_menu.children = list_menu_subitems
            list_drawer_rows.append(v.Row(justify="center", children=[vw_menu]))
        self.vw_navigation_drawer.children = list_drawer_rows
