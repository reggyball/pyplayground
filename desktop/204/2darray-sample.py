class TwoDArray:
    def __init__(self, rows, cols, default_value=0):
        """Initialize a 2D array with given rows and cols, filled with default_value."""
        self.rows = rows
        self.cols = cols
        self.array = [[default_value for _ in range(cols)] for _ in range(rows)]

    def insert(self, row, col, value):
        """Inserts a value at a specific position in the 2D array."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.array[row][col] = value
        else:
            raise IndexError("Index out of bounds")

    def search(self, value):
        """Searches for a value in the 2D array and returns its position(s)."""
        positions = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.array[i][j] == value:
                    positions.append((i, j))
        return positions if positions else None  # Return None if not found

    def delete(self, row, col):
        """Deletes a value by resetting it to the default (e.g., 0) at the specified position."""
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.array[row][col] = 0  # Assuming 0 is the default "deleted" value
        else:
            raise IndexError("Index out of bounds")

    def display(self):
        """Prints the 2D array in a matrix format."""
        for row in self.array:
            print(" ".join(map(str, row)))
        print()

# Example Usage
matrix = TwoDArray(3, 3)  # Creates a 3x3 matrix with default value 0
matrix.insert(1, 1, 5)  # Insert 5 at position (1,1)
matrix.insert(0, 2, 7)  # Insert 7 at position (0,2)
matrix.display()

# Searching for a value
print("Searching for 5:", matrix.search(5))  # Output: [(1, 1)]
print("Searching for 7:", matrix.search(7))  # Output: [(0, 2)]
print("Searching for 9:", matrix.search(9))  # Output: None

# Deleting a value
matrix.delete(1, 1)
matrix.display()
