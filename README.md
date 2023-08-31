# Touhou_characters_analysis

  ![yachie2](https://github.com/cutecaribou/Touhou_characters_analysis/assets/71663347/4058a7b0-7a4a-40cd-92dd-d7a22ef7f52f)

## About

В данном проекте выполнено построение и анализ сетевого графа для героев серии игр Touhou Project при помощи NLP и Network Analytics.
Используется распознавание именованных объектов (NER) для идентификации и классификации именованных объектов по заранее определенным категориям. Цель NER — извлечь структурированную информацию из неструктурированных текстовых данных.

## Description

Сбор информации обо всех героях с сайта Touhou Wiki осуществлялся с помощью скрипта на языке Python с использованием фреймворка `scrapy`, сформированный датасет размещен как characters.csv.

Для извлечения взаимоотношений между героями из текстового описания каждой игры был использован метод `Named Entity Recognition` с некоторыми правилами. Основная идея приведена ниже:
1)  Предложения текста были размечены: имена получили лейблы PERSON, места - LOCATION и тд.
   
2)  Для каждого предложеня был составлен список встретившихся в нем сущностей и оставлены лишь сущности с лейблом PERSON.
  
3)  Далее был определен размер скользящего окна, показывающий, насколько далеко 2 предложения могут находятся друг от друга. Проходимся окном по всему тексту и предполагаем, что если несколько предложенй попали в окно, то между героями, упомянутыми в предложениях, существует связь.

После выделения всех отношений между героями был построен и проанализирован сетевой граф.

## Social graph

Ниже приведен сетевой граф для всех идентифицированных персонажей.

 ![net_1](https://github.com/cutecaribou/Touhou_characters_analysis/assets/71663347/1d55595f-db0a-410e-831a-a1b976a4c121)


## Community detection

Выделение подгрупп - техника анализа графа для получения информации, какие группы образуют граф и как они взаимодейстувют друг с другом. 
Для данной цели был использован `Louvain detection algorithm`.

![comm](https://github.com/cutecaribou/Touhou_characters_analysis/assets/71663347/52f1faba-abfa-4a70-af40-4abb6e71e555)

Разными цветами выделены персонажи, относящиеся к разным группам. Персонажи будут относиться к одной группе при близком расположении их имен в тексте.

## Centrality measures

Centrality measures - меры для нахождения влиятельных людей в сообществах. Под центральностью подразумевается некоторую меру значимости вершины или ребра.

Степень центральности - количество ребер, которые имеет вершина. Логично предположить, что узы, имеющие больше всего ребер являются самыми важными. Ниже представлен график ТОП-10 персонажей по кол-ву ребер

![centrality](https://github.com/cutecaribou/Touhou_characters_analysis/assets/71663347/fbadcb9c-3676-4080-83d1-372ae4131fe2)

> ТОП-10 персонажей с наибольшей степенью централизации

Центральность по посредничеству для вершины — это количество кратчайших путей, проходящих через вершину. Узлы с высокой посреднической центральностью могут иметь стратегический контроль и влияние на других.

![betw_centrality](https://github.com/cutecaribou/Touhou_characters_analysis/assets/71663347/6445e592-65fb-4a70-8735-984fcc44dd7e)

> ТОП-10 персонажей с наибольшей степенью центральность по посредничеству

Как видно, наибольшее влияение у персонажа Marisa, который имеет как наибольшую степень центрольности, так и наибольшую степень центральности по посредничеству. 

## Link prediction

Предсказание связей оценивает вероятность наличия ребра между двумя отдельными вершинами в том случае, если его не существует на графе. Связи, подобранные таким образом, могут помочь, например, при рекомендации друзей.

Ниже представлен график предсказанных связей между персонажами и их вероятности.

<img align="centre" width="400" height="500" src="https://github.com/cutecaribou/Touhou_characters_analysis/assets/71663347/335188fc-f615-44cf-b0a9-a1639f9ad19c">

<img align="centre" width="600" height="500" src="https://github.com/cutecaribou/Touhou_characters_analysis/assets/71663347/793a83a7-a1f9-469a-bea0-f40f8e3705de">


