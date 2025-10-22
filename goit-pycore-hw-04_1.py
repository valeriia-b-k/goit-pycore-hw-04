# virsion 1
def total_salary(path):
    try:     
        with open("devs.txt", mode="r") as file:    
            lines = file.readlines()
            total = 0
            count = 0
            for line in lines:
                cleaned_line = line.strip()
                parts = cleaned_line.split(",")
                name = parts[0]
                salary = parts[1]
                salary_number = int(salary)
                total += salary_number
                count += 1
            average = total / count
            return total, average
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0

total, average = total_salary("devs.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


# virsion 2
def total_salary(path):
    try:     
        with open("devs.txt", mode="r") as file:    
            lines = file.readlines()
            total = 0
            count = 0
            for line in lines:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1
            average = total // count
            return total, average
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return 0, 0

total, average = total_salary("devs.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

