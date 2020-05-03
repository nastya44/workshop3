DECLARE
    TYPE INTS IS VARRAY(10) OF human.health%TYPE;
    TYPE CHARS IS VARRAY(10) OF human.sex%TYPE;
    
    humanid INTS;
    health INTS;
    sex CHARS;
    age INTS;
    guardian CHARS;
BEGIN
    humanid := INTS(19,20,21,22,23,24,25,26,27,28);
    health := INTS(1,5,3,1,2,2,4,5,3,5);
    sex := CHARS('F','M','F','M','F','M','F','M','F','M');
    age := INTS(13,14,15,13,11,13,15,11,12,16);
    guardian := CHARS('mother','father','other','father','mother','other','mother','father','other','mother');
    FOR i IN 1 .. humanid.count
    LOOP
        INSERT INTO human (humanid,health,sex,age,guardian) VALUES (humanid(i),health(i),sex(i),age(i),guardian(i));
        COMMIT;
    END LOOP;
END;
