CREATE TABLE GroupInformation (
    GroupID VARCHAR(255) NOT NULL,
    GroupName VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    StartDay VARCHAR(255) NOT NULL,
    EndDay VARCHAR(255) NOT NULL,
    StartHour VARCHAR(255) NOT NULL,
    EndHour VARCHAR(255) NOT NULL,
    PRIMARY KEY (GroupID)
);

-- 2つ目の参加者情報テーブル
CREATE TABLE PerticipantInformation (
　RefID VARCHAR(255) NOT NULL,
    GroupID VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    PRIMARY KEY (RefID)
);