from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favorite_colours = defaultdict(list)

for name, colour in colours:
    favorite_colours[name].append(colour)

print(favorite_colours)