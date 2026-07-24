### Section 02 - Core Data Concepts Showcase ###

import statistics
import math
import numpy

DATASET_01 = [10, 20, 30, 40, 50]
DATASET_02 = [5, 10, 15, 20, 25, 30]

#Functions
# Formula for Mean

POPULATION_MEAN_TOTAL = 0
SAMPLE_MEAN_TOTAL = 0
POPULATION_Variance_TOTAL = 0
SAMPLE_Variance_TOTAL = 0


### User Population ### ---------------------------------------------------------------------------------------------
def user_population_mean():
    global POPULATION_MEAN_TOTAL
    population_mean_sum = math.fsum(DATASET_01)
    dataset_01_length = len(DATASET_01)
    user_population_mean_divided = population_mean_sum/dataset_01_length
    # print(f"The Population Mean Sum of {DATASET_01} is = {population_mean_sum}")
    # print(f"The number of values in, DATASET_01 {DATASET_01}, is = {dataset_01_length}")
    # print(f"The result of The Population Mean Sum, {population_mean_sum}, divided by The Number of Values in the "
    #       f"Dataset, {dataset_01_length}, is = {user_population_mean_divided}")

    POPULATION_MEAN_TOTAL = user_population_mean_divided

    return user_population_mean_divided


### User Population ### ---------------------------------------------------------------------------------------------
### User Sample ### ---------------------------------------------------------------------------------------------
def user_sample_mean():
    sample_mean_sum = math.fsum(DATASET_01)
    dataset_01_length = len(DATASET_01)
    user_sample_mean_divided = sample_mean_sum/dataset_01_length
    # print(f"The Sample Mean Sum of {DATASET_01} is = {sample_mean_sum}")
    # print(f"The number of values in, DATASET_01 {DATASET_01}, is = {dataset_01_length}")
    # print(f"The result of The Sample Mean Sum, {sample_mean_sum}, divided by The Number of Values in the "
    #       f"Dataset, {dataset_01_length}, is = {user_sample_mean_divided}")
    return user_sample_mean_divided


### User Sample ### ---------------------------------------------------------------------------------------------
### library Population ### ------------------------------------------------------------------------------------------

def library_population():
    library_population_mean = statistics.mean(DATASET_01)
    # print(f"The Python library has an in-built function to calculate the mean. "
    #       f"So the data in DATASET_01, {DATASET_01}, would result out to "
    #       f"library_population_mean {library_population_mean}")
    return library_population_mean


### library Population ### ------------------------------------------------------------------------------------------
### library Sample ### ---------------------------------------------------------------------------------------------
def library_sample():
    library_sample_mean = statistics.mean(DATASET_01)
    # print(f"The Python library has an in-built function to calculate the mean. "
    #       f"So the data in DATASET_01, {DATASET_01}, would result out to "
    #       f"library_sample_mean {library_sample_mean}")
    return library_sample_mean


### library Sample ### ---------------------------------------------------------------------------------------------
# Formula for Variance
### User Population Variance ### ---------------------------------------------------------------------------------------------
def user_population_variance():
    global POPULATION_MEAN_TOTAL
    POPULATION_MEAN_TOTAL = user_population_mean()
    variance_sum_total = 0
    user_population_variance_total = 0

    for x in DATASET_01:
        x_minus = x - POPULATION_MEAN_TOTAL
        # print("Variance minus")
        # print(x_minus)
        variance_squared_total = x_minus ** 2
        # print("Variance Squared")
        # print(variance_squared_total)

        variance_sum_total += variance_squared_total
    # print("Variance Sum Total")
    # print(variance_sum_total)

    user_population_variance_total = variance_sum_total/len(DATASET_01)


    return user_population_variance_total



### User Population Variance ### ---------------------------------------------------------------------------------------------
### User Sample Variance ### ---------------------------------------------------------------------------------------------
def user_sample_variance():
    global SAMPLE_MEAN_TOTAL
    SAMPLE_MEAN_TOTAL = user_sample_mean()
    variance_sum_total = 0
    user_sample_variance_total = 0

    for x in DATASET_01:
        x_minus = x - SAMPLE_MEAN_TOTAL
        # print("Variance minus")
        # print(x_minus)
        variance_squared_total = x_minus ** 2
        # print("Variance Squared")
        # print(variance_squared_total)

        variance_sum_total += variance_squared_total
    # print("Variance Sum Total")
    # print(variance_sum_total)

    user_sample_variance_total = variance_sum_total/(len(DATASET_01)-1)


    return user_sample_variance_total

