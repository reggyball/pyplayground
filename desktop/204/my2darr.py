class array_2d:
    def __init__(self, rows, cols, def_value = "-"):
        self.rows = rows
        self.cols = cols
        self.def_value = def_value
        self.array = [[def_value for _ in range(cols)] for _ in range(rows)]

    def validate(self, row, col):                                                          #to check if indicated row and col are within the initialized 2d array
        if not(0 <= row < self.rows and 0 <= col < self.cols): 
            print("Position out of bounds")
            return False
        else:
            return True

    def set(self, row, col, value):                                     #update/inserts data in defined coordinate
        if self.validate(row, col) == True:
            self.array[row][col] = value

    def delete(self, row, col):                                     #resets value of specified cell given the coordinate
        self.set(row, col, self.def_value)
    
    def get_val(self, row, col):                                        #returns the value of a specific cell in given the coordinate
        if self.validate(row, col) == True:
            return f"{self.array[row][col]}"


    def search(self, target):                                           #returns the coordinates, given the data
       for row_index, row in enumerate(self.array):
        for col_index, value in enumerate(row):
            if value == target:
                return row_index, col_index                                   #f"{target} found at {row_index}, {col_index}" 
        return None

    def display(self):                                              #prints current 2d array
        for row in self.array:
            print((" ").join([str(val) for val in row]))

catcafe = array_2d(4, 4)
catcafe.display()

catcafe.set(0, 0, "Appa") 
catcafe.set(0, 1, "Feb/18")
catcafe.set(0, 2, "8hrs")
catcafe.set(0, 3, "Fish")           
catcafe.display()

catcafe.set(1, 0, "Bunner")  
catcafe.display()
catcafe.delete(1, 0)    
catcafe.display()

ax, ay = catcafe.search("Appa")
print(ax, ay)
print(f'''Appa worked for {catcafe.get_val(ax, 2)}  
        on {catcafe.get_val(ax, 1)}. 
        Reward him 
        with {catcafe.get_val(ax, 3)}!''')

