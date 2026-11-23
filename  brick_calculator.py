length = float(input("Wall Length (ft): "))
height = float(input("Wall Height (ft): "))
thickness = float(input("Wall Thickness inch me (4.5 ya 9): "))

wall_area = length * height
wall_volume = wall_area * (thickness / 12)

brick_volume = (9/12) * (4/12) * (3/12)
bricks = wall_volume / brick_volume
bricks = bricks * 1.1  # 10% wastage

cement_bags = wall_volume * 0.15
sand_cft = wall_volume * 4

print("\n--- Result ---")
print(f"Bricks: {int(bricks)} nos")
print(f"Cement: {cement_bags:.1f} bags")
print(f"Sand: {sand_cft:.1f} CFT")