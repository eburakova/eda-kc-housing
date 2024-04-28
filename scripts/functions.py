import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

PI = np.pi
R = 6371 # km - Earth radius

def geoplot(data, size_col, color_col, 
            title="King county housings",
            alpha=1, marker_max_size=20,
            colorscheme="Portland"):
    
    cb_title=color_col.capitalize()
    cb_title=cb_title.replace('_', ' ')

    hover_label = size_col.capitalize()
    hover_label = hover_label.replace('_', ' ')
    
    marker_sizes = np.exp(data[size_col].max() + 2 - data[size_col])

    # Plots the main figure
    fig = px.scatter_mapbox(
        data,
        lat='lat',
        lon='long',
        opacity=alpha,
        zoom=8.2,
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
        hovertemplate = data['lat'].round(4).astype(str) + '<br>' + data['long'].round(4).astype(str) + f'<br><b>{cb_title}</b>: ' + data[color_col].astype(str) + f'<br><b>{hover_label}</b>: ' + data[size_col].astype(str) + '<br>' 
                #f'{data.lat.astype(str)}<br>{data.long.astype(str)}<br><b>{cb_title}: {data[color_col].astype(str)}</b><br><b>{hover_label}</b>: {data[size_col].astype(str)}</b><br>' 
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
    """
    Plots a correlation matrix.

    Parameters:
    - corm (numpy.ndarray): The correlation matrix to be plotted.
    - labels (list): List of labels for the columns and rows of the correlation matrix.
    - ax (matplotlib Axes): The axes object to draw the plot onto.

    Returns:
    - cm (Axes): The heatmap Axes object.
    """
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
        fill='tonexty',
        fillcolor=color_fill,
        line_color='rgba(255,255,255,0)',
        showlegend=False,    
    ))

    fig.add_trace(go.Scatter(
        x=x_rev,
        y=y_lower,
        #fill='tonexty',
        #fillcolor=color_fill,
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

def plot_feature_kde_row(df, x_vars, y_vars, hue, cmap='inferno', title=None):
    """
    Plot Kernel Density Estimate (KDE) plots for each pair of features in a DataFrame.

    Parameters:
    - df (DataFrame): The input DataFrame.
    - x_vars (list): List of column names to be plotted on the x-axis.
    - y_vars (list): List of column names to be plotted on the y-axis.
    - hue (str): Column name to map plot aspects to different colors.
    - cmap (str): Name of mpl.Colormap to use for the color dimension.
    - title (str): Figure suptitle

    Returns:
    - None
    """
     
    color_dim_unique_vals = sorted(df[hue].unique().tolist())
    palette = sns.color_palette(cmap, len(color_dim_unique_vals))
    g = sns.PairGrid(df, x_vars=x_vars, y_vars=y_vars, palette=cmap, hue=hue)
    g.map_offdiag(sns.kdeplot, cl=5, linewidths=1, alpha=0.999)

    # Manually create a legend
    legend_elements = [plt.Line2D([0], [0], color=palette[i-min(color_dim_unique_vals)], label=f'{hue.capitalize()} {i}') 
                    for i in color_dim_unique_vals]

    # Adding legend to the rightmost axis
    legend = g.axes[-1, -1].legend(handles=legend_elements)
    legend.set_bbox_to_anchor((1.8, 1.1))
    if title:
        plt.gcf().suptitle(title, x=0.1, y=1.1, ha='left', va='top')
    return plt.gcf()
