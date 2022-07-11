def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f"reverse: {fruit_list}")
    fruit_list.append("orange")
    print(f"reverse: {fruit_list}")
    index = fruit_list.index("apple")
    fruit_list.insert(index, "cherry")
    print(fruit_list)
    print(fruit_list.pop())
    fruit_list.sort()
    print(fruit_list)
    fruit_list.clear()
    print(fruit_list)


main()
