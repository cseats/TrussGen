import math
import matplotlib.pyplot as plt

def find_circle_line_intersection(x0, y0, r, y_line, plot=False):
    # Check if the horizontal line intersects the circle
    if abs(y_line - y0) > r:
        return False #"The line does not intersect the circle"
    
    # Calculate the x-coordinates of the intersection points
    x_diff = math.sqrt(r**2 - (y_line - y0)**2)
    
    x1 = x0 + x_diff
    x2 = x0 - x_diff
    
    intersection_points = (x1, y_line), (x2, y_line)
    
    if plot:
        # Plotting the circle
        circle = plt.Circle((x0, y0), r, color='blue', fill=False, label='Circle')
        
        fig, ax = plt.subplots()
        ax.add_patch(circle)
        
        # Plotting the horizontal line
        plt.axhline(y=y_line, color='red', linestyle='--', label='Horizontal Line')
        
        # Plotting the intersection points
        plt.plot([x1, x2], [y_line, y_line], 'go', label='Intersection Points')
        
        # Plot settings
        ax.set_aspect('equal', 'box')
        ax.set_xlim(x0 - r - 1, x0 + r + 1)
        ax.set_ylim(y0 - r - 1, y0 + r + 1)
        
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Circle and Line Intersection')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    return intersection_points

# Example usage
origin = (0, 0)
radius = 5
y_line = 3

intersection_points = find_circle_line_intersection(origin[0], origin[1], radius, y_line, plot=True)

# Print the intersection points
print(f"The intersection points are: {intersection_points}")
