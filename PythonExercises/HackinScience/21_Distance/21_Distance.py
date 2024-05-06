def dist(points):
    smallest = min(points)
    largest = max(points)
    return largest - smallest

print(dist([1, 2, 3]))
print(dist([1, 2, 3, 2.5]))
print(dist([1, 2, 3, 2.5, 3.5]))
print(dist([1, 2, 3, 2.5, 3.5, 120]))
print(dist([1, 2, 3, 2.5, 3.5, 120, -1000]))

print("---------")

def manualDist(points):
    smallest = points[0]
    largest = 0
    for i in points:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    return largest - smallest

print(manualDist([1, 2, 3]))
print(manualDist([1, 2, 3, 2.5]))
print(manualDist([1, 2, 3, 2.5, 3.5]))
print(manualDist([1, 2, 3, 2.5, 3.5, 120]))
print(manualDist([1, 2, 3, 2.5, 3.5, 120, -1000]))