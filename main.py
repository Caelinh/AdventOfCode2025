from Day1.Day1 import Day1
from Day1.Day1Part2 import Day2


def main():
    day1 = Day1()
    result = day1.calculateDistance()
    print(f"Day 1 Total distance: {result}")

    day2 = Day2()
    result = day2.calculateSimScore()
    print(f"Day 2 total score: {result}")

if __name__ == '__main__':
    main()