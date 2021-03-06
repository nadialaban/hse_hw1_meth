## Домашнее задание №1
### Абу Аль Лабан Надя, группа 2

Целью данного домашнего задания является изучение глобального изменения уровня CpG метилирования ДНК при раннем эмбриональном развитии мыши.

Тетрадки с решением
---
- [Ссылка](https://colab.research.google.com/drive/1j0H1Ti6ePoXuRn-Y-gp6Im0XDrugUWYG?usp=sharing) на коллаб

1.Отчет FastQC
---
Отчеты в директории `fastqc`, общий отчет - в директории `multiqc`. Для сравнения возьмем MultiQC отчет с [ДЗ 3](https://github.com/nadialaban/hse21_hw3) прошлого семестра. Там мы генерировали отчет для РНК-последовательностей. Рассмотрим сводную таблицу со статистикой:
#### Для РНК-последовательностей:
![image](https://user-images.githubusercontent.com/23341597/155021983-4cbe0938-fa39-4eff-a1e1-d050d1003fab.png)
#### Для QC-прочтений:
![image](https://user-images.githubusercontent.com/23341597/155025168-0f3f65b1-c2d3-4b68-8c61-a4277d2b962e.png)
  
Доля GC для РНК-последовательностей гораздо больше (> чем в 2 раза). Это объясняется тем, что в процессе бисульфитного секвенирования бисульфит действует на одноцепочечную ДНК, превращая цитозин в урацил ([источник](https://ru.wikipedia.org/wiki/Бисульфитное_секвенирование)), таким образом %GC падает для QC-прочтений.
  
2.Вопросы
---
### a. Сколько ридов пришлось на целевые регионы
| Образец  | 11347700-11367700 | 40185800-40195800 |
|----------|-------------------|-------------------|
| 8cell    | 1090              | 464               |
| icm      | 1456              | 630               |
| epiblast | 2328              | 1062              |

### b. Сколько процентов прочтений дуплицированно в каждом из образцов
| Образец  | Процент прочтений |
|----------|-------------------|
| 8cell    | 81.69%            |
| icm      | 90.92%            |
| epiblast | 97.08%            |

bash-скрипт для выполнения дедупликации для всех образцов одновременно:  
`! ls *pe.bam | xargs -P 2 -tI{} deduplicate_bismark  --bam  --paired  -o s_{} {}`

### c. Коллинг метилирования цитозинов
Тамада хороший и конкурсы инетересные  
![image](https://user-images.githubusercontent.com/23341597/154609427-6209574a-55fc-421d-ac3d-38996952d828.png)

### d. M-bias
Отчеты в директории `reports`
#### 8-cell  
![image](https://user-images.githubusercontent.com/23341597/154606573-5191ca05-8f12-43fc-996e-bef24ad8ee51.png)

#### icm  
![image](https://user-images.githubusercontent.com/23341597/154606684-c38fa2ef-d266-49f1-86b4-83443c44726a.png)  

#### epiblast  
![image](https://user-images.githubusercontent.com/23341597/154606635-4fd00e6e-ee68-47bd-9630-f1a041c1a4dc.png)  

#### Ответ
Согласно руководству, M-bias графики показывают процент метилирования для каждой возможной позиции в прочтении.  
Судя по графикам выше, на стадии восьмиклеточного эмбриона доля метилирования примерно 43-44%, затем на стадии бластоциста доля метилирования падает примерно до 23% и в дальнейшем достигает примерно 77-78% на стадии эпибласта. Примерно таким же уровень метелирования останется до конца жизни огранизма.

### e. Распределение метилирования цитозинов по хромосоме
Код в файле `src/hist.py`
![image](https://user-images.githubusercontent.com/23341597/154611277-42461777-4774-4bca-8ddc-3dba10ba7bf5.png)  
![image](https://user-images.githubusercontent.com/23341597/154611348-766b289f-0d7f-4656-a0bf-577e94922acc.png)  
![image](https://user-images.githubusercontent.com/23341597/154611425-5a7c8bf4-98da-45c8-8019-7be21b6831cf.png)  
  
Чаще всего 100% метелирования встречается у образца на стадии эпибласта. У образца восьмиклеточного эмбриона уровень метилирования немного меньше, но все же 100% встречаются довольно часто (примерно 0.3). Реже всего 100% метилирования встречается у образца на стадии бластоцита, что подтверждает предыдущий пункт.  

 ### f. Визуализация для каждого образца
 #### Уровень метилирования
 ![image](https://user-images.githubusercontent.com/23341597/154614372-6c8c7462-4bdf-43b2-a5fe-05f5550769ab.png)

 #### Уровень покрытия
 ![image](https://user-images.githubusercontent.com/23341597/154614350-8985e8ab-b992-4de1-a0a6-eecc6694b771.png)
