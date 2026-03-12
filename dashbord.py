import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# יצירת נתוני דמו
df = pd.DataFrame({
    "קטגוריה": ["A", "B", "C", "D"],
    "ערך": [10, 23, 15, 8]
})

# יצירת הפיגורמה של בר-צ'ארט
fig = px.bardf, x="קטגוריה", y="ערך", title=("mody_dashborad")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("דאשבורד קטן לדוגמה"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)