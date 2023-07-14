## Проект по предмету "Алгоритмическая Теория Графов"

- [Реализованные алгоритмы раскраски графов.](#1)
-  [Настройка проекта](#2)
    + [Виртуальное окружение*](#3)
    + [Установка зависимостей](#4)
-  [Запуск проекта](#5)
-  [Запуск тестов](#6)

<div id="1"></a>

## Реализованные алгоритмы раскраски графов 
- Жадная раскраска без эвристик
- Жадная раскраска с эвристикой сортировки вершин
- RLF алгоритм
- алгоритм Зыкова (удаление и стягивание)

## Жадная раскраска без эвристик


```
Жадная раскраска с эвристикой сортировки вершин
```

```
RLF алгоритм
```

## Алгоритм Зыкова (удаление и стягивание)
Идея: Основан на операции стягивания $G/e$ и рекурретном соотношении: $P(G, q) = P(G/e, q) − P(G − e, q)$    
Inpyt: $G(V, E)$, q - количество цветов  
Oupput: $P(G, q)$  
где $P(G, q)$ - хроматеческий многочлен, который считает количество правильных раскрасок в цвет k  
Связь P(G, q) и X(G): $X(G) = min{q : P(G, q) > 0}$  
Асимптотика: $O(1.619^{n+m})$  

<div id="2"></a>

## Настройка проекта 

<div id="3"></a>

### Виртуальное окружение* 
Рекомендуется создать вирутальное окружение командой 
> python -m venv venv

Данная команда создаст виртуальное окружение python в текущей директории. 
Для активации окружения необходимо прописать:

##### Windows
> .\venv\Scripts\activate.bat

##### Unix
> source venv/bin/activate

<div id="4"></a>

### Установка зависимостей 
> pip install -r requirements.txt

<div id="5"></a>

## Запуск проекта 

> python main.py

Генерация графа, запуск всех алгоритмов и вывод количества использованных цветов.
~~~
Опциональный параметр -v
Указывает количество вершин у сгенерированного графа.
Опциональный параметр -с
Указывает количество красок для которых нужно построить хроматический многочлен
~~~
Раскашенный граф визуализируется в graph.html

<div id="6"></a>

## Запуск тестов
~~~
$ cd tests
$ python -m unittest discover
~~~




