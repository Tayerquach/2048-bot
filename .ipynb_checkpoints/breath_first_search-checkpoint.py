from queue import Queue

adj = {
    'u': ['v', 'x'],
    'x': ['u', 'v', 'y'],
    'v': ['u', 'x', 'y'],
    'y': ['w'],
    'w': ['y', 'z'],
    'z': ['w']
    }

visited = {}
level = {}
parent = {}
traversal_output = []
queue = Queue()