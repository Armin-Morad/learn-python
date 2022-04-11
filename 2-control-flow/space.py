# Space Boxer 🥊
# Sonny Li

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19

print("Your weight:", weight)


#The below could be an alternative solution to the question: (alternative code solution) ☟

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:

if planet == 1:
  print(0.91 * weight)
elif planet == 2:
  print(0.38 * weight)
elif planet == 3:
  print(2.34 * weight)
elif planet == 4:
  prnt(1.06 * weight)
elif planet == 5:
  print(0.92 * weight)
elif planet == 6:
  print(1.19 * weight) 
