import re

def verify_date(text):
    """
    Funkcja sprawdza czy przekazana data jest poprawna w formacie.
    Założenia:
    - dni: 01-31 dla każdego miesiąca
    - miesiące: 01-12
    - rok: 0-2023
    - opcjonalnie: p.n.e na końcu dla dat historycznych
    """
    pattern = r"\b(0?[1-9]|[12][0-9]|3[01])\.(0?[1-9]|1[0-2])\.(0|[1-9][0-9]{0,2}|1[0-9]{3}|20[01][0-9]|202[0-3])\s*(p\.n\.e\.)?\b"
    
    if_match = re.search(pattern, text)
    
    if if_match:
        return if_match.group()
    else:
        return "Niepoprawny format daty"

if __name__ == "__main__":
    examples = [
        "12.05.2022",
        "12.5.2022",
        "04.05.14 p.n.e",
        "50.50.5050",
        "12.12.12",
        "test test",
        "12.12",
        "01.02.2023",
        "01.02.2024",
        "12.12.2012 p.n.e",
        "31.01.1985",
        "12.05.145"
    ]

    for data in examples:
        result = verify_date(data)
        print(f"Dla daty [{data}] wynik to: {result}")
