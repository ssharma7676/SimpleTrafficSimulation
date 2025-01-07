Traffic Flow Simulation

This project simulates traffic flow on a straight road, visualizing the movement of cars with dynamically adjusted speeds based on proximity to other cars and speed limits.
The simulation features two real-time graphs:
1. Car Positions on the Road
2. Average Speed Over Time


Features
* Simulates 20 cars moving at random speeds, constrained by:
    * Maximum speed: 90 mph
    * Minimum speed: 20 mph
    * Speed limit: 60 mph
* Cars dynamically accelerate or decelerate to maintain safe distances
* Real-time visualization:
    * Graph 1: Displays car positions on the road with annotated markers
    * Graph 2: Tracks the average speed over time


Simulation Details
1. Initialization:
    * Cars are evenly spaced on the road, starting at the speed limit
    * Movement is calculated as speed × time, with adjustments for safety
2. Dynamic Behavior:
    * Acceleration: Cars increase speed randomly when conditions allow
    * Deceleration: Cars slow down if too close to the vehicle ahead
    * Speeds are continuously adjusted to stay within defined limits

  
Dependencies
* Python 3.x
* Matplotlib (install using pip install matplotlib)


Ideas for Improvement
* Introduce traffic lights or stop signs
* Simulate multi-lane roads with lane-switching
