from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import firebase_admin
from firebase_admin import credentials, firestore

# TẢI DỮ LIỆU TỪ FIRESTORE
cred = credentials.Certificate(
    "./data/iuh-19529651-firebase-adminsdk-3v4ij-8387769ee6.json")
appLoadData = firebase_admin.initialize_app(cred)

dbFireStore = firestore.client()


# TRỰC QUAN HÓA DỮ LIỆU WEB APP
app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
app.title = "Finance Data Analysis"

# TRỰC QUAN HÓA DỮ LIỆU WEB APP

queryResults = list(dbFireStore.collection(
    "tbl-19529651").select(['PRICEEACH', 'QUANTITYORDERED', 'SALES', 'PRODUCTLINE', 'YEAR_ID']).stream())
listQueryResult = list(map(lambda x: x.to_dict(), queryResults))

# doanh số sale
df = pd.DataFrame(listQueryResult)
revenue = round(df['SALES'].sum(), 2)

# doanh thu
df['TOTAL_SALES'] = df['PRICEEACH'] * df['QUANTITYORDERED']
df['PROFIT'] = df['SALES'] - df['TOTAL_SALES']
profit = round(df['PROFIT'].sum(), 2)

# top doanh số
top_revenue = df.groupby('PRODUCTLINE').sum().sort_values(
    by='SALES', ascending=False).head(1)
top_revenue = top_revenue.reset_index()
top_revenue_name = top_revenue.get('PRODUCTLINE').to_string(index=False)
top_revenue_value = top_revenue.get('SALES').to_string(index=False)

# top doanh thu
top_profit = df.groupby('PRODUCTLINE').sum().sort_values(
    by='PROFIT', ascending=False).head(1)
top_profit = top_profit.reset_index()
top_profit_name = top_profit.get('PRODUCTLINE').to_string(index=False)
top_profit_value = top_profit.get('PROFIT').to_string(index=False)

# chart

# doanh số bán hàng theo năm - bar chart
figDoanhSo = px.bar(df, y='SALES', x='YEAR_ID',
                    labels={'YEAR_ID': 'Năm', 'SALES': 'Doanh số'},
                    title='Doanh số bán hàng theo năm', )

# tỉ lệ đóng góp của doanh số theo từng danh mục sản phẩm trong từng năm - sunburst chart
figTiLeDoanhThu = px.sunburst(df, path=['YEAR_ID', 'PRODUCTLINE'], values='SALES',
                              labels={'YEAR_ID': 'Năm', 'SALES': 'Doanh số'},
                              title='Tỉ lệ đóng góp của doanh số theo từng danh mục sản phẩm trong từng năm')

# lợi nhuận bán hàng theo năm - line chart
total_profit = df.groupby('YEAR_ID').sum()['PROFIT'].reset_index()
figLoiNhuan = px.line(total_profit, y='PROFIT', x='YEAR_ID',
                      labels={'YEAR_ID': 'Năm', 'PROFIT': 'Lợi nhuận'},
                      title='Lợi nhuận bán hàng theo năm')

# tỉ lệ đóng góp của lợi nhuận theo từng danh mục sản phẩm trong từng năm - sunburst chart
figTiLeLoiNhuan = px.sunburst(df, path=['YEAR_ID', 'PRODUCTLINE'], values='PROFIT',
                              labels={'YEAR_ID': 'Năm', 'PROFIT': 'Lợi nhuận'},
                              title='Tỉ lệ đóng góp của lợi nhuận theo từng danh mục sản phẩm trong từng năm')

app.layout = html.Div(
    children=[
        # header
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.H5(
                                    children=[
                                        html.Span(
                                            children="Xây dựng dan",
                                            className="bg-white text-black"
                                        ),
                                        html.Span("h mục sản phẩm tiềm năng"),
                                    ],
                                    className="ms-5 text-white text-uppercase"),
                            ],
                            className="col-6",
                        ),
                        html.Div(
                            children=[
                                html.H5(children="ĐHCN tp.HCM - ĐHKTPM15B - 19529651 - Phạm Đăng Đan",
                                        className="text-white text-uppercase"),
                            ],
                            className="col-6",
                        )
                    ],
                    className="row pt-3"
                )
            ],
            className="bg-primary container-fluid",
        ),
        # wrapper
        html.Div(
            children=[
                html.Div(
                    children=[
                        # doanh số sale
                        html.Div(
                            html.Div(
                                children=[
                                    html.H6(
                                        children="Doanh số sale",
                                        className="text-uppercase fw-bold"),
                                    html.P(revenue),
                                ],
                                className="bg-white pt-3 pb-2 ps-3 card",
                            ),
                        ),

                        # lợi nhuận
                        html.Div(
                            html.Div(
                                children=[
                                    html.H6(children="Lợi nhuận",
                                            className="text-uppercase fw-bold"),
                                    html.P(profit),
                                ],
                                className="bg-white pt-3 pb-2 ps-3 card",
                            )
                        ),

                        # top doanh số
                        html.Div(
                            html.Div(
                                children=[
                                    html.H6(
                                        children="top doanh số",
                                        className="text-uppercase fw-bold"),
                                    html.P(top_revenue_name + \
                                           ", " + top_revenue_value),
                                ],
                                className="bg-white pt-3 pb-2 ps-3 card",
                            )
                        ),

                        # top lợi nhuận
                        html.Div(
                            html.Div(
                                children=[
                                    html.H6(
                                        children="Top lợi nhuận",
                                        className="text-uppercase fw-bold"),
                                    html.P(top_profit_name + \
                                           ", " + top_profit_value),
                                ],
                                className="bg-white pt-3 pb-2 ps-3 card",
                            )
                        ),
                    ],
                    className="row mt-3 row-cols-4"
                ),
                html.Div(
                    children=[
                        html.Div(
                            html.Div(
                                children=dcc.Graph(
                                    id='doanhso-graph',
                                    figure=figDoanhSo),
                                className="bg-white card"
                            )),
                        html.Div(
                            html.Div(
                                children=dcc.Graph(
                                    id='tiledoanhthu-graph',
                                    figure=figTiLeDoanhThu),
                                className="bg-white card"
                            )),
                    ],
                    className="row mt-1 row-cols-2"
                ),
                html.Div(
                    children=[
                        html.Div(
                            html.Div(
                                children=dcc.Graph(
                                    id='loinhuan-graph',
                                    figure=figLoiNhuan),
                                className="bg-white card"
                            )),
                        html.Div(
                            html.Div(
                                children=dcc.Graph(
                                    id='tileloinhuan-graph',
                                    figure=figTiLeLoiNhuan),
                                className="bg-white card"
                            )),
                    ],
                    className="row mt-1 row-cols-2"
                ),
            ],
            className="container",
        ),
    ],
    className="bg-light",
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8091)
