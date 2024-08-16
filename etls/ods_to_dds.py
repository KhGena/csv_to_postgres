ods_to_dds = '''
DO $$
DECLARE
    v_step TEXT;
BEGIN
    -- Truncate operations with v_step updates
    v_step := 'Truncating dds.dbms';
    TRUNCATE TABLE dds.dbms;

    v_step := 'Truncating dds.dbms_employee_grade';
    TRUNCATE TABLE dds.dbms_employee_grade;

    v_step := 'Truncating dds.development_environments';
    TRUNCATE TABLE dds.development_environments;

    v_step := 'Truncating dds.development_environments_employee_grade';
    TRUNCATE TABLE dds.development_environments_employee_grade;

    v_step := 'Truncating dds.employees';
    TRUNCATE TABLE dds.employees;

    v_step := 'Truncating dds.frameworks';
    TRUNCATE TABLE dds.frameworks;

    v_step := 'Truncating dds.frameworks_employee_grade';
    TRUNCATE TABLE dds.frameworks_employee_grade;

    v_step := 'Truncating dds.platforms';
    TRUNCATE TABLE dds.platforms;

    v_step := 'Truncating dds.platforms_employee_grade';
    TRUNCATE TABLE dds.platforms_employee_grade;

    v_step := 'Truncating dds.prog_lang_employee_grade';
    TRUNCATE TABLE dds.prog_lang_employee_grade;

    v_step := 'Truncating dds.programming_languages';
    TRUNCATE TABLE dds.programming_languages;

    v_step := 'Truncating dds.system_types';
    TRUNCATE TABLE dds.system_types;

    v_step := 'Truncating dds.system_types_employee_grade';
    TRUNCATE TABLE dds.system_types_employee_grade;

    v_step := 'Truncating dds.technologies';
    TRUNCATE TABLE dds.technologies;

    v_step := 'Truncating dds.technologies_employee_grade';
    TRUNCATE TABLE dds.technologies_employee_grade;

    v_step := 'Truncating dds.tools';
    TRUNCATE TABLE dds.tools;

    v_step := 'Truncating dds.tools_employee_grade';
    TRUNCATE TABLE dds.tools_employee_grade;

    v_step := 'Truncating dds.user_certificates';
    TRUNCATE TABLE dds.user_certificates;

    v_step := 'Truncating dds.grades';
    TRUNCATE TABLE dds.grades;

    -- Insert operations with v_step updates
    v_step := 'Inserting into dds.dbms';
    INSERT INTO dds.dbms(id, dbm)
    SELECT 
        id, 
        dbm
    FROM 
        ods.dbms;

    v_step := 'Inserting into dds.dbms_employee_grade';
    WITH dbms_employee_grade_with_dub AS (
        SELECT
            id,
            employee_id,
            dbm_id,
            grade_id,
            dt,
            row_number() OVER (PARTITION BY employee_id, dbm_id, grade_id ORDER BY id) AS ranked_dubpicates
        FROM
            ods.dbms_employee_grade
    ),
    dbms_employee_grade_without_dub AS (
        SELECT
            id,
            employee_id,
            dbm_id,
            grade_id,
            dt
        FROM dbms_employee_grade_with_dub
        WHERE ranked_dubpicates = 1
    )
    INSERT INTO dds.dbms_employee_grade(id, employee_id, dbm_id, grade_id, dt, sort, highest_grade)
    SELECT
        deg.id AS id,
        deg.employee_id AS employee_id,
        deg.dbm_id AS dbm_id,
        deg.grade_id AS grade_id,
        deg.dt AS dt,
        g.sort AS sort,
        row_number() OVER (PARTITION BY deg.employee_id, deg.dbm_id ORDER BY g.sort DESC) AS highest_grade 
    FROM 
        dbms_employee_grade_without_dub deg
        JOIN ods.employees e ON e.id = deg.employee_id
        JOIN ods.dbms d ON d.id = deg.dbm_id
        JOIN ods.grades g ON g.id = deg.grade_id;

    v_step := 'Inserting into dds.development_environments';
    INSERT INTO dds.development_environments(id, dev_environment)
    SELECT 
        id, 
        dev_environment
    FROM 
        ods.development_environments;

    v_step := 'Inserting into dds.development_environments_employee_grade';
    WITH dev_env_employee_grade_with_dub AS (
        SELECT
            id,
            employee_id,
            dev_environment_id,
            grade_id,
            date,
            row_number() OVER (PARTITION BY employee_id, dev_environment_id, grade_id ORDER BY id) AS ranked_duplicates
        FROM
            ods.development_environments_employee_grade
    ),
    dev_env_employee_grade_without_dub AS (
        SELECT
            id,
            employee_id,
            dev_environment_id,
            grade_id,
            date
        FROM dev_env_employee_grade_with_dub
        WHERE ranked_duplicates = 1
    )
    INSERT INTO dds.development_environments_employee_grade(id, employee_id, dev_environment_id, grade_id, dt, sort, highest_grade)
    SELECT
        deeg.id AS id,
        deeg.employee_id AS employee_id,
        deeg.dev_environment_id AS dev_environment_id,
        deeg.grade_id AS grade_id,
        deeg.date AS dt,
        g.sort AS sort,
        row_number() OVER (PARTITION BY deeg.employee_id, deeg.dev_environment_id ORDER BY g.sort DESC) AS highest_grade
    FROM 
        dev_env_employee_grade_without_dub deeg
        JOIN ods.employees e ON e.id = deeg.employee_id
        JOIN ods.development_environments de ON de.id = deeg.dev_environment_id
        JOIN ods.grades g ON g.id = deeg.grade_id;

    v_step := 'Inserting into dds.employees';
    INSERT INTO dds.employees(id, birth_date, active, last_name, first_name, position, email)
    SELECT 
        id, 
        birth_date,
        active,
        last_name,
        first_name,
        position,
        email
    FROM 
        ods.employees;

    v_step := 'Inserting into dds.frameworks';
    INSERT INTO dds.frameworks(id, framework)
    SELECT 
        id, 
        framework
    FROM 
        ods.frameworks;

    v_step := 'Inserting into dds.frameworks_employee_grade';
    WITH frameworks_employee_grade_with_dub AS (
        SELECT
            id,
            employee_id,
            framework_id,
            grade_id,
            date,
            row_number() OVER (PARTITION BY employee_id, framework_id, grade_id ORDER BY id) AS ranked_duplicates
        FROM
            ods.frameworks_employee_grade
    ),
    frameworks_employee_grade_without_dub AS (
        SELECT
            id,
            employee_id,
            framework_id,
            grade_id,
            date
        FROM frameworks_employee_grade_with_dub
        WHERE ranked_duplicates = 1
    )
    INSERT INTO dds.frameworks_employee_grade(id, employee_id, framework_id, grade_id, dt, sort, highest_grade)
    SELECT
        feg.id AS id,
        feg.employee_id AS employee_id,
        feg.framework_id AS framework_id,
        feg.grade_id AS grade_id,
        feg.date AS dt,
        g.sort AS sort,
        row_number() OVER (PARTITION BY feg.employee_id, feg.framework_id ORDER BY g.sort DESC) AS highest_grade
    FROM 
        frameworks_employee_grade_without_dub feg
        JOIN ods.employees e ON e.id = feg.employee_id
        JOIN ods.frameworks f ON f.id = feg.framework_id
        JOIN ods.grades g ON g.id = feg.grade_id;

    v_step := 'Inserting into dds.platforms';
    INSERT INTO dds.platforms(id, platform)
    SELECT 
        id, 
        platform
    FROM 
        ods.platforms;

    v_step := 'Inserting into dds.platforms_employee_grade';
    WITH platforms_employee_grade_with_dub AS (
        SELECT
            id,
            employee_id,
            platform_id,
            grade_id,
            date,
            row_number() OVER (PARTITION BY employee_id, platform_id, grade_id ORDER BY id) AS ranked_duplicates
        FROM
            ods.platforms_employee_grade
    ),
    platforms_employee_grade_without_dub AS (
        SELECT
            id,
            employee_id,
            platform_id,
            grade_id,
            date
        FROM platforms_employee_grade_with_dub
        WHERE ranked_duplicates = 1
    )
    INSERT INTO dds.platforms_employee_grade(id, employee_id, platform_id, grade_id, dt, sort, highest_grade)
    SELECT
        peg.id AS id,
        peg.employee_id AS employee_id,
        peg.platform_id AS platform_id,
        peg.grade_id AS grade_id,
        peg.date AS dt,
        g.sort AS sort,
        row_number() OVER (PARTITION BY peg.employee_id, peg.platform_id ORDER BY g.sort DESC) AS highest_grade
    FROM 
        platforms_employee_grade_without_dub peg
        JOIN ods.employees e ON e.id = peg.employee_id
        JOIN ods.platforms p ON p.id = peg.platform_id
        JOIN ods.grades g ON g.id = peg.grade_id;

    v_step := 'Inserting into dds.programming_languages';
    INSERT INTO dds.programming_languages(id, programming_language)
    SELECT 
        id, 
        programming_language
    FROM 
        ods.programming_languages;

    v_step := 'Inserting into dds.prog_lang_employee_grade';
    WITH prog_lang_employee_grade_with_dub AS (
        SELECT
            id,
            employee_id,
            programming_language_id,
            grade_id,
            date,
            row_number() OVER (PARTITION BY employee_id, programming_language_id, grade_id ORDER BY id) AS ranked_duplicates
        FROM
            ods.prog_lang_employee_grade
    ),
    prog_lang_employee_grade_without_dub AS (
        SELECT
            id,
            employee_id,
            programming_language_id,
            grade_id,
            date
        FROM

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
END $$;
'''