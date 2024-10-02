import matplotlib.pyplot as plt
import numpy as np
import math

def find_intersection(x0, y0, r0, x1, y1, r1):
    # Calculate the distance between the centers
    d = np.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    
    # Check if the circles intersect
    if d > r0 + r1:
        # print("Case 1")
        return [False, False]  #"The circles do not intersect"
    elif d < abs(r0 - r1):
        # print("Case 2")
        return [False, False]  #"One circle is contained within the other"
    elif d == 0 and r0 == r1:
        # print("Case 3")
        return [False, False]  #"The circles are coincident"
    
    # Calculate the intersection points
    a = (r0**2 - r1**2 + d**2) / (2 * d)
    h = np.sqrt(r0**2 - a**2)
    
    x2 = x0 + a * (x1 - x0) / d
    y2 = y0 + a * (y1 - y0) / d
    
    x3 = x2 + h * (y1 - y0) / d
    y3 = y2 - h * (x1 - x0) / d
    
    x4 = x2 - h * (y1 - y0) / d
    y4 = y2 + h * (x1 - x0) / d

    if x3<0 and x4<0:
        return [x3, y3], [x4, y4]
    if x3<0:
        return [[x3, y3],False]
    if x4<0:
        return [[x4, y4],False]
    
    
    return [False, False]

def plot_circles(x0, y0, r0, x1, y1, r1, intersection_points=None):
    fig, ax = plt.subplots()
    
    # Circle 1
    circle1 = plt.Circle((x0, y0), r0, color='blue', fill=False)
    ax.add_patch(circle1)
    
    # Circle 2
    circle2 = plt.Circle((x1, y1), r1, color='red', fill=False)
    ax.add_patch(circle2)
    
    # Intersection points
    if intersection_points:
        for point in intersection_points:
            ax.plot(point[0], point[1], 'go')  # Green dots for intersection points
    
    ax.set_aspect('equal', 'box')
    ax.set_xlim(min(x0 - r0, x1 - r1) - 1, max(x0 + r0, x1 + r1) + 1)
    ax.set_ylim(min(y0 - r0, y1 - r1) - 1, max(y0 + r0, y1 + r1) + 1)
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Intersection of Two Circles')
    plt.grid(True)
    plt.show()


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
        
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        
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


def find_circle_line_intersection(x0, y0, r, y_line, plot=False):
    # Check if the horizontal line intersects the circle
    if abs(y_line - y0) > r:
        return [False,False] #"The line does not intersect the circle"
    
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
    
    if x2<0 and x1<0:
        [[x1,y_line],[x2, y_line]]
    if x2<0:
        return [[x2, y_line],False]#intersection_points
    if x1<0:
        return [[x1,y_line], False]
    return[False,False]

# Input circle parameters
# x0, y0, r0 = 0, 0, 5  # Circle 1: Center (0, 0), Radius 5
# x1, y1, r1 = 7, 0, 3  # Circle 2: Center (4, 0), Radius 3

# # Find intersection points
# intersection_points = find_intersection(x0, y0, r0, x1, y1, r1)

# # Print the intersection points
# if isinstance(intersection_points, str):
#     print(intersection_points)
# else:
#     print(f"The circles intersect at points: {intersection_points}")

# # Plot the circles and their intersection points
# plot_circles(x0, y0, r0, x1, y1, r1, intersection_points if not isinstance(intersection_points, str) else None)

def flat_line_2_force(x1,x2,stock):

    delta = abs(x1 - x2)
    maxUt = 0
    for e in stock:
        curUt = delta/e

        if curUt<=1 and curUt>0.2 and curUt>maxUt:
            maxUt = curUt
            elMaxUt = e


        
    if maxUt == 0:
        return [False, False]
    
    return [maxUt, elMaxUt]

def circle_intersections(x, origin, radius):
    h, k = origin
    # Check if the x value is within the range of the circle
    if abs(x - h) > radius:
        return [False,False]  # No intersection
    
    # Calculate y values
    y_offset = math.sqrt(radius**2 - (x - h)**2)
    y1 = k + y_offset
    y2 = k - y_offset
    
    # Return the intersection points
    return [(x, y1), (x, y2)]


def removeDups(data):
    singleDesigns = {}
    for k,v in data.items():
        m = []
        memData = v['memberInfo']
        for i in range(1,len(memData)+1):
            m.append(memData[i]['slope'])
        
        
        if len(singleDesigns)>1:
            newDesign = True
            for d,md in singleDesigns.items():
                if m == md: 
                    newDesign = False
                    data[k]['designNumber'] = d
            if newDesign:
                singleDesigns[k] = m      
            
        else:
            singleDesigns[k] = m
    
    return singleDesigns, data