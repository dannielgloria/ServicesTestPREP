-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema INEDATABASE
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema INEDATABASE
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `INEDATABASE` DEFAULT CHARACTER SET utf8 ;
USE `INEDATABASE` ;

-- -----------------------------------------------------
-- Table `INEDATABASE`.`ServiceTable`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `INEDATABASE`.`ServiceTable` (
  `Sec` INT NOT NULL,
  `Consec` INT NOT NULL,
  `TipoQR` VARCHAR(5) NOT NULL,
  `Estado` VARCHAR(4) NOT NULL,
  `Distrito` INT NOT NULL,
  `Seccion` VARCHAR(45) NOT NULL,
  `Casilla` VARCHAR(8) NOT NULL,
  `TipoActa` INT NOT NULL,
  `ShaTCA` VARCHAR(65) NULL,
  `ShaMCAD` VARCHAR(65) NULL,
  `ShaCotejo` VARCHAR(65) NULL,
  `IpMCAD` VARCHAR(45) NULL,
  `UsuarioMCAD` VARCHAR(45) NULL,
  `FechaMCAD` DATETIME NULL,
  `IpTCA1` VARCHAR(45) NULL,
  `UsuarioTCA1` VARCHAR(45) NULL,
  `FechaTCA1` DATETIME NULL,
  `ErrorTCA1` VARCHAR(5) NULL DEFAULT 'False',
  `IpTCA2` VARCHAR(45) NULL,
  `UsuarioTCA2` VARCHAR(45) NULL,
  `FechaTCA2` DATETIME NULL,
  `ErrorTCA2` VARCHAR(5) NULL DEFAULT 'False',
  `IpTCA3` VARCHAR(45) NULL,
  `UsuarioTCA3` VARCHAR(45) NULL,
  `FechaTCA3` DATETIME NULL,
  `ErrorTCA3` VARCHAR(5) NULL DEFAULT 'False',
  `IpTCA4` VARCHAR(45) NULL,
  `UsuarioTCA4` VARCHAR(45) NULL,
  `FechaTCA4` DATETIME NULL,
  `ErrorTCA4` VARCHAR(5) NULL DEFAULT 'False',
  `IpCotejo` VARCHAR(45) NULL,
  `UsuarioCotejo` VARCHAR(45) NULL,
  `FechaCotejo` DATETIME NULL,
  `BolSob` INT NOT NULL,
  `PersVot` INT NOT NULL,
  `RepVot` INT NULL,
  `TotPVnRep` INT NOT NULL,
  `P1` INT NULL,
  `P2` INT NULL,
  `P3` INT NULL,
  `P4` INT NULL,
  `P5` INT NULL,
  `P6` INT NULL,
  `P7` INT NULL,
  `P8` INT NULL,
  `P9` INT NULL,
  `P10` INT NULL,
  `P11` INT NULL,
  `P12` INT NULL,
  `C1` INT NULL,
  `C2` INT NULL,
  `C3` INT NULL,
  `C4` INT NULL,
  `CNoReg` INT NULL,
  `VotNulos` INT NULL,
  `Tot1` INT NULL,
  `Tot2` INT NULL,
  PRIMARY KEY (`Sec`, `TipoActa`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
