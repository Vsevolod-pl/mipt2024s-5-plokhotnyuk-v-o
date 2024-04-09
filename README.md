# mipt2024s-5-modern-cv

[описание некоторых видов баркодов](barcode_types.md)

# Участники

| участник              | данные | задача (кратко)                           |
| --------------------- | -------| ----------------------------------------- |
|[Белков Алексей](https://github.com/alexeybelkov/mipt2024s-5-belkov-alexey)| |Оптимизация генератора
|[Белков Арсений](https://github.com/arseniybelkov/mipt2024s-5-belkov-arseniy)|  | Rotated rectangles detection |
|[Зайченкова Екатерина](https://github.com/Zayrina/mipt2024s-5-zaychenkova-e-e)   |        | zone image dewrapper |
|Корчагин Сергей        |        | coarse zone detection (bbox) |
|[Кулакова Анна](https://github.com/kulakovaanna/mipt2024s-5-kulakova-a-d)| [git](https://github.com/kulakovaanna/mipt2024s-5-kulakova-a-d/tree/main/data) | refining synthetic images |
|Малеванный Всеволод| |
|Плохотнюк Всеволод |     | генерация эталонных данных |
|[Полевой Дмитрий](https://github.com/dvpsun/mipt2024s-5-modern-cv)|[я-облако](https://disk.yandex.ru/d/eOlAMqBw1xbWeg)        | координация, техэкспертиза                |
|Сабанцев Лев     |       | общий pipeline + общая оценка качества |
|[Тиняков Артём](https://github.com/ArtemTinyakov/mipt2024s-5-Tiniakov-A-D)| [photos](https://disk.yandex.ru/d/yKHmNgF8G0FKxg) | in zone instance segmentation |

# Домашние задания

## неделя 07 (20.03-26.03)
0. **создаем на github хранилище** (можно приватное) на семестр, с именем mipt2024s-5-lastname-f-s (в конце фамилия и инициалы) + добавляем в участники dvpsun + **ссылку фиксируем в таблице участников** и скидываем в личку преподавателю
1. пишем недельный отчет (до 23:59 вторника вы  дописываете ваш очередной отчет сверху в файл reports.md в корне вашего личного git хранилища, т.е. в этом файле отчеты можно будет прочитать в обратном порядке, отчет содержит краткое описание ваших результатов за неделю, текущего состояния и планов работ на следующую неделю, если присутствовать на занятии не смогли, то отчет пишется максимально четко и полно)
2. собираем м размечаем + 10 изображений, данные публикуем

## неделя 06 (13.03-19.03)
0. собрать еще минимум 10 изображений и разметить их (уже должно быть у каждого по 60), картинки и разметку залить в индвидуальный git (папка data)
1. продолжить проработку индивидуальной задачи (уточнить и описать ожидаемые входные данные, описать выходные данные, описать способ оценки качества для вашего этапа/задачи)
2. сделать файл с описанием соответствия инстанса (типа) баркода и его цвета для визуализации
3. провести анализ правильного размера рецептивного поля (Артём)
4. продумать как приводить бокс к нужному полю (Артём)
5. посмотреть как оценивать качество границ (Артём)

## неделя 05 (06.03-12.03)
0. создаем на github хранилище (можно приватное) на семестр, с именем mipt2024s-5-lastname-f-s (в конце фамилия и инициалы) + добавляем в участники dvpsun + ссылку фиксируем в таблице участников и скидываем в личку преподавателю
0. собрать еще минимум 10 изображений и разметить их (уже должно быть у каждого по 50), картинки и разметку залить в индвидуальный git (папка data)

1. продолжить проработку индивидуальной задачи (найти и пощупать SOTA готовые к употреблению, продумать входы/выходы для своих частей, продумать оценку качества)
2. сделать нормальное описание вашей части в вашем хранилище - "что сейчас SOTA в этой части", "как вы сейчас себе представляете вашу часть", "как вы планируете проверять ваши результаты", "как вы покажете ваши результаты"

3. сделать базовую инструкцию для разметки (Артём)
4. понять можно ли в разметке-ломаной кривой навесить на какие-то точки теги (например узнать какие из них являются реальными углами) (Сева)
5. сделать минимальный pipeline для квадратных - проективная нормализация по разметке + декодирование OS декодерами

## неделя 04 (28.02-05.03)
0. собрать еще минимум 10 изображений и разметить их (уже должно быть у каждого по 40), картинки и разметку залить в индвидуальный git (папка data)
1. сделать нормальный структурированный файл с описанием найденных дайнных на общем гите
2. сделать нормальный структурированный файл с описанием видов баркодов на общем гите
3. продолжить проработку индивидуальной задачи (найти и пощупать SOTA готовые к употреблению, продумать входы/выходы для своих частей, продумать оценку качества)
5. сделать нормальное описание вашей части в вашем хранилище - "что сейчас SOTA в этой части", "как вы сейчас себе представляете вашу часть", "как вы планируете проверять ваши результаты", "как вы покажете ваши результаты"

## неделя 03 (21.02-27.02)
1. собрать еще 10 изображений и разметить их (уже должно быть у каждого по 30), картинки и разметку залить в индвидуальный git (папка data)
2. попробовать найти готовые датасеты с бар-кодами (и возможно с готовой разметкой?)
3. для разметки выбрали via, необходимо создать шаблон для разметки изображений (надеюсь сделает Сергей, у него опыт работы с via есть), для каждого изображения необходимо делать отдельный файл разметки
4. на этапе разметки необходимо понимать какой класс бар-кода перед нами, необходимо сформировать базу с описаниями бар-кодов (база будет общая и лежать тут, на гите, скорее всего будет пополняться)
5. каждый выбрал себе задачу, теперь необходимо посмотреть на существующие state-of-the-art решения, потрогать руками, попробовать позапускать, понять от чего можно отталкиваться

## неделя 02 (14.02-20.02)
1. собираем собственный набор данных - фотографируем самые разные штрихкоды в самых разных условиях
2. пробуем разметить 10-20 разных по сложности геометрии примеров из личных запасов
3. формируем мненние об иструментах ручной разметки ([LabelMe](https://github.com/labelmeai/labelme) и [VGG Image Annotator](https://www.robots.ox.ac.uk/~vgg/software/via/) или [LabelStudio](https://github.com/HumanSignal/label-studio))
4. выбираем себе индивидуальную задачу
5. изучаем доступные данные и готовые открытые SOTA решения (в первую очередь по выбранной задаче)
6. создаем на github хранилище (можно приватное) на семестр, с именем mipt2024s-5-lastname-f-s (в конце фамилия и инициалы) + добавляем в участники dvpsun + ссылку фиксируем в таблице участников и скидываем в личку преподавателю

## неделя 01 (07.02-13.02)
1. собираем собственный набор данных - фотографируем самые разные штрихкоды в самых разных условиях
2. думаем, как внутри может быть устроена система распознавания штрихкодов, как будет устроена система обучения такой распознавалки, какую часть вам интересно сделать
3. ищем готовые open source компоненты системы распознавания штрихкодов
4. ищем описания критериев оценки качества компонент системы распознавания штрихкодов 
5. ищем открытые наборы данных, оцениваем их пригодность для нашей разработки
6. находим в телеге по имени пользователя преподавателю и пишем ему приветственное сообщение (что это студент, 5 курс, ФИО, номер группы, id пользователя на github)
