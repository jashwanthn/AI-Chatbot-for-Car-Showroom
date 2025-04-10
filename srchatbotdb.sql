-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 06, 2025 at 09:26 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `srchatbotdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointments`
--

CREATE TABLE `appointments` (
  `aid` int(11) NOT NULL,
  `custname` varchar(100) DEFAULT NULL,
  `dated` varchar(100) DEFAULT NULL,
  `car` varchar(100) DEFAULT NULL,
  `remarks` varchar(100) DEFAULT NULL,
  `timeslot` varchar(100) DEFAULT NULL,
  `bookedby` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `appointments`
--

INSERT INTO `appointments` (`aid`, `custname`, `dated`, `car`, `remarks`, `timeslot`, `bookedby`) VALUES
(3, 'Sunil Kumar', '2025-04-08', 'Mahindra XUV 500', 'ss', '05', 'madhsunil@gmail.com'),
(4, ' Sudhanshuxx ', ' 10-10-2024 ', 'Mahindra XUV', ' Fatigue ', '7.45 pm', 'madhsunil@gmail.com'),
(5, ' Sudhanshuyyy ', ' 10-10-2024 ', 'Mahindra XUV', ' Fatigue ', '7.45 pm', 'madhsunil@gmail.com'),
(6, ' Sunil ', ' 11-10-2024 ', 'Mahindra Thar', ' pickup', '7', 'madhsunil@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `cars`
--

CREATE TABLE `cars` (
  `id` int(11) NOT NULL,
  `car` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cars`
--

INSERT INTO `cars` (`id`, `car`) VALUES
(1, 'Mahindra Thar'),
(2, 'Mahindra XUV 500'),
(3, 'Mahindra XUV 700'),
(4, 'Mahindra Roxx');

-- --------------------------------------------------------

--
-- Table structure for table `showroomdata`
--

CREATE TABLE `showroomdata` (
  `uid` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `pswd` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `dtype` varchar(50) DEFAULT NULL,
  `darea` varchar(50) DEFAULT NULL,
  `location` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `showroomdata`
--

INSERT INTO `showroomdata` (`uid`, `name`, `pswd`, `email`, `phone`, `dtype`, `darea`, `location`) VALUES
('S24041', 'Sunny Boyka', 'qazwsx', 'madhsunil1@gmail.com', '9036453696', '', 'Rajajinagar', '');

-- --------------------------------------------------------

--
-- Table structure for table `userdata`
--

CREATE TABLE `userdata` (
  `Uid` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `Uname` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `Name` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `Pswd` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `Email` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `Phone` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `Address` varchar(255) CHARACTER SET utf8mb4 NOT NULL,
  `age` varchar(50) CHARACTER SET utf8mb4 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userdata`
--

INSERT INTO `userdata` (`Uid`, `Uname`, `Name`, `Pswd`, `Email`, `Phone`, `Address`, `age`) VALUES
('User72394', 'abhi72394', 'abhi', '1234', 'abhi@gmail.com', '7353339571', 'SJH ROAD vidyaranyapuram', '5'),
('User3224', 'indresh3224', 'indresh', '123', 'indreshgowdru07@gmail.com', '7353339571', 'SJH ROAD vidyaranyapuram', '17'),
('User23158', 'Sunny Boyka23158', 'Sunny Boyka', 'qazwsx', 'madhsunil@gmail.com', '9036453696', 'Mysore\njj', '23');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `appointments`
--
ALTER TABLE `appointments`
  ADD PRIMARY KEY (`aid`);

--
-- Indexes for table `cars`
--
ALTER TABLE `cars`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `appointments`
--
ALTER TABLE `appointments`
  MODIFY `aid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `cars`
--
ALTER TABLE `cars`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
