def is_unique(l):
    if len(l) == len(set(l)):
        return True
    return False

print(is_unique([1,5,5,7,9]))