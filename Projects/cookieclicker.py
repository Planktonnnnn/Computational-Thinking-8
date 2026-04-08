import time

cookies = 0
cookies_per_click = 1
auto_clickers = 0

def show_status():
    print(f"\nCookies: {cookies}")
    print(f"Cookies per click: {cookies_per_click}")
    print(f"Auto clickers: {auto_clickers}")

def shop():
    global cookies, cookies_per_click, auto_clickers

    print("\n--- Shop ---")
    print("1. Upgrade click (+1 per click) - Cost: 10 cookies")
    print("2. Buy auto clicker (+1/sec) - Cost: 50 cookies")
    print("3. Exit shop")

    choice = input("Choose an option: ")

    if choice == "1" and cookies >= 10:
        cookies -= 10
        cookies_per_click += 1
        print("Upgraded clicking power!")
    elif choice == "2" and cookies >= 50:
        cookies -= 50
        auto_clickers += 1
        print("Bought an auto clicker!")
    elif choice == "3":
        return
    else:
        print("Not enough cookies or invalid choice!")

def game_loop():
    global cookies

    last_time = time.time()

    while True:
        # Passive income
        current_time = time.time()
        elapsed = current_time - last_time
        cookies += int(elapsed * auto_clickers)
        last_time = current_time

        show_status()
        print("\nActions:")
        print("1. Click cookie")
        print("2. Open shop")
        print("3. Quit")

        choice = input("What do you want to do? ")

        if choice == "1":
            cookies += cookies_per_click
        elif choice == "2":
            shop()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    print("Welcome to Cookie Clicker (Python Edition) ")
    game_loop()
