import math


def main():
    """Main program that calls two funcions
    and print the results values
    Parameters
        Nothing
    Return
        Nothing
    """
    # Definitions of variables names, raiuds and height of cans.
    storage_efficiencies = []
    name_cans = ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder',
                 '#5', '#6Z', '#8Z short', '#10', '#211', '#300', '#303']
    radius_cans = [6.83, 7.78, 8.73, 10.32, 10.79,
                   13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    height_cans = [10.16, 11.91, 11.59, 11.91, 17.78,
                   14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    for i in range(len(name_cans)):
        print(name_cans[i] + ' ' + str(round(compute_volume(radius_cans[i], height_cans[i]
                                                            )/compute_surface_area(radius_cans[i], height_cans[i]), 1)))


def compute_volume(radius, height):
    """Compute the volume of a can.
    Parameters
        radius: The radius of a can.
        height: The volume of a can.
    Return
        volume: The volume of a can."""
    return math.pi * (radius*radius) * height


def compute_surface_area(radius, height):
    """Compute the surface area of a can.
    Parameters
        radius: The radius of a can.
        height: The volume of a can.
    Return
        area: The area of a can."""
    return 2 * math.pi * radius * (radius + height)


# Call to main function
main()
