import math

def get_valid_input(prompt: str) -> float:
    """Safely prompts the user for a numeric angle in degrees."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid numerical value.")

def display_trig_results(degrees: float):
    """Calculates and prints standard and inverse trigonometric functions."""
    radians = math.radians(degrees)
    sin_val = math.sin(radians)
    cos_val = math.cos(radians)
    
    print(f"\n======================================")
    print(f"📊 TRIGONOMETRIC RESULTS FOR {degrees}°")
    print(f"======================================")
    print(f" • Radians      : {radians:.4f} rad")
    print(f" • Sine (sin)   : {sin_val:.4f}")
    print(f" • Cosine (cos) : {cos_val:.4f}")
    
    # Safely handle the mathematical asymptote for Tangent (e.g., 90°, 270°)
    if math.isclose(cos_val, 0, abs_tol=1e-9):
        print(" • Tangent (tan) : Undefined (Asymptote)")
    else:
        print(f" • Tangent (tan) : {math.tan(radians):.4f}")
        
    print(f"--------------------------------------")
    print(f"🔄 INVERSE FUNCTIONS (Outputs in Degrees)")
    print(f"--------------------------------------")
    
    # Arcsine is only defined between -1 and 1
    if -1 <= degrees <= 1:
        print(f" • Arcsine (asin)   : {math.degrees(math.asin(degrees)):.2f}°")
        print(f" • Arccosine (acos) : {math.degrees(math.acos(degrees)):.2f}°")
    else:
        print(" • Arcsine (asin)   : Undefined (Input must be between -1 and 1)")
        print(" • Arccosine (acos) : Undefined (Input must be between -1 and 1)")
        
    print(f" • Arctangent (atan): {math.degrees(math.atan(degrees)):.2f}°")
    print(f"======================================\n")

def main():
    print("📐 Welcome to Harina's Advanced Trig Calculator 📐")
    while True:
        angle = get_valid_input("Enter an angle/value: ")
        display_trig_results(angle)
        
        # Check if user wants to calculate another angle
        choice = input("Calculate another angle? (y/n): ").strip().lower()
        if choice != 'y':
            print("\n👋 Goodbye! Happy math learning!")
            break

if __name__ == "__main__":
    main()