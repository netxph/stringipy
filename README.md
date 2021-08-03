# stringipy: developer utilities for strings


## What is it?

There are instances that you got a list over the internet, and you want to transform those strings so you can paste them easily in your code? Or you just want to make use this library to perform basic string transformation. **stringipy** got you covered.

**stringipy** is created guided with functional programming paradigms that can easily pipe operations in a single line of code.



## Main Features

* `FluentString` and `FluentStringList` handles the functional string operations
* Current features are `snake_case`, `prefix`, `suffix`, `join`... more to come
* This applies to both string and list of strings



## How to install

Library is available in Python Package Index (PyPI).

```bash
pip install stringipy
```



## Getting Started

Here's an example of how to perform and chain string operations.

```python
data = ["HelloDarkness", "MyOldFriend"]

FluentStringList(data) \
	.snake_case() \
	.prefix("\"") \
    .suffix("\"") \
    .join(", ") \
    .prefix("[") \
    .suffix("]") \
    .print()
```

Output

```
["hello_darkness", "my_old_friend"]
```



## Contributing

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

The library does not require much except for `pytest` and should work with the `python 3.x` versions. Feel free to send me a pull request or open an issue to discuss feature requests.

## License

MIT
