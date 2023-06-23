# Notes Hristo

Задачи:
- Рецептите като точки.
    - Да представим рецептите като точки в декартова координатна система, така че близки точки да са близки по съставки рецепти.
    - Това ще ни позволи да открием интересни групи/островчета от подобни рецепти.
    - Представяне = representation = embedding = vector.


Steps:
- download cooking recipies (=documents)
- light preprocess
- produce document representations (use Sentence Transformers)


Sentence Transformers = семейство от езикови модели настроени специално за да създават (числови) представяния на документи.