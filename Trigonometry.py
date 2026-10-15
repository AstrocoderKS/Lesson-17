import math

print("📐 Marina's Simple Multi-Angle Calculator 📐")
print("Enter 3 different angles to find their Sine, Cosine, and Tangent.\n")

# Collect 3 angles directly
angle1 = float(input("Enter the 1st angle: "))
angle2 = float(input("Enter the 2nd angle: "))
angle3 = float(input("Enter the 3rd angle: "))

# Put them in a list to loop through easily
all_angles = [angle1, angle2, angle3]

print("\n========================================")
print("📊 YOUR MATHEMATICAL RESULTS:")
print("========================================")

for angle in all_angles:
    # Convert to radians because python math needs it
    rads = math.radians(angle)
    cos_val = math.cos(rads)
    
    print(f"\n📈 Results for {angle}°:")
    print(f"  -> Sine: {round(math.sin(rads), 4)}")
    print(f"  -> Cosine: {round(cos_val, 4)}")
    
    # Simple check to stop 90 or 270 degrees from crashing tangent
    if abs(cos_val) < 0.00001:
        print("  -> Tangent: Undefined (Error!)")
    else:
        print(f"  -> Tangent: {round(math.tan(rads), 4)}")

print("\n========================================")
print("👋 Done! Have a good day!")