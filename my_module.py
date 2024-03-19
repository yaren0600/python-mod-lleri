# my_module.py

def find_vowels(text):
    """
    Metindeki sesli harfleri bulan fonksiyon.
    """
    vowels = "aeıioöuüAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count

def reverse_string(text):
    """
    Metni tersine çeviren fonksiyon.
    """
    return text[::-1]

def check_if_letter(char):
    """
    Verilen karakterin bir harf olup olmadığını kontrol eden fonksiyon.
    """
    if char.isalpha():
        return True
    else:
        return False

def convert_to_lowercase(char):
    """
    Büyük harfi küçük harfe çeviren fonksiyon.
    """
    return char.lower()

def calculate_letter_frequency(text):
    """
    Metindeki harflerin kullanım sıklığını yüzdelik oranını bulan fonksiyon.
    """
    letter_count = {}
    total_letters = 0

    for char in text:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
            total_letters += 1

    frequency_percentage = {}
    for char, count in letter_count.items():
        frequency_percentage[char] = (count / total_letters) * 100

    return frequency_percentage

def info():

    print("Yazar: Begüm Yaren ÖZTÜRK")
    print("Öğrenci Numarası: 211213021")
    
