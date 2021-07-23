-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: oneted
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `applies`
--

DROP TABLE IF EXISTS `applies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `applies` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `job_posting_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `applies_job_posting_id_659b0e1c_fk_job_postings_id` (`job_posting_id`),
  KEY `applies_user_id_343ca350_fk_users_id` (`user_id`),
  CONSTRAINT `applies_job_posting_id_659b0e1c_fk_job_postings_id` FOREIGN KEY (`job_posting_id`) REFERENCES `job_postings` (`id`),
  CONSTRAINT `applies_user_id_343ca350_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applies`
--

LOCK TABLES `applies` WRITE;
/*!40000 ALTER TABLE `applies` DISABLE KEYS */;
/*!40000 ALTER TABLE `applies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookmarks`
--

DROP TABLE IF EXISTS `bookmarks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookmarks` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `job_posting_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `bookmarks_job_posting_id_cb7bd654_fk_job_postings_id` (`job_posting_id`),
  KEY `bookmarks_user_id_12990ce0_fk_users_id` (`user_id`),
  CONSTRAINT `bookmarks_job_posting_id_cb7bd654_fk_job_postings_id` FOREIGN KEY (`job_posting_id`) REFERENCES `job_postings` (`id`),
  CONSTRAINT `bookmarks_user_id_12990ce0_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookmarks`
--

LOCK TABLES `bookmarks` WRITE;
/*!40000 ALTER TABLE `bookmarks` DISABLE KEYS */;
/*!40000 ALTER TABLE `bookmarks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companies` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `description` longtext NOT NULL,
  `employee_count` int NOT NULL,
  `coordinate` json NOT NULL,
  `region_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `companies_region_id_263602c0_fk_regions_id` (`region_id`),
  CONSTRAINT `companies_region_id_263602c0_fk_regions_id` FOREIGN KEY (`region_id`) REFERENCES `regions` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies`
--

LOCK TABLES `companies` WRITE;
/*!40000 ALTER TABLE `companies` DISABLE KEYS */;
/*!40000 ALTER TABLE `companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'contenttypes','contenttype'),(3,'jobpostings','company'),(4,'jobpostings','country'),(5,'jobpostings','experience'),(6,'jobpostings','job'),(7,'jobpostings','jobgroup'),(8,'jobpostings','jobposting'),(12,'jobpostings','region'),(9,'jobpostings','tag'),(10,'jobpostings','tagcategory'),(11,'jobpostings','tagjobposting'),(15,'resumes','apply'),(16,'resumes','resume'),(17,'resumes','resumeapply'),(2,'sessions','session'),(14,'users','bookmark'),(13,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-07-23 16:12:20.378230'),(2,'contenttypes','0002_remove_content_type_name','2021-07-23 16:12:20.428586'),(3,'jobpostings','0001_initial','2021-07-23 16:12:20.919667'),(4,'users','0001_initial','2021-07-23 16:12:21.026453'),(5,'resumes','0001_initial','2021-07-23 16:12:21.315222'),(6,'sessions','0001_initial','2021-07-23 16:12:21.346118');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiences`
--

DROP TABLE IF EXISTS `experiences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiences` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiences`
--

LOCK TABLES `experiences` WRITE;
/*!40000 ALTER TABLE `experiences` DISABLE KEYS */;
/*!40000 ALTER TABLE `experiences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_groups`
--

DROP TABLE IF EXISTS `job_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_groups`
--

LOCK TABLES `job_groups` WRITE;
/*!40000 ALTER TABLE `job_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `job_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job_postings`
--

DROP TABLE IF EXISTS `job_postings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job_postings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `title` varchar(300) NOT NULL,
  `salary` int NOT NULL,
  `description` longtext,
  `main_task` longtext,
  `requirement` longtext,
  `preference` longtext,
  `benefit` longtext,
  `due_date` datetime(6) DEFAULT NULL,
  `image_url` varchar(3000) DEFAULT NULL,
  `company_id` bigint NOT NULL,
  `experience_id` bigint NOT NULL,
  `job_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `job_postings_company_id_348fdca4_fk_companies_id` (`company_id`),
  KEY `job_postings_experience_id_70284f63_fk_experiences_id` (`experience_id`),
  KEY `job_postings_job_id_dc3dd544_fk_jobs_id` (`job_id`),
  CONSTRAINT `job_postings_company_id_348fdca4_fk_companies_id` FOREIGN KEY (`company_id`) REFERENCES `companies` (`id`),
  CONSTRAINT `job_postings_experience_id_70284f63_fk_experiences_id` FOREIGN KEY (`experience_id`) REFERENCES `experiences` (`id`),
  CONSTRAINT `job_postings_job_id_dc3dd544_fk_jobs_id` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job_postings`
--

LOCK TABLES `job_postings` WRITE;
/*!40000 ALTER TABLE `job_postings` DISABLE KEYS */;
/*!40000 ALTER TABLE `job_postings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `job_group_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `jobs_job_group_id_065a5785_fk_job_groups_id` (`job_group_id`),
  CONSTRAINT `jobs_job_group_id_065a5785_fk_job_groups_id` FOREIGN KEY (`job_group_id`) REFERENCES `job_groups` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs`
--

LOCK TABLES `jobs` WRITE;
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regions`
--

DROP TABLE IF EXISTS `regions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `regions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `country_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `regions_country_id_432a4d4c_fk_countries_id` (`country_id`),
  CONSTRAINT `regions_country_id_432a4d4c_fk_countries_id` FOREIGN KEY (`country_id`) REFERENCES `countries` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regions`
--

LOCK TABLES `regions` WRITE;
/*!40000 ALTER TABLE `regions` DISABLE KEYS */;
/*!40000 ALTER TABLE `regions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resumes`
--

DROP TABLE IF EXISTS `resumes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resumes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `title` varchar(100) NOT NULL,
  `is_done` tinyint(1) NOT NULL,
  `file_url` varchar(200) DEFAULT NULL,
  `content` json NOT NULL,
  `is_file` tinyint(1) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `resumes_user_id_c088c4b3_fk_users_id` (`user_id`),
  CONSTRAINT `resumes_user_id_c088c4b3_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resumes`
--

LOCK TABLES `resumes` WRITE;
/*!40000 ALTER TABLE `resumes` DISABLE KEYS */;
INSERT INTO `resumes` VALUES (1,'2021-07-23 17:13:08.250435','2021-07-23 17:13:08.250452','호머 심슨 이력서',1,NULL,'{\"skill\": \"마지 심슨 골려먹기\", \"career\": \"원자력 발전소 3년차\", \"education\": \"도넛대학교 2학년 중퇴\", \"description\": \"DDDDDDDDDDDDhough!\"}',0,1),(2,'2021-07-23 17:13:08.259264','2021-07-23 17:13:08.259324','바트 심슨 이력서',1,NULL,'{\"skill\": \"매기 심슨 돌보다 말기\", \"career\": \"중학교 1년차\", \"education\": \"도넛중학교 2학년 중퇴\", \"description\": \"lalalaaa!\"}',0,2),(3,'2021-07-23 17:13:08.264380','2021-07-23 17:13:08.264432','리사 심슨 이력서',1,NULL,'{\"skill\": \"토익 900점\", \"career\": \"범생이 3년차\", \"education\": \"도넛대학교 2학년 \", \"description\": \"hi!\"}',0,3),(4,'2021-07-23 17:13:08.268349','2021-07-23 17:13:08.268401','마지 심슨 이력서',1,NULL,'{\"skill\": \"머리 볶기\", \"career\": \"주부 10년차\", \"education\": \"도넛대학교 졸업\", \"description\": \"don\'t do that!\"}',0,4),(5,'2021-07-23 17:13:08.272833','2021-07-23 17:13:08.272881','매기 심슨 이력서',1,NULL,'{\"skill\": \"\", \"career\": \"아기 3년차\", \"education\": \"\", \"description\": \"응애!\"}',0,5),(6,'2021-07-23 17:48:02.249667','2021-07-23 17:52:53.479902','영어 이력서',1,NULL,'{\"skill\": \"Django, python, javascript\", \"career\": \"worked at ~~~\", \"education\": \"~~ university\", \"description\": \"hello!\"}',0,1),(7,'2021-07-23 19:30:16.282276','2021-07-23 19:30:16.282295','홍길동의 이력서',1,NULL,'{\"skill\": \"장고, 파이썬, 자바스크립트\", \"career\": \"샘성전자 5년 근무\", \"education\": \"샘성대\", \"description\": \"안녕하세요~\"}',0,1),(8,'2021-07-23 19:35:05.509472','2021-07-23 19:35:05.509488','PARK',0,NULL,'{\"skill\": \"123123\", \"career\": \"3213133\", \"education\": \"123213\", \"description\": \"1231\"}',0,1),(9,'2021-07-23 19:39:22.844366','2021-07-23 19:39:22.844400','PARK',0,NULL,'{\"skill\": \"\", \"career\": \"\", \"education\": \"\", \"description\": \"123131233123131232131313131232131311231312331231312321313131312321313112313123312313123213131313123213131123131233123131232131313131232131311231312331231312321313131312321313112313123312313123213131313123213131123131233123131232131313131232131311231312331231312321313131312321313112313123312313123213131313123213131123131233123131232131313131232131311231312331231312321313131312321313112313123312313123213131313123213131123131233123131232131313131232131311231312331231312321313131312321313112313123312313123213131313123213131123131233123131232131313131232131311231312331231312321313131312321313112313123312313123213131313123213131\"}',0,1),(10,'2021-07-23 19:41:14.973641','2021-07-23 19:41:14.973657','PARK',0,NULL,'{\"skill\": \"\", \"career\": \"\", \"education\": \"\", \"description\": \"\"}',0,1),(11,'2021-07-23 19:41:45.067351','2021-07-23 19:41:45.067366','PARK',1,NULL,'{\"skill\": \"\", \"career\": \"\", \"education\": \"\", \"description\": \"asdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdfasdfadsfasdfasdfasdfasfasdf\"}',0,1);
/*!40000 ALTER TABLE `resumes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resumes_applies`
--

DROP TABLE IF EXISTS `resumes_applies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resumes_applies` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `apply_id` bigint NOT NULL,
  `resume_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `resumes_applies_resume_id_apply_id_763b909a_uniq` (`resume_id`,`apply_id`),
  KEY `resumes_applies_apply_id_2fcbff69_fk_applies_id` (`apply_id`),
  CONSTRAINT `resumes_applies_apply_id_2fcbff69_fk_applies_id` FOREIGN KEY (`apply_id`) REFERENCES `applies` (`id`),
  CONSTRAINT `resumes_applies_resume_id_ae67db0e_fk_resumes_id` FOREIGN KEY (`resume_id`) REFERENCES `resumes` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resumes_applies`
--

LOCK TABLES `resumes_applies` WRITE;
/*!40000 ALTER TABLE `resumes_applies` DISABLE KEYS */;
/*!40000 ALTER TABLE `resumes_applies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag_categories`
--

DROP TABLE IF EXISTS `tag_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tag_categories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `is_multiple_choice` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag_categories`
--

LOCK TABLES `tag_categories` WRITE;
/*!40000 ALTER TABLE `tag_categories` DISABLE KEYS */;
/*!40000 ALTER TABLE `tag_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `tag_category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tags_tag_category_id_cf11706c_fk_tag_categories_id` (`tag_category_id`),
  CONSTRAINT `tags_tag_category_id_cf11706c_fk_tag_categories_id` FOREIGN KEY (`tag_category_id`) REFERENCES `tag_categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags_job_postings`
--

DROP TABLE IF EXISTS `tags_job_postings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tags_job_postings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `job_posting_id` bigint NOT NULL,
  `tag_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tags_job_postings_tag_id_job_posting_id_09091c50_uniq` (`tag_id`,`job_posting_id`),
  KEY `tags_job_postings_job_posting_id_8de9ca26_fk_job_postings_id` (`job_posting_id`),
  CONSTRAINT `tags_job_postings_job_posting_id_8de9ca26_fk_job_postings_id` FOREIGN KEY (`job_posting_id`) REFERENCES `job_postings` (`id`),
  CONSTRAINT `tags_job_postings_tag_id_20ca1b81_fk_tags_id` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags_job_postings`
--

LOCK TABLES `tags_job_postings` WRITE;
/*!40000 ALTER TABLE `tags_job_postings` DISABLE KEYS */;
/*!40000 ALTER TABLE `tags_job_postings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `profile_image` varchar(200) NOT NULL,
  `kakao_api_id` int DEFAULT NULL,
  `google_api_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'2021-07-23 16:54:54.402310','2021-07-23 16:54:54.402329','Homer Simpson','homer@google.com','https://metro.co.uk/wp-content/uploads/2020/02/PRI_142406335-e1589297035275.jpg?quality=90&strip=all&zoom=1&resize=480%2C276',1,NULL),(2,'2021-07-23 16:54:54.405417','2021-07-23 16:54:54.405430','Bart Simpson','bart@google.com','https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/f15f5662080793.5a8432e3d5b6b.jpg',2,NULL),(3,'2021-07-23 16:54:54.408407','2021-07-23 16:54:54.408418','Lisa Simpson','lisa@google.com','https://upload.wikimedia.org/wikipedia/en/e/ec/Lisa_Simpson.png',3,NULL),(4,'2021-07-23 16:54:54.410907','2021-07-23 16:54:54.410918','Marge Simpson','marge@google.com','https://media.npr.org/assets/img/2013/05/07/ap0908140151727_vert-06dfa531201681c1ebe2d126471494fdeb5048ae-s800-c85.jpg',4,NULL),(5,'2021-07-23 16:54:54.413629','2021-07-23 16:54:54.413640','Maggie Simpson','maggie@google.com','https://ichef.bbci.co.uk/news/640/cpsprodpb/02F9/production/_104516700_3_spongebob_squarepants__hr.jpg',5,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-24 14:28:00
