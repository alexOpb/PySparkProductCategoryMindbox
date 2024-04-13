# PySparkProductCategoryMindbox
## Как запустить:
Для этой инструкции нужен VS Code с установленным расширением Docker (ms-azuretools.vscode-docker).
 
 1. Собрать образ (1.12GB)
    - Открыть терминал в папке с Dockerfile.
    - Ввести в терминал: ```docker build -t my-pyspark-image .```
    - Запустить образ: ```docker run -it --rm -p 8888:8888 -v ${PWD}:/app my-pyspark-image```
    - ```-v ${PWD}:/app my-pyspark-image``` связывает текущую директорию (PWD) с директорией в контейнере (/app). Позволит изменять скрипт в контейнере, изменяя скрипт в VS Code.
 2. Присоединить VS Code c контейнеру
    - В VS Code ```Ctrl+Shift+P```
    - Docker Containers: Attach Shell
    - Выбрать Individual Containers
    - Выбрать my-pyspark-image
 4. Запустить python-скрипт
    - В VS Code в панели Terminal будет терминал с именем Containers: Shell: XXXXXX (pyspark_mindbox).
    - В нем набрать команду ```python script.py```
   
## Результат:
```
+--------------+--------+
|          name|category|
+--------------+--------+
|product_null_3|    null|
|  product_ab_1|       A|
|  product_ac_2|       A|
|  product_ac_2|       C|
|  product_ab_1|       B|
+--------------+--------+
```

Состояние dataframe-ов products и categories:
Dataframe: products:
```
+---+--------------+
| id|          name|
+---+--------------+
|  1|  product_ab_1|
|  2|  product_ac_2|
|  3|product_null_3|
+---+--------------+
```
Dataframe: categories:
```
+---+--------+
| id|category|
+---+--------+
|  1|       A|
|  2|       B|
|  3|       C|
+---+--------+
```
Dataframe: product_categories:
```
+----------+-----------+
|product_id|category_id|
+----------+-----------+
|         1|          1|
|         1|          2|
|         2|          1|
|         2|          3|
+----------+-----------+
```

