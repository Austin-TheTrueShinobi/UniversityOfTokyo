import plotly.express as px 
df = px.data.tips()  
fig = px.density_heatmap(df, x="correlation", y="feature", marginal_x="histogram", marginal_y="histogram") 
fig.show()
