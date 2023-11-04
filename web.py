import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout='wide')

def add_todo():
    new_todo = st.session_state['new_todo'] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is leadin")
st.write("This app is to increase your <strong>productivity.</strong>", unsafe_allow_html=True)

st.text_input(label="Enter a todo: ",
              placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')

st.write("<strong>Todos List: </strong>", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

