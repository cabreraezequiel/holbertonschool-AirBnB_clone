# Holbertonschool-AirBnB_clone
![alt text](https://techcrunch.com/wp-content/uploads/2015/11/holberton-logo-horizontal.jpg)

# Description
This is a Team project in the Holberton school´s fundamental´s program.
This is the first step towards building a full web application clone of the AirBnB service. 

# Console
The console is a command line interpreter for data management.
New instances can be created, destroyed or information can be deployed.
The usage is limited to the commands below

# Usage
The console supports interactiva and non-interactive mode.
| Command | Description |
| --- | --- |
| help | Show documented commands |
| help \<command\> | Show help section for each command |
| EOF | exit the program |
| create | Creates a new instance of a class, saves it and prints id |
| count | Retrive the number of instances of a class |

Non-interactive mode 
```
$ echo "create BaseModel" | ./console.py
(hbnb) 27eb1663-0e90-4475-b304-d3b9e5404378
```
# Models
| File | Class name | attributes |
| --- | --- | --- |
| base_model.py | Base class for every other class to inherit | id, created_at, updated_at |
| user.py | User | email, password, first_name, last_name |
| state.py | State | name |
| city.py | City | state_id, name |
| amenity.py | Amenity | name |
| place.py | Place | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids |
| review.py | Review | place_id, user_id, text |

# Data management
### Storage
Through JSON serialization the dictionaries get saved in file.json
The flow of the Data storage is \<object\> -> to_dict() -> \<dictionary\> -> JSON dump -> \<json string\> -> FILE -> \<json string\> -> JSON loads -> \<dictionary\> -\> \<object\>
###Loading
The file.json gets read, a dictionary gets casted as each class instance.
The reload method is called by __init__.py

# Test
Unittest can be found here (add link)

### Feel free to use our console
Clone repository in a ubuntu base system.
```
$ clone https://github.com/cabreraezequiel/holbertonschool-AirBnB_clone
```

Execute the console.
```
./console.py
```

# Authors
Ezequiel Cabrera - ezequielcabrera2601@gmail.com
Agustin Labadie - labalabadie@gmail.com
