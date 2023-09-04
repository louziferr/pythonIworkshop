
def get_ages_churn_rate(data):
    # create two dictionaries
    # one contains the number of churner for each age
    # the other the number of customers for each age
    churn_number_by_age = {}
    customer_number_by_age = {}

    for customer in data:
        age = customer["Age"]
        exited = customer["Exited"]
        if age not in churn_number_by_age:
            churn_number_by_age[age] = exited
            customer_number_by_age[age] = 1
        else:
            churn_number_by_age[age] += exited
            customer_number_by_age[age] += 1

    # make a list of tuples (age, churn_rate) to be able to sort by age later
    churn_rates_by_age = []
    for age in churn_number_by_age.keys():
        churn_rate = churn_number_by_age[age] / customer_number_by_age[age]
        churn_rates_by_age.append((age, churn_rate))
        
    # sort the list by age (sort will automatically sort by the 0th tuple entry)
    churn_rates_by_age.sort()

    # seperate ages and churn rates into two lists
    ages = [x[0] for x in churn_rates_by_age]
    churn_rates = [x[1] for x in churn_rates_by_age]

    return ages, churn_rates