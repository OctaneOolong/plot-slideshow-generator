import pandas as pd
from scripts.matplotlib_origin_style_genner import matplotlib_plot_origin_default_style

def x_y_data_extractor(file, x_label, y_label):
        """
        takes an excel file consisting of two column data and returns a dictionary of each column with user specified keys. 
        """
        x_y_data_dict = {}
        
        df = pd.read_excel(file, header = None)

        df.columns = [x_label, y_label]

        x_y_data_dict[x_label] = df[x_label]
        x_y_data_dict[y_label] = df[y_label]

        return x_y_data_dict

def excel_data_plotter(file, x_title=None, y_title=None, plot_title = None):
    """
    Depends on x_y_data_extractor() and matplotlib_plot_origin_default_style() to extract column data from excel files and output .png's of plots of the data, in Origin default styling. Simply ties together the two previously mentioned functions and returns a plot object. 
    """
    if x_title == None:
        x_title = 'x'
    
    if y_title == None:
        y_title = 'y'

    if plot_title == None:
        plot_title = file.stem

    data = x_y_data_extractor(file, x_title, y_title)
    plot = matplotlib_plot_origin_default_style(x = data[x_title], y = data[y_title], plot_title = plot_title, x_title = x_title, y_title = y_title)

    return(plot)

