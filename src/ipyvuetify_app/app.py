"""ipyvuetify App template"""
# Standard library imports
import traceback
from functools import partial

# Third party imports
import ipyvuetify as v
from IPython.display import display
from IPython.display import HTML
from char import char

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
    """Template for building ipyvuetify applications faster"""

    @char
    def __init__(
            self,
            vue_app_router,
            list_vw_fab_app_bar_left=None,
            list_vw_fab_app_bar_right=None,
            list_footer_vw_children=None,
    ):
        """ipyvuetify App where only main section is up to user

        Args:
            vue_app_router (VueAppRouter): Router over pages
            list_vw_fab_app_bar_left (list): fab buttons to show on appbar
            list_vw_fab_app_bar_right (list): fab buttons to show on appbar
            list_footer_vw_children (list): Footer ipyvuetify children to show
        """
        display(HTML(CSS_DELETE_MARGINS))
        super().__init__(
            class_="ma-0 pa-2",
            style_="min-height:98vh;"
            # style_="min-height:99vh; width:99vw; "
        )
        self.router = vue_app_router
        # 1) Init basic widgets
        self.init_basic_widgets()
        # 2) Build App container
        self.build_app_container(
            list_vw_fab_app_bar_left=list_vw_fab_app_bar_left,
            list_vw_fab_app_bar_right=list_vw_fab_app_bar_right,
            list_footer_vw_children=list_footer_vw_children,
        )
        # 3) Build App routing for menu
        self.build_app_routing()

    def init_basic_widgets(self):
        """Create ipyvuetify widgets that should be initialized only once"""
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
        self.vw_appbar_menu = v.SlideGroup(show_arrows=True,)
        self.vw_dialog_page_loading = v.Dialog(
            v_model=False,
            persistent=True,
            open_delay="500",
            width="190px",
            content_class="elevation-0",
            children=[
                v.Card(
                    height="300px",
                    color="transparent",
                    children=[
                        v.ProgressCircular(
                            size="150",
                            color="primary",
                            indeterminate=True
                        ),
                        v.CardTitle(children=["Loading...."])
                    ]
                )
            ],
        )
    @char
    def build_app_container(
            self,
            list_vw_fab_app_bar_left=None,
            list_vw_fab_app_bar_right=None,
            list_footer_vw_children=None,
    ):
        """Build all scaffold of the application

        Args:
            list_vw_fab_app_bar_left (list): fab buttons to show on appbar
            list_vw_fab_app_bar_right (list): fab buttons to show on appbar
            list_footer_vw_children (list): Footer ipyvuetify children to show
        """
        # 1) Prepare AppBar container
        self.vw_appbar = v.AppBar(
            app=True,
            dense=True,
        )
        list_app_bar_children = [self.vw_fab_show_drawer]
        if list_vw_fab_app_bar_left:
            list_app_bar_children += list_vw_fab_app_bar_left
        list_app_bar_children += [
            v.Divider(vertical=True),
            v.Spacer(),
            v.Col(cols="10", children=[self.vw_appbar_menu,]),
            v.Spacer(),
            v.Divider(vertical=True),
        ]
        if list_vw_fab_app_bar_right:
            list_app_bar_children += list_vw_fab_app_bar_right
        list_app_bar_children += [self.vw_fab_night_mode]
        self.vw_appbar.children = list_app_bar_children
        # 2) Prepare NavigationDrawer container
        self.vw_navigation_drawer = v.NavigationDrawer(
            v_model=False,
            app=True,
            temporary=True,
            left=True,
            class_="px-2",
        )
        list_first_row = []
        if list_vw_fab_app_bar_left:
            list_first_row += list_vw_fab_app_bar_left
            list_first_row.append(v.Divider(vertical=True))
        list_first_row.append(v.Spacer())
        if list_vw_fab_app_bar_right:
            list_first_row += list_vw_fab_app_bar_right
        self.vw_row_nav_drawer_first_row = v.Row(children=list_first_row)
        # 3) Prepare Main container
        self.vw_app_main = v.Content()
        # 4) Prepare Footer
        self.vw_footer = v.Footer(app=True,)
        if list_footer_vw_children:
            self.vw_footer.children = [
                v.Row(justify="center", children=list_footer_vw_children)]
        # 5) Fill App container with all elements
        self.children = [
            self.vw_appbar,
            self.vw_navigation_drawer,
            self.vw_app_main,
            self.vw_footer,
            self.vw_dialog_page_loading,
        ]

    def change_theme(self, *_):
        """Change application theme: light <-> dark
        """
        v.theme.dark = not v.theme.dark
        if v.theme.dark:
            but_icon = "mdi-weather-sunny"
            self.vw_fab_night_mode.color = "yellow"
        else:
            but_icon = "mdi-weather-night"
            self.vw_fab_night_mode.color = "blue darken"
        self.vw_fab_night_mode.children = [v.Icon(children=[but_icon])]

    def show_drawer(self, *_):
        """Show drawer for the application"""
        self.vw_navigation_drawer.v_model = True

    def build_app_routing(self, ):
        """Build all routing for the application"""
        self.build_routing_appbar()
        self.build_routing_navigation_drawer()

    def update_app_routing(self):
        """Update menus if router was changed"""
        self.build_routing_appbar()
        self.build_routing_navigation_drawer()

    @char
    def change_main_content(self, str_item, str_subitem, *_):
        """Change main content of the application for asked menu item->subitem

        Args:
            str_item (str): selected menu
            str_subitem (str): clicked subitem
        """
        self.vw_navigation_drawer.v_model = False
        self.vw_dialog_page_loading.v_model = True
        # If selected page not given then build the first page
        if str_item is None:
            str_item = list(self.router.dict_list_subitems_by_item)[0]
        if str_subitem is None:
            str_subitem = self.router.dict_list_subitems_by_item[str_item][0]

        try:
            self.vw_app_main.children = [
                self.router.get_main_content(str_item, str_subitem)
            ]
        except Exception as ex:
            list_rows = []
            for str_traceback_row in traceback.format_tb(ex.__traceback__):
                list_rows.append(v.Row(children=[str_traceback_row]))
            vw_exp_panel_traceback = v.ExpansionPanels(children=[
                v.ExpansionPanel(children=[
                    v.ExpansionPanelHeader(children=[
                        v.Row(justify="center", color="info", children=[
                            v.Html(tag="b", children=["Full traceback:"])
                        ])
                    ]),
                    v.ExpansionPanelContent(children=list_rows),
                ])
            ])
            vw_alert = v.Alert(
                type_="error",
                color="error",
                class_="mb-5",
                dense=True,
                outlined=True,
                dismissible=True,
                children=[
                    v.Row(justify="center", children=[
                        f"During page load exception happen: {ex}"]),
                    vw_exp_panel_traceback,
                ]
            )
            self.children = self.children + [vw_alert]
        self.vw_dialog_page_loading.v_model = False

    def build_routing_appbar(self):
        """Build Appbar for the application"""
        list_tabs_children = []
        for str_item in self.router.dict_list_subitems_by_item:
            list_str_subitems = self.router.dict_list_subitems_by_item[str_item]
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
                        rounded=True,
                        children=[str_item]
                    )
                }]
            )
            list_menu_subitems = []
            for str_subitem in list_str_subitems:
                vw_item = v.ListItem(children=[
                    v.ListItemTitle(children=[str(str_subitem)])
                ])
                vw_item.on_event(
                    "click",
                    partial(self.change_main_content, str_item, str_subitem)
                )
                list_menu_subitems.append(vw_item)
            vw_menu.children = [v.List(children=list_menu_subitems)]
            list_tabs_children.append(v.SlideItem(children=[vw_menu]))
        self.vw_appbar_menu.children = [
            v.Row(justify="center", children=list_tabs_children)]

    def build_routing_navigation_drawer(self):
        """Build navigation drawer for the application"""
        list_drawer_rows = [self.vw_row_nav_drawer_first_row]
        for str_item in self.router.dict_list_subitems_by_item:
            list_str_subitems = self.router.dict_list_subitems_by_item[str_item]
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
                        color="primary",
                        rounded=True,
                        children=[str(str_item)]
                    )
                }]
            )
            list_menu_subitems = []
            for str_subitem in list_str_subitems:
                vw_item = v.ListItem(children=[
                    v.ListItemTitle(children=[str(str_subitem)])
                ])
                vw_item.on_event(
                    "click",
                    partial(self.change_main_content, str_item, str_subitem)
                )
                list_menu_subitems.append(vw_item)
            vw_menu.children = [v.List(children=list_menu_subitems)]
            list_drawer_rows.append(v.Row(justify="center", children=[vw_menu]))
        self.vw_navigation_drawer.children = list_drawer_rows
