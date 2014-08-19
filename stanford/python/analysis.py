import numpy as np
from matplotlib import pyplot

def read_csv_file(input_csv_file):
    '''
    This code will read in a csv file of year, temperature, rainfall, and number of mosquitos and return 4 arrays, 
    one for each column
    '''
    years, temperature, rainfall, mosquitos = np.genfromtxt(input_csv_file, unpack=True,skiprows=1,delimiter=",")
    return years, temperature, rainfall, mosquitos
    
def convert_fahrenheit_to_celsius(temp_in_f):
    '''
    This code will convert an array of temperatures from fahrenheit to celsius
    '''
    temp_in_c = (temp_in_f - 32) * 5 / 9.0
    return temp_in_c
    
def plot_data(x,y,marker, plot_name):
    '''
    This code will plot arrays into to x and y with a symbol
    '''
    pyplot.ion()
    pyplot.figure()  ## Careful with this command, if in a loop, you'll get tons of figures!
    pyplot.plot(x,y,str(marker))
    pyplot.savefig(plot_name)
    pyplot.close()

# test temp conversion
assert convert_fahrenheit_to_celsius(32) == 0

years, temperature, rainfall, mosquitos = read_csv_file('mosquito_data_A1.csv')
temp_in_c = convert_fahrenheit_to_celsius(temperature)
plot_data(mosquitos, temperature, '^', 'fourth_plot.pdf')
