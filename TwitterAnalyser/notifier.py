import streamlit as st


class StreamlitNotifier:
    notifier = None
    timeout = 5

    def __init__(self, timeout=5):
        self.notifier = st.empty()
        self.timeout = timeout

    def info(msg=""):
        notifier.info(msg)

    def success(msg=""):
        notifier.success(msg)
