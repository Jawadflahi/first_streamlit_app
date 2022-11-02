import streamlit as slt
import requests
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
# Picking the set of fruits to make the smoothie
selected_fruit = slt.multiselect('Choose the fruits that you want to make the smoothie of ',list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[selected_fruit]
slt.dataframe(fruits_to_show)
# New section to display the response 
slt.header("Fruityvice Fruit Advice!")
fruit_choice = slt.text_input('What fruit would you like information about?','Kiwi')
slt.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/kiwi"+fruit_choice)
fruityvice_normalised = pd.json_normalize(fruityvice_response.json())
slt.dataframe(fruityvice_normalised)



