import plotly.express as px
import plotly.graph_objs as go
import pandas as pd


url = "https://raw.githubusercontent.com/dez08/python_lessons/refs/heads/main/MSFT.csv"
df = pd.read_csv(url)

# Назначение переменных данным из CSV файла
years = df['year']  # Год
earnings = df['earnings']  # Выручка
net_profit = df['revenue']  # Чистая прибыль
gross_profit = df['gross_profit']  # Валовая прибыль

# Создание линейного графика
fig = go.Figure()
fig.add_trace(go.Scatter(x=years, y=net_profit, mode='lines+markers', name='Чистая прибыль', line=dict(color='red')))
fig.add_trace(go.Scatter(x=years, y=earnings, mode='lines+markers', name='Выручка', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=years, y=gross_profit, mode='lines+markers', name='Валовая прибыль',
                         line=dict(color='green', width=5, dash='dot')))
fig.update_layout(title='Финансовые показатели Microsoft Corporation с 2011 по 2024 гг.')
fig.update_layout(yaxis_title='Млрд. $', xaxis_title='Год', title={'font': dict(size=24), 'x': 0.5},
                  legend_orientation='h', legend_font_size=12)
fig.update_xaxes(gridcolor='black', titlefont=dict(size=18), tickfont=dict(size=16))
fig.update_yaxes(titlefont=dict(size=18), tickfont=dict(size=16))
fig.update_traces(hoverinfo='all', hovertemplate='Год: %{x}<br>Объем: %{y}')
fig.show()

# Создание столбчатой диаграммы
fig = go.Figure(data=[
    go.Bar(x=years, y=earnings, name='Выручка', marker_color='blue'),
    go.Bar(x=years, y=gross_profit, name='Валовая прибыль', marker_color='green'),
    go.Bar(x=years, y=net_profit, name='Чистая прибыль', marker_color='red'),
])
fig.update_layout(barmode='group', title='Финансовые показатели Microsoft Corporation с 2011 по 2024 гг.')
fig.update_layout(yaxis_title='Млрд. $', xaxis_title='Год', title={'font': dict(size=24), 'x': 0.5},
                  legend_orientation='h', legend_font_size=12)
fig.update_xaxes(titlefont=dict(size=18), tickfont=dict(size=16))
fig.update_yaxes(titlefont=dict(size=18), tickfont=dict(size=16))
fig.update_traces(hoverinfo='all', hovertemplate='Год: %{x}<br>Объем: %{y}')
fig.show()

# Создание круговой диаграммы
data = [earnings.sum(), net_profit.sum(), gross_profit.sum()]
labels = ['Выручка', 'Чистая прибыль', 'Валовая прибыль']
fig = px.pie(values=data, names=labels, title='Общие финансовые показатели Microsoft Corporation с 2011 по 2024 гг.')
fig.update_layout(title={'font': dict(size=24), 'x': 0.5}, legend_title='Условные обозначения:',
                  legend=dict(font=dict(size=12)), font={'size': 16})
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()
