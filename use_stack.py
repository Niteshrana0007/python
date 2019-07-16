stack_data = []

def push(item):
    stack_data.append(item)

def peek():
    top_index = len(stack_data)
    top_element = stack_data[top_index]
    return top_element

def pop():
    if len(stack_data)==0:
        return None
    top_index = len(stack_data)-1
    top_element = stack_data[top_index]
    del stack_data[top_index]
    return top_element
