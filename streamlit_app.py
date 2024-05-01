# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
cnx = st.connection("snowflake")
session = cnx.session()


# Write directly to the app
st.title("Example Streamlit App :balloon:")
st.write(
    """Replace this example with your own code!
    **And if you're new to Streamlit,** check
    out our easy-to-follow guides at
    [docs.streamlit.io](https://docs.streamlit.io).
    """
)

name_on_order = st.text_input('Name on Smoothie:') 
st.write('The name on your smoothie will be:', name_on_order)


#session = get_active_session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect('Choose up to five ingredients:', my_dataframe, max_selections = 5)

if ingredients_list:
        INGREDIENTS_STRING = ''
        for fruit_chosen in ingredients_list:
            INGREDIENTS_STRING += fruit_chosen + ' '
        #st.write(INGREDIENTS_STRING) 

        my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + INGREDIENTS_STRING + """', '""" + name_on_order + """' )"""

        #st.write(my_insert_stmt)
        #st.stop() 
        time_to_insert = st.button('Submit_Order') 

        if time_to_insert:
            session.sql(my_insert_stmt).collect()
            st.success('Your Smoothie is ordered!', icon="✅")

#new section to display fruit info
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response)
 

