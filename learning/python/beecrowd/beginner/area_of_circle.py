PI = 3.14159
R = input()
casted_R = float(R)
def area_of_circle(r: float):
    result = (r**2) * PI
    return round(result, 4)
print(f"A={area_of_circle(casted_R):.4f}")