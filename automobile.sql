/*
 Navicat Premium Data Transfer

 Source Server         : connect-mysql
 Source Server Type    : MySQL
 Source Server Version : 80018
 Source Host           : localhost:3306
 Source Schema         : Auto

 Target Server Type    : MySQL
 Target Server Version : 80018
 File Encoding         : 65001

 Date: 02/12/2019 16:34:05
*/


-- ----------------------------
-- Create schema
-- ----------------------------
DROP SCHEMA IF EXISTS `automobile`;
CREATE SCHEMA `automobile`;
USE `automobile`;

-- ----------------------------
-- Table structure for userType
-- ----------------------------
DROP TABLE IF EXISTS `userType`;
CREATE TABLE `userType` (
  `id` INT NOT NULL,
  `type` VARCHAR(31) NOT NULL,
  PRIMARY KEY (`id`)
);

-- ----------------------------
-- Records of userType
-- ----------------------------
BEGIN;
INSERT INTO `userType` VALUES (0, 'administrator');
INSERT INTO `userType` VALUES (1, 'salesperson');
INSERT INTO `userType` VALUES (2, 'businessCustomer');
INSERT INTO `userType` VALUES (3, 'homeCustomer');
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `type` INT NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `zip` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`type`)
    REFERENCES userType(id) ON UPDATE CASCADE ON DELETE NO ACTION
);

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (0, 'root', 0, 'Jack New York City NY', '12345');
INSERT INTO `user` VALUES (1, 'Paul', 1, 'Pocusset Pittsburgh PA', '15217');
INSERT INTO `user` VALUES (2, 'Mia', 2, 'Beechwood Pittsburgh PA', '15217');
INSERT INTO `user` VALUES (3, 'Ivan', 3, 'Orpwood Pittsburgh PA', '15213');
INSERT INTO `user` VALUES (4, 'Grace', 1, 'Centre Pittsburgh PA', '15213');
INSERT INTO `user` VALUES (5, 'Ethan', 2, 'Forbes Pittsburgh PA', '15213');
INSERT INTO `user` VALUES (6, 'Jackie', 3, 'Centre Pittsburgh PA', '15213');
COMMIT;

