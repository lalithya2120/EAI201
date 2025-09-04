def get_turn_radius(shape):
    if shape == "round":
        return 1
    elif shape == "square":
        return 2
    elif shape == "triangle":
        return 3
    elif shape == "heptagon":
        return 1.5
    else:
        return 2


def simulate_cleaning(shape, width, height):
    cleaned_cells = 0
    steps_taken = 0
    radius = get_turn_radius(shape)

    for y in range(height):
        if y % 2 == 0:
            row = range(width)
        else:
            row = range(width - 1, -1, -1)

        for x in row:
            cleaned_cells += 1
            steps_taken += radius

    return cleaned_cells, steps_taken


def find_best_shape():
    shapes = ["round", "square", "triangle", "heptagon"]
    width, height = 10, 10
    results = []

    for shape in shapes:
        cells, time = simulate_cleaning(shape, width, height)
        results.append((shape, cells, time))

    best_shape = min(results, key=lambda s: s[2])
    return best_shape, results


def show_results(category, item):
    print("\n--- Cleaning Results ---")
    print(f"Category: {category}")
    print(f"Item: {item}")

    best, results = find_best_shape()

    print(f"\nBest Shape: {best[0].capitalize()}")
    print(f"Cells Cleaned: {int(best[1])}")
    print(f"Time Taken: {best[2]} steps")

    print("\nTime Taken by Each Shape:")
    for shape, cells, time in results:
        print(f"- {shape.capitalize()}: {time} steps")
    print()


def clean_solid():
    print("\nChoose Solid Type:")
    print("1. Dust")
    print("2. Rocks / Papers")
    print("3. Others")
    choice = input("Enter choice (1-3): ")

    if choice == "1":
        show_results("Solid", "Dust")
    elif choice == "2":
        show_results("Solid", "Rocks / Papers")
    elif choice == "3":
        show_results("Solid", "Others")
    else:
        print("Invalid option. Try again.")


def clean_liquid():
    print("\nChoose Liquid Type:")
    print("1. Water")
    print("2. Beverage")
    print("3. Others")
    choice = input("Enter choice (1-3): ")

    if choice == "1":
        show_results("Liquid", "Water")
    elif choice == "2":
        show_results("Liquid", "Beverage")
    elif choice == "3":
        show_results("Liquid", "Others")
    else:
        print("Invalid option. Try again.")


def start_cleaning():
    print("\nVacuum Started")
    print("1. Clean Solid")
    print("2. Clean Liquid")
    print("3. Back to Main Menu")
    choice = input("Choose option (1-3): ")

    if choice == "1":
        clean_solid()
    elif choice == "2":
        clean_liquid()
    elif choice == "3":
        return
    else:
        print("Invalid choice. Returning to main menu.")


def turn_left():
    print("Vacuum turned left.")


def turn_right():
    print("Vacuum turned right.")


def dock_vacuum():
    print("Vacuum is docked and stopped.")


def main():
    while True:
        print("\n--- Vacuum Cleaner Menu ---")
        print("1. Start Cleaning")
        print("2. Turn Left")
        print("3. Turn Right")
        print("4. Dock Vacuum")
        print("5. Stop Program")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            start_cleaning()
        elif choice == "2":
            turn_left()
        elif choice == "3":
            turn_right()
        elif choice == "4":
            dock_vacuum()
        elif choice == "5":
            print("Vacuum program stopped.")
            break
        else:
            print("Invalid input. Please enter 1–5.")


main()
