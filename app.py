import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import yfinance as yf
from dash.dependencies import Input, Output
import datetime
import time

# Create the Dash app using the Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], external_scripts=[])

# Get the initial data for BTC and ETH
btc_price = yf.Ticker("BTC-USD").history(period='1d', interval='1m')
eth_price = yf.Ticker("ETH-USD").history(period='1d', interval='1m')

# Create the figure objects for BTC and ETH charts
btc_fig = px.line(
    {"x": btc_price.index, "y": btc_price["Close"]},
    hover_data={"x": "2023-05-21"},
    template="plotly_dark",
    labels={"x": "Date", "y": "Price (BTC)"},
)
btc_fig.update_traces(name="BTC")

eth_fig = px.line(
    {"x": eth_price.index, "y": eth_price["Close"]},
    hover_data={"x": "2023-05-21"},
    template="plotly_dark",
    labels={"x": "Date", "y": "Price (ETH)"},
)
eth_fig.update_traces(name="ETH")

# Create a layout for the app using Bootstrap components
layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H2("BTC:", style={"font-size": "30px"}),
                            html.Div(id="btc-price", className="quote-value", style={"font-size": "30px"}),
                            html.Span(id="btc-change", className="change-value"),
                        ],
                        className="quote-container",
                        style={"font-size": "24px"},
                    ),
                    width=6,
                ),
                dbc.Col(
                    html.Div(
                        [
                            html.H2("ETH:", style={"font-size": "30px"}),
                            html.Div(id="eth-price", className="quote-value", style={"font-size": "30px"}),
                            html.Span(id="eth-change", className="change-value"),
                        ],
                        className="quote-container",
                        style={"font-size": "24px"},
                    ),
                    width=6,
                ),
            ],
            className="quote-row",
        ),
        html.H1("Cryptocurrency Dashboard"),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id="btc-chart",
                        figure=btc_fig,
                    ),
                    width=6,
                ),
                dbc.Col(
                    dcc.Graph(
                        id="eth-chart",
                        figure=eth_fig,
                    ),
                    width=6,
                ),
            ],
            className="chart-container",
        ),
        dbc.Row(
            dbc.Button("Update Data", id="update-data-button", color="primary", className="mt-4", n_clicks=0),
            justify="center"
        ),
        dcc.Interval(
            id='interval-component',
            interval=60 * 1000,  # 1 minute in milliseconds
            n_intervals=0
        )
    ],
    fluid=True,
)


# Define a function to update the data
def update_data():
    global btc_price, eth_price
    btc_price = yf.Ticker("BTC-USD").history(period='1d', interval='1m')
    eth_price = yf.Ticker("ETH-USD").history(period='1d', interval='1m')
    btc_change = (btc_price['Close'].iloc[-1] - btc_price['Close'].iloc[0]) / btc_price['Close'].iloc[0] * 100
    eth_change = (eth_price['Close'].iloc[-1] - eth_price['Close'].iloc[0]) / eth_price['Close'].iloc[0] * 100
    btc_change_formatted = "{:.2f}%".format(btc_change)
    eth_change_formatted = "{:.2f}%".format(eth_change)
    return "${:,.2f}".format(btc_price['Close'].iloc[-1]), "${:,.2f}".format(eth_price['Close'].iloc[-1]), btc_change_formatted, eth_change_formatted


# Register the callback for updating the data
@app.callback(
    Output("btc-price", "children"),
    Output("eth-price", "children"),
    Output("btc-change", "children"),
    Output("eth-change", "children"),
    Output("btc-chart", "figure"),
    Output("eth-chart", "figure"),
    Input("update-data-button", "n_clicks"),
    Input('interval-component', 'n_intervals')
)
def update_data_callback(n_clicks, n_intervals):
    # Update data
    btc_price_latest, eth_price_latest, btc_change_formatted, eth_change_formatted = update_data()
    btc_change_color = "green" if float(btc_change_formatted[:-1]) >= 0 else "red"
    eth_change_color = "green" if float(eth_change_formatted[:-1]) >= 0 else "red"

    btc_price_elem = html.Div("${:,.2f}".format(float(btc_price_latest.replace("$", "").replace(",", ""))),
                             id="btc-price", className="quote-value", style={"font-size": "30px"})
    btc_change_elem = html.Span(btc_change_formatted, id="btc-change", className="change-value",
                                style={"color": btc_change_color})
    eth_price_elem = html.Div("${:,.2f}".format(float(eth_price_latest.replace("$", "").replace(",", ""))),
                             id="eth-price", className="quote-value", style={"font-size": "30px"})
    eth_change_elem = html.Span(eth_change_formatted, id="eth-change", className="change-value",
                                style={"color": eth_change_color})

    # Update figures
    btc_fig.update_traces(x=btc_price.index, y=btc_price["Close"])
    eth_fig.update_traces(x=eth_price.index, y=eth_price["Close"])

    return btc_price_elem, eth_price_elem, btc_change_elem, eth_change_elem, btc_fig, eth_fig


# Set the layout for the app
app.layout = layout

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
