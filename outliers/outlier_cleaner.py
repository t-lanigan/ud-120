#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    removal_percentage = 0.1

    cleaned_data = []



    for i in range(len(ages)):
        error = abs(predictions[i][0] - net_worths[i][0]) 
        cleaned_data.append((ages[i][0],net_worths[i][0],error))

    #sorts the data form the 2 index of each tuple in the list.
    cleaned_data.sort(key=lambda tup: tup[2])

    #removes the top removal_percentage
    for i in range(int(len(cleaned_data)*removal_percentage)):
        cleaned_data.pop()


    for i in range(len(cleaned_data)):
        print cleaned_data[i]



    return cleaned_data

