# Описание

Домашнее задание №1 по дисциплине "Конфигурационное управление", РТУ МИРЭА, 3 семестр

# Задание

Разработать эмулятор для языка оболочки ОС. 
Необходимо сделать работу
эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС.
Эмулятор должен запускаться из реальной командной строки, а файл с
виртуальной файловой системой не нужно распаковывать у пользователя.
Эмулятор принимает образ виртуальной файловой системы в виде файла формата
zip. 
Эмулятор должен работать в режиме CLI.

Ключами командной строки задаются:
• Путь к архиву виртуальной файловой системы.

Необходимо поддержать в эмуляторе команды ls, cd и exit, а также
следующие команды:
1. who.
2. rmdir.
   
Все функции эмулятора должны быть покрыты тестами, а для каждой из
поддерживаемых команд необходимо написать 3 теста.


# Запуск

Установите тулчейн языка программирования Python (если таковой отсутствует на вашем компьютере)

Создайте zip-архив в любом удобном месте (желательно, в директории `src/`)

С директории `src/config/` создайте файл `FileSystem.zip`. Далее заполните его в соответствии со желаемой структурой вашего проекта.

Выполните следующую команду в корне проекта:

```sh
cargo run
```

# Тестирование

Для запуска тестов в корне проекта выполните:

```sh
cargo test
```
