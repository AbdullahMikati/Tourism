import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset
data = pd.read_csv('/Users/abdullah/Documents/MSBA325/Tourism.csv')

# Streamlit app layout
st.title("Interactive Tourism Data Visualizations")
st.write("""
         Welcome to this interactive dashboard, which explores tourism infrastructure across various districts and towns in Lebanon. 
         Use the interactive features to dive deeper into the tourism landscape, understand the distribution of facilities, and identify areas with the most potential.
         """)

# First visualization: Stacked Bar Chart (Interactive by District)
st.header("Stacked Bar Chart: Distribution of Tourism Facilities by District")
st.write("""
         The stacked bar chart below displays the number of tourism facilities (hotels, restaurants, guest houses) in each district. 
         You can select a district to filter the data and focus on specific towns within that district. This helps highlight how tourism infrastructure is spread across different areas.
         """)

# Select District for interactivity
selected_district = st.selectbox("Choose a district to filter", data['District'].unique())

# Filter data by the selected district
filtered_data = data[data['District'] == selected_district]

# Group the data by 'Town' within the selected district and sum the values for tourism categories
grouped_data = filtered_data.groupby('Town')[['Total number of hotels', 'Total number of restaurants', 'Total number of guest houses']].sum().reset_index()

# Create a stacked bar chart using Plotly
fig1 = px.bar(grouped_data, 
              x='Town', 
              y=['Total number of hotels', 'Total number of restaurants', 'Total number of guest houses'], 
              title=f"Tourism Facilities in {selected_district}",
              labels={'value': 'Number of Facilities'},
              barmode='stack')

# Display the bar chart in Streamlit
st.plotly_chart(fig1)

# Add insights about the bar chart
st.write(f"""
         **Insights**: The stacked bar chart helps us understand the composition of tourism facilities in each town within the selected district. 
         By observing the bars, we can easily identify which towns have a more diverse set of tourism services and which are lacking in specific categories. 
         For example, a town with more hotels might attract a different type of tourist compared to a town with more cafes or guest houses.
         """)

# Second visualization: Treemap with Context
st.header("Treemap: Tourism Index by District and Town")
st.write("""
         The treemap provides a hierarchical view of the Tourism Index, which indicates the overall tourism potential of different areas. 
         You can use the slider to filter towns based on a minimum Tourism Index, allowing you to focus on higher-ranked areas.
         Hover over each area to get additional information on the number of restaurants, guest houses, hotels, and cafes in each town.
         """)

# Add a slider for user interaction to filter by the minimum Tourism Index
min_tourism_index = st.slider("Select the minimum Tourism Index to display", min_value=int(data['Tourism Index'].min()), max_value=int(data['Tourism Index'].max()), value=0)

# Filter data based on the selected minimum Tourism Index
filtered_data_treemap = data[data['Tourism Index'] >= min_tourism_index]

# Create a treemap with Plotly
fig2 = px.treemap(filtered_data_treemap, 
                  path=['District', 'Town'], 
                  values='Tourism Index',
                  title='Treemap of Tourism Index by District and Town',
                  hover_data={
                      'Total number of restaurants': True,
                      'Total number of guest houses': True,
                      'Total number of hotels': True,
                      'Total number of cafes': True
                  })

# Display the treemap in Streamlit
st.plotly_chart(fig2)

# Add insights about the treemap
st.write(f"""
         **Insights**: The treemap allows us to quickly identify which towns and districts have the highest Tourism Index. 
         By adjusting the slider, you can filter out areas with lower tourism potential and focus on those that are more developed.
         This visualization helps stakeholders prioritize areas for tourism development, by showing not just the tourism potential but also the distribution of key facilities like restaurants, guest houses, and hotels.
         """)

# Add some concluding remarks
st.write("""
         **Conclusion**: These visualizations allow us to explore tourism infrastructure in Lebanon interactively. 
         The stacked bar chart focuses on the distribution of tourism facilities in individual towns, while the treemap highlights tourism potential across the country. 
         By using these tools, decision-makers can gain valuable insights into where to focus their efforts for tourism development and infrastructure improvement.
         """)

