import wikipedia as w
try:

 g="ru"
 w.set_lang(g)
 h=(int(input("До начала использования википедии нажмите 1")))
 if h==1:

    i1=input(" вопрос выводится  на русский")
    w.set_lang(g)
    page=w.page(i1)
    print("Вот что нашлось на вопрос:"+page.original_title)
    print(page.summary)
    i11=input("Оцените википедию 1 лайк, 2 дизлайк")
 if i11=="1":
    print("Спасибо")
 elif i11=="2":
    print("Мы стараемся улучшатся")
except w.exceptions.PageError:
    print("Простите такой статьи нет")

except NameError:
    print("Простите что-то пошло не так")
except ValueError:
    print("Ведите число")
except w.exceptions.WikipediaException:
    print("Ведите запрос!")
try:
    while True:
     i2=input(" вопрос выводится  на русский")
     w.set_lang(g)
     page=w.page(i2)
     print("Вот что нашлось на вопрос:"+page.original_title)
     print(page.summary)
except w.exceptions.WikipediaException:
    print("Ведите запрос!")