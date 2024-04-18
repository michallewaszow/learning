
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
#  1 5 10 10 5 1
import argparse

def entry(height: int) -> list[list[int]]:
    if height > 0:
        tree = []
        i = 1 
        return generate_tree_recursevily(i, height, tree)
    else:
        raise Exception('height must be positive number')

def generate_tree_recursevily(i: int, height: int, tree: list[list[int]]) -> list[list[int]]:
    if i == 1:
        tree.append([i])
        i += 1
        return generate_tree_recursevily(i, height, tree)
    elif i <= height:
        last_level = tree[-1]
        new_level = [1 if num == 0 or num == len(last_level) else sum(last_level[num-1:num+1]) for num in range(0, len(last_level)+1)]
        tree.append(new_level)
        i += 1
        return generate_tree_recursevily(i, height, tree)
    else:
        return tree

if __name__ == '__main__':
    print('lol')
    parser = argparse.ArgumentParser()
    parser.add_argument('-n')
    args = parser.parse_args()
    res = entry(int(args.n))
    print(res)
