# Usage

```py
start = (3, 3)
end = (1, 2)

matrix = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', '0', '2', '0', '0', '0', 'x'],
    ['x', '0', 'x', '0', 'x', '0', 'x'],
    ['x', '0', 'x', '0', 'x', '0', 'x'],
    ['x', '0', '0', '1', 'x', '0', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
]

matrix, route = find_path(matrix, start, end)
```