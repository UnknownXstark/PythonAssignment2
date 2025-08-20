from collections import deque

def snake_game(grid, start, directions, food):
    rows, cols = grid
    moves = {"U": (1,0), "D": (-1,0), "R": (0,1), "L": (0,-1)}

    snake = deque([start])
    body = set([start])

    for d in directions:
        head_rows, head_cols = snake[0]
        drows, dcols = moves[d]
        new_head = (head_rows + drows, head_cols + dcols)

        if not (0 <= new_head[0] < rows and 0 <= new_head[1] < cols):
            return "Game Over"
        
        tail = snake[-1]
        if new_head in body and new_head != tail:
            return "Game Over"
        
        snake.appendleft(new_head)
        body.add(new_head)

        if new_head in food:
            food.remove(new_head)
        else:
            removed = snake.pop()
            body.remove(removed)

    return list(snake)


grid = (5,5)
start = (2,2)
directions = ['U','U','R','D','D','L','L','U']
food = {(1,2), (2,3)}

print(snake_game(grid, start, directions, food))