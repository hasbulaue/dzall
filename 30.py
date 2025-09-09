import asyncio
import os
import json
from pathlib import Path
import time

async def analyze_file(file_path):
    try:
        stat = os.stat(file_path)
        return {
            "path": str(file_path),
            "size": stat.st_size,
            "extension": file_path.suffix.lower(),
            "modified_time": stat.st_mtime
        }
    except Exception as e:
        print(f"Ошибка при анализе файла {file_path}: {e}")
        return None

async def scan_directory(directory_path):
    tasks = []
    total_files = 0
    total_size = 0
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = Path(root) / file
            task = asyncio.create_task(analyze_file(file_path))
            tasks.append(task)
    
    results = await asyncio.gather(*tasks)
    
    valid_results = [result for result in results if result is not None]
    
    for result in valid_results:
        total_files += 1
        total_size += result["size"]
    
    return valid_results, total_files, total_size

async def main():
    directory = input("Введите путь к директории для сканирования: ")
    
    if not os.path.exists(directory):
        print("Директория не существует!")
        return
    
    print("Сканирование начато...")
    start_time = time.time()
    
    results, total_files, total_size = await scan_directory(directory)
    
    end_time = time.time()
    
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    

    print(f"Общее количество файлов: {total_files}")
    print(f"Общий размер файлов: {total_size} байт")
    print(f"Общий размер файлов: {total_size / 1024 / 1024:.2f} МБ")
    print(f"Время выполнения: {end_time - start_time:.2f} секунд")
    print(f"Результаты сохранены в файл: results.json")

if __name__ == "__main__":
    asyncio.run(main())