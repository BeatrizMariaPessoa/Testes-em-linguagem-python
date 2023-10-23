from manterclienteUI import ManterClienteUI
import streamlit as st

class IndexUI:
    def sidebar():
      op = st.sidebar.selectbox("Menu", ["Central do Cliente", "Central de Serviços", "Agendamentos"])
      if op == "Central do Cliente": ManterClienteUI()
      if op == "Central de Serviços": ManterClienteUI()
      if op == "Agendamentos": ManterClienteUI()
    def main():
      IndexUI.sidebar()

IndexUI.main()