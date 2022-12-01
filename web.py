import streamlit as st
from modules import functions

todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("What's next?")
st.write("Directions: Enter a to-do in the textbox and press enter.")

for index, todo in enumerate(todos):
    unique_key="todo" + str(index)
    st.checkbox(todo, key=unique_key)

st.text_input(label="", placeholder="Add new to-do...")