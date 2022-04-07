# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time

if __name__ == "__main__":
    print(add_time("2:59 AM", "24:00", "saturDay"))

