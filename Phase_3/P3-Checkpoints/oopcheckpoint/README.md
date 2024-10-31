## Object Oriented Programming

In this exercise you will primarily be exploring a Pokemon dataset. Pokemon are fictional creatures from the [Nintendo franchise](https://en.wikipedia.org/wiki/Pok%C3%A9mon) of the same name.

Some Pokemon facts that might be useful:
* The word "pokemon" is both singular and plural. You may refer to "one pokemon" or "many pokemon".
* Pokemon have attributes such as a name, weight, and height.
* Pokemon have one or multiple "types". A type is something like "electric", "water", "ghost", or "normal" that indicates the abilities that pokemon may possess.
* The humans who collect pokemon are called "trainers".

As a pokemon trainer we want to make sure our pokemon are performing at their peak. To measure this, we want to calculate a pokemon's Body Mass Index (or BMI). This is a statistic calculated using the pokemon's height and weight. 

To help with this task we we will create Pokemon objects that methods can be called on. 

You'll be working with following dictionaries to create the `Pokemon` objects


```python
# Run this cell without changes
bulbasaur_data = {
    "name": 'bulbasaur',
    "weight": 69,
    "height": 7,
    "base_experience": 64,
    "types": ["grass", "poison"]
}
charmander_data = {
    "name": 'charmander',
    "weight": 85,
    "height": 6,
    "base_experience": 62,
    "types": ["fire"]
}
squirtle_data = {
    "name": 'squirtle',
    "weight": 90,
    "height": 5,
    "base_experience": 63,
    "types": ["water"]
}
```

### 1. Creating a Class

Create a class called `Pokemon` with an `__init__` method. 

Along with the necessary `self` parameter, the `__init__` method should 
take in `data` as a parameter.

With the idea that one of the dictionaries above will be passed in as `data`, 
assign these specific attributes within the `__init__` method:
 
* `name` : value from the 'name' key of the dictionary passed in `data`
* `weight`: value from the 'weight' key of the dictionary passed in `data`
* `height`: value from the 'height' key of the dictionary passed in `data`


```python
# Create your class below with the correct syntax, including an __init__ method.

# your code here
raise NotImplementedError
```


```python
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

# Pokemon should be a class that exists in this namespace
assert type(Pokemon) == type

```

    
### 2. Instantiating Objects

Using the `bulbasaur_data`, `charmander_data` and `squirtle_data` variables, create the corresponding pokemon objects.


```python
# Replace None with appropriate code

bulbasaur = None
charmander = None
squirtle = None

# your code here
raise NotImplementedError

# This code will test your implementation. Make sure the values printed
# match the dictionaries above!
def print_pokeinfo(pkmn):
    print('Name: ' + pkmn.name)
    print('Weight: ' + str(pkmn.weight))
    print('Height: ' + str(pkmn.height))
    print('\n')
    
print_pokeinfo(bulbasaur)
print_pokeinfo(charmander)
print_pokeinfo(squirtle)
```


```python
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

assert type(bulbasaur) == Pokemon
assert type(charmander) == Pokemon
assert type(squirtle) == Pokemon

```

### 3. Update an instance attribute

Using the charmander instance, increase the weight attribute by 5. 


```python
# your code here
raise NotImplementedError
```


```python
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

```

### 4. Instance Methods

Re-write the class `Pokemon` below, so that it has an instance method called `bmi` that calculates the BMI of a Pokemon.

BMI is defined by the formula: $\frac{weight}{height^{2}}$ 

The BMI should be calculated with weight in **kilograms** and height in **meters**. 

The height and weight data of Pokemon from the dictionaries above is in **decimeters** and **hectograms**, respectively. 

You will have to convert the given values of height and weight to kilograms and meters to make the BMI calculations correct.

For your convenience, here are the conversions:

```
1 decimeter = 0.1 meters
1 hectogram = 0.1 kilograms
```

**Don't forget**: since you are changing the `Pokemon` class, you will have to create **new objects** of this **new class**. 

If you use the objects created by the first class you wrote, they will not have the `bmi` instance!

You can assign these new objects the same names as you assigned the old ones:
`bulbasaur`, `charmander` and `squirtle`


```python
# Define the new Pokemon class here

# Replace None with appropriate code
bulbasaur = None
charmander = None
squirtle = None

# your code here
raise NotImplementedError

# This code will test your implementation
print(bulbasaur.bmi()) 
print(charmander.bmi()) 
print(squirtle.bmi()) 
```


```python
# PUT ALL WORK FOR THE ABOVE QUESTION ABOVE THIS CELL
# THIS UNALTERABLE CELL CONTAINS HIDDEN TESTS

# bulbasaur.bmi should be a method on an instance of type Pokemon
import types
assert type(bulbasaur.bmi) == types.MethodType
# bulbasaur.bmi() should return a floating point number
assert type(bulbasaur.bmi()) == float
```
