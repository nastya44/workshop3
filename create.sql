CREATE TABLE alcoholcons (
    dalc      INTEGER NOT NULL,
    walc      INTEGER NOT NULL,
    humanid   INTEGER NOT NULL
);

ALTER TABLE alcoholcons ADD CONSTRAINT alcoholcons_pk PRIMARY KEY ( humanid );

CREATE TABLE alcoholconsdalc (
    dalc INTEGER NOT NULL
);

ALTER TABLE alcoholconsdalc ADD CONSTRAINT alcoholconsdalc_pk PRIMARY KEY ( dalc );

CREATE TABLE alcoholconswalc (
    walc INTEGER NOT NULL
);

ALTER TABLE alcoholconswalc ADD CONSTRAINT alcoholconswalc_pk PRIMARY KEY ( walc );

CREATE TABLE human (
    humanid    INTEGER NOT NULL,
    sex        VARCHAR2(10) NOT NULL,
    health     INTEGER NOT NULL,
    guardian   VARCHAR2(10) NOT NULL,
    age        INTEGER
);

ALTER TABLE human ADD CONSTRAINT human_pk PRIMARY KEY ( humanid );

CREATE TABLE humanguardian (
    guardian VARCHAR2(10) NOT NULL
);

ALTER TABLE humanguardian ADD CONSTRAINT humanguardian_pk PRIMARY KEY ( guardian );

CREATE TABLE humanhealth (
    health INTEGER NOT NULL
);

ALTER TABLE humanhealth ADD CONSTRAINT humanhealth_pk PRIMARY KEY ( health );

CREATE TABLE humansex (
    sex VARCHAR2(10) NOT NULL
);

ALTER TABLE humansex ADD CONSTRAINT humansex_pk PRIMARY KEY ( sex );

CREATE TABLE school (
    title     VARCHAR2(10) NOT NULL,
    humanid   INTEGER NOT NULL
);

ALTER TABLE school ADD CONSTRAINT school_pk PRIMARY KEY ( humanid );

CREATE TABLE schooltitle (
    title VARCHAR2(10) NOT NULL
);

ALTER TABLE schooltitle ADD CONSTRAINT schooltitle_pk PRIMARY KEY ( title );

ALTER TABLE alcoholcons
    ADD CONSTRAINT alcoholcons_alcoholconsdalc_fk FOREIGN KEY ( dalc )
        REFERENCES alcoholconsdalc ( dalc );

ALTER TABLE alcoholcons
    ADD CONSTRAINT alcoholcons_alcoholconswalc_fk FOREIGN KEY ( walc )
        REFERENCES alcoholconswalc ( walc );

ALTER TABLE alcoholcons
    ADD CONSTRAINT alcoholcons_human_fk FOREIGN KEY ( humanid )
        REFERENCES human ( humanid );

ALTER TABLE human
    ADD CONSTRAINT human_humanguardian_fk FOREIGN KEY ( guardian )
        REFERENCES humanguardian ( guardian );

ALTER TABLE human
    ADD CONSTRAINT human_humanhealth_fk FOREIGN KEY ( health )
        REFERENCES humanhealth ( health );

ALTER TABLE human
    ADD CONSTRAINT human_humansex_fk FOREIGN KEY ( sex )
        REFERENCES humansex ( sex );

ALTER TABLE school
    ADD CONSTRAINT school_human_fk FOREIGN KEY ( humanid )
        REFERENCES human ( humanid );

ALTER TABLE school
    ADD CONSTRAINT school_schooltitle_fk FOREIGN KEY ( title )
        REFERENCES schooltitle ( title );
