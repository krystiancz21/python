class NameException(Exception):
    """Zgłaszany gdy imię lub nazwisko nie zaczyna się wielką literą."""
    pass

class EmailException(Exception):
    """Zgłaszany gdy email nie pasuje do domeny."""
    pass

class IndexException(Exception):
    """Zgłaszany gdy numer indeksu jest nieprawidłowy."""
    pass

class GradeException(Exception):
    """Zgłaszany gdy ocena jest nieprawidłowa."""
    pass 