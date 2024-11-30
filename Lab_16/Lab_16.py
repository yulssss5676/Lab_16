import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
import string

# Завантажуємо необхідні дані NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('gutenberg')

# Завантажуємо текст з Project Gutenberg
text = gutenberg.raw('edgeworth-parents.txt')  # Завантажуємо текст Марії Еджворт

# Токенізація тексту
words = word_tokenize(text)

# Визначення загальної кількості слів
word_count = len(words)
print(f"Загальна кількість слів у тексті: {word_count}")

# Підрахунок частоти слів
word_frequencies = Counter(words)

# 10 найбільш вживаних слів (включно зі знаками пунктуації)
most_common_words = word_frequencies.most_common(10)
print("10 найбільш вживаних слів (включаючи пунктуацію):")
print(most_common_words)

# Побудова діаграми
words_list, counts = zip(*most_common_words)
plt.figure(figsize=(10, 6))
plt.bar(words_list, counts, color='skyblue')
plt.title('Топ-10 найбільш вживаних слів (включаючи пунктуацію)')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()

# Видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
filtered_words = [
    word.lower() for word in words if word.isalpha() and word.lower() not in stop_words
]

# Підрахунок частоти слів після видалення стоп-слів
filtered_word_frequencies = Counter(filtered_words)

# 10 найбільш вживаних слів після видалення стоп-слів
most_common_filtered_words = filtered_word_frequencies.most_common(10)
print("10 найбільш вживаних слів після видалення стоп-слів:")
print(most_common_filtered_words)

# Побудова діаграми
filtered_words_list, filtered_counts = zip(*most_common_filtered_words)
plt.figure(figsize=(10, 6))
plt.bar(filtered_words_list, filtered_counts, color='orange')
plt.title('Топ-10 найбільш вживаних слів (без стоп-слів та пунктуації)')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# Завантаження необхідних ресурсів для NLTK
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


# Функція для обробки тексту
def process_text(input_file, output_file):
    try:
        # Читання тексту з вхідного файлу
        with open(input_file, 'r') as file:
            text = file.read()
            print("Вхідний файл успішно прочитаний.")
    except FileNotFoundError:
        print(f"Файл {input_file} не знайдено!")
        return

    # Токенізація по словам
    words = word_tokenize(text)

    # Лемматизація та стеммінг
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()

    # Видалення пунктуації та стоп-слів
    stop_words = set(stopwords.words('english'))
    words_processed = []

    for word in words:
        if word not in stop_words and word not in string.punctuation:
            # Лемматизація
            lemma_word = lemmatizer.lemmatize(word.lower())
            # Стеммінг
            stem_word = stemmer.stem(lemma_word)
            words_processed.append(stem_word)

    # Друк обробленого тексту в консоль
    print("Оброблений текст:", ' '.join(words_processed))

    # Запис обробленого тексту в інший файл
    try:
        with open(output_file, 'w') as file:
            file.write(' '.join(words_processed))
            print("Оброблений файл успішно записаний.")
    except IOError:
        print(f"Не вдалося записати файл {output_file}!")


# Виклик функції для обробки тексту
input_file = 'input_text.txt'  # Файл з довільним текстом до 100 слів
output_file = 'processed_text.txt'  # Файл для обробленого тексту

process_text(input_file, output_file)


