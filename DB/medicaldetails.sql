# HeidiSQL Dump 
#
# --------------------------------------------------------
# Host:                 127.0.0.1
# Database:             medicaldetails
# Server version:       5.0.37-community-nt
# Server OS:            Win32
# Target-Compatibility: Standard ANSI SQL
# HeidiSQL version:     3.2 Revision: 1129
# --------------------------------------------------------

/*!40100 SET CHARACTER SET latin1;*/
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ANSI';*/
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;*/


#
# Database structure for database 'medicaldetails'
#

CREATE DATABASE /*!32312 IF NOT EXISTS*/ "medicaldetails" /*!40100 DEFAULT CHARACTER SET latin1 */;

USE "medicaldetails";


#
# Table structure for table 'feedback'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "feedback" (
  "Username" varchar(50) default NULL,
  "doctorusername" varchar(50) default NULL,
  "feedback" varchar(500) default NULL
) /*!40100 DEFAULT CHARSET=latin1*/;



#
# Dumping data for table 'feedback'
#

LOCK TABLES "feedback" WRITE;
/*!40000 ALTER TABLE "feedback" DISABLE KEYS;*/
REPLACE INTO "feedback" ("Username", "doctorusername", "feedback") VALUES
	('geetha','thirukp','I have heat pain at nigh. Please guggest medicine');
REPLACE INTO "feedback" ("Username", "doctorusername", "feedback") VALUES
	('geetha','kumar','I have High BP Please suggest Tabs');
/*!40000 ALTER TABLE "feedback" ENABLE KEYS;*/
UNLOCK TABLES;


#
# Table structure for table 'login'
#

CREATE TABLE /*!32312 IF NOT EXISTS*/ "login" (
  "name" varchar(50) default NULL,
  "username" varchar(50) default NULL,
  "password" varchar(50) default NULL,
  "email" char(50) default NULL,
  "mobile" varchar(50) default NULL,
  "type" varchar(50) default NULL
) /*!40100 DEFAULT CHARSET=latin1*/;



#
# Dumping data for table 'login'
#

LOCK TABLES "login" WRITE;
/*!40000 ALTER TABLE "login" DISABLE KEYS;*/
REPLACE INTO "login" ("name", "username", "password", "email", "mobile", "type") VALUES
	('thirumalai kumar','thirukp','123456','thirumalaikumarp@gmail.com','9600095047','Doctor');
REPLACE INTO "login" ("name", "username", "password", "email", "mobile", "type") VALUES
	('geetha','geetha','123456','geethdk2001@gmail.com','9600095046','Patient');
REPLACE INTO "login" ("name", "username", "password", "email", "mobile", "type") VALUES
	('kumar','kumar','123','kumar@gmail.com','9600095045','Doctor');
/*!40000 ALTER TABLE "login" ENABLE KEYS;*/
UNLOCK TABLES;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE;*/
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;*/
