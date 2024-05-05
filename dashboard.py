### THIS IS A ONE PAGE THE DATA EXPLORATION APP
### MENT FOR THE INTERNAL USE (NOT FOR THE CLINTS)

import streamlit as st
import pandas as pd

from scripts.functions import * 

st.set_page_config(page_title='King County Housing: the dashboard', 
                   layout="wide")

 # Load the house sale history dataset
df = pd.read_csv('data/houses_processed.csv', parse_dates=['sale_date'])

map_fig = geoplot(df, 'condition', 'price', 
                  title="Object overview",
                  alpha=0.8, colorscheme='Cividis')

map_fig.update_coloraxes(colorbar={'orientation': 'h',
                                   'tickprefix': '$',
                                   'xanchor': 'center',
                                   'yanchor': 'top',
                                   #'xref': 'container', 
                                   #'yref': 'container',
                                   'x': .5, 
                                   'y': -.1
                                   }
                                   )

map_fig.update_layout(height=800,
                      title_font_size=28,
                        margin=dict(l=0, r=0, t=60, b=0),  # Set margins (pixels)
                        title={
                            'y':1,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'},)

cols = st.columns([.4, .6])
with cols[0]:
    st.plotly_chart(map_fig, use_container_width=True)

    pr_min, pr_max = st.slider(label='Select the price range', 
                                min_value=df.price.min(),
                                max_value=df.price.max(),
                                step=1e4,
                                #formatc="${:.2f}",
                                value=[1e6, 2e6])
    st.write(pr_min, pr_max)

with cols[1]:
    
    trade_volume = df[['price', 'sale_date']].set_index('sale_date').sort_index()\
            .groupby(
        pd.Grouper(freq='1W')).agg(['sum', 'count']).droplevel(0, axis=1)
    
    volume_chart = px.bar(trade_volume, y='sum', title='Volume of the houses sold ($)', 
                          color='sum',
                          color_continuous_scale='teal', height=370)
    st.plotly_chart(volume_chart)

    count_chart = px.bar(trade_volume, y='count', 
                         color='count',
                         color_continuous_scale='teal',
                         title='Number of houses sold', height=370)
    st.plotly_chart(count_chart)
    #st.dataframe(trade_volume)
