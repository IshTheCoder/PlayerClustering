import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%".format(pct, absolute)


def draw_pie_chart(name, year):
    '''
    Function to draw the pie chart of players of different PlayType.
    Just input the player name and the year you want to know.
    :param name: Player name, string
    :param year: year
    :return:
    '''
    assert isinstance(name, str)
    assert 2015 <= year <= 2019
    path = "aggr_data/" + str(year) + "_pca_table.csv"
    df = pd.read_csv(path)
    new_df = df[df['PLAYER_NAME'] == name]
    data = new_df[["iso_freq", "tr_freq", "prb_freq", "prr_freq", "pu_freq", "su_freq", "ho_freq", "cut_freq", "os_freq",
                  "putback_freq", "misc_freq"]]
    data = data.values.tolist()
    data = np.array(data)[0]
    data = data / np.sum(data)
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    recipe = ["Isolation",
              "Transition",
              "PRBallHandler",
              "PRRollMan",
              "Postup",
              "Spotup",
              "Handoff",
              "Cut",
              "Offscreen",
              "OffRebound",
              "Misc"]
    ingredients = [x.split()[-1] for x in recipe]
    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                      textprops=dict(color="w"), shadow=False,
                                      colors=["cornflowerblue", "mediumseagreen", "gray", "salmon", "burlywood", "plum",
                                              "peru", "sandybrown", "teal", "darkkhaki", "pink"])
    ax.legend(wedges, ingredients,
              title="Freq of PlayTypes",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title(name + "  " + str(year))

    plt.show()
    return

draw_pie_chart("Nikola Jokic", 2018)