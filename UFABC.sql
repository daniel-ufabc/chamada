-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 20, 2019 at 09:12 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `UFABC`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_chamadas`
--

CREATE TABLE `tb_chamadas` (
  `id_chamada` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `data_chamada` date NOT NULL,
  `id_turma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_chamadas`
--

INSERT INTO `tb_chamadas` (`id_chamada`, `id_usuario`, `data_chamada`, `id_turma`) VALUES
(41, 1, '2020-06-20', 7),
(42, 1, '2019-06-21', 7),
(43, 1, '2020-06-21', 7);

-- --------------------------------------------------------

--
-- Table structure for table `tb_coordenadas`
--

CREATE TABLE `tb_coordenadas` (
  `id_coordenada` int(11) NOT NULL,
  `x` int(11) NOT NULL,
  `y` int(11) NOT NULL,
  `w` int(11) NOT NULL,
  `h` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_foto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_coordenadas`
--

INSERT INTO `tb_coordenadas` (`id_coordenada`, `x`, `y`, `w`, `h`, `id_usuario`, `id_foto`) VALUES
(5, 209, 84, 165, 165, 1, 8),
(6, 209, 84, 165, 165, 1, 9);

-- --------------------------------------------------------

--
-- Table structure for table `tb_dia_semanal`
--

