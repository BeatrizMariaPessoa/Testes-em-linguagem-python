from tkinter import Button
import streamlit as st
import pandas as pd
from views import View
import time

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterClienteUI.listar()
        with tab2:
            ManterClienteUI.inserir()
        with tab3:
            ManterClienteUI.atualizar()
            pass
        with tab4:
            ManterClienteUI.excluir()
    def listar():
        clientes = View.cliente_listar()
        dic = []
        for c in clientes:
            dic.append(c.__dict__)
        df = pd.DataFrame(dic)
        st.dataframe(df)   
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.experimental_rerun()

    def atualizar():
        clientes = View.cliente_listar()
        op = st.selectbox("Atualização de clientes", clientes)
        nome = st.text_input("Informe o novo nome")
        email = st.text_input("Informe o novo e-mail")
        fone = st.text_input("Informe o novo telefone")
        if st.button("Atualizar cliente"):
            id = op.get_id()
            View.cliente_atualizar(id, nome, email, fone)
            st.success("Cliente atualizado com sucesso")
            time.sleep(2)
            st.experimental_rerun()

    def excluir():
        clientes = View.cliente_listar()
        op = st.selectbox("Exclusão de clientes", clientes)
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")

        elif st.button("Excluir cliente"):
            id = op.get_id()
            View.cliente_excluir(id)
            st.success("Cliente excluído com sucesso")
            time.sleep(2)
            st.experimental_rerun()