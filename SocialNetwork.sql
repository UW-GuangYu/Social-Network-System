DROP DATABASE IF EXISTS `SocialNetwork`;
CREATE DATABASE  IF NOT EXISTS `SocialNetwork` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `SocialNetwork`;


CREATE TABLE `User` (
    userID int NOT NULL AUTO_INCREMENT,
    userName varchar(100) NOT NULL UNIQUE,
    firstName varchar(100),
    middleName varchar(100),
    lastName varchar(100),
	birthdate DATE,
    sex varchar(100),
    vocation varchar(100),
    religion varchar(100),
    PRIMARY KEY (userID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Group` (
    groupID int NOT NULL AUTO_INCREMENT,
    groupName varchar(100) NOT NULL,
    PRIMARY KEY (groupID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `User_Group` (
    userID int NOT NULL,
    groupID int NOT NULL,
    PRIMARY KEY (userID,groupID),
	FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE,
    FOREIGN KEY (groupID) REFERENCES `Group`(groupID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Follow_User`(
    userID int NOT NULL,
    followerID int NOT NULL,
    PRIMARY KEY (userID, followerID),
    FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE,
    FOREIGN KEY (followerID) REFERENCES User(userID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Post`(
    postID int NOT NULL AUTO_INCREMENT,
    userID int NOT NULL,
	postTitle varchar(100),
    text varchar(1000),
    createTime DATETIME DEFAULT CURRENT_TIMESTAMP,
	thumbsUp int(11) DEFAULT 0,
    thumbsDown int(11) DEFAULT 0,
    PRIMARY KEY (postID),
    FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Read_Post` (
    userID int NOT NULL,
    postID int NOT NULL,
    PRIMARY KEY (userID,postID),
	FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE,
    FOREIGN KEY (postID) REFERENCES Post(postID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Respond_Post` (
    respondID int NOT NULL,
    postID int NOT NULL,
    PRIMARY KEY (respondID, postID),
    FOREIGN KEY (respondID) REFERENCES Post(postID) ON DELETE CASCADE,
	FOREIGN KEY (postID) REFERENCES Post(postID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Post_Image` (
    postID int NOT NULL,
    imageID varchar(100) NOT NULL,
    PRIMARY KEY (postID, imageID),
    FOREIGN KEY (postID) REFERENCES Post(postID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Post_Link` (
    postID int NOT NULL,
    linkID varchar(100) NOT NULL,
    PRIMARY KEY (postID, linkID),
    FOREIGN KEY (postID) REFERENCES Post(postID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Topic`(
    topicID int NOT NULL AUTO_INCREMENT,
    topicTitle varchar(100),
    PRIMARY KEY (topicID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Post_Topic` (
    postID int NOT NULL,
    topicID int NOT NULL,
    PRIMARY KEY (postID, topicID),
    FOREIGN KEY (postID) REFERENCES Post(postID) ON DELETE CASCADE,
    FOREIGN KEY (topicID) REFERENCES Topic(topicID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Sub_Topic`(
    topicID int NOT NULL,
    subTopicID int NOT NULL,
    PRIMARY KEY (topicID, subTopicID),
    FOREIGN KEY (topicID) REFERENCES Topic(topicID) ON DELETE CASCADE,
    FOREIGN KEY (subTopicID) REFERENCES Topic(topicID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Subscribe_Topic`(
    userID int NOT NULL,
    topicID int NOT NULL,
    PRIMARY KEY (userID,topicID),
	FOREIGN KEY (userID) REFERENCES User(userID) ON DELETE CASCADE,
    FOREIGN KEY (topicID) REFERENCES Topic(topicID) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;








-- ----------------------------
--  Records of `User`
-- ----------------------------
BEGIN;
INSERT INTO `User` (userName,firstName,middleName,lastName,birthdate,sex,vocation,religion) VALUES
    ('Austin6','Yu','Guang','Wu',"1996-10-25",'male','Student','Christianity'), 
    ('William3','Yi','Jing','Wei',"1998-06-18",'Androgyne','Driver','Buddhism'),
    ('Joe9','Zhou','N','Xiao',"1993-09-30",'male','Teacher','Nonreligious'),
    ('Michelle4','Bi','Sha','Da',"1994-11-09",'Female','Doctor','Christianity'),
    ('Bob7','Qiu','Yang','Lve',"1995-01-13",'Agender','Student','Buddhism');
COMMIT;

-- ----------------------------
--  Records of `Group`
-- ----------------------------
BEGIN;
INSERT INTO `Group` (groupName) VALUES
    ('SpringFans'),('SummerFans'),('AutumnFans'),('WinterFans');
COMMIT;

-- ----------------------------
--  Records of `User_Group`
-- ----------------------------
BEGIN;
INSERT INTO `User_Group` (userID,groupID) VALUES
    (1,1),(2,2),(3,3),(4,4),(5,3);
COMMIT;


-- ----------------------------
--  Records of `Follow_User`
-- ----------------------------
BEGIN;
INSERT INTO `Follow_User` (userID,followerID) VALUES
    (1,2),(2,3),(3,4),(4,5),(5,1);
COMMIT;


-- ----------------------------
--  Records of `Post`
-- ----------------------------
BEGIN;
INSERT INTO `Post` (userID,postTitle,text,createTime,thumbsUp,thumbsDown) VALUES
    (1,'Austin','Austin wants to shared his birthday party with you',"2020-03-28 06:11:22", 0, 0), 
    (2,'William','Thank you very much for marking my project',"2020-03-29 07:22:33", 0, 0),
    (3,'Joe','Have a wonderful day and take it easy',"2020-03-30 08:33:44", 0, 0),
    (4,'Michelle','Please drink as much water as you can because it is good for your health',"2020-03-31 09:44:55",0,0),
    (5,'Bob','Do not drive too fast and enjoy your life',"2020-04-01 10:55:56",0,0);
COMMIT;


-- ----------------------------
--  Records of `Respond_Post`
-- ----------------------------
BEGIN;
INSERT INTO `Respond_Post` (respondID,postID) VALUES
    (1,2),(2,3),(3,4),(4,5),(5,1);
COMMIT;


-- ----------------------------
--  Records of `Topic`
-- ----------------------------
BEGIN;
INSERT INTO `Topic` (topicTitle) VALUES
    ('politics'),('sports'),('business'),('finance'),('news'),('Canadian politics'),('oil business'),('Toronto politics'),('Alberta oil business');
COMMIT;


-- ----------------------------
--  Records of `Post_Topic`
-- ----------------------------
BEGIN;
INSERT INTO `Post_Topic` (postID, topicID) VALUES
    (1,1),(2,2),(3,3),(4,4),(5,5);
COMMIT;



-- ----------------------------
--  Records of `Sub_Topic`
-- ----------------------------
BEGIN;
INSERT INTO `Sub_Topic` (topicID, subTopicID) VALUES
    (1,6),(1,8),(3,7),(3,9),(6,8),(7,9);
COMMIT;

-- ----------------------------
--  Records of `Subscribe_Topic`
-- ----------------------------
BEGIN;
INSERT INTO `Subscribe_Topic` (userID,topicID) VALUES
    (1,1),(2,2),(3,3),(4,4),(5,5),(1,6),(2,7),(3,8),(4,9);
COMMIT;






