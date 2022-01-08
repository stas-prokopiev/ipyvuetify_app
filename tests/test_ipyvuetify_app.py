""""""
# Standard library imports

# Third party imports

# Local imports


def test_that_app_starts():
    """"""
    from ipyvuetify_app import VueApp
    from ipyvuetify_app import VueAppRouter
    vue_app_router = VueAppRouter()
    VueApp(
        vue_app_router,
        list_footer_vw_children=["Footer example"],
    )
