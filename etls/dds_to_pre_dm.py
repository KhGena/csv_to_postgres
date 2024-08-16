dds_to_pre_dm = '''
DO $$
DECLARE
    v_step TEXT;
BEGIN
    -- Начало транзакции
    BEGIN
        -- insertion_employee_cer_table
        v_step := 'Truncating pre_dm.employee_certificate';
        TRUNCATE TABLE pre_dm.employee_certificate;

        v_step := 'Inserting into pre_dm.employee_certificate';
        INSERT INTO pre_dm.employee_certificate(user_id, title, "year")
        SELECT 
            user_id,
            title, 
            "year"
        FROM dds.employee_certificate;

        -- insertion_employee_table
        v_step := 'Truncating pre_dm.employee';
        TRUNCATE TABLE pre_dm.employee;

        v_step := 'Inserting into pre_dm.employee';
        INSERT INTO pre_dm.employee(id, "name", surname, email, department, "position")
        SELECT 
            id, 
            "name", 
            surname, 
            email, 
            department, 
            "position"
        FROM dds.employee;

        -- insertion_employee_year_cer_flag
        v_step := 'Truncating pre_dm.employee_year_cer_flag';
        TRUNCATE TABLE pre_dm.employee_year_cer_flag;

        v_step := 'Inserting into pre_dm.employee_year_cer_flag';
        WITH RECURSIVE years AS (
          SELECT 1997 AS year
          UNION
          SELECT year + 1 AS year
          FROM years
          WHERE year < EXTRACT(YEAR FROM NOW())
        ),
        user_years AS (
          SELECT *
          FROM years, (SELECT DISTINCT id FROM pre_dm.employee e) AS e
        ),
        user_cer_prev_year AS (
          SELECT id,
                 year,
                 CASE
                   WHEN EXISTS(SELECT *
                                 FROM pre_dm.employee_certificate ec
                                 WHERE u.id = user_id AND u.year = ec.year)
                   THEN 1
                   ELSE 0
                 END cer_flag
          FROM user_years u
          ORDER BY id, year DESC
        )
        INSERT INTO pre_dm.employee_year_cer_flag(id, "year", cer_flag)
        SELECT *
        FROM user_cer_prev_year;

        -- insertion_esg_and_skills_tables
        v_step := 'Truncating pre_dm.employee_skill_grade';
        TRUNCATE TABLE pre_dm.employee_skill_grade;

        v_step := 'Truncating pre_dm.skills';
        TRUNCATE TABLE pre_dm.skills;

        v_step := 'Calling etl_func.pre_dm_em_skill_grade for dbms_and_employee_grade';
        CALL etl_func.pre_dm_em_skill_grade('dbms_and_employee_grade', 'dbms', 'dbms', 'dbms');

        v_step := 'Calling etl_func.pre_dm_em_skill_grade for program_and_employee_grade';
        CALL etl_func.pre_dm_em_skill_grade('program_and_employee_grade', 'program', 'program', 'program');

        v_step := 'Calling etl_func.pre_dm_em_skill_grade for programming_language_and_employee_grade';
        CALL etl_func.pre_dm_em_skill_grade('programming_language_and_employee_grade', 'programming_language', 'programming_language', 'prog_lang');

        v_step := 'Calling etl_func.pre_dm_em_skill_grade for tool_and_employee_grade';
        CALL etl_func.pre_dm_em_skill_grade('tool_and_employee_grade', 'tool', 'tool', 'tool');

        v_step := 'Calling etl_func.pre_dm_em_skill_grade for framework_and_employee_grade';
        CALL etl_func.pre_dm_em_skill_grade('framework_and_employee_grade', 'framework', 'framework', 'framework');

        v_step := 'Calling etl_func.pre_dm_em_skill_grade for platform_and_employee_grade';
        CALL etl_func.pre_dm_em_skill_grade('platform_and_employee_grade', 'platform', 'platform', 'platform');

        v_step := 'Calling etl_func.pre_dm_software_type_em_skill_grade for software_type_employee_grade';
        CALL etl_func.pre_dm_software_type_em_skill_grade('software_type_employee_grade', 'software_type', 'software_type', 'type', 'sw_t');

        -- insertion_grade_table
        v_step := 'Truncating pre_dm.grade';
        TRUNCATE TABLE pre_dm.grade;

        v_step := 'Inserting into pre_dm.grade';
        INSERT INTO pre_dm.grade(id, grade_name)
        SELECT 
            id, 
            grade
        FROM dds.grade;

        v_step := 'Updating sort in pre_dm.grade for id 283045';
        UPDATE pre_dm.grade
        SET sort = 100
        WHERE id = 283045;

        v_step := 'Updating sort in pre_dm.grade for id 115637';
        UPDATE pre_dm.grade
        SET sort = 0
        WHERE id = 115637;

        -- Завершение транзакции
        COMMIT;

        EXCEPTION
                WHEN OTHERS THEN
                    BEGIN
                        INSERT INTO err_log.err_log_t(v_step, err)
                        VALUES (              
                            v_step,                      
                            SQLERRM                      
                        );
                        COMMIT;
                    END;
                ROLLBACK:
    END;
END;
$$
LANGUAGE plpgsql;
'''