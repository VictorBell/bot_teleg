def calculation(text):
    try:
            return eval(text)
    except:
            return("Произошла ошибка, введите верное выражение")
