radius = float(input())

def sphere_volume(radius) -> float:
    return (4/3) * 3.14159 * (radius**3)

print(f"VOLUME = {sphere_volume(radius):.3f}")