CREATE TABLE `tb_dia_semanal` (
  `id_dia_semanal` int(11) NOT NULL,
  `dia_da_semana` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_dia_semanal`
--

INSERT INTO `tb_dia_semanal` (`id_dia_semanal`, `dia_da_semana`) VALUES
(1, 'Domingo'),
(2, 'Segunda-feira'),
(3, 'Terca-feira'),
(4, 'Quarta-feira'),
(5, 'Quinta-feira'),
(6, 'Sexta-feira'),
(7, 'Sabado'),
(8, 'Domingo'),
(9, 'Segunda-feira'),
(10, 'Terca-feira'),
(11, 'Quarta-feira'),
(12, 'Quinta-feira'),
(13, 'Sexta-feira'),
(14, 'Sabado');

-- --------------------------------------------------------

--
-- Table structure for table `tb_fotos`
--

CREATE TABLE `tb_fotos` (
  `id_foto` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `largura` int(11) NOT NULL,
  `altura` int(11) NOT NULL,
  `nome_arquivo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_fotos`
--

INSERT INTO `tb_fotos` (`id_foto`, `id_usuario`, `largura`, `altura`, `nome_arquivo`) VALUES
(7, 1, 640, 480, '41.jpg'),
(8, 1, 640, 480, '42.jpg'),
(9, 1, 640, 480, '43.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tb_status_turma`
--

CREATE TABLE `tb_status_turma` (
  `id_status` int(11) NOT NULL,
  `status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_status_turma`
--

INSERT INTO `tb_status_turma` (`id_status`, `status`) VALUES
(0, 'Inativo'),
(1, 'Ativo');

-- --------------------------------------------------------

--
-- Table structure for table `tb_turmas`
--

CREATE TABLE `tb_turmas` (
  `id_turma` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `nome_turma` varchar(200) NOT NULL,
  `id_status` int(11) NOT NULL DEFAULT '1',
  `campus` varchar(100) NOT NULL,
  `qtd_alunos` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_turmas`
--

INSERT INTO `tb_turmas` (`id_turma`, `id_usuario`, `nome_turma`, `id_status`, `campus`, `qtd_alunos`) VALUES
(6, 1, 'Bases Computacionais', 0, 'Santo Andre', 30),
(7, 1, 'Sistemas digitais', 1, 'Santo Andre', 40),
(9, 1, 'Calculo vetorial e tensorial', 1, 'Santo Andre', 50);

-- --------------------------------------------------------

--
-- Table structure for table `tb_turma_horarios`
--

CREATE TABLE `tb_turma_horarios` (
  `id_turma` int(11) NOT NULL,
  `id_dia_semanal` int(11) NOT NULL,
  `horario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_turma_horarios`
--

INSERT INTO `tb_turma_horarios` (`id_turma`, `id_dia_semanal`, `horario`) VALUES
(6, 2, 8),
(6, 4, 10),
(6, 6, 8),
(6, 8, 10),
(6, 10, 8),
(6, 12, 10),
(7, 2, 19),
(7, 4, 19),
(7, 6, 19),
(9, 2, 19),
(9, 4, 19),
(9, 6, 19),
(7, 2, 19),
(7, 4, 19),
(7, 6, 19),
(9, 2, 19),
(9, 4, 19),
(9, 6, 19);

-- --------------------------------------------------------

--
-- Table structure for table `tb_usuarios`
--

CREATE TABLE `tb_usuarios` (
  `id_usuario` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `id_permissao` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_usuarios`
--

INSERT INTO `tb_usuarios` (`id_usuario`, `email`, `senha`, `id_permissao`) VALUES
(1, 'prof1@gmail.com', '1234', 1),
(2, 'prof2@gmail.com', '1234', 1),
(3, 'prof3@gmail.com', '1234', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_chamadas`
--
ALTER TABLE `tb_chamadas`
  ADD PRIMARY KEY (`id_chamada`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_turma` (`id_turma`);

--
-- Indexes for table `tb_coordenadas`
--
ALTER TABLE `tb_coordenadas`
  ADD PRIMARY KEY (`id_coordenada`),
  ADD KEY `id_foto` (`id_foto`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indexes for table `tb_dia_semanal`
--
ALTER TABLE `tb_dia_semanal`
  ADD PRIMARY KEY (`id_dia_semanal`);

--
-- Indexes for table `tb_fotos`
--
ALTER TABLE `tb_fotos`
  ADD PRIMARY KEY (`id_foto`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indexes for table `tb_status_turma`
--
ALTER TABLE `tb_status_turma`
  ADD PRIMARY KEY (`id_status`);

--
-- Indexes for table `tb_turmas`
--
ALTER TABLE `tb_turmas`
  ADD PRIMARY KEY (`id_turma`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indexes for table `tb_turma_horarios`
--
ALTER TABLE `tb_turma_horarios`
  ADD KEY `id_turma` (`id_turma`),
  ADD KEY `id_dia_semanal` (`id_dia_semanal`);

--
-- Indexes for table `tb_usuarios`
--
ALTER TABLE `tb_usuarios`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_chamadas`
--
ALTER TABLE `tb_chamadas`
  MODIFY `id_chamada` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `tb_coordenadas`
--
ALTER TABLE `tb_coordenadas`
  MODIFY `id_coordenada` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `tb_fotos`
--
ALTER TABLE `tb_fotos`
  MODIFY `id_foto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `tb_turmas`
--
ALTER TABLE `tb_turmas`
  MODIFY `id_turma` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `tb_usuarios`
--
ALTER TABLE `tb_usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_chamadas`
--
ALTER TABLE `tb_chamadas`
  ADD CONSTRAINT `tb_chamadas_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `tb_usuarios` (`id_usuario`),
  ADD CONSTRAINT `tb_chamadas_ibfk_2` FOREIGN KEY (`id_turma`) REFERENCES `tb_turmas` (`id_turma`);

--
-- Constraints for table `tb_coordenadas`
--
ALTER TABLE `tb_coordenadas`
  ADD CONSTRAINT `tb_coordenadas_ibfk_1` FOREIGN KEY (`id_foto`) REFERENCES `tb_fotos` (`id_foto`),
  ADD CONSTRAINT `tb_coordenadas_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `tb_usuarios` (`id_usuario`);

--
-- Constraints for table `tb_fotos`
--
ALTER TABLE `tb_fotos`
  ADD CONSTRAINT `tb_fotos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `tb_usuarios` (`id_usuario`);

--
-- Constraints for table `tb_turmas`
--
ALTER TABLE `tb_turmas`
  ADD CONSTRAINT `tb_turmas_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `tb_usuarios` (`id_usuario`);

--
-- Constraints for table `tb_turma_horarios`
--
ALTER TABLE `tb_turma_horarios`
  ADD CONSTRAINT `tb_turma_horarios_ibfk_1` FOREIGN KEY (`id_turma`) REFERENCES `tb_turmas` (`id_turma`),
  ADD CONSTRAINT `tb_turma_horarios_ibfk_2` FOREIGN KEY (`id_dia_semanal`) REFERENCES `tb_dia_semanal` (`id_dia_semanal`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
