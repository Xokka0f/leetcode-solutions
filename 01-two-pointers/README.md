# Two Pointers

## Теория

Два указателя для обхода массива или строки. Вместо двух вложенных циклов O(n²) — один проход за O(n).

### Два типа

**Встречные (opposite direction)** — один в начале, другой в конце, двигаются навстречу. Для отсортированных массивов, палиндромов, поиска пар.

**Однонаправленные (same direction)** — оба идут в одну сторону. slow = граница готовой части, fast = разведчик. Для удаления дубликатов, перемещения элементов in-place.

## Задачи

### От ментора
- [x] #125 Valid Palindrome — Easy
- [x] #167 Two Sum II — Easy
- [x] #283 Move Zeroes — Easy
- [x] #15 3Sum — Medium

### Самостоятельная практика
- [ ] #26 Remove Duplicates from Sorted Array — Easy
- [x] #11 Container With Most Water — Medium
- [ ] #75 Sort Colors — Medium
- [x] #344 Reverse String — Easy
- [ ] #977 Squares of a Sorted Array — Easy
- [ ] #42 Trapping Rain Water — Hard
