import streamlit as st
from modules import functions

todos = functions.read_file()


def add_todo():
    todo = st.session_state["new_todo"]
    if len(todo) >= 1:
        todos.append(todo.title() + "\n")
        functions.write_file(todos)

    st.session_state.new_todo = ""


st.title("Todo Tracker")
st.subheader("My Todos:")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_file(todos)
        del st.session_state[todo]
        st.experimental_rerun()

user_todo = st.text_input(label="label", label_visibility='hidden', placeholder="Add new todo...",
                          on_change=add_todo, key='new_todo')

st.write(user_todo)
