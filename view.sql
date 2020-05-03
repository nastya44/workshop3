CREATE VIEW HUMAN_INFO AS
    SELECT
       human.humanid,
       sex,
       age,
       health,
       guardian,
       school.title,
       alcoholcons.dalc,
       alcoholcons.walc
    FROM
        human
        INNER JOIN school ON human.humanid = school.humanid
        INNER JOIN alcoholcons ON human.humanid = alcoholcons.humanid;
