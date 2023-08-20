import matplotlib
import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt

from io import BytesIO
import base64
import threading
from queue import Queue

def get_graph(db_data):
    df = pd.DataFrame(db_data)
    print(df)

    heat_plot = plotter(df['heat_index'].value_counts(), 'Heat Index Categories')
    wind_plot = plotter(df['wind_index'].value_counts(), 'Wind Index Categories')
    # rainfall_plot = plotter(df['rainfall_index'].value_counts(), 'Rainfall Index Categories')
    # visibility_plot = plotter(df['Visibility_index'].value_counts(), 'Visibility Index Categories')
    return heat_plot, wind_plot#, rainfall_plot, visibility_plot

    '''for heat index'''
    category_counts = df['heat_index'].value_counts()

    # Create the pie chart using matplotlib
    plt.figure(figsize=(6, 6))
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Heat Index Categories')
    plt.tight_layout()

    # Save the plot to a BytesIO buffer
    pi_buffer = BytesIO()
    plt.savefig(pi_buffer, format='png')
    pi_buffer.seek(0)
    plt.close()
    encoded_image = base64.b64encode(pi_buffer.getvalue()).decode()

    '''for wind index'''
    category_counts = df['wind_index'].value_counts()

    # Create the pie chart using matplotlib
    plt.figure(figsize=(6, 6))
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Wind Index Categories')
    plt.tight_layout()

    # Save the plot to a BytesIO buffer
    pi_buffer = BytesIO()
    plt.savefig(pi_buffer, format='png')
    pi_buffer.seek(0)
    plt.close()
    encoded_image_wind_index = base64.b64encode(pi_buffer.getvalue()).decode()

    '''for rainfall index'''
    category_counts = df['rainfall_index'].value_counts()

    # Create the pie chart using matplotlib
    plt.figure(figsize=(6, 6))
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Rainfall Index Categories')
    plt.tight_layout()

    # Save the plot to a BytesIO buffer
    pi_buffer = BytesIO()
    plt.savefig(pi_buffer, format='png')
    pi_buffer.seek(0)
    plt.close()
    encoded_image_rainfall = base64.b64encode(pi_buffer.getvalue()).decode()
    encoded_image_visibility_index = base64.b64encode(pi_buffer.getvalue()).decode()
    return encoded_image, encoded_image_wind_index, encoded_image_rainfall


def get_gp2(db_data):
    df = pd.DataFrame(db_data)
    rainfall_plot = plotter(df['rainfall_index'].value_counts(), 'Rainfall Index Categories')
    visibility_plot = plotter(df['visibility_index'].value_counts(), 'Visibility Index Categories')
    return rainfall_plot, visibility_plot
def plotter(data, title):
    plt.figure(figsize=(4, 5))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.tight_layout()
    pi_buffer = BytesIO()
    plt.savefig(pi_buffer, format='png')
    pi_buffer.seek(0)
    plt.close()
    encoded_image = base64.b64encode(pi_buffer.getvalue()).decode()
    return encoded_image
