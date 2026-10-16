# Module for calculating paint labor costs

def galpaint(area):
    """Calculates the gallons of paint needed for a given area."""
    return area / 112
def paintcost(galpaint, price):
    """Calculates the cost of paint based on gallons and price per gallon."""
    return galpaint * price
def labortime(area):
    """Calculates the labor time needed for a given area."""
    return int((area / 112) * 8)
def laborcost(labortime):
    """Calculates the labor cost based on labor time and hourly rate."""
    return labortime * 35
def totalcost(paintcost, laborcost):
    """Calculates the total cost of paint and labor."""
    return paintcost + laborcost