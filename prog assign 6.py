# Paint Job Estimator
import paintlabor

print("What is the area you want to paint in square feet?")
area = float(input())
gallons = paintlabor.galpaint(area)
price = float(input("What is the price per gallon of paint? "))
paint_cost = paintlabor.paintcost(gallons, price)
labor_time = paintlabor.labortime(area)
labor_cost = paintlabor.laborcost(labor_time)
total_cost = paintlabor.totalcost(paint_cost, labor_cost)

print(f"Gallons of paint needed: {gallons:.2f}")
print(f"Cost of paint: ${paint_cost:.2f}")
print(f"Labor time needed: {labor_time} hours")
print(f"Labor cost: ${labor_cost:.2f}")
print(f"Total cost: ${total_cost:.2f}")