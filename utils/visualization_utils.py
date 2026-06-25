import matplotlib.pyplot as plt


def set_labels(title, xlabel, ylabel="Frequency"):
    """Set title, xlabel, and ylabel for a matplotlib plot."""
    title = title.title()
    xlabel = xlabel.title()
    fontdict = {"fontsize": 12, "fontweight": "bold"}
    plt.title(title, fontdict=fontdict)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)



def highlight_max_bar(ax):
    """Highlight the highest bar in a barplot."""
    max_val = max(bar.get_height() for bar in ax.patches)
    for bar in ax.patches:
        if bar.get_height() == max_val:
            bar.set_color("red")