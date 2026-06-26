### Python Showcase Statistics Methods ###
print("Beginning of the Python Statistics Methods Showcase\n\n\n")


print("Python has a built-in module that you can use to calculate mathematical statistics of"
      " numeric data. The statistics module was new in Python 3.4.")
import statistics



Statistics_Harmonic_Mean_def = ("Statistics Harmonic Mean: The statistics.harmonic_mean() method calculates the"
                                " harmonic mean (central location) of the given data set. "
                                "Harmonic mean = The reciprocal of the arithmetic mean() of the reciprocals"
                                " of the data. The harmonic mean is calculated as follows: If you have four values"
                                " (a, b, c and d) - it will be equivalent to 4 / (1/a + 1/b + 1/c + 1/d).")
print(f"\n{Statistics_Harmonic_Mean_def}")
print("    # Calculate harmonic mean")
print(f"        print(statistics.harmonic_mean([40, 60, 80])) ="
                    f" {statistics.harmonic_mean([40, 60, 80])}")
print(f"        print(statistics.harmonic_mean([10, 30, 50, 70, 90])) ="
                    f" {statistics.harmonic_mean([10, 30, 50, 70, 90])}")




Statistics_Mean_def = ("Statistics Mean: The statistics.mean() method calculates the mean (average) of "
                       "the given data set. "
                       "Tip: Mean = add up all the given values, then divide by how many values there are.")
print(f"\n{Statistics_Mean_def}")
print("    # Calculate average values")
print(f"        print(statistics.mean([1, 3, 5, 7, 9, 11, 13])) = {statistics.mean([1, 3, 5, 7, 9, 11, 13])}")
print(f"        print(statistics.mean([1, 3, 5, 7, 9, 11])) = {statistics.mean([1, 3, 5, 7, 9, 11])}")
print(f"        print(statistics.mean([-11, 5.5, -3.4, 7.1, -9, 22])) = {statistics.mean([-11, 5.5, -3.4, 7.1, -9, 22])}")




Statistics_Medium_def = "Statistics Medium: The statistics.median() method calculates the median (middle value) of the given data set. This method also sorts the data in ascending order before calculating the median. Tip: The mathematical formula for Median is: Median = {(Math_Comb_n + 1) / 2}th value, where Math_Comb_n is the number of values in a set of data. In order to calculate the median, the data must first be sorted in ascending order. The median is the number in the middle. Note: If the number of data values is odd, it returns the exact middle value. If the number of data values is even, it returns the average of the two middle values."
print(f"\n{Statistics_Medium_def}")
print("    # Calculate middle values")
print(f"        print(statistics.median([1, 3, 5, 7, 9, 11, 13])) = {statistics.median([1, 3, 5, 7, 9, 11, 13])}")
print(f"        print(statistics.median([1, 3, 5, 7, 9, 11])) = {statistics.median([1, 3, 5, 7, 9, 11])}")
print(f"        print(statistics.median([-11, 5.5, -3.4, 7.1, -9, 22])) = {statistics.median([-11, 5.5, -3.4, 7.1, -9, 22])}")




Statistics_Median_Grouped_def = ("Statistics Median Grouped: The statistics.median_grouped() method calculates the median of grouped continuous data, calculated as the 50th percentile. This method treats the data points as continuous data and calculates the 50% percentile median by first finding the median range using specified interval width (default is 1), and then interpolating within that range using the position of the values from the data set that fall in that range.\n"
                                 " Tip: The mathematical formula for Grouped Median is: GMedian = L + interval * (N / 2 - CF) / F.)\n"
                                 " L = The lower limit of the median interval\n"
                                 " interval = The interval width\n"
                                 " N = The total number of data points\n"
                                 " CF = The number of data points below the median interval\n"
                                 " F = The number of data points in the median interval")
