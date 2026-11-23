length = float(input("Length (ft): "))
width = float(input("Width (ft): "))
thickness = float(input("Thickness inch me: "))

volume_cft = length * width * (thickness/12)
volume_m3 = volume_cft / 35.31

# M20 - 1:1.5:3
cement_bags = volume_m3 * 8
sand_cft = volume_m3 * 15.5
aggregate_cft = volume_m3 * 31

print("\n--- Result ---")
print(f"Concrete Volume: {volume_cft:.1f} CFT / {volume_m3:.2f} m3")
print(f"Cement: {cement_bags:.1f} bags")
print(f"Sand: {sand_cft:.1f} CFT")
print(f"Aggregate: {aggregate_cft:.1f} CFT")