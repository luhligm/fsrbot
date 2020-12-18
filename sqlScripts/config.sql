-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Erstellungszeit: 18. Dez 2020 um 20:07
-- Server-Version: 10.3.21-MariaDB
-- PHP-Version: 7.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `fsrbot`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `config`
--

CREATE TABLE `config` (
  `ID` int(11) NOT NULL,
  `feld` varchar(120) NOT NULL,
  `wert` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Daten für Tabelle `config`
--

INSERT INTO `config` (`ID`, `feld`, `wert`) VALUES
(2, 'regChannel', '771398994651381842'),
(3, 'Token', 'NzcxNDExMjU5OTQwNjY3Mzky.X5ruuA.vNOcIXtNBvL76rhngLvnopOTy6k'),
(4, 'firstRegMsg', '774465363437944834'),
(5, 'secondRegMsg', '774465370828046336');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `config`
--
ALTER TABLE `config`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `config`
--
ALTER TABLE `config`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
