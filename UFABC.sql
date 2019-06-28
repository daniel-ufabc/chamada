-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 28, 2019 at 09:26 PM
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
  `id_turma` int(11) NOT NULL,
  `id_status` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_chamadas`
--

INSERT INTO `tb_chamadas` (`id_chamada`, `id_usuario`, `data_chamada`, `id_turma`, `id_status`) VALUES
(92, 1, '2013-06-19', 9, 1),
(93, 1, '2014-06-19', 9, 0);

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
  `id_foto` int(11) NOT NULL,
  `id_status` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_coordenadas`
--

INSERT INTO `tb_coordenadas` (`id_coordenada`, `x`, `y`, `w`, `h`, `id_usuario`, `id_foto`, `id_status`) VALUES
(1898, 168, 42, 127, 127, 1, 54, 0),
(1899, 168, 42, 127, 127, 1, 55, 0);

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
-- Table structure for table `tb_faltas_alunos`
--

CREATE TABLE `tb_faltas_alunos` (
  `id_usuario` int(11) NOT NULL,
  `id_chamada` int(11) NOT NULL,
  `id_turma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tb_fotos`
--

CREATE TABLE `tb_fotos` (
  `id_foto` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `largura` int(11) NOT NULL,
  `altura` int(11) NOT NULL,
  `nome_arquivo` varchar(255) DEFAULT NULL,
  `id_chamada` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_fotos`
--

INSERT INTO `tb_fotos` (`id_foto`, `id_usuario`, `largura`, `altura`, `nome_arquivo`, `id_chamada`) VALUES
(54, 1, 450, 312, '92.jpeg', 92),
(55, 1, 450, 312, '93.jpeg', 93);

-- --------------------------------------------------------

--
-- Table structure for table `tb_presenca_alunos`
--

CREATE TABLE `tb_presenca_alunos` (
  `id_usuario` int(11) NOT NULL,
  `id_chamada` int(11) NOT NULL,
  `id_coordenada` int(11) NOT NULL,
  `id_turma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

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
  `campus` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_turmas`
--

INSERT INTO `tb_turmas` (`id_turma`, `id_usuario`, `nome_turma`, `id_status`, `campus`) VALUES
(6, 1, 'Bases Computacionais', 1, 'Santo Andre'),
(9, 1, 'Calculo vetorial e tensorial', 1, 'Santo Andre'),
(13, 1, 'Estrutura da materia', 0, 'Santo André');

-- --------------------------------------------------------

--
-- Table structure for table `tb_turma_alunos`
--

CREATE TABLE `tb_turma_alunos` (
  `id_turma` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_turma_alunos`
--

INSERT INTO `tb_turma_alunos` (`id_turma`, `id_usuario`) VALUES
(6, 3),
(6, 4);

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
(6, 1, 8),
(9, 4, 8),
(6, 14, 20);

-- --------------------------------------------------------

--
-- Table structure for table `tb_usuarios`
--

CREATE TABLE `tb_usuarios` (
  `id_usuario` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `id_permissao` int(11) NOT NULL DEFAULT '0',
  `RA` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tb_usuarios`
--

INSERT INTO `tb_usuarios` (`id_usuario`, `email`, `senha`, `id_permissao`, `RA`) VALUES
(1, 'prof1@gmail.com', '1234', 1, NULL),
(2, 'prof2@gmail.com', '1234', 1, NULL),
(3, 'aluno1@gmail.com', '1234', 0, 1120180000),
(4, 'aluno2@gmail.com', '1234', 0, 112017001);

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
-- Indexes for table `tb_faltas_alunos`
--
ALTER TABLE `tb_faltas_alunos`
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_chamada` (`id_chamada`),
  ADD KEY `id_turma` (`id_turma`);

--
-- Indexes for table `tb_fotos`
--
ALTER TABLE `tb_fotos`
  ADD PRIMARY KEY (`id_foto`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_chamada` (`id_chamada`);

--
-- Indexes for table `tb_presenca_alunos`
--
ALTER TABLE `tb_presenca_alunos`
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_chamada` (`id_chamada`),
  ADD KEY `id_coordenada` (`id_coordenada`),
  ADD KEY `id_turma` (`id_turma`);

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
-- Indexes for table `tb_turma_alunos`
--
ALTER TABLE `tb_turma_alunos`
  ADD KEY `id_turma` (`id_turma`),
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
  MODIFY `id_chamada` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;

--
-- AUTO_INCREMENT for table `tb_coordenadas`
--
ALTER TABLE `tb_coordenadas`
  MODIFY `id_coordenada` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1900;

--
-- AUTO_INCREMENT for table `tb_fotos`
--
ALTER TABLE `tb_fotos`
  MODIFY `id_foto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `tb_turmas`
--
ALTER TABLE `tb_turmas`
  MODIFY `id_turma` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `tb_usuarios`
--
ALTER TABLE `tb_usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

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
-- Constraints for table `tb_faltas_alunos`
--
ALTER TABLE `tb_faltas_alunos`
  ADD CONSTRAINT `tb_faltas_alunos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `tb_usuarios` (`id_usuario`),
  ADD CONSTRAINT `tb_faltas_alunos_ibfk_2` FOREIGN KEY (`id_chamada`) REFERENCES `tb_chamadas` (`id_chamada`),
  ADD CONSTRAINT `tb_faltas_alunos_ibfk_3` FOREIGN KEY (`id_turma`) REFERENCES `tb_turmas` (`id_turma`);

--
-- Constraints for table `tb_fotos`
--
ALTER TABLE `tb_fotos`
  ADD CONSTRAINT `tb_fotos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `tb_usuarios` (`id_usuario`),
  ADD CONSTRAINT `tb_fotos_ibfk_2` FOREIGN KEY (`id_chamada`) REFERENCES `tb_chamadas` (`id_chamada`);

--
-- Constraints for table `tb_presenca_alunos`
--
ALTER TABLE `tb_presenca_alunos`
  ADD CONSTRAINT `tb_presenca_alunos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `tb_usuarios` (`id_usuario`),
  ADD CONSTRAINT `tb_presenca_alunos_ibfk_2` FOREIGN KEY (`id_chamada`) REFERENCES `tb_chamadas` (`id_chamada`),
  ADD CONSTRAINT `tb_presenca_alunos_ibfk_3` FOREIGN KEY (`id_coordenada`) REFERENCES `tb_coordenadas` (`id_coordenada`),
  ADD CONSTRAINT `tb_presenca_alunos_ibfk_4` FOREIGN KEY (`id_turma`) REFERENCES `tb_turmas` (`id_turma`);

--
-- Constraints for table `tb_turmas`
--
ALTER TABLE `tb_turmas`
  ADD CONSTRAINT `tb_turmas_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `tb_usuarios` (`id_usuario`);

--
-- Constraints for table `tb_turma_alunos`
--
ALTER TABLE `tb_turma_alunos`
  ADD CONSTRAINT `tb_turma_alunos_ibfk_1` FOREIGN KEY (`id_turma`) REFERENCES `tb_turmas` (`id_turma`),
  ADD CONSTRAINT `tb_turma_alunos_ibfk_2` FOREIGN KEY (`id_usuario`) REFERENCES `tb_usuarios` (`id_usuario`);

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
