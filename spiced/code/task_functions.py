
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_y_given_slope_and_intercept(x, a, b):
    """
    This function calculates variable y 
    given independent variable x
    param x: x values (independent)
    param a: slope
    param b: intercept
    return: list 
    """
    return [a * x[i] + b for i in range(len(x))]

def round(x, dplaces):
    """
    This function is a repetition of the numpy
    function that rounds off numbers. It is meant
    to avoid importing numpy again in the main.py
    script
    param x: a single float
    param dplaces: no of decimal places to round-off to
    return: single float
    """
    return np.round(x, dplaces)


    
class DataProcessing:
    """
    This class is meant to process x,y data provided 
    under data folder and perform the tasks requested 
    as pre-requisites to enrol for the data science 
    course at Spiced GmbH
    """
    def __init__(self, filename, save_directory):
        """
        Initialization function
        param filename: link to the file location
        param save_directory: link to directory where
        results are saved
        """
        self.filename = filename
        self.save_directory = save_directory

    def read_data(self):
        """
        This function reads the csv data into a pandas
        table in line with task 1 request
        return: a pandas table
        """
        return pd.read_csv(self.filename)
    
    def get_x_and_y_as_dict(self):
        """
        This function extracts x and y values as lists
        from pandas table and puts them into a dictionary
        return: dictionary with x and y as lists
        """
        data = self.read_data()
        x = data["x"].tolist()
        y = data["y"].tolist()
        return {"x": x, "y": y}

    def create_scatter_plot(self):
        """
        This function creates a scatter plot
        and saves image to a directory in line 
        with task 2 request
        return: scatter plot image in png format
        """
        xy = self.get_x_and_y_as_dict()
        x = xy["x"]
        y = xy["y"]
        plt.scatter(x, y)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Scatter plot of x and y values")
        plt.savefig(f"{self.save_directory}/task_2_scatter_plot.png")
    
    def calculate_y_given_x(self, a, b):
        """
        This function performs task 3, i.e. calculates
        values of y given x, slope and intercept and saves
        the results as csv file
        param a: slope
        param b: intercept
        return: pandas table
        """
        data_dict = self.get_x_and_y_as_dict()
        x = data_dict["x"]
        y_true = data_dict["y"]        
        y = calculate_y_given_slope_and_intercept(x=x, a=a, b=b)
        df = pd.DataFrame(data = {"x": x, "y_true":y_true, "y":y})
        df.to_csv(f'{self.save_directory}/task_3.csv', index=False)
        return df
    
    def calculate_mse(self, y, y_true):
        """
        This function calculates the mean square error
        given y and y_true in line with task number 4
        param y: list of Extrapolated/interpolated y values
        param y_true: list of original y values
        return: one value
        """
        square_diff = [(y[i] - y_true[i]) ** 2 for i in range(len(y))]
        sum_square_diff = np.sum(square_diff)
        return 1/len(y) * sum_square_diff


