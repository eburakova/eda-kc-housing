import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import seaborn as sns

PI = np.pi
R = 6371 # km - Earth radius

def geoplot(data, size_col, color_col, 
            title="King county housings",
            alpha=1, marker_max_size=20,
            colorscheme="Portland"):
    
    cb_title=color_col.capitalize()
    cb_title=cb_title.replace('_', ' ')

    hover_label=size_col.capitalize()
    hover_label=hover_label.replace('_', ' ')
    
    marker_sizes = np.exp(data[size_col].max() + 2 - data[size_col])

    # Plots the main figure
    fig = px.scatter_mapbox(
        data,
        lat='lat',
        lon='long',
        opacity=alpha,
        zoom=8,
        mapbox_style='open-street-map', 
        size=marker_sizes,
        size_max=marker_max_size,  
        color=color_col,
        color_continuous_scale = colorscheme,
        title = title,
        template='plotly_white'
    )

    # updates markers and tooltips
    fig.update_traces(
        hovertemplate =
                f'<b>{hover_label}<b>: ' + data[size_col].astype('str') + '</b><br>' 
    )

    # updating height, width, margins and other layout properties
    fig.update_layout(
        width=700,
        height=500,
        title_font_size=28,
        margin=dict(l=0, r=0, t=60, b=0),  # Set margins (pixels)
        title={
            'text': title,
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        coloraxis_colorbar=dict(
            title=cb_title,
            #tickvals=np.linspace(df.price_log.min(), df.price_log.max(), 5),
            #ticktext=np.linspace(df.price.min(), df.price.max(), 5),
                        )
    )

    return fig

def plot_corr_matrix(corm, labels, ax):
    mask = np.zeros_like(corm, dtype='bool')
    mask[np.tril_indices_from(mask)] = True
    mask[np.diag_indices_from(mask)] = False
    cm = sns.heatmap(corm, mask=mask, annot=True, fmt='.2f',
                cmap='seismic', vmin=-1, vmax=1, 
                #style='white',
                cbar=False, square=True,
                xticklabels=labels,
                yticklabels=labels, ax=ax)
    return cm

def radians(degrees):  
    return degrees * PI / 180

def geo_distance_km(coord1, coord2):
    '''Calculates distance between two points on the map
    according to Haversine formula:
    d = 2R × sin⁻¹(√[sin²((θ₂ - θ₁)/2) + cosθ₁ × cosθ₂ × sin²((φ₂ - φ₁)/2)])
    
    Parameters:
    coord1, coord2 - pairs of coordinates in the form (lat, long)
    Returns:
     d - distance between coord1 and coord2 in kilometers '''
    
   # d = 2R × sin⁻¹(√[sin²((θ₂ - θ₁)/2) + cosθ₁ × cosθ₂ × sin²((φ₂ - φ₁)/2)])
    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    # Calculate the differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    d = 2 * R * np.arcsin(np.sqrt( 
          np.sin(dlat)**2 + np.cos(lat1) * np.cos(lat2) \
        * np.sin(dlon/2)**2
    ))
    return d

def filledline(data, ycol, ystdcol, xcol=None, xlabel='', ylabel='', title='', color='rgba(71, 103, 158, 1)'):
    if xcol is None:
        x = list(data.index.values)
    x_rev = x[::-1]
    y = list(data[ycol].values)
    color_fill=color.replace(' ', '')
    color_fill=color_fill.replace(',1)', ',0.2)')

    y_upper = list((data[ycol] + data[ystdcol]*0.5).values)
    y_lower = list((data[ycol] - data[ystdcol]*0.5).values)

    y_lower = y_lower[::-1]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x+x_rev,
        y=y_upper+y_lower,
        fill='toself',
        fillcolor=color_fill,
        line_color='rgba(255,255,255,0)',
        showlegend=False,    
    ))

    fig.add_trace(go.Scatter(
        x=x, y=y,
        line_color=color,
        name='Price',
        showlegend=False, 
        marker=dict(size=data['count']/100, sizemin=1, 
                          line_color='rgba(255,255,255,0)', ),
        text=data['count'],
        hovertemplate='Total of %{text} houses',
    ))

    fig.update_layout(title=title, margin=dict(l=0, r=0, t=80, b=0), 
                      xaxis_title=xlabel, yaxis_title=ylabel, template='seaborn')
    return fig