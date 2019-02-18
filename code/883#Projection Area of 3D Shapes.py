def projectionArea(self, grid):
    return (sum(map(max, grid)) + sum(map(max, zip(*grid))) + sum(v > 0 for row in grid for v in row))