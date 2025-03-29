arr = ["appa", "sunny", "theo", "monggi"]

#access element by index
cat = arr[1]
#find index using element
cat_index = arr.index("sunny")
#display output
print(f"\nAccessing:\n{cat} at location {cat_index}\n")

#modify
print("\nModify: ")
print(f"Original array: {arr} ")
#modify index
arr[3] = "seulpi"
print(f"Modified array: {arr}")
print()

arr = [20, 30, 40, 50, 60, 70, 80, 90]
num = arr[6]
print(num)