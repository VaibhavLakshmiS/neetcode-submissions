from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific_reachable = set()
        atlantic_reachable = set()

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        def bfs(queue, visited):
            while queue:
                row, col = queue.popleft()

                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change

                    # Check if the new cell is inside the grid
                    if (
                        new_row < 0
                        or new_row >= rows
                        or new_col < 0
                        or new_col >= cols
                    ):
                        continue

                    # Do not visit the same cell again
                    if (new_row, new_col) in visited:
                        continue

                    # Moving backwards from ocean:
                    # we can only move to an equal or higher cell
                    if heights[new_row][new_col] < heights[row][col]:
                        continue

                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))

        pacific_queue = deque()
        atlantic_queue = deque()

        # Top row touches Pacific
        # Bottom row touches Atlantic
        for col in range(cols):
            pacific_queue.append((0, col))
            pacific_reachable.add((0, col))

            atlantic_queue.append((rows - 1, col))
            atlantic_reachable.add((rows - 1, col))

        # Left column touches Pacific
        # Right column touches Atlantic
        for row in range(rows):
            pacific_queue.append((row, 0))
            pacific_reachable.add((row, 0))

            atlantic_queue.append((row, cols - 1))
            atlantic_reachable.add((row, cols - 1))

        bfs(pacific_queue, pacific_reachable)
        bfs(atlantic_queue, atlantic_reachable)

        answer = []

        for row in range(rows):
            for col in range(cols):
                if (
                    (row, col) in pacific_reachable
                    and (row, col) in atlantic_reachable
                ):
                    answer.append([row, col])

        return answer