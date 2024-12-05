import re
def check_mul(text) -> int:
    finalTotal = 0
    pattern = r'mul\(([1-9]\d{0,2}),\s*([1-9]\d{0,2})\)'

    match = re.findall(pattern, text)
    if match:
        print(match)
        for each in match:
            num1, num2 = each
            finalTotal += int(num1) * int(num2)

    return finalTotal

def check_mul2() -> int:
    finalTotal = 0
    pattern = r'(?:mul\(([1-9]\d{0,2}),\s*([1-9]\d{0,2})\)|do\(\)|don\'t\(\))'
    mulToggle = True
    try:
        with open('./Data/Day3Input.txt', 'r') as file:
            for line in file:
                report = line
                matches = re.finditer(pattern, report)
                for match in matches:
                    fullMatch = match.group(0)
                    if fullMatch.startswith('mul') and mulToggle:
                        num1, num2 = match.groups()
                        finalTotal += int(num1) * int(num2)
                    elif fullMatch == 'do()':
                        mulToggle = True
                    elif fullMatch == "don't()":
                        mulToggle = False
    except FileNotFoundError:
        print("File Not Found")
    except Exception as e:
        print(f"Error loading data: {e}")
    return finalTotal