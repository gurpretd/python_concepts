from typing import Union

# myVar accepts both integers and strings
newVar: Union[int, str]
newVar = 5
newVar = "I am string"

from typing import List, Union

# Can assign both integer and string to the list.
mylist: List[Union[int, str]] = ["a", 1, "b", 2]