print(f"\n{Statistics_Median_Grouped_def}")
print("    # Calculate the median of grouped continuous data")
print(f"        print(statistics.median_grouped([1, 2, 3, 4])) = {statistics.median_grouped([1, 2, 3, 4])}")
print(f"        print(statistics.median_grouped([1, 2, 3, 4, 5])) = {statistics.median_grouped([1, 2, 3, 4, 5])}")
print(f"        print(statistics.median_grouped([1, 2, 3, 4], 2)) = {statistics.median_grouped([1, 2, 3, 4], 2)}")
print(f"        print(statistics.median_grouped([1, 2, 3, 4], 3)) = {statistics.median_grouped([1, 2, 3, 4], 3)}")
print(f"        print(statistics.median_grouped([1, 2, 3, 4], 5)) = {statistics.median_grouped([1, 2, 3, 4], 5)}")




Statistics_Median_High_def = "Statistics Median High: The statistics.median_high() method calculates the high median of the given data set. This method also sorts the data in ascending order before calculating the high median. Note: If the number of data values is odd, it returns the exact middle value. If the number of data values is even, it returns the larger of the two middle values."
print(f"\n{Statistics_Median_High_def}")
print("    # Calculate the high middle values")
print(f"        print(statistics.median_high([1, 3, 5, 7, 9, 11, 13])) = {statistics.median_high([1, 3, 5, 7, 9, 11, 13])}")
print(f"        print(statistics.median_high([1, 3, 5, 7, 9, 11])) = {statistics.median_high([1, 3, 5, 7, 9, 11])}")
print(f"        print(statistics.median_high([-11, 5.5, -3.4, 7.1, -9, 22])) = {statistics.median_high([-11, 5.5, -3.4, 7.1, -9, 22])}")




Statistics_Median_Low_def = "Statistics Median Low: The statistics.median_low() method calculates the low median of the given data set. This method also sorts the data in ascending order before calculating the low median. Note: If the number of data values is odd, it returns the exact middle value. If the number of data values is even, it returns the smaller of the two middle values."
print(f"\n{Statistics_Median_Low_def}")
print("    # Calculate the low middle values")
print(f"        print(statistics.median_low([1, 3, 5, 7, 9, 11, 13])) = {statistics.median_low([1, 3, 5, 7, 9, 11, 13])}")
print(f"        print(statistics.median_low([1, 3, 5, 7, 9, 11])) = {statistics.median_low([1, 3, 5, 7, 9, 11])}")
print(f"        print(statistics.median_low([-11, 5.5, -3.4, 7.1, -9, 22])) = {statistics.median_low([-11, 5.5, -3.4, 7.1, -9, 22])}")




Statistics_Mode_def = "Statistics Mode: The statistics.mode() method calculates the mode (central tendency) of the given numeric or nominal data set."
print(f"\n{Statistics_Mode_def}")
print("    # Calculate the mode")
print(f"        print(statistics.mode([1, 3, 3, 3, 5, 7, 7, 9])) = {statistics.mode([1, 3, 3, 3, 5, 7, 7, 9])}")
print(f"        print(statistics.mode([1, 1, -3, 3, 7, -9])) = {statistics.mode([1, 1, -3, 3, 7, -9])}")
print(f"        print(statistics.mode(['red', 'green', 'blue', 'red'])) = {statistics.mode(['red', 'green', 'blue', 'red'])}")




Statistics_PopulationStandardDeviation_def = "Statistics Population Standard Deviation: The statistics.pstdev() method calculates the standard deviation from an entire population. Standard deviation is a measure of how spread out the numbers are. A large standard deviation indicates that the data is spread out, - a small standard deviation indicates that the data is clustered closely around the mean. Tip: Standard deviation is (unlike the Variance) expressed in the same units as the data. Tip: Standard deviation is the square root of sample variance. Tip: To calculate the standard deviation from a sample of data, look at the statistics.stdev() method. "
print(f"\n{Statistics_PopulationStandardDeviation_def}")
print("    # Calculate the standard deviation from an entire population")
print(f"        print(statistics.pstdev([1, 3, 5, 7, 9, 11])) = {statistics.pstdev([1, 3, 5, 7, 9, 11])}")
print(f"        print(statistics.pstdev([2, 2.5, 1.25, 3.1, 1.75, 2.8])) = {statistics.pstdev([2, 2.5, 1.25, 3.1, 1.75, 2.8])}")
print(f"        print(statistics.pstdev([-11, 5.5, -3.4, 7.1])) = {statistics.pstdev([-11, 5.5, -3.4, 7.1])}")
print(f"        print(statistics.pstdev([1, 30, 50, 100])) = {statistics.pstdev([1, 30, 50, 100])}")




