import sqlite3

connection = sqlite3.connect('Lesson6_Base.db')
cur = connection.cursor()

# Скрипт создания таблицы Категорий
cur.executescript(
    "DROP TABLE IF EXISTS 'categories'; "
    "CREATE TABLE IF NOT EXISTS `categories`"
    "(`category` INTEGER PRIMARY KEY NOT NULL, "
    "`category_name` VARCHAR(50) NOT NULL, "
    "`category_description` TEXT NOT NULL);"
)

# Скрипт создания таблицы Единицы измерения товаров
cur.executescript(
    "DROP TABLE IF EXISTS 'units'; "
    "CREATE TABLE IF NOT EXISTS `units`"
    "(`unit` VARCHAR(150) PRIMARY KEY NOT NULL)"
)

# Скрипт создания таблицы Должности
cur.executescript(
    "DROP TABLE IF EXISTS 'positions'; "
    "CREATE TABLE IF NOT EXISTS `positions`"
    "(`position` VARCHAR(150) PRIMARY KEY NOT NULL)"
)

# Скрипт создания таблицы Товары
cur.executescript(
    "DROP TABLE IF EXISTS 'goods'; "
    "CREATE TABLE IF NOT EXISTS `goods`"
    "(`good_id` INTEGER PRIMARY KEY NOT NULL,"
    "`good_name` VARCHAR(100) UNIQUE NOT NULL,"
    "`good_unit` VARCHAR(150) NOT NULL,"
    "`good_cat` INTEGER NOT NULL,"
    "FOREIGN KEY (good_unit) REFERENCES units(unit) ON DELETE CASCADE,"
    "FOREIGN KEY (good_id) REFERENCES categories(category) ON DELETE CASCADE)"
)

# Скрипт создания таблицы Сотрудники
cur.executescript(
    "DROP TABLE IF EXISTS 'employees'; "
    "CREATE TABLE IF NOT EXISTS `employees`"
    "(`employee_id` INTEGER PRIMARY KEY NOT NULL,"
    "`employee_fio` VARCHAR(150) NOT NULL,"
    "`employee_position` VARCHAR(150) NOT NULL,"
    "FOREIGN KEY (employee_position) REFERENCES positions(position) ON DELETE CASCADE)"
)

# Скрипт создания таблицы Поставщики
cur.executescript(
    "DROP TABLE IF EXISTS 'vendors'; "
    "CREATE TABLE IF NOT EXISTS `vendors`"
    "(`vendor_id` INTEGER PRIMARY KEY NOT NULL,"
    "`vendor_name` VARCHAR(220) UNIQUE NOT NULL,"
    "`vendor_ownerchipform` VARCHAR(50) NOT NULL,"
    "`vendor_address` TEXT NOT NULL,"
    "`vendor_phone` BIGINT UNIQUE NOT NULL,"
    "`vendor_email` VARCHAR(150) UNIQUE NOT NULL)"
)

connection.commit()

connection.close()
