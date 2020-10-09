def search(word:str)-> set:
    """Возвращает гласные в слове"""
    vow = set('аеоияюёэыу')
    return vow.intersection(set(word))
