def test(word:str, test:str):
    
    if int(word) == int(test):
        return True
    return False

print(test("hello", "he"))