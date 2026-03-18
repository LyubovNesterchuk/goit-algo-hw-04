# №1
import pathlib 

# file_path = "salary.txt"
# data = ["Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000\n"]

# with open(file_path, "w", encoding="utf-8") as file:
#     file.write("\n".join(data))

current_dir = pathlib.Path(__file__).parent 

def total_salary(path: str) -> tuple[float, float]:
    try:
        with open(current_dir / path, "r", encoding="utf-8") as file:
            salary = file.readlines()

            total_salary = 0
            employee_count = 0

            for line in salary:
                name, salary_str = line.split(",")
                total_salary += float(salary_str)
                employee_count += 1

            average = total_salary / employee_count  
            print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average}")
            return total_salary, average
        
    except FileNotFoundError:
        print("Не вдалося знайти файл з зарплатами співробітників") 
        return None
    

total_salary("salary.txt")    


