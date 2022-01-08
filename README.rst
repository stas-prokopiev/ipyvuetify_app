===================
ipyvuetify_app
===================

.. image:: https://img.shields.io/github/last-commit/stas-prokopiev/ipyvuetify_app
   :target: https://img.shields.io/github/last-commit/stas-prokopiev/ipyvuetify_app
   :alt: GitHub last commit

.. image:: https://img.shields.io/github/license/stas-prokopiev/ipyvuetify_app
    :target: https://github.com/stas-prokopiev/ipyvuetify_app/blob/master/LICENSE.txt
    :alt: GitHub license<space><space>

.. image:: https://img.shields.io/pypi/v/ipyvuetify_app
   :target: https://img.shields.io/pypi/v/ipyvuetify_app
   :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/ipyvuetify_app
   :target: https://img.shields.io/pypi/pyversions/ipyvuetify_app
   :alt: PyPI - Python Version


.. contents:: **Table of Contents**

Short Overview.
=========================
ipyvuetify_app is a python package (**py>=3.7**) with a scaffold/template for writing ipyvuetify application

Installation via pip:
======================

.. code-block:: bash

    pip install ipyvuetify_app

How to use it
===========================

| To create an application by the given template you need to create a class
| That will be in charge of what to show in the main application section
| For every selected menu item -> subitem
| Then you just give it to ipyvuetify_app.VueApp and it does all the magic for you

.. code-block:: python

    from ipyvuetify_app import VueApp
    from ipyvuetify_app import VueAppRouter
    vue_app_router = VueAppRouter()
    VueApp(
        vue_app_router,
        list_footer_vw_children=["Footer example"],
    )

Examples how your app can look like
----------------------------------------

.. image:: images/light_1.PNG
.. image:: images/dark_1.PNG

Router example
*********************

| Every router should satisfy 2 conditions:
| 1) It has method **get_main_content(self, item, subitem)** which should return page main content
| 2) It has attribute **self.dict_list_subitems_by_item** with all subitems for every menu item

.. code-block:: python

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

Full VuaApp signature
=============================

.. code-block:: python

    VueApp(
        vue_app_router,
        list_vw_fab_app_bar_left=None,
        list_vw_fab_app_bar_right=None,
        list_footer_vw_children=None,
    )

Links
=====

    * `PYPI <https://pypi.org/project/ipyvuetify_app/>`_
    * `readthedocs <https://ipyvuetify_app.readthedocs.io/en/latest/>`_
    * `GitHub <https://github.com/stas-prokopiev/ipyvuetify_app>`_

Project local Links
===================

    * `CHANGELOG <https://github.com/stas-prokopiev/ipyvuetify_app/blob/master/CHANGELOG.rst>`_.
    * `CONTRIBUTING <https://github.com/stas-prokopiev/ipyvuetify_app/blob/master/CONTRIBUTING.rst>`_.

Contacts
========

    * Email: stas.prokopiev@gmail.com
    * `vk.com <https://vk.com/stas.prokopyev>`_
    * `Facebook <https://www.facebook.com/profile.php?id=100009380530321>`_

License
=======

This project is licensed under the MIT License.