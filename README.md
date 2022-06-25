# Record py

## Install
```shell
pip install git+https://github.com/AldieNightStar/record_py.git
```

## Usage
```python
from record import *

# Init namespace where to put data classes
record_init(globals(), locals())

# Create data class "Profile" with "name", "age", "inv" arguments
# Optional `extends` parameter leads to class which could be extended
record("Profile", "name", "age", "inv", extends=SuperProfile)

# The rest samples of record's use
record("Inv", "items", "size")
record("Spell", "name", "effectId")

# Create instances
p = Profile("Ihor", 18,
	Inv(["knife", "ball",
		Spell("fireball", 32)], 3)
)
```
