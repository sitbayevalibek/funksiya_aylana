# Aylanaga doir funksiya
def funksiya_aylana(radius,pi=3.14):
    aylana = {"radius":radius,
              "diametr":2*radius,
              "perimetr":2*radius*pi,
              "yuza":pi*radius**2}
    return aylana


j = funksiya_aylana(5)

print(f"Radius: {j['radius']:.2f}")
print(f"Diametr: {j['diametr']:.2f}")
print(f"Perimetr: {j['perimetr']:.2f}")
print(f"Yuza: {j['yuza']:.2f}")
