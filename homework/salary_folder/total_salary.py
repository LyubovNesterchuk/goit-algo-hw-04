# №1
import pathlib 

# file_path = "salary.txt"
# data = ["Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000\n"]

# with open(file_path, "w", encoding="utf-8") as file:
#     file.write("\n".join(data))

# def total_salary(path: str) -> tuple[float, float]:
#     current_dir = pathlib.Path(__file__).parent 
#     try:
#         with open(current_dir / path, "r", encoding="utf-8") as file:
#             salary = file.readlines()

#             total_salary = 0
#             employee_count = 0

#             for line in salary:
#                 name, salary_str = line.split(",")
#                 total_salary += float(salary_str)
#                 employee_count += 1

#             average = total_salary / employee_count  
#             print(f"Загальна сума заробітної плати: {total_salary}, Середня заробітна плата: {average}")
#             return total_salary, average
        
#     except FileNotFoundError:
#         print("Не вдалося знайти файл з зарплатами співробітників") 
#         return None
    

# total_salary("salary.txt")    

def total_salary(path: str) -> tuple[float, float] | None:
    current_dir = pathlib.Path(__file__).parent 
    try:
        with open(current_dir / path, "r", encoding="utf-8") as file:
          
            total = 0
            employee_count = 0

            for line in file:
                name, salary_str = line.strip().split(",")
                total += float(salary_str)
                employee_count += 1

            if employee_count == 0:
                print("Файл порожній")
                return 0.0, 0.0

            average = total / employee_count

            print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
            return total, average

    except FileNotFoundError:
        print("Не вдалося знайти файл з зарплатами співробітників")
        return None
total_salary("salary.txt")

# в терміналі 
# cd homework/salary_folder
# python total_salary.py