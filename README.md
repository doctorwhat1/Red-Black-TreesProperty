# Red-Black-TreesProperty
Условия задачи:
Задан граф G, являющийся деревом. Гарантируется, что у данного дерева есть ровно один корень (вершина без родительских узлов, но с возможными дочерними). Все вершины пронумерованы идентификаторами от 0 до V - 1 (V - количество вершин). Для каждой вершины указан набор дочерних вершин и её цвет - красный или чёрный.
Необходимо ответить на вопрос - удовлетворяет ли предложенная структура всем свойствам красно-чёрных деревьев (за исключением свойства связанного со значениями в вершинах и значениями в поддеревьях).

Формат ввода
В первой строке входных данных задано число вершин в графе - V.
Далее следует V строк с описаниями вершин.
Каждая строка i (от 0 до V-1) описывает вершину i и содержит количество потомков, идентификаторы потомков и цвет самой вершины (0 - чёрный, 1 - красный).
Если потомков у вершины нет, строка содержит значение 0 и значение цвета вершины.

Формат вывода
В качестве ответа на задачу нужно вывести единственную фразу - "YES", если представленная структура удовлетворяет требованиям к красно-чёрным деревьям и "NO" в противном случае.
![image](https://user-images.githubusercontent.com/86233023/164065989-b9aab2f3-7200-47c0-af57-8afe6b869e47.png)
