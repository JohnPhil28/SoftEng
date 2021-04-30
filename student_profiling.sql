-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 30, 2021 at 06:16 AM
-- Server version: 8.0.21
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_profiling`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE IF NOT EXISTS `admin` (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `username`, `password`) VALUES
(1, 'admin', 'admin123');

-- --------------------------------------------------------

--
-- Table structure for table `student_table`
--

DROP TABLE IF EXISTS `student_table`;
CREATE TABLE IF NOT EXISTS `student_table` (
  `student_id` varchar(10) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `student_address` varchar(255) NOT NULL,
  `course_year` varchar(100) NOT NULL,
  `birth_date` date NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mobile_no` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  UNIQUE KEY `student_id_UNIQUE` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=armscii8;

--
-- Dumping data for table `student_table`
--

INSERT INTO `student_table` (`student_id`, `fname`, `lname`, `student_address`, `course_year`, `birth_date`, `email`, `mobile_no`) VALUES
('2001744448', 'Silvervale', 'Mia', 'Bukidnon, Philippines', 'BFA-1', '2001-10-08', 'epicyeah@gmail.com', '09040753520'),
('2004227637', 'Mia', 'Rosario', 'Bukidnon, Philippines', 'BE-3', '1998-09-08', 'Jadeepic@gmail.com', '09588699323'),
('2004979997', 'Mia', 'Merle', 'Akihabara, Japan', 'BOFA-3', '2003-05-04', 'baseddummy@gmail.com', '09908319175'),
('2016643212', 'Mia', 'Johnny', 'Bukidnon, Philippines', 'BJ-3', '1996-04-11', 'Ventigamer@gmail.com', '09169586111'),
('2018230475', 'Mabini', 'Weiss', 'Palawan, Philippines', 'BN-3', '1996-01-14', 'shadowmiphat@gmail.com', '09096763603'),
('2019459517', 'Thea', 'Ceylon', 'Wyoming, Canada', 'BHMCT-2', '2001-04-17', 'ThiaCeylon@gmail.com', '09769616942'),
('2031236856', 'Ceobe', 'Ina', 'Palawan, Philippines', 'BHMCT-1', '2004-03-05', 'Noellemiphat@gmail.com', '09363157940'),
('2039202698', 'Noelle', 'Haato', 'Cagayan de Oro, Philippines', 'BAE-1', '1998-01-27', 'boiawesome@gmail.com', '09981302019'),
('2048384757', 'Haato', 'Noelle', 'Kuala Lumpur, Malaysia', 'BAE-2', '2001-11-11', 'awesomecho_con@gmail.com', '09849040540'),
('2066362648', 'Melody', 'Rosario', 'Dipolog, Philippines', 'CE-2', '1999-09-24', 'Dilucdummy@gmail.com', '09930090553'),
('2072560471', 'Rosenthal', 'Ina', 'Dipolog, Philippines', 'BOFA-2', '1995-04-16', 'cringecringe@gmail.com', '09543739781'),
('2081327768', 'Ceobe', 'Diluc', 'Palawan, Philippines', 'BN-3', '1996-02-12', 'miphatelegance@gmail.com', '09371671982'),
('2088817163', 'Johnny', 'Noelle', 'Bukidnon, Philippines', 'BBM-1', '2003-04-24', '8a11slmao@gmail.com', '09924752045'),
('2089752542', 'Jaden', 'Matagas', 'Quezon, Philippines', 'BSCS-1', '2003-08-12', 'greenEyes@gmail.com', '09459439432'),
('2097879534', 'Mia', 'Mia', 'Dipolog, Philippines', 'BAE-3', '1996-02-11', 'elegance8a11s@gmail.com', '09975413877'),
('2099726873', 'Mori', 'Calliope', 'Kuala Lumpur, Malaysia', 'BAE-3', '2001-09-24', 'miphatdummy@gmail.com', '09780479703');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
