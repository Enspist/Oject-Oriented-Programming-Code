def fare_calculator(klicks):
    """This function will generate the fare for a bus ride based on the distance traveled
    The base fare is 4 dollars and then .25 will be added for every 140 meters traveled. 

    Args:
        klicks (int): This is the amount of Kilometers traveled. 

    Returns:
        string: The total fare is returned with a short note.
    """
    base_fare = 4.00
    meters = klicks * 1000
    
    meters_fare = meters / 140
    
    calculated_fare = base_fare + (meters_fare * .25)
    
    final_fare = '%.2f' % calculated_fare
    
    return f"Your fare is ${final_fare}"


print(fare_calculator(1.4))