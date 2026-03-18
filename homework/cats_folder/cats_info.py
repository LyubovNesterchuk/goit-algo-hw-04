# №2
import pathlib 

current_dir = pathlib.Path(__file__).parent 

def get_cats_info(path: str) -> list[dict]:
    try:
        with open(current_dir / path, "r", encoding="utf-8") as file:
            
            cats_info = file.readlines()
            cats_info_list = []
            
            for line in cats_info:
                try:
                    cat_id, name, age = line.strip().split(",")
                except ValueError:
                    print(f"Невірний формат рядка: {line}")
                    continue

                cats_info_list.append({"id": cat_id, "name": name, "age": age})
            
            return cats_info_list
        
    except FileNotFoundError:
        print("Не вдалося знайти файл з інформацією про котиків") 
        return []
  
    
cats_info = get_cats_info("cats_file.txt")
print(cats_info)