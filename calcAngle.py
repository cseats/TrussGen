import math
import matplotlib.pyplot as plt

def calculate_counterclockwise_angle(origin, point, plot=False):
    # Unpack the coordinates
    x0, y0 = origin
    x1, y1 = point
    
    # Calculate the vector from the origin to the point
    dx = x1 - x0
    dy = y1 - y0
    
    # Calculate the angle from the positive x-axis
    angle_rad = math.atan2(dy, dx)
    
    # Convert the angle to degrees
    angle_deg = math.degrees(angle_rad)
    
    # Normalize the angle to the range [0, 360) for counterclockwise measurement
    if angle_deg < 0:
        angle_deg += 360
    
    counterclockwise_angle = angle_deg
    
    if plot:
        # Plot the origin and point
        plt.plot([x0, x1], [y0, y1], 'ro-', label='Vector')
        
        # Plot the positive x-axis for reference
        plt.plot([x0, x0 + 10], [y0, y0], 'b--', label='+X Axis')
        
        # Mark the origin and the point
        plt.text(x0, y0, 'Origin', fontsize=12, ha='right', color='black')
        plt.text(x1, y1, f'Point ({x1}, {y1})', fontsize=12, ha='right', color='black')
        
        # Add the angle arc
        angle_arc = plt.Circle((x0, y0), 1, color='green', fill=False, linestyle='-', linewidth=1.5)
        ax = plt.gca()
        ax.add_patch(angle_arc)
        
        plt.xlim(x0 - 1, x0 + max(dx, 10))
        plt.ylim(y0 - 1, y0 + max(dy, 10))
        
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'Counterclockwise Angle: {counterclockwise_angle:.2f}°')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True)
        plt.legend()
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()
    
    return counterclockwise_angle

# Example usage
origin = (6, 2)
point = (3, 4)

angle = calculate_counterclockwise_angle(origin, point, plot=True)

# Print the counterclockwise angle
print(f"The counterclockwise angle from +X to the point is: {angle:.2f}°")
