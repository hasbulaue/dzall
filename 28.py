import argparse
import threading
import re
from collections import Counter
from typing import Dict, List, Tuple

class FileProcessor:
    def __init__(self):
        self.lock = threading.Lock()
        self.global_word_counter = Counter()
        self.global_unique_words = set()
        self.results = {}
        self.threads = []

    def process_file(self, filename: str) -> Dict:
        """Обработка одного файла: подсчет слов и статистики"""
        word_counter = Counter()
        unique_words = set()
        total_words = 0
        
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    # Очистка текста и разделение на слова
                    words = re.findall(r'\b\w+\b', line.lower())
                    word_counter.update(words)
                    unique_words.update(words)
                    total_words += len(words)
                    
        except FileNotFoundError:
            print(f"Ошибка: Файл {filename} не найден")
            return {}
        except Exception as e:
            print(f"Ошибка при чтении файла {filename}: {e}")
            return {}
        
        # Получаем топ-5 слов
        top_words = word_counter.most_common(5)
        
        result = {
            'filename': filename,
            'total_words': total_words,
            'unique_words_count': len(unique_words),
            'unique_words': unique_words,
            'top_words': top_words,
            'word_counter': word_counter
        }
        
        # Синхронизированное обновление глобальной статистики
        with self.lock:
            self.global_word_counter.update(word_counter)
            self.global_unique_words.update(unique_words)
            self.results[filename] = result
        
        return result

    def print_file_stats(self, result: Dict):
        """Вывод статистики для одного файла"""
        print(f"\n=== Статистика для файла: {result['filename']} ===")
        print(f"Общее количество слов: {result['total_words']}")
        print(f"Количество уникальных слов: {result['unique_words_count']}")
        print("Топ-5 самых частых слов:")
        for word, count in result['top_words']:
            print(f"  {word}: {count} раз(а)")

    def process_files(self, filenames: List[str]):
        """Обработка списка файлов в многопоточном режиме"""
        # Создаем и запускаем потоки
        for filename in filenames:
            thread = threading.Thread(
                target=lambda f=filename: self.process_file(f)
            )
            self.threads.append(thread)
            thread.start()
        
        # Ожидаем завершения всех потоков
        for thread in self.threads:
            thread.join()

    def print_global_stats(self):
        """Вывод глобальной статистики по всем файлам"""
        print("\n" + "="*50)
        print("ГЛОБАЛЬНАЯ СТАТИСТИКА ПО ВСЕМ ФАЙЛАМ")
        print("="*50)
        
        total_words_all = sum(result['total_words'] for result in self.results.values())
        total_unique_words_all = len(self.global_unique_words)
        
        print(f"Общее количество слов во всех файлах: {total_words_all}")
        print(f"Общее количество уникальных слов: {total_unique_words_all}")
        
        # Топ-5 слов по всем файлам
        global_top_words = self.global_word_counter.most_common(5)
        print("Топ-5 самых частых слов по всем файлам:")
        for i, (word, count) in enumerate(global_top_words, 1):
            print(f"  {i}. {word}: {count} раз(а)")

    def print_detailed_stats(self):
        """Вывод детальной статистики по каждому файлу"""
        print("\n" + "="*50)
        print("ДЕТАЛЬНАЯ СТАТИСТИКА ПО ФАЙЛАМ")
        print("="*50)
        
        for result in self.results.values():
            self.print_file_stats(result)

def main():
    # Настройка аргументов командной строки
    parser = argparse.ArgumentParser(
        description='Многопоточный анализатор текстовых файлов'
    )
    parser.add_argument(
        'files', 
        nargs='+',
        help='Список текстовых файлов для анализа'
    )
    parser.add_argument(
        '--detailed', 
        '-d',
        action='store_true',
        help='Показать детальную статистику по каждому файлу'
    )
    
    args = parser.parse_args()
    
    if not args.files:
        print("Ошибка: Не указаны файлы для анализа")
        return
    
    print(f"Начинаем обработку {len(args.files)} файлов...")
    
    # Создаем и запускаем процессор
    processor = FileProcessor()
    processor.process_files(args.files)
    
    # Выводим результаты
    if args.detailed:
        processor.print_detailed_stats()
    
    processor.print_global_stats()

if __name__ == "__main__":
    main()