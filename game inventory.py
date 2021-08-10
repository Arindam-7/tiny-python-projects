stuffs = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory: ")
    total = 0
    for i, j in inventory.items():
        print(str(j) + ' ' + i)
        total += j
    print("Total number of items: " + str(total))

def addToInventory(inventory, addedItems):
    for loot in addedItems:
        if loot not in inventory:
            inventory[loot] = 1
        else:
            inventory[loot] += 1
    return inventory

stuffs = addToInventory(stuffs, dragonLoot)
displayInventory(stuffs)