Statistics_Standard_Deviation_def = "Statistics Standard Deviation: Definition and Usage. The statistics.stdev() method calculates the standard deviation from a sample of data. Standard deviation is a measure of how spread out the numbers are. A large standard deviation indicates that the data is spread out, - a small standard deviation indicates that the data is clustered closely around the mean. Tip: Standard deviation is (unlike the Variance) expressed in the same units as the data. Tip: Standard deviation is the square root of sample variance. Tip: To calculate the standard deviation of an entire population, look at the statistics.pstdev() method. "





print(f"\n{Statistics_Standard_Deviation_def}")
print("    # Calculate the standard deviation from a sample of data")
print(f"        print(statistics.stdev([1, 3, 5, 7, 9, 11])) = {statistics.stdev([1, 3, 5, 7, 9, 11])}")
print(f"        print(statistics.stdev([2, 2.5, 1.25, 3.1, 1.75, 2.8])) = {statistics.stdev([2, 2.5, 1.25, 3.1, 1.75, 2.8])}")
print(f"        print(statistics.stdev([-11, 5.5, -3.4, 7.1])) = {statistics.stdev([-11, 5.5, -3.4, 7.1])}")
print(f"        print(statistics.stdev([1, 30, 50, 100])) = {statistics.stdev([1, 30, 50, 100])}")




Statistics_PopulationVariance_def = "Statistics Population Variance: The statistics.pvariance() method calculates the variance of an entire population. A large variance indicates that the data is spread out, - a small variance indicates that the data is clustered closely around the mean. Tip: To calculate the variance from a sample of data, look at the statistics.variance() method."
print(f"\n{Statistics_PopulationVariance_def}")
print("    # Calculate the variance of an entire population")
print(f"        print(statistics.pvariance([1, 3, 5, 7, 9, 11])) = {statistics.pvariance([1, 3, 5, 7, 9, 11])}")
print(f"        print(statistics.pvariance([2, 2.5, 1.25, 3.1, 1.75, 2.8])) = {statistics.pvariance([2, 2.5, 1.25, 3.1, 1.75, 2.8])}")
print(f"        print(statistics.pvariance([-11, 5.5, -3.4, 7.1])) = {statistics.pvariance([-11, 5.5, -3.4, 7.1])}")
print(f"        print(statistics.pvariance([1, 30, 50, 100])) = {statistics.pvariance([1, 30, 50, 100])}")




Statistics_Variance_def = "Statistics Variance: The statistics.variance() method calculates the variance from a sample of data (from a population). A large variance indicates that the data is spread out, - a small variance indicates that the data is clustered closely around the mean. Tip: To calculate the variance of an entire population, look at the statistics.pvariance() method."
print(f"\n{Statistics_Variance_def}")
print("    # Calculate the variance from a sample of data")
print(f"        print(statistics.variance([1, 3, 5, 7, 9, 11])) = {statistics.variance([1, 3, 5, 7, 9, 11])}")
print(f"        print(statistics.variance([2, 2.5, 1.25, 3.1, 1.75, 2.8])) = {statistics.variance([2, 2.5, 1.25, 3.1, 1.75, 2.8])}")
print(f"        print(statistics.variance([-11, 5.5, -3.4, 7.1])) = {statistics.variance([-11, 5.5, -3.4, 7.1])}")
print(f"        print(statistics.variance([1, 30, 50, 100])) = {statistics.variance([1, 30, 50, 100])}")



print("\n\n\nEnd of the Python Statistics Methods Showcase")

