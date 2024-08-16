stg_lgc_ods = '''
DO $$
DECLARE
    v_step TEXT;
BEGIN
        -- Truncate operations
        v_step := 'Truncating ods.dbms';
        TRUNCATE TABLE ods.dbms;

        v_step := 'Truncating ods.dbms_employee_grade';
        TRUNCATE TABLE ods.dbms_employee_grade;

        v_step := 'Truncating ods.development_environments_employee_grade';
        TRUNCATE TABLE ods.development_environments_employee_grade;

        v_step := 'Truncating ods.development_environments';
        TRUNCATE TABLE ods.development_environments;

        v_step := 'Truncating ods.domain_knowledge_levels';
        TRUNCATE TABLE ods.domain_knowledge_levels;

        v_step := 'Truncating ods.domains';
        TRUNCATE TABLE ods.domains;

        v_step := 'Truncating ods.education_levels';
        TRUNCATE TABLE ods.education_levels;

        v_step := 'Truncating ods.employee_domain_experience';
        TRUNCATE TABLE ods.employee_domain_experience;

        v_step := 'Truncating ods.employee_industry_experience';
        TRUNCATE TABLE ods.employee_industry_experience;

        v_step := 'Truncating ods.industries';
        TRUNCATE TABLE ods.industries;

        v_step := 'Truncating ods.industry_knowledge_levels';
        TRUNCATE TABLE ods.industry_knowledge_levels;

        v_step := 'Truncating ods.grades';
        TRUNCATE TABLE ods.grades;

        v_step := 'Truncating ods.platforms';
        TRUNCATE TABLE ods.platforms;

        v_step := 'Truncating ods.platforms_employee_grade';
        TRUNCATE TABLE ods.platforms_employee_grade;

        v_step := 'Truncating ods.proficiency_levels';
        TRUNCATE TABLE ods.proficiency_levels;

        v_step := 'Truncating ods.system_types';
        TRUNCATE TABLE ods.system_types;

        v_step := 'Truncating ods.system_types_employee_grade';
        TRUNCATE TABLE ods.system_types_employee_grade;

        v_step := 'Truncating ods.technologies';
        TRUNCATE TABLE ods.technologies;

        v_step := 'Truncating ods.technologies_employee_grade';
        TRUNCATE TABLE ods.technologies_employee_grade;

        v_step := 'Truncating ods.tools';
        TRUNCATE TABLE ods.tools;

        v_step := 'Truncating ods.tools_employee_grade';
        TRUNCATE TABLE ods.tools_employee_grade;

        v_step := 'Truncating ods.user_certificates';
        TRUNCATE TABLE ods.user_certificates;

        v_step := 'Truncating ods.programming_languages_employee_grade';
        TRUNCATE TABLE ods.prog_lang_employee_grade;

        v_step := 'Truncating ods.programming_languages';
        TRUNCATE TABLE ods.programming_languages;

        v_step := 'Truncating ods.employees';
        TRUNCATE TABLE ods.employees;
		
		-- Insert operations
        -- Inserting into ods.dbms
        v_step := 'Inserting into ods.dbms';
        INSERT INTO ods.dbms(id, dbm, active, sort, updated_at)
        SELECT 
            id, 
            old_id,
            dbm::text, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp
        FROM lgc.dbms;

        -- Inserting into ods.dbms_employee_grade
        v_step := 'Inserting into ods.dbms_employee_grade';
        INSERT INTO ods.dbms_employee_grade(id, employee_id, active, sort, updated_at, dbm_id, dt, grade_id)
        SELECT 
            id, 
            old_id,
            etl_func.extract_employee_id(employee_id) AS employee_id, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp AS updated_at, 
            etl_func.extract_skill_id(dbm_id) AS dbm_id, 
            etl_func.extract_date_from_text(dt) AS dt, 
            etl_func.extract_grade_id(grade_id) AS grade_id 
        FROM lgc.dbms_employee_grade;

        -- Inserting into ods.development_environments_employee_grade
        v_step := 'Inserting into ods.development_environments_employee_grade';
        INSERT INTO ods.development_environments_employee_grade(id, employee_id, active, sort, updated_at, "date", dev_environment_id, grade_id)
        SELECT 
            id, 
            old_id,
            etl_func.extract_employee_id(employee_id) AS employee_id, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp AS updated_at, 
            etl_func.extract_date_from_text(dt) AS dt,
            etl_func.extract_skill_id(dev_environment_id) AS dev_environment_id, 
            etl_func.extract_grade_id(grade_id) AS grade_id 
        FROM lgc.development_environments_employee_grade;

        -- Inserting into ods.development_environments
        v_step := 'Inserting into ods.development_environments';
        INSERT INTO ods.development_environments(id, dev_environment, active, sort, updated_at)
        SELECT 
            id, 
            old_id,
            dev_environment::text, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp
        FROM lgc.development_environments;

        -- Inserting into ods.domain_knowledge_levels
        v_step := 'Inserting into ods.domain_knowledge_levels';
        INSERT INTO ods.domain_knowledge_levels(id, domain_knowledge_level, active, sort, updated_at)
        SELECT 
            id,
            old_id,
            domain_knowledge_level::text AS domain_knowledge_level, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp
        FROM lgc.domain_knowledge_levels;

        -- Inserting into ods.domains
        v_step := 'Inserting into ods.domains';
        INSERT INTO ods.domains(id, "domain", active, sort, updated_at)
        SELECT 
            id, 
            old_id,
            "domain"::text AS "domain", 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp
        FROM lgc.domains;

        -- Inserting into ods.education_levels
        v_step := 'Inserting into ods.education_levels';
        INSERT INTO ods.education_levels(id, education_level, active, sort, updated_at)
        SELECT 
            id, 
            old_id,
            education_level::text, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp
        FROM lgc.education_levels;

        -- Inserting into ods.employee_domain_experience
        v_step := 'Inserting into ods.employee_domain_experience';
        INSERT INTO ods.employee_domain_experience(id, employee_id, active, sort, updated_at, "date", domain_id, domain_knowledge_level_id)
        SELECT 
            id, 
            old_id,
            user_id AS employee_id, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp, 
            etl_func.extract_date_from_text(dt) AS dt,
            etl_func.extract_skill_id("domain") AS "domain_id", 
            etl_func.extract_grade_id(domain_knowledge_level) AS domain_knowledge_level_id
        FROM lgc.employee_domain_experience;

        -- Inserting into ods.employee_industry_experience
        v_step := 'Inserting into ods.employee_industry_experience';
        INSERT INTO ods.employee_industry_experience(id, employee_id, active, sort, updated_at, "date", industry_id, industry_knowledge_level_id)
        SELECT 
            id, 
            old_id,
            user_id AS employee_id, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp, 
            etl_func.extract_date_from_text(dt) AS dt,
            etl_func.extract_skill_id(industry) AS industry_id, 
            etl_func.extract_grade_id(industry_knowledge_level) AS industry_knowledge_level_id
        FROM lgc.employee_industry_experience;

        -- Inserting into ods.industries
        v_step := 'Inserting into ods.industries';
        INSERT INTO ods.industries(id, industry, active, sort, updated_at)
        SELECT 
            id, 
            old_id,
            industry::text, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp
        FROM lgc.industries;

        -- Inserting into ods.industry_knowledge_levels
        v_step := 'Inserting into ods.industry_knowledge_levels';
        INSERT INTO ods.industry_knowledge_levels(id, industry_knowledge_level, active, sort, updated_at)
        SELECT 
            id, 
            old_id,
            industry_knowledge_level::text, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp
        FROM lgc.industry_knowledge_levels;

        -- Inserting into ods.grades
        v_step := 'Inserting into ods.grades';
        INSERT INTO ods.grades(id, grade, active, sort, updated_at)
        SELECT 
            id, 
            old_id,
            grade::text, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp
        FROM lgc.grades;

        -- Inserting into ods.platforms
        v_step := 'Inserting into ods.platforms';
        INSERT INTO ods.platforms(id, platform, active, sort, updated_at)
        SELECT
            id, 
            old_id,
            platform::text, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp
        FROM lgc.platforms;

        -- Inserting into ods.platforms_employee_grade
        v_step := 'Inserting into ods.platforms_employee_grade';
        INSERT INTO ods.platforms_employee_grade(id, employee_id, active, sort, updated_at, "date", platform_id, grade_id)
        SELECT 
            id, 
            old_id,
            user_id, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp, 
            etl_func.extract_date_from_text(dt) AS dt,
            etl_func.extract_skill_id(platform_id) AS platform_id, 
            etl_func.extract_grade_id(grade_id) AS grade_id
        FROM lgc.platforms_employee_grade;

        -- Inserting into ods.proficiency_levels
        v_step := 'Inserting into ods.proficiency_levels';
        INSERT INTO ods.proficiency_levels(id, proficiency_level, active, sort, updated_at)
        SELECT 
            id, 
            old_id,
            proficiency_level::text AS proficiency_level, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp
        FROM lgc.proficiency_levels;

        -- Inserting into ods.system_types
        v_step := 'Inserting into ods.system_types';
        INSERT INTO ods.system_types(id, system_type, active, sort, updated_at)
        SELECT 
            id,
            old_id,
            system_type::text, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp
        FROM lgc.system_types;

        -- Inserting into ods.system_types_employee_grade
        v_step := 'Inserting into ods.system_types_employee_grade';
        INSERT INTO ods.system_types_employee_grade(id, employee_id, active, sort, updated_at, "date", system_type_id, grade_id)
        SELECT 
            id, 
            old_id,
            etl_func.extract_employee_id(employee_id) AS employee_id, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp AS updated_at, 
            etl_func.extract_date_from_text(dt) AS dt,
            etl_func.extract_skill_id(system_type_id) AS system_type_id, 
            etl_func.extract_grade_id(grade_id) AS grade_id
        FROM lgc.system_types_employee_grade;

        -- Inserting into ods.technologies
        v_step := 'Inserting into ods.technologies';
        INSERT INTO ods.technologies(id, technology, active, sort, updated_at)
        SELECT 
            id,
            old_id,
            technology::text, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp AS updated_at
        FROM lgc.technologies;

        -- Inserting into ods.technologies_employee_grade
        v_step := 'Inserting into ods.technologies_employee_grade';
        INSERT INTO ods.technologies_employee_grade(id, employee_id, active, sort, updated_at, "date", technology_id, grade_id)
        SELECT 
            id, 
            old_id,
            etl_func.extract_employee_id(employee_id) AS employee_id, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp AS updated_at,
            etl_func.extract_date_from_text(dt) AS dt,
            etl_func.extract_skill_id(technology_id) AS technology_id, 
            etl_func.extract_grade_id(grade_id) AS grade_id
        FROM lgc.technologies_employee_grade;

        -- Inserting into ods.tools
        v_step := 'Inserting into ods.tools';
        INSERT INTO ods.tools(id, tool, active, sort, updated_at)
        SELECT 
            id, 
            old_id,
            tool::text, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp AS updated_at
        FROM lgc.tools;

        -- Inserting into ods.tools_employee_grade
        v_step := 'Inserting into ods.tools_employee_grade';
        INSERT INTO ods.tools_employee_grade(id, employee_id, active, sort, updated_at, dt, tool_id, grade_id)
        SELECT 
            id, 
            old_id,
            etl_func.extract_employee_id(employee_id) AS employee_id, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp AS updated_at,
            etl_func.extract_date_from_text(dt) AS dt,
            etl_func.extract_skill_id(tool_id) AS tool_id, 
            etl_func.extract_grade_id(grade_id) AS grade_id
        FROM lgc.tools_employee_grade;

        -- Inserting into ods.user_certificates
        v_step := 'Inserting into ods.user_certificates';
        INSERT INTO ods.user_certificates(id, employee_id, active, sort, updated_at, certificate_year, certificate_name, issuing_organization)
        SELECT 
            id, 
            old_id,
            employee_id, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp AS updated_at, 
            certificate_year::int4, 
            certificate_name, 
            issuing_organization
        FROM lgc.user_certificates;

        -- Inserting into ods.prog_lang_employee_grade
        v_step := 'Inserting into ods.programming_languages_employee_grade';
        INSERT INTO ods.programming_languages_employee_grade(id, employee_id, active, sort, updated_at, "date", programming_language_id, grade_id)
        SELECT 
            id, 
            old_id,
            etl_func.extract_employee_id(employee_id) AS employee_id, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp AS updated_at, 
            etl_func.extract_date_from_text(dt) AS dt, 
            etl_func.extract_skill_id(programming_language_id) AS programming_language_id,
            etl_func.extract_grade_id(grade_id) AS grade_id
        FROM lgc.prog_lang_employee_grade;

        -- Inserting into ods.programming_languages
        v_step := 'Inserting into ods.programming_languages';
        INSERT INTO ods.programming_languages(id, programming_language, active, sort, updated_at)
        SELECT 
            id, 
            old_id,
            programming_language::text, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            sort::int4, 
            TO_TIMESTAMP(updated_at, 'DD.MM.YYYY HH24:MI:SS')::timestamp AS updated_at
        FROM lgc.programming_languages;

        -- Inserting into ods.employees
        v_step := 'Inserting into ods.employees';
        INSERT INTO ods.employees(id, old_id, birth_date, active, gender, last_name, first_name, last_authorization, "position", cfo, registration_date, update_date, department, email, login, company, city_of_residence)
        SELECT 
            id, 
            old_id, 
            birth_date::date, 
            CASE WHEN active = 'Да' THEN true ELSE false END AS active, 
            gender, 
            last_name, 
            first_name,
            TO_TIMESTAMP(last_authorization, 'DD.MM.YYYY HH24:MI:SS')::timestamp AS last_authorization,
            "position", 
            cfo, 
            registration_date,
            updated_at, 
            regexp_replace(departments, '^(\s*\.\s*)+', '') AS departments, 
            email, 
            login, 
            company, 
            city_of_residence
        FROM lgc.employees;
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
            ROLLBACK;
        RAISE;
END $$;
'''