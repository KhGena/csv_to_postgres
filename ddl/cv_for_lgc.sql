CREATE SCHEMA IF NOT EXISTS lgc;

CREATE OR REPLACE VIEW lgc.dbms AS 
SELECT
    id,
    название AS dbm,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg.базы_данных;

CREATE OR REPLACE VIEW lgc.dbms_employee_grade AS
SELECT 
    id, 
    название AS employee_id,
    активность AS active,
    "Сорт." AS sort, 
    "Дата изм." AS updated_at, 
    "Базы данных" AS dbm_id, 
    дата AS dt, 
    "Уровень знаний" AS grade_id
FROM stg.базы_данных_и_уровень_знаний_сотру;

CREATE OR REPLACE VIEW lgc.tools AS 
SELECT
    id,
    название AS tool,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg.инструменты;

CREATE OR REPLACE VIEW lgc.tools_employee_grade AS
SELECT 
    id, 
    название AS employee_id,
    активность AS active, 
    "Сорт." AS sort, 
    "Дата изм." AS updated_at, 
    инструменты AS tool_id, 
    дата AS dt, 
    "Уровень знаний" AS grade_id
FROM stg.инструменты_и_уровень_знаний_сотр;

CREATE OR REPLACE VIEW lgc.user_education AS 
SELECT
    id,
    "User ID" AS employee_id,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at,
    "Уровень образование" AS education_level,
    "Название учебного заведения" AS institution_name,
    "Фиктивное название" AS fictitious_name,
    "Факультет, кафедра" AS faculty_department,
    специальность AS specialty,
    квалификация AS qualification,
    "Год окончания" AS graduation_year
FROM stg.образование_пользователей;

CREATE OR REPLACE VIEW lgc.employee_industry_experience AS 
SELECT
    id,
    "User ID" AS employee_id,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at,
    дата AS dt,
    отрасли AS industry,
    "Уровень знаний в отрасли" AS industry_knowledge_level
FROM stg.опыт_сотрудника_в_отраслях;

CREATE OR REPLACE VIEW lgc.employee_domain_experience AS 
SELECT
    id,
    "User ID" AS employee_id,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at,
    дата AS dt,
    "Предментые области" AS domain,
    "Уровень знаний в предметной облас" AS domain_knowledge_level
FROM stg.опыт_сотрудника_в_предметных_обла;

CREATE OR REPLACE VIEW lgc.industries AS 
SELECT
    id,
    название AS industry,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg.отрасли;

CREATE OR REPLACE VIEW lgc.platforms AS 
SELECT
    id,
    название AS platform,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg.платформы;

CREATE OR REPLACE VIEW lgc.platforms_employee_grade AS
SELECT 
    id,
    "User ID" AS employee_id,
    активность AS active, 
    "Сорт." AS sort, 
    "Дата изм." AS updated_at, 
    платформы AS platform_id, 
    дата AS dt, 
    "Уровень знаний" AS grade_id
FROM stg.платформы_и_уровень_знаний_сотруд;

CREATE OR REPLACE VIEW lgc.domains AS 
SELECT
    id,
    название AS domain,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg.предметная_область;

CREATE OR REPLACE VIEW lgc.user_certificates AS 
SELECT
    id,
    "User ID" AS employee_id,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at,
    "Год сертификата" AS certificate_year,
    "Наименование сертификата" AS certificate_name,
    "Организация, выдавшая сертификат" AS issuing_organization
FROM stg.сертификаты_пользователей;

CREATE OR REPLACE VIEW lgc.employees AS 
SELECT
    id,
    "Дата рождения" AS birth_date,
    активность AS active,
    пол AS gender,
    фамилия AS last_name,
    имя AS first_name,
    "Последняя авторизация" AS last_authorization,
    должность AS position,
    цфо AS cfo,
    "Дата регистрации" AS registration_date,
    "Дата изменения" AS updated_at,
    подразделения AS departments,
    "E-Mail" AS email,
    логин AS login,
    компания AS company,
    "Город проживания" AS city_of_residence
FROM stg.сотрудники;

CREATE OR REPLACE VIEW lgc.development_environments AS 
SELECT
    id,
    название AS dev_environment,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg.среды_разработки;

