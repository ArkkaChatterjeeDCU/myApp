import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def get_graph(db_data):

    df = pd.DataFrame(db_data)
    print(df)
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
    return encoded_image
    # df = df.groupby('location')
    # json_data = {}
    # for loc,group in df:
    #     json_data[loc]= group.to_dict(orient="records")
    # json_string = pd.io.json.dumps(json_data)
    # print(json_string)




