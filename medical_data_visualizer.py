import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
overweight = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = overweight.apply(lambda x: 1 if x > 25 else 0)

# 3 normalize data
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x <= 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x <= 1 else 1)



# 4
def draw_cat_plot():
    # 5
    # 6
    # 7
    # 8
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'], var_name='variable', value_name='value')
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['height'] >= df['height'].quantile(0.025)) & (df['ap_lo'] <= df['ap_hi']) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()
    #print (corr)

    # 13
    mask = np.triu(corr)



    # 14
    fig, ax = plt.subplots()

    # 15
    sns.color_palette("icefire", as_cmap=True)
    sns.heatmap(corr, mask=mask, ax=ax, annot=True, fmt='.1f')


    # 16
    fig.savefig('heatmap.png')
    return fig
draw_heat_map()