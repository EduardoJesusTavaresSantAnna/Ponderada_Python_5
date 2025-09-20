import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    resultado_todos = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    anos_todos = np.arange(df['Year'].min(), 2051)
    plt.plot(anos_todos, resultado_todos.intercept + resultado_todos.slope * anos_todos, 'r', label='Ajuste todos os anos')

    df_recente = df[df['Year'] >= 2000]
    resultado_recente = linregress(df_recente['Year'], df_recente['CSIRO Adjusted Sea Level'])
    anos_recente = np.arange(2000, 2051)
    plt.plot(anos_recente, resultado_recente.intercept + resultado_recente.slope * anos_recente, 'g', label='Ajuste 2000+')

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.xticks(np.arange(1850, 2080, 25))

    plt.savefig('sea_level_plot.png')
    return plt.gca()