CREATE OR REPLACE VIEW lgc.development_environments_employee_grade AS
SELECT 
    id,
    название AS employee_id,
    активность AS active, 
    "Сорт." AS sort, 
    "Дата изм." AS updated_at, 
    дата AS dt, 
    "Среды разработки" AS dev_environment_id, 
    "Уровень знаний" AS grade_id
FROM stg.среды_разработки_и_уровень_знаний;

CREATE OR REPLACE VIEW lgc.technologies AS 
SELECT
    id,
    название AS technology,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg.технологии;

CREATE OR REPLACE VIEW lgc.technologies_employee_grade AS
SELECT 
    id,
    название AS employee_id,
    активность AS active, 
    "Сорт." AS sort, 
    "Дата изм." AS updated_at, 
    дата AS dt, 
    технологии AS technology_id, 
    "Уровень знаний" AS grade_id
FROM stg.технологии_и_уровень_знаний_сотру;

CREATE OR REPLACE VIEW lgc.system_types AS 
SELECT
    id,
    название AS system_type,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg.типы_систем;

CREATE OR REPLACE VIEW lgc.system_types_employee_grade AS
SELECT 
    id,
    название AS employee_id,
    активность AS active, 
    "Сорт." AS sort,
    "Дата изм." AS updated_at, 
    дата AS dt, 
    "Типы систем" AS system_type_id, 
    "Уровень знаний" AS grade_id
FROM stg.типы_систем_и_уровень_знаний_сотру;

CREATE OR REPLACE VIEW lgc.education_levels AS 
SELECT
    id,
    название AS education_level,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg.уровень_образования;

CREATE OR REPLACE VIEW lgc.proficiency_levels AS 
SELECT
    id,
    название AS proficiency_level,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg.уровни_владения_ин_я;

CREATE OR REPLACE VIEW lgc.grades
AS SELECT id,
    "название" AS grade,
    "активность" AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
   FROM stg."уровни_знаний";

CREATE OR REPLACE VIEW lgc.industry_knowledge_levels AS 
SELECT
    id,
    название AS industry_knowledge_level,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg.уровни_знаний_в_отрасли;

CREATE OR REPLACE VIEW lgc.domain_knowledge_levels AS 
SELECT
    id,
    название AS domain_knowledge_level,
    активность AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg.уровни_знаний_в_предметной_област;

CREATE OR REPLACE VIEW lgc.platforms_employee_grade AS
SELECT 
    id,
    "User ID" AS employee_id,
    "активность" AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at,
    "платформы" AS platform_id,
    "дата" AS dt,
    "Уровень знаний" AS grade_id
FROM stg."платформы_и_уровень_знаний_сотруд";

CREATE OR REPLACE VIEW lgc.system_types_employee_grade AS
SELECT 
    id,
    "название" AS employee_id,
    "активность" AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at,
    "дата" AS dt,
    "Типы систем" AS system_type_id,
    "Уровень знаний" AS grade_id
FROM stg."типы_систем_и_уровень_знаний_сотру";

CREATE OR REPLACE VIEW lgc.technologies_employee_grade AS
SELECT 
    id,
    "название" AS employee_id,
    "активность" AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at,
    "дата" AS dt,
    "технологии" AS technology_id,
    "Уровень знаний" AS grade_id
FROM stg."технологии_и_уровень_знаний_сотру";

CREATE OR REPLACE VIEW lgc.programming_languages AS
SELECT 
    id,
    "название" AS programming_language,
    "активность" AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg."языки_программирования";

CREATE OR REPLACE VIEW lgc.programming_languages_employee_grade AS
SELECT 
    id,
    "название" AS employee_id,
    "активность" AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at,
    "дата" AS dt,
    "Языки программирования" AS programming_language_id,
    "Уровень знаний" AS grade_id
FROM stg."языки_программирования_и_уровень";

CREATE OR REPLACE VIEW lgc.frameworks_employee_grade AS
SELECT 
    id,
    "название" AS employee_id,
    "активность" AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at,
    "дата" AS dt,
    "фреймворки" AS framework_id,
    "Уровень знаний" AS grade_id
FROM stg."фреймворки_и_уровень_знаний_сотру";

CREATE OR REPLACE VIEW lgc.frameworks AS
SELECT 
    id,
    "название" AS framework,
    "активность" AS active,
    "Сорт." AS sort,
    "Дата изм." AS updated_at
FROM stg."фреймворки";