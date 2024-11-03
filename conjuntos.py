
x = [1,2,3,1,2,3,1,2,3]
set(x)
# {1, 2, 3} 
y = [1, 1, 6, 6, 6, 6, 6, 8, 8]
set(y)
# {1, 6, 8}
z = [("Bird", "Cat", "Dog", "Dog", "Bird", "Bird")]
set(z)
# {('Bird', 'Cat', 'Dog', 'Dog', 'Bird', 'Bird')}


animals = set(["Cow", "Fish", "Pig", "Horse"])
animals.add ("Cat")
print (animals)
# {'Pig', 'Cow', 'Cat', 'Fish', 'Horse'}