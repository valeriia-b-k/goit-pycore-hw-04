def get_cats_info(path):
    cats = []
    try:     
        with open("cats.txt", mode="r") as file:    
            lines = file.readlines()
            
            for line in lines:
                cleaned_line = line.strip()
                parts = cleaned_line.split(",")
                cat = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": int(parts[2])
                }
                cats.append(cat)
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []
    return cats
    
cats_info = get_cats_info("cats.txt")
print(cats_info)