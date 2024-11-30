import nltk
from nltk.corpus import gutenberg, stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
import string

# ����������� �������� ��� NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('gutenberg')

# ����������� ����� � Project Gutenberg
text = gutenberg.raw('edgeworth-parents.txt')  # ����������� ����� ��� �������

# ���������� ������
words = word_tokenize(text)

# ���������� �������� ������� ���
word_count = len(words)
print(f"�������� ������� ��� � �����: {word_count}")

# ϳ�������� ������� ���
word_frequencies = Counter(words)

# 10 ������� �������� ��� (������� � ������� ����������)
most_common_words = word_frequencies.most_common(10)
print("10 ������� �������� ��� (��������� ����������):")
print(most_common_words)

# �������� �������
words_list, counts = zip(*most_common_words)
plt.figure(figsize=(10, 6))
plt.bar(words_list, counts, color='skyblue')
plt.title('���-10 ������� �������� ��� (��������� ����������)')
plt.xlabel('�����')
plt.ylabel('�������')
plt.show()

# ��������� ����-��� �� ����������
stop_words = set(stopwords.words('english'))
filtered_words = [
    word.lower() for word in words if word.isalpha() and word.lower() not in stop_words
]

# ϳ�������� ������� ��� ���� ��������� ����-���
filtered_word_frequencies = Counter(filtered_words)

# 10 ������� �������� ��� ���� ��������� ����-���
most_common_filtered_words = filtered_word_frequencies.most_common(10)
print("10 ������� �������� ��� ���� ��������� ����-���:")
print(most_common_filtered_words)

# �������� �������
filtered_words_list, filtered_counts = zip(*most_common_filtered_words)
plt.figure(figsize=(10, 6))
plt.bar(filtered_words_list, filtered_counts, color='orange')
plt.title('���-10 ������� �������� ��� (��� ����-��� �� ����������)')
plt.xlabel('�����')
plt.ylabel('�������')
plt.show()

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer, PorterStemmer
import string

# ������������ ���������� ������� ��� NLTK
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


# ������� ��� ������� ������
def process_text(input_file, output_file):
    try:
        # ������� ������ � �������� �����
        with open(input_file, 'r') as file:
            text = file.read()
            print("������� ���� ������ ����������.")
    except FileNotFoundError:
        print(f"���� {input_file} �� ��������!")
        return

    # ���������� �� ������
    words = word_tokenize(text)

    # ������������ �� �������
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()

    # ��������� ���������� �� ����-���
    stop_words = set(stopwords.words('english'))
    words_processed = []

    for word in words:
        if word not in stop_words and word not in string.punctuation:
            # ������������
            lemma_word = lemmatizer.lemmatize(word.lower())
            # �������
            stem_word = stemmer.stem(lemma_word)
            words_processed.append(stem_word)

    # ���� ����������� ������ � �������
    print("���������� �����:", ' '.join(words_processed))

    # ����� ����������� ������ � ����� ����
    try:
        with open(output_file, 'w') as file:
            file.write(' '.join(words_processed))
            print("���������� ���� ������ ���������.")
    except IOError:
        print(f"�� ������� �������� ���� {output_file}!")


# ������ ������� ��� ������� ������
input_file = 'input_text.txt'  # ���� � �������� ������� �� 100 ���
output_file = 'processed_text.txt'  # ���� ��� ����������� ������

process_text(input_file, output_file)


