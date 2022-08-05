import numpy as np
import matplotlib.pyplot as plt

def matplotlib_plot_origin_default_style(x, y, plot_title, x_title, y_title):
    """
    20220804 - Intended to replicate the default format style of OriginLab. Simple to use, pass x and y data, plot name, and axis names. 

    Returns a figure object that can be used to display or save to file. 
    """
    plt.rcParams.update({'font.family':'arial'})

    fig, ax = plt.subplots(figsize = (13.3,7.5))
    
    ax.plot(x, y, linewidth = 1.5, color = 'k')

    ax.set_title(label = plot_title, fontsize=30, pad = 22)
    
    ax.set_xlabel(x_title, fontsize = 20, labelpad = 10)
    ax.set_xlim(0, 20)
    
    ax.set_ylabel(y_title, fontsize = 20, labelpad = 20)
    ax.set_ylim(-50, 1000)
    
    ax.minorticks_on()
    
    ax.set_yticks(np.arange(0, 1001, 200))
    ax.set_yticklabels(ax.get_yticks(), fontsize = 18)
    
    ax.set_xticks(np.arange(0, 21, 5))
    ax.set_xticklabels(ax.get_xticks(), fontsize = 18)

    ax.tick_params(which = 'major', length = 10, width = 1.5)
    ax.tick_params(which='minor', length = 5, width = 1.5)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.grid(False)
    
    return fig