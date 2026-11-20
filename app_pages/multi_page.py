import streamlit as st


class MultiPage:
    def __init__(self,  app_name) -> None:

        # Empty list to store the pages, and app name
        self.pages = []
        self.app_name = app_name

        # Browser title - wide layout
        st.set_page_config(page_title=self.app_name, page_icon=":police_car:", layout="wide")

    def add_page(self, title, func) -> None:
        # Store the page title and function in the pages list
        self.pages.append({"title": title, "function": func})

    def run(self):
        # Show the app title
        st.title(self.app_name)

        # Sidebar for navigation
        page = st.sidebar.radio("Menu", self.pages,
            format_func=lambda page: page["title"])

        # Run the selected page function
        page["function"]()
