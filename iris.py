import streamlit as st

# Title of the app
st.title("Todo List App")

# Initialize an empty list to store todo items
todo_items = []

# Function to add a new todo item
def add_todo_item(item):
    todo_items.append(item)

# Function to remove a todo item
def remove_todo_item(index):
    del todo_items[index]

# Function to clear all todo items
def clear_all_items():
    todo_items.clear()

# Text input to add a new todo item
new_item = st.text_input("Add a new todo item:")

# Button to add the new todo item
if st.button("Add"):
    add_todo_item(new_item)

# Display the list of todo items
for i, item in enumerate(todo_items):
    # Display each item with a checkbox
    st.write(f"{i+1}. {item}")

# Button to clear all todo items
if st.button("Clear all"):
    clear_all_items()
    st.write("All items cleared!")