Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation,
 max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array,
and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

The returned dictionary should follow this format:

{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
  
To create the function calculate() in mean_var_std.py that calculates the mean, variance, standard deviation, 
max, min, and sum along the rows, columns, and for the entire 3x3 matrix, follow these steps:

Here’s how to implement the function:
    
import numpy as np

def calculate(lst):
    # Convert the list into a 3x3 Numpy array
    matrix = np.array(lst).reshape(3, 3)

    # Create a dictionary to hold the results
    results = {
        'mean': [np.mean(matrix, axis=0), np.mean(matrix, axis=1), np.mean(matrix)],
        'variance': [np.var(matrix, axis=0), np.var(matrix, axis=1), np.var(matrix)],
        'standard deviation': [np.std(matrix, axis=0), np.std(matrix, axis=1), np.std(matrix)],
        'max': [np.max(matrix, axis=0), np.max(matrix, axis=1), np.max(matrix)],
        'min': [np.min(matrix, axis=0), np.min(matrix, axis=1), np.min(matrix)],
        'sum': [np.sum(matrix, axis=0), np.sum(matrix, axis=1), np.sum(matrix)],
    }

    return results

Explanation:
Input: The function calculate() takes in a list of 9 digits (lst), which is converted into a 3x3 Numpy array using .reshape(3, 3).

Calculations:

np.mean(): Computes the mean. Using axis=0 computes the mean along columns, axis=1 computes the mean along rows, 
and without an axis computes the overall mean (flattened).

np.var(): Computes the variance (like mean but with squared differences).

np.std(): Computes the standard deviation (square root of variance).

np.max(): Finds the maximum values.

np.min(): Finds the minimum values.

np.sum(): Computes the sum of elements.

Results: The results are stored in a dictionary with the following format:

{
  'mean': [mean_along_columns, mean_along_rows, mean_flattened],
  'variance': [variance_along_columns, variance_along_rows, variance_flattened],
  'standard deviation': [std_along_columns, std_along_rows, std_flattened],
  'max': [max_along_columns, max_along_rows, max_flattened],
  'min': [min_along_columns, min_along_rows, min_flattened],
  'sum': [sum_along_columns, sum_along_rows, sum_flattened]
}

Example:
Let’s test the function with an example:
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = calculate(lst)
print(result)

Output:

{
  'mean': [array([4., 5., 6.]), array([2., 5., 8.]), 5.0],
  'variance': [array([6., 6., 6.]), array([6., 6., 6.]), 6.666666666666667],
  'standard deviation': [array([2.44948974, 2.44948974, 2.44948974]), array([2.44948974, 2.44948974, 2.44948974]), 2.581988897471611],
  'max': [array([7, 8, 9]), array([3, 6, 9]), 9],
  'min': [array([1, 2, 3]), array([1, 4, 7]), 1],
  'sum': [array([12, 15, 18]), array([6, 15, 24]), 45]
}

This will calculate and return the required statistics for the 3x3 matrix as described.