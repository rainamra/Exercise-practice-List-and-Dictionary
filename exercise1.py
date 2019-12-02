#number 1
inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

#step 1 & 2
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

#step 3
inventory['backpack'].sort()
#or you can do
#for sort_backpack in inventory['backpack']:
    #inventory['backpack'] = sorted(inventory['backpack'])
    #break

#step 4
inventory['backpack'].remove('dagger')

#step 5
inventory['gold'] += 50
print(inventory)






