""" 
This script file contains answers to 
tasks 1 - 7.It first imports methods of class 
DataProcessing to fulfill its tasks
"""

from spiced.code.task_methods import DataProcessing

# Get data file path
filename = "spiced/data/datapoints.csv"

# Set directory where to save results
save_directory = "spiced/results"

# Create data processing object
data_processing_obj = DataProcessing(filename=filename, save_directory=save_directory)

# Task 1: Read x/y data points and save results to table
table = data_processing_obj.read_data()
print(table)

# Task 2: Create a scatter plot and save the image to results folder
data_processing_obj.create_scatter_plot()

# Task 3: Set slope to 10 and intercept to 0 and calculate y
updated_table = data_processing_obj.calculate_y_given_x(a=10, b=0)
y = updated_table["y"].tolist()
print(y)

# Task 4: Calculate the mean squared error (MSE) of y and y_true
y_true = updated_table["y_true"].tolist()
mse = data_processing_obj.calculate_mse(y=y, y_true=y_true)
print(mse)

# Task 5 and 6 combined: Find value of a and b that gives the lowest possible mse.
# We shall write a function first that can switch between task 5 and task 6

def find_minimum_mse(a, b, increment = -0.1, task_5 = True):
    """
    This function performs task 5 and 6 by modifying
    a or both a and b
    param a: slope
    param b: intercept
    increment: a value by which a/b decreases by per iteration
    task_5: Boolean. if False, perform task 6
    return: dictionary of mse, a and b
    """
    # initialize iteration index
    i = 0
    while(i < 100):
        
        # Recalculate y
        if task_5: # b set to zero
            running_table = data_processing_obj.calculate_y_given_x(a=a, b=0)
        else: # b must be incremented under task 6
            running_table = data_processing_obj.calculate_y_given_x(a=a, b=b)
        y = running_table["y"]
        y_true = running_table["y_true"]

        # calculate new_mse
        new_mse = data_processing_obj.calculate_mse(y=y, y_true=y_true)

        # Capture this new_mse, a and b at the first iteration and store them
        if i == 0:
            stored_mse = new_mse
            stored_a = a
            stored_b = b
        
        # for rest of iterations, assign stored_mse to the
        # calculated new_mse if the latter is less than 
        # than the stored value, otherwise discard it!
        else:
            if new_mse < stored_mse:
                stored_mse = new_mse
                stored_a = a
                stored_b = b

        # update value of a and b
        a = round(a+increment, 2)
        if task_5 == False:
            b = round(b+increment, 2)

        # update iteration index
        i += 1

    # We have the lowest possible mse and corresponding values of a and b
    result = {
                "mse": stored_mse, 
                "a": stored_a, 
                "b": stored_b
        }
    return result

# Task 5: result
min_mse = find_minimum_mse(a = 10, b = 0, task_5 = True)
print(min_mse)

# Task 6: result
min_mse = find_minimum_mse(a = 10, b = 0, task_5 = False) 
print(min_mse)

# Task 7: How could the algorithm be improved.
# By using a package that has a lower language implementation to speed up the iteration
# e.g linear_model function from sklearn


    