-- ----------------------------
-- Table structure for businessCustomer
-- ----------------------------
DROP TABLE IF EXISTS `businessCustomer`;
CREATE TABLE `businessCustomer` (
  `id` INT NOT NULL,
  `category` VARCHAR(255) DEFAULT NULL,
  `gross` INT DEFAULT NULL,
  FOREIGN KEY (`id`)
    REFERENCES user(`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

-- ----------------------------
-- Records of businessCustomer
-- ----------------------------
BEGIN;
INSERT INTO `businessCustomer` VALUES (2, 'IT', 99999);
INSERT INTO `businessCustomer` VALUES (5, 'Art', 9999);
COMMIT;

-- ----------------------------
-- Table structure for homeCustomer
-- ----------------------------
DROP TABLE IF EXISTS `homeCustomer`;
CREATE TABLE `homeCustomer` (
  `id` INT NOT NULL,
  `marriage` VARCHAR(31) DEFAULT NULL,
  `gender` INT DEFAULT NULL,
  `age` INT DEFAULT NULL,
  `income` INT DEFAULT NULL,
  FOREIGN KEY(`id`)
    REFERENCES user(`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

-- ----------------------------
-- Records of homeCustomer
-- ----------------------------
BEGIN;
INSERT INTO `homeCustomer` VALUES (3, 'marriaged', 0, 21, 9999);
INSERT INTO `homeCustomer` VALUES (6, 'single', 1, 58, 9998);
COMMIT;

-- ----------------------------
-- Table structure for region
-- ----------------------------
DROP TABLE IF EXISTS `region`;
CREATE TABLE `region` (
  `id` INT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `managerId` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY(`managerId`)
    REFERENCES user(`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

-- ----------------------------
-- Records of region
-- ----------------------------
BEGIN;
INSERT INTO `region` VALUES (1, 'A', 2);
INSERT INTO `region` VALUES (2, 'B', 2);
INSERT INTO `region` VALUES (3, 'C', 2);
INSERT INTO `region` VALUES (4, 'D', 2);
COMMIT;

-- ----------------------------
-- Table structure for store
-- ----------------------------
DROP TABLE IF EXISTS `store`;
CREATE TABLE `store` (
  `id` INT NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  `regionId` INT NOT NULL,
  `managerId` INT NOT NULL,
  `numberOfSalesperson` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`managerId`)
    REFERENCES user(`Id`) ON UPDATE CASCADE ON DELETE NO ACTION,
  FOREIGN KEY (`regionId`)
    REFERENCES region(`Id`) ON UPDATE CASCADE ON DELETE NO ACTION
);

-- ----------------------------
-- Records of store
-- ----------------------------
BEGIN;
INSERT INTO `store` VALUES (1, '1234 1st Ave. Pitt P.A. U.S', 1, 1, 255);
INSERT INTO `store` VALUES (2, '5678 1st St. New York N.Y. U.S', 3, 4, 2);
COMMIT;

-- ----------------------------
-- Table structure for jobTitle
-- ----------------------------
DROP TABLE IF EXISTS `jobTitle`;
CREATE TABLE `jobTitle` (
  `id` INT NOT NULL,
  `type` VARCHAR(31) NOT NULL,
  PRIMARY KEY (`id`)
);

-- ----------------------------
-- Records of jobTitle
-- ----------------------------
BEGIN;
INSERT INTO `jobTitle` VALUES (1, 'salesperson');
INSERT INTO `jobTitle` VALUES (2, 'manager');
COMMIT;

-- ----------------------------
-- Table structure for salesperson
-- ----------------------------
DROP TABLE IF EXISTS `salesperson`;
CREATE TABLE `salesperson` (
  `id` INT NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `jobTitle` INT NOT NULL,
  `storeId` INT NOT NULL,
  `salary` INT NOT NULL,
  FOREIGN KEY (`id`)
    REFERENCES user(`id`) ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (`jobTitle`)
    REFERENCES jobTitle(`id`) ON UPDATE CASCADE ON DELETE NO ACTION,
  FOREIGN KEY (`storeId`)
    REFERENCES store(`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

-- ----------------------------
-- Records of salesperson
-- ----------------------------
BEGIN;
INSERT INTO `salesperson` VALUES (1, '123@gmail.com', 1, 1, 1000);
INSERT INTO `salesperson` VALUES (4, '234@outlook.com', 2, 2, 2200);
COMMIT;

-- ----------------------------
-- Table structure for productType
-- ----------------------------
DROP TABLE IF EXISTS `productType`;
CREATE TABLE `productType` (
  `id` INT NOT NULL,
  `type` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
);

-- ----------------------------
-- Records of productType
-- ----------------------------
BEGIN;
INSERT INTO `productType` VALUES (1, 'sedan');
INSERT INTO `productType` VALUES (2, 'SUV');
INSERT INTO `productType` VALUES (3, 'coupe');
INSERT INTO `productType` VALUES (4, 'truck');
COMMIT;

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `productId` INT NOT NULL,
  `productName` VARCHAR(255) NOT NULL,
  `inventory` INT NOT NULL,
  `price` INT NOT NULL,
  `type` INT NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`productId`),
  FOREIGN KEY (`type`)
    REFERENCES productType(`id`) ON UPDATE CASCADE ON DELETE NO ACTION
);

-- ----------------------------
-- Records of product
-- ----------------------------
BEGIN;
INSERT INTO `product` VALUES (1, 'Passat', 999, 8888, 1, 'clean title');
INSERT INTO `product` VALUES (2, 'CIvic', 998, 7788, 1, 'salvage title');
INSERT INTO `product` VALUES (3, 'G-wagon', 321, 998877, 2, 'salvage title');
INSERT INTO `product` VALUES (4, 'Range rover', 23, 889900, 2, 'rebuild title');
INSERT INTO `product` VALUES (5, '458 spider', 99, 8899666, 3, 'clean title');
INSERT INTO `product` VALUES (6, 'Huracan', 45, 999983, 3, 'rebuild title');
INSERT INTO `product` VALUES (7, 'F150', 8899, 15668, 4, 'clean title');
INSERT INTO `product` VALUES (8, 'Ram', 7889, 34866, 4, 'salvage title');
COMMIT;

-- ----------------------------
-- Table structure for transaction
-- ----------------------------
DROP TABLE IF EXISTS `transaction`;
CREATE TABLE `transaction` (
  `id` INT NOT NULL,
  `productName` VARCHAR(255) NOT NULL,
  `customerId` INT NOT NULL,
  `salespersonId` INT NOT NULL,
  `storeId` INT NOT NULL,
  `date` DATETIME NOT NULL,
  `price` INT NOT NULL,
  `quantity` INT NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`customerId`)
    REFERENCES user(`id`) ON UPDATE CASCADE ON DELETE NO ACTION,
  FOREIGN KEY (`salespersonId`)
    REFERENCES user(`id`) ON UPDATE CASCADE ON DELETE NO ACTION,
  FOREIGN KEY (`storeId`)
    REFERENCES store(`id`) ON UPDATE CASCADE ON DELETE NO ACTION
);

-- ----------------------------
-- Records of transaction
-- ----------------------------
BEGIN;
INSERT INTO `transaction` VALUES (1, 'Passat', 2, 1, 1, '2019-11-01 18:47:30', 9989, 1);
INSERT INTO `transaction` VALUES (2, 'Range rover', 2, 1, 2, '2019-12-01 18:48:05', 8866, 2);
INSERT INTO `transaction` VALUES (3, 'F150', 4, 4, 2, '2019-11-13 18:48:32', 7788, 3);
INSERT INTO `transaction` VALUES (4, 'Ram', 6, 4, 2, '2019-11-15 18:49:18', 6688, 2);
COMMIT;
