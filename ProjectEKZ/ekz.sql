-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Янв 15 2024 г., 08:48
-- Версия сервера: 8.2.0
-- Версия PHP: 8.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `ekz`
--

-- --------------------------------------------------------

--
-- Структура таблицы `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('1a4589709f1f');

-- --------------------------------------------------------

--
-- Структура таблицы `car`
--

CREATE TABLE `car` (
  `id` int NOT NULL,
  `model` varchar(50) NOT NULL,
  `driver` varchar(100) NOT NULL,
  `number` varchar(10) NOT NULL,
  `on_duty` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `car`
--

INSERT INTO `car` (`id`, `model`, `driver`, `number`, `on_duty`) VALUES
(1, 'Kia Rio', 'Корунов Александр Владимирович', 'а712ее99', 1),
(2, 'Lada Vesta', 'Рунов Дмитрий Борисович', 'а171мр97', 0),
(3, 'Kia Optima', 'Косачков Кирилл Павлович', 'м196ос50', 1);

-- --------------------------------------------------------

--
-- Структура таблицы `order`
--

CREATE TABLE `order` (
  `id` int NOT NULL,
  `car_id` int NOT NULL,
  `passenger` varchar(100) NOT NULL,
  `destination` varchar(100) NOT NULL,
  `sms_code` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `order`
--

INSERT INTO `order` (`id`, `car_id`, `passenger`, `destination`, `sms_code`) VALUES
(1, 1, 'Корунов Александр Владимирович', 'Беговая, 5', '7124'),
(2, 3, 'Косачков Кирилл Павлович', 'Аргуновская, 8', '1981');

-- --------------------------------------------------------

--
-- Структура таблицы `user`
--

CREATE TABLE `user` (
  `id` int NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `password_hash` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Индексы таблицы `car`
--
ALTER TABLE `car`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_car_number` (`number`);

--
-- Индексы таблицы `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_order_car_id_car` (`car_id`);

--
-- Индексы таблицы `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uq_user_phone_number` (`phone_number`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `car`
--
ALTER TABLE `car`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `order`
--
ALTER TABLE `order`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `user`
--
ALTER TABLE `user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `fk_order_car_id_car` FOREIGN KEY (`car_id`) REFERENCES `car` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
