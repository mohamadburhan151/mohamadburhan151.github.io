-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 06 Jun 2022 pada 21.34
-- Versi server: 10.4.22-MariaDB
-- Versi PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tugas_besar`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `landingpage`
--

CREATE TABLE `landingpage` (
  `id` int(11) NOT NULL,
  `judul` varchar(50) NOT NULL,
  `deskripsi` text NOT NULL,
  `gambar` varchar(155) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `landingpage`
--

INSERT INTO `landingpage` (`id`, `judul`, `deskripsi`, `gambar`) VALUES
(1, 'Uciha Shisui', 'Tolong lindungi desa ini, dan kehormatan Klan Uchiha. Jika aku mati, mungkin keadaan akan berubah. Aku sudah meninggalkan catatan milikku. Jangan coba hentikan ku Itachi, kau adalah teman terbaikku.', 'sishui.jpg'),
(2, 'Uzumaki Naruto', 'Aku tidak suka dengan orang yang membohongi dirinya sendiri ditengah turunnya salju.', 'naruto.jpg'),
(3, 'Uchiha Itachi', 'Sebenarnya aku tak percaya dengan kesempurnaan, karena itulah kita terlahir untuk mempelajari sesuatu.. dan membandingkan diri kita dengan yang lain, kita dapat belajar lebih lagi.', 'itachi.jpg'),
(4, 'Uciha Madara', 'Semakin lama kamu hidup. Semakin kamu menyadari bahwa kenyataan hanya terbuat dari rasa sakit, penderitaan dan kekosongan.', 'madara.jpg'),
(5, 'Uciha Sasuke', 'Seorang ninja menunggu sampai waktunya tepat. Ketika musuh tidur dan menurunkan pertahanan. Ketika senjata tergeletak terlupakan di keheningan malam. Itulah saat untuk seorang ninja untuk menyerang.', 'sasuke.jpg'),
(6, 'Uciha Sasuke', 'Seorang ninja menunggu sampai waktunya tepat. Ketika musuh tidur dan menurunkan pertahanan. Ketika senjata tergeletak terlupakan di keheningan malam. Itulah saat untuk seorang ninja untuk menyerang.', 'sasuke.jpg');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `idUser` int(255) NOT NULL,
  `namaUser` varchar(45) NOT NULL,
  `userName` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  `keterangan` text NOT NULL,
  `level` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`idUser`, `namaUser`, `userName`, `password`, `keterangan`, `level`) VALUES
(1, 'Mohamad Burhanudin', 'burhan', '6bec9c852847242e384a4d5ac0962ba0', 'udin', 'admin'),
(2, 'Mohamad Burhanudin', 'test', '6bec9c852847242e384a4d5ac0962ba0', 'udin', 'user'),
(3, 'Mohamad Burhanudin', 'user', 'd8578edf8458ce06fbc5bb76a58c5ca4', 'qwerty', 'user');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `landingpage`
--
ALTER TABLE `landingpage`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`idUser`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `landingpage`
--
ALTER TABLE `landingpage`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `idUser` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
