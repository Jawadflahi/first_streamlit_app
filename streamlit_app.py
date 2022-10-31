import streamlit as slt
import pandas as pd
slt.title('My Parents new healthy diner')
slt.header('Breakfast Menu')
slt.text(' 🥣  Omaga 3 and Blueberry Meal')
slt.text('🥗 Kale,Spinach & Rocket Smoothie')
slt.text(' 🐔 Hard boiled Free-Range Egg')
slt.text('🥑🍞 Avacado toast')

slt.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Setting the fruit column as index
my_fruit_list = my_fruit_list.set_index('Fruit')
slt.dataframe(my_fruit_list)
# Picking the set of fruits to make the smoothie
slt.multiselect('Choose the fruits',list(my_fruit_list.index)
