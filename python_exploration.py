#Function for visualising effect size vs. sample size with power and significance

##required packages and libraries
import numpy as np 
import matplotlib.pyplot as plt #for plotting
import seaborn as sns 
from statsmodels.stats.power import TTestIndPower #Power calculatons
import ipywidgets  #for creating interactive sliders
import warnings
warnings.filterwarnings('ignore')

def n_es_plot(alpha = 0.05, power = 0.8, es_in = 0.3):
    
    """
    Funtion for creating a plot for given signifiacnce and power
    """
    
    effect_sizes = np.arange(0.005, 2, 0.005) #Range of effect sizes
    
    #Empty lists for storing results
    es_list = []
    n_list =[]
    for es in effect_sizes:
        power_analysis = TTestIndPower() #uses pooled variances
        n_needed = power_analysis.solve_power(effect_size = es, 
                                               alpha = alpha,
                                               power = power,
                                               alternative = "two-sided") #Calculate the power of a t-test for two independent sample
        es_list.append(es)
        n_list.append(n_needed)
        
    n_in = n_list[es_list.index(es_in)]
    
    sns.set_style('darkgrid')
    plt.plot(n_list, es_list, '-', color = 'mediumorchid')
    plt.scatter(n_in, es_in, c="midnightblue")
    plt.plot([n_in, n_in], [0,es_in], c = "slateblue", linestyle = "--")
    plt.plot([0, n_in], [es_in, es_in], c = "slateblue", linestyle = "--")
    plt.xlim([0, 500]) #setting limits on x
    plt.xlabel("Sample Size")
    plt.ylabel("Effect Size")
    plt.title(f'Sample size vs. effect size for \n significance {alpha} and power {power}')
    annotation = plt.annotate(text = f'{round(n_in)} samples', 
                xy = (n_in,0),
                xytext = (15, 15),
                              color = 'w',
                textcoords = 'offset points',
                bbox = {'boxstyle': 'round', 'fc':'mediumorchid'},
                arrowprops = {'arrowstyle':'->', 'color': "mediumorchid"}
                             )
    annotation.set_visible(True)
    plt.grid(True, linestyle = '--')
    
  
#implementing function
ipywidgets.interact(n_es_plot, alpha = (0, 0.1, 0.01), power = (0,1, 0.01), es_in = (0, 2, 0.05))

