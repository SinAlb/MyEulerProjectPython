def search(word:str)-> set:
    """Возвращает гласные в слове"""
    vow = set('aiuoe')
    return vow.intersection(set(word))