### User Sample Variance ### ---------------------------------------------------------------------------------------------
### Library Population Variance ### ---------------------------------------------------------------------------------------------

def library_population_variance():
    result_lib_pop_var = statistics.pvariance(DATASET_01)
    return result_lib_pop_var
### Library Population Variance ### ---------------------------------------------------------------------------------------------
### Library Sample Variance ### ---------------------------------------------------------------------------------------------
def library_sample_variance():
    result_lib_smpl_var = statistics.variance(DATASET_01)
    return result_lib_smpl_var
### Library Sample Variance ### ---------------------------------------------------------------------------------------------
# Formula for Standard Deviation
### User Population Standard Deviation ### ---------------------------------------------------------------------------------------------

def user_population_standard_deviation():
    global POPULATION_Variance_TOTAL
    POPULATION_Variance_TOTAL = user_population_variance()
    pop_sigma = math.sqrt(POPULATION_Variance_TOTAL ** 2)
    return pop_sigma

### User Population Standard Deviation ### ---------------------------------------------------------------------------------------------
### User Sample Standard Deviation ### ---------------------------------------------------------------------------------------------
def user_sample_standard_deviation():
    global SAMPLE_Variance_TOTAL
    SAMPLE_Variance_TOTAL = user_sample_variance()
    sample_s = math.sqrt(POPULATION_Variance_TOTAL ** 2)
    return sample_s
### User Sample Standard Deviation ### ---------------------------------------------------------------------------------------------
### Library Population Standard Deviation ### ---------------------------------------------------------------------------------------------
def library_population_standard_deviation():
    lib_pop_sigma = statistics.pstdev(DATASET_01)
    return lib_pop_sigma
### Library Population Standard Deviation ### ---------------------------------------------------------------------------------------------
### Library Sample Standard Deviation ### ---------------------------------------------------------------------------------------------
def library_sample_standard_deviation():
    lib_sample_s = statistics.stdev(DATASET_01)
    return lib_sample_s
### Library Sample Standard Deviation ### ---------------------------------------------------------------------------------------------
### Weighted Mean ### ---------------------------------------------------------------------------------------------
MEAN_EXAMPLE = [2,4,6,8,10]
def weighted_mean():

    weighted_mean_dividend = 0
    weighted_mean_divisor = 0
    total_weighted_mean = 0
    current_dataset_value = 0
    current_mean_example_value = 0

    x = numpy.average(DATASET_01, MEAN_EXAMPLE)
    print(x)

    # weighted_mean_dividend = math.fsum([DATASET_01[i] * MEAN_EXAMPLE[i] for i in range(len(DATASET_01)))]
    # for w in DATASET_01:
    #     current_dataset_value = w
    #     # print(current_dataset_value)
    #     for x in MEAN_EXAMPLE:
    #         current_mean_example_value = x
    #         # print(current_mean_example_value)
    #         weighted_mean_dividend += current_dataset_value * current_mean_example_value
    # print(weighted_mean_dividend)
    #
    # for wi in MEAN_EXAMPLE:
    #     weighted_mean_divisor += wi
    # print(weighted_mean_divisor)




    # return total_weighted_mean
### Weighted Mean ### ---------------------------------------------------------------------------------------------


# t o d o
# weighted mean function
# Mode Function (return message of Mode, Bi-Modal, or no mode)

# truncated function
# Quartiles function          add if check for even or odd number of values
# IQR function
# range function

# Median Function








### FINAL RUN ### ---------------------------------------------------------------------------------------------
# print("\n")
# print(user_population_variance())
# print("\n")
# print(user_sample_variance())
# print("\n")
# print(library_population_variance())
# print("\n")
# print(library_sample_variance())
# print("\n")
# print(user_population_standard_deviation())
# print("\n")
# print(user_sample_standard_deviation())
# print("\n")
# print(library_population_standard_deviation())
# print("\n")
# print(library_sample_standard_deviation())
print(weighted_mean())



# print(POPULATION_MEAN_TOTAL)

