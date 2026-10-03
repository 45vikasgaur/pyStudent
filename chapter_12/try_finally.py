def main():
    try:
        a = int(input("Enter a number: "))
        print(a)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("I am in finally block ")
main()