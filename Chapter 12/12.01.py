enemies = 1

def increase_enemies():
    enemies = 2
    print(enemies)
    print(id(enemies))

increase_enemies()
print(enemies)
print(id(enemies))