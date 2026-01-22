import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Sample dataset (replace with your real Pink Morsels data)
df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] * 4,
    "sales": [10, 15, 20, 18, 22, 25,
              12, 14, 19, 21, 23, 26,
              8, 11, 15, 17, 19, 22,
              14, 16, 18, 20, 24, 28],
    "region": ["north"] * 6 + ["east"] * 6 + ["south"] * 6 + ["west"] * 6
})

app = dash.Dash(__name__)

app.layout = html.Div(
    className="container",
    children=[
        html.H1("Pink Morsels Sales Dashboard", className="title"),

        html.Div(
            className="radio-container",
            children=[
                html.Label("Select Region:", className="label"),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"},
                    ],
                    value="all",
                    className="radio-buttons"
                )
            ]
        ),

        dcc.Graph(id="sales-chart", className="chart")
    ]
)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="month",
        y="sales",
        color="region",
        markers=True,
        title=f"Pink Morsels Sales ({selected_region.capitalize()})"
    )

    fig.update_layout(
        plot_bgcolor="#ffffff",
        paper_bgcolor="#f7f7f7",
        font=dict(size=14)
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)

