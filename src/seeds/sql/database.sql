CREATE DATABASE  IF NOT EXISTS `dashboard_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dashboard_db`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: dashboard_db
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `orderDate` varchar(255) DEFAULT NULL,
  `orderTime` time DEFAULT NULL,
  `checkin` varchar(255) DEFAULT NULL,
  `checkinTime` time DEFAULT NULL,
  `checkout` varchar(255) DEFAULT NULL,
  `checkoutTime` time DEFAULT NULL,
  `notes` text,
  `idRoom` int DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idRoom` (`idRoom`),
  CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`idRoom`) REFERENCES `rooms` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings`
--

LOCK TABLES `bookings` WRITE;
/*!40000 ALTER TABLE `bookings` DISABLE KEYS */;
INSERT INTO `bookings` VALUES (1,'Jose Pfannerstill','2024-01-22','14:14:28','2024-01-26','06:27:31','2024-02-18','18:17:47','Attero occaecati vulgaris avarus.',4,'checked-in'),(2,'Ray West','2023-08-04','02:12:11','2024-01-30','22:07:31','2024-02-15','05:43:15','Occaecati tibi absens vae tardus degusto adversus demum.',3,'checked-in'),(3,'Alvin Hane','2023-11-12','09:12:54','2024-01-29','05:45:08','2024-02-10','07:57:29','Repudiandae abbas adicio chirographum cuius timor curso comis nemo doloribus.',11,'checked-in'),(4,'Erika Lakin','2023-10-09','08:33:31','2024-01-25','05:08:20','2024-02-17','14:04:22','Amplitudo sublime utor quisquam terror degusto amplexus voluptatum.',10,'pending'),(5,'Clay Parisian','2023-10-17','05:37:53','2024-01-23','13:34:47','2024-02-08','03:46:11','Aestivus virtus velum considero totidem aegre ante ver.',3,'checked-in'),(6,'Mona Erdman','2023-08-07','08:50:04','2024-02-01','20:02:11','2024-02-03','14:04:20','Crinis suffragium cupiditas copia adeo varietas adsidue ipsam calamitas.',13,'pending'),(7,'Stephen Murray','2023-12-08','09:33:02','2024-01-27','21:13:51','2024-02-17','03:29:02','Illo virgo color cognatus bellum vacuus conor tremo.',5,'checked-out'),(8,'Sherri Champlin','2023-09-26','12:02:29','2024-01-28','18:20:52','2024-02-16','19:26:13','Amoveo laborum thesaurus tabernus culpo.',3,'pending'),(9,'Glenda Robel','2023-11-11','22:11:17','2024-01-27','23:36:44','2024-02-04','08:49:42','Adflicto thesis veritatis tactus nulla viridis calculus.',5,'pending'),(10,'Jessie Osinski','2023-09-05','07:11:55','2024-01-30','10:37:42','2024-02-05','00:48:10','Cariosus administratio ut viscus accommodo armarium.',11,'checked-out'),(11,'Veronica Nienow','2023-10-14','03:41:47','2024-01-28','03:25:21','2024-02-05','08:12:24','Cohibeo acies sum vix una conduco desipio.',10,'checked-out'),(12,'Jill Ratke','2024-01-16','21:29:11','2024-01-29','18:07:11','2024-02-18','21:36:52','Consequatur crux audacia deorsum caritas aduro.',10,'pending'),(13,'Brandon Fisher PhD','2023-12-17','11:16:00','2024-01-23','01:36:47','2024-02-11','07:18:41','Volva contigo uter degero.',13,'checked-in'),(14,'Naomi Lowe','2023-10-17','02:17:44','2024-01-30','00:19:44','2024-02-08','19:16:54','Asporto alii crebro hic sto arx.',3,'pending');
/*!40000 ALTER TABLE `bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `photo` varchar(255) DEFAULT NULL,
  `date` varchar(255) DEFAULT NULL,
  `hour` time DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  `archived` tinyint(1) DEFAULT NULL,
  `review` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts`
--

LOCK TABLES `contacts` WRITE;
/*!40000 ALTER TABLE `contacts` DISABLE KEYS */;
INSERT INTO `contacts` VALUES (1,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/857.jpg','2023-12-16','19:02:07','Janice','Hauck','Nickolas_Cremin44@hotmail.com','994.779.7242 x2699',1,'Sopor tepesco apparatus ipsam cena comminor decimus tendo.'),(2,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/778.jpg','2023-11-03','11:16:54','Alaina','Gusikowski','Madelyn_Hand61@hotmail.com','951-803-1898 x9632',0,'Aurum thesis adeo corrumpo fugit saepe vapulus succurro timor.'),(3,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/636.jpg','2023-12-16','12:55:58','Rafael','Gerlach','Jaydon.Morar0@hotmail.com','375-364-9240 x98275',1,'Quisquam appello ducimus quod quibusdam auctor alii.'),(4,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/1045.jpg','2023-02-04','21:27:24','Minerva','Thiel','Hubert31@gmail.com','(789) 656-8247 x3298',1,'Verbera hic desidero cavus adipiscor.'),(5,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/1123.jpg','2023-07-17','06:19:21','Boris','Bode','Camden.OKeefe@gmail.com','354.917.5871 x1928',0,'Tempora armarium dicta corporis talio commodi celebrer complectus iure.'),(6,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/625.jpg','2023-06-20','14:48:57','Gennaro','Kessler','Earlene.Wisozk@gmail.com','403-652-5402 x4044',0,'Aegrotatio aeger conor explicabo appositus aegre paens stips patruus stipes.'),(7,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/398.jpg','2023-08-12','19:36:06','Jimmy','Schulist','Telly.Cronin65@hotmail.com','(988) 887-3747 x331',0,'Candidus qui tergiversatio vereor volup cognatus provident timor possimus usque.'),(8,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/1033.jpg','2023-05-30','02:49:56','Austen','Prohaska','Junior.Schneider@yahoo.com','(339) 905-8171 x6845',1,'Conspergo bibo coniecto amplexus.'),(9,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/924.jpg','2023-08-15','02:56:34','Mack','Kihn','Samanta_Rodriguez96@yahoo.com','1-708-674-7797 x2241',0,'Corpus cribro creber magnam colligo.'),(10,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/36.jpg','2023-12-14','01:58:26','Kayli','Aufderhar','Lesley.Casper@yahoo.com','(225) 672-9398 x956',0,'Spoliatio vestrum arguo tempore attonbitus.'),(11,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/104.jpg','2023-06-21','14:05:01','Reva','Carroll','Lera.Franecki75@gmail.com','877.649.4209 x49157',1,'Vulgo dolores altus tui talis timidus ex avarus.'),(12,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/334.jpg','2023-10-28','17:39:46','Alexa','Kohler','Margarete33@yahoo.com','1-671-464-5704',1,'Comedo coaegresco coaegresco quisquam caelum summa turbo universe.');
/*!40000 ALTER TABLE `contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rooms`
--

DROP TABLE IF EXISTS `rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rooms` (
  `id` int NOT NULL AUTO_INCREMENT,
  `photo` varchar(255) DEFAULT NULL,
  `room` varchar(50) DEFAULT NULL,
  `bed` varchar(50) DEFAULT NULL,
  `facilities` json DEFAULT NULL,
  `description` text,
  `price` decimal(10,2) DEFAULT NULL,
  `discount` int DEFAULT NULL,
  `cancel` text,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rooms`
--

LOCK TABLES `rooms` WRITE;
/*!40000 ALTER TABLE `rooms` DISABLE KEYS */;
INSERT INTO `rooms` VALUES (1,'https://picsum.photos/seed/hikwnKHn/640/480','Double Superior','X-13','[\"Shop near\", \"Smart Security\", \"Kitchen\", \"Grocery\", \"High speed WiFi\"]','Carpo nulla laborum surgo baiulus. Ambulo admiratio clam corrigo volva atque communis occaecati tricesimus. Valeo inventore amiculum tubineus.',252.00,15,'Excepturi ea desipio vallum voluntarius.','available'),(2,'https://picsum.photos/seed/cEzIW2iVuh/640/480','Single Bed','G-49','[\"Breakfast\", \"Shower\", \"High speed WiFi\", \"Air conditioner\", \"24/7 Online Support\", \"Smart Security\"]','Sonitus amita facilis. Spiritus abutor vomica tolero iusto umbra quas necessitatibus ademptio comptus. Aestus cresco acerbitas.',223.00,20,'Celo voluptates deripio cumque caelum sed pectus demens vinum.','available'),(3,'https://picsum.photos/seed/hc6gazp/640/480','Suite','U-29','[\"24/7 Online Support\", \"High speed WiFi\", \"Towels\", \"Breakfast\", \"Air conditioner\"]','Quis tot spargo crastinus claudeo consequatur. Surgo umquam approbo sopor vereor cursim vigilo solium. Quam rerum sopor cernuus sponte arguo villa anser torrens aliquid.',288.00,25,'Cubitum verus coruscus appono.','booked'),(4,'https://picsum.photos/seed/u9gv2/640/480','Single Bed','Q-14','[\"Single bed\", \"Air conditioner\", \"Breakfast\", \"Towels\", \"Kitchen\"]','Angelus succedo demulceo cimentarius dicta omnis nam omnis. Vulnero alioqui abutor angustus ademptio aspernatur benevolentia. Aqua adnuo praesentium spiculum corporis animi.',185.00,0,'Abduco audacia alo suppellex approbo suus temporibus tego creator.','booked'),(5,'https://picsum.photos/seed/6cpVDNs/640/480','Double Superior','Y-31','[\"Kitchen\", \"Smart Security\", \"Expert Team\", \"Cleaning\", \"Shower\"]','Caste patrocinor conturbo culpo vulgo id tam virgo charisma coniecto. Tamen solitudo sustineo ab laboriosam. Contra speciosus artificiose desino vel aranea una accusantium creber vere.',275.00,15,'Vinitor abeo tunc conforto.','booked'),(6,'https://picsum.photos/seed/kiHmL/640/480','Single Bed','W-31','[\"Towels\", \"Grocery\", \"Expert Team\"]','Volva cur tenetur super appositus modi. Tamdiu suggero comis vito abstergo tibi suscipio copia cetera. Cervus absconditus demo.',158.00,15,'Calco nulla commemoro sumptus vesica.','booked'),(7,'https://picsum.photos/seed/Gs4EyFg/640/480','Double Bed','L-40','[\"Cleaning\", \"Single bed\", \"Air conditioner\", \"Shower\", \"Shop near\", \"Grocery\", \"Kitchen\"]','Tamen comedo arma corroboro bos sollicito votum accommodo adipisci. Defendo templum considero antea. Vestigium corrumpo facilis tribuo amaritudo.',179.00,0,'Ager audeo adsum acer tyrannus coniecto vinco complectus.','available'),(8,'https://picsum.photos/seed/1FNEH/640/480','Double Superior','H-36','[\"Kitchen\", \"Single bed\", \"Cleaning\", \"Smart Security\", \"Towels\", \"Shower\", \"Strong Locker\"]','Quasi utroque vigilo sollers advoco aestus demum vallum testimonium. Urbs tum undique spargo voluptas vulpes unde. Cervus solus utrum depraedor tabgo aduro.',226.00,25,'Teres cursus validus.','available'),(9,'https://picsum.photos/seed/I51AT/640/480','Single Bed','C-3','[\"Shop near\", \"Single bed\", \"Cleaning\", \"Kitchen\", \"High speed WiFi\", \"Air conditioner\", \"24/7 Online Support\"]','Tamisium basium depraedor odio tubineus crapula neque summisse attollo. Ultio vicinus admitto decretum allatus arceo aspicio pecco surgo. Cubo cilicium adulatio dicta suus.',159.00,15,'Bellicus illo templum quos adamo timor depraedor aequitas a ex.','available'),(10,'https://picsum.photos/seed/4RxQXEDQi/640/480','Double Superior','Z-38','[\"Shop near\", \"Air conditioner\", \"Strong Locker\", \"Grocery\", \"Kitchen\"]','Denuncio utpote rerum repellendus. Doloremque vindico clementia capto qui degenero minima degusto verbum. Soluta thymbra caelum.',238.00,30,'Thalassinus accommodo viduo acies.','booked'),(11,'https://picsum.photos/seed/y75quASR/640/480','Double Superior','Z-44','[\"Breakfast\", \"Smart Security\", \"High speed WiFi\", \"Shower\", \"Expert Team\", \"Single bed\"]','Facere ascit ascisco defetiscor tollo debitis. Doloremque custodia dicta virga tepesco voco clamo cohibeo. Absens sunt absum comminor anser tristis.',177.00,0,'Sperno thesaurus cur vito.','booked'),(12,'https://picsum.photos/seed/RYWAVNUPs/640/480','Suite','D-16','[\"High speed WiFi\", \"Breakfast\", \"Shower\", \"Towels\", \"Shop near\", \"Smart Security\", \"Expert Team\"]','Thesis candidus maiores. Amo creber vallum amplitudo dignissimos tendo adflicto tolero. Catena vito possimus vulpes cervus absorbeo armarium adamo.',248.00,15,'Thesis stipes rem antiquus thorax adsum.','available'),(13,'https://picsum.photos/seed/net739/640/480','Double Superior','N-48','[\"Expert Team\", \"Air conditioner\", \"Breakfast\", \"Towels\", \"Kitchen\", \"Grocery\"]','Reprehenderit voluptate viridis consuasor ascit tamdiu totam. Delicate deprecator virtus vobis tabernus volubilis deprecator. Aspicio odio vindico spes.',170.00,30,'Crustulum alienus depereo usus.','booked');
/*!40000 ALTER TABLE `rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `photo` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `description` text,
  `status` varchar(10) DEFAULT NULL,
  `startDate` date DEFAULT NULL,
  `position` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/646.jpg','Rochelle Gibson','Weldon_Schuster@hotmail.com','992.787.3754 x063','Suffragium cedo sustineo contabesco vilitas acies somniculosus labore fugit.','inactive','2023-11-22','Manager','ByRHxG8WCbrYUwR'),(2,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/1189.jpg','Austin Cronin','Friedrich.Collins@hotmail.com','(754) 594-1224 x5596','Adsidue amita cicuta ager uberrime.','active','2023-03-16','Service','hOAygTRCA21ztWF'),(3,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/208.jpg','Jacqueline Pagac','Clara.Satterfield@hotmail.com','(702) 946-0157 x306','Tamisium laudantium victus.','active','2023-03-03','Manager','gZGMpZWSl35gFV5'),(4,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/412.jpg','Pedro Macejkovic','Retta.Franey@yahoo.com','500.965.5243 x27950','Repellendus cruciamentum arceo cerno demoror avarus appositus minima.','active','2023-02-14','Service','alpuFhngM0y727O'),(5,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/640.jpg','Benny Champlin','Otho.Toy-DuBuque6@gmail.com','426.223.6696','Virgo earum utrimque cuius conforto creber cado avarus stips.','active','2023-09-19','Manager','3vGHy_RG_ESluhZ'),(6,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/452.jpg','Alice Kulas MD','Everardo_Hahn5@hotmail.com','(432) 648-4416','Fugit ago aegrotatio ullus aer sonitus.','active','2023-06-22','Manager','cacKHUTQ7t9tjMT'),(7,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/1222.jpg','Brett Steuber','Yazmin52@gmail.com','1-281-797-9350 x4630','Curo copiose spiculum itaque.','active','2023-11-06','Manager','pVsQ__DiZ9Yd4Pt'),(8,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/118.jpg','Mr. Bruce Quigley','Annetta98@hotmail.com','622-674-9933 x3413','Abstergo acies taceo beatus harum currus delicate barba nulla.','active','2023-09-30','Reception','AjHKCRHLIQ7qzJ4'),(9,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/903.jpg','Dr. Dean O\'Keefe MD','Cleta.Schowalter39@hotmail.com','1-582-422-8006','Complectus ultio dapifer terga annus.','inactive','2024-01-07','Service','pNn5JHz2pG4weD0'),(10,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/170.jpg','Allison Greenholt','Randall19@yahoo.com','599-969-5128 x9263','Cuius repellendus delicate vivo cupressus amita defaeco aro.','active','2023-02-28','Manager','8jQ1YANkLw4WEQe'),(11,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/1009.jpg','Wanda Conroy','Guiseppe_Stiedemann@yahoo.com','462-857-5283','Deripio capillus vester pecto ipsam aeternus suadeo abeo theologus vivo.','active','2023-07-05','Service','X8fJEraUWr5GW08');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'dashboard_db'
--

--
-- Dumping routines for database 'dashboard_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-01 15:49:15
