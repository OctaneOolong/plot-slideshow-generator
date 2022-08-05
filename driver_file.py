from scripts.excel_data_plot_genner import excel_data_plotter
from scripts.python_pptx_gen import python_pptx_gen
from pathlib import Path
import pandas as pd

def driver_func():
    """
    Input x_title, y_title, a plot_title list corresponding to the filenames, will produce png plots for each file then collate them into a power point slide and delete the png files. 

    Todo:
    - parametize the driver function to take input form the command line.
    - set the sample title list to be gathered from a text file.
    """
    data_file_list = sorted(list(Path.cwd().glob('signal*.xlsx')), reverse = True)

    x_title = 'Time (min)'
    y_title = 'Signal (mV)'

    sample_title_list = [
                        'Instant: Woolworths Classic',
                        'Instant: Nescafe Gold',
                        'Instant: Nescafe Blend 43',
                        'Instant: Vittoria',
                        'Instant: Moccona Classic',
                        'Capsule: Vittoria Espresso',
                        'Capsule: Vittoria Italian',
                        'Capsule: Woolies Medium Roast',
                        'Capsule: L\'Or Ristretto',
                        'Vittoria Bag',
                        ]
    
    plot_title_dict = dict(zip(data_file_list, sample_title_list))

    for file in data_file_list:
        
        plot = excel_data_plotter(file, x_title, y_title, plot_title = plot_title_dict[file])
        plot.savefig('{}.png'.format(file.stem))
    
    image_file_list = sorted(list(Path.cwd().glob('*.png')), reverse = True)

    prs = python_pptx_gen(image_file_list, delete_input_files='y')

    out_file_name = 'plot_slideshow.pptx'
    
    prs.save(out_file_name)

driver_func()