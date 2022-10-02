def segment_length(x1, y1, x2, y2):
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return length


def rectangle_perimeter(coordinates):
    perimeter = segment_length(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
    perimeter += segment_length(coordinates[2], coordinates[3], coordinates[4], coordinates[5])
    perimeter += segment_length(coordinates[4], coordinates[5], coordinates[6], coordinates[7])
    perimeter += segment_length(coordinates[6], coordinates[7], coordinates[0], coordinates[1])

    return perimeter


nums = [float(num) for num in input('Enter coordinates: ').split()]
print(rectangle_perimeter(nums))
