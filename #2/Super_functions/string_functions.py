# obliczająca liczbę wyrazów w napisie,
def words_in_string(input_string: str) -> int:
    return len(input_string.split())

# odwracająca kolejność wyrazów
def reverse_words_in_string(input_string: str) -> str:
    return ' '.join(input_string.split())[::-1]

# usuwająca znaki białe w napisie
def remove_whitespace(input_string: str) -> str:
    return ''.join(input_string.split())
