# SKWiki

SK Wiki is an library that gets information about weapons/helm/armor/shield from Spiral Knights wiki.

## Usage
```python
# first you import the library
from SK_Wiki import *
	
# first you make a request to the wiki using the class Gear()
Item = Gear("chaos cloak")
	
# To get the Item description you use the description method
Item.Description() 
>>> "A forbidden mantle said to grant the wearer protection within the nameless realm where all elements are said to converge into one and divide into all."

# To get the equipped item image you use the Image() method
Item.Image()
>>> "https://media3.spiralknights.com/wiki-images/6/6f/Chaos_Cloak-Equipped.png"
	
# To get the item status you can use the Status() method
Item.Status()
>>> "https://media3.spiralknights.com/wiki-images/8/8a/Equipment-Chaos_Cloak_Stats.png"

# You can also get the item tier (it's the number of stars)
Item.Tier()
>>> "★★★★★"
```
