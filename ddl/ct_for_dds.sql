CREATE SCHEMA IF NOT EXISTS dds;

create table if not exists dds.dbms (
	id int4 NOT NULL,
	dbm text NULL,
	CONSTRAINT dbms_pkey PRIMARY KEY (id)
);

create table if not exists dds.dbms_employee_grade (
	id int4 NOT NULL,
	employee_id int4 NULL,
	dbm_id int4 NULL,
	dt date NULL,
	grade_id int4 NULL,
	sort int4 NULL,
	highest_grade int4 NULL,
	CONSTRAINT dbms_employee_grade_pkey PRIMARY KEY (id)
);

create table if not exists dds.development_environments (
	id int4 NOT NULL,
	dev_environment text NULL,
	CONSTRAINT development_environments_pkey PRIMARY KEY (id)
);

create table if not exists dds.development_environments_employee_grade (
	id int4 NOT NULL,
	employee_id int4 NULL,
	dt date NULL,
	dev_environment_id int4 NULL,
	grade_id int4 NULL,
	sort int4 NULL,
	highest_grade int4 NULL,
	CONSTRAINT dev_env_employee_grade_pkey PRIMARY KEY (id)
);

create table if not exists dds.employees (
	id int4 NOT NULL,
	birth_date date NULL,
	active bool NULL,
	last_name text NULL,
	first_name text NULL,
	"position" text NULL,
	email text NULL,
	CONSTRAINT employees_pkey PRIMARY KEY (id)
);

create table if not exists dds.frameworks (
	id int4 NOT NULL,
	framework text NULL,
	CONSTRAINT frameworks_pkey PRIMARY KEY (id)
);

create table if not exists dds.frameworks_employee_grade (
	id int4 NOT NULL,
	employee_id int4 NULL,
	dt date NULL,
	framework_id int4 NULL,
	grade_id int4 NULL,
	sort int4 NULL,
	highest_grade int4 NULL,
	CONSTRAINT frameworks_employee_grade_pkey PRIMARY KEY (id)
);

create table if not exists dds.grades (
	id int4 NOT NULL,
	grade text NULL,
	sort int4 NULL,
	CONSTRAINT grades_pkey PRIMARY KEY (id)
);

create table if not exists dds.platforms (
	id int4 NOT NULL,
	platform text NULL,
	CONSTRAINT platforms_pkey PRIMARY KEY (id)
);

create table if not exists dds.platforms_employee_grade (
	id int4 NOT NULL,
	employee_id int4 NULL,
	dt date NULL,
	platform_id int4 NULL,
	grade_id int4 NULL,
	sort int4 NULL,
	highest_grade int4 NULL,
	CONSTRAINT platforms_employee_grade_pkey PRIMARY KEY (id)
);

create table if not exists dds.prog_lang_employee_grade (
	id int4 NOT NULL,
	employee_id int4 NULL,
	dt date NULL,
	programming_language_id int4 NULL,
	grade_id int4 NULL,
	sort int4 NULL,
	highest_grade int4 NULL,
	CONSTRAINT prog_lang_employee_grade_pkey PRIMARY KEY (id)
);

create table if not exists dds.programming_languages (
	id int4 NOT NULL,
	programming_language text NULL,
	CONSTRAINT programming_languages_pkey PRIMARY KEY (id)
);

create table if not exists dds.system_types (
	id int4 NOT NULL,
	system_type text NULL,
	CONSTRAINT system_types_pkey PRIMARY KEY (id)
);

create table if not exists dds.system_types_employee_grade (
	id int4 NOT NULL,
	employee_id int4 NULL,
	dt date NULL,
	system_type_id int4 NULL,
	grade_id int4 NULL,
	sort int4 NULL,
	highest_grade int4 NULL,
	CONSTRAINT system_types_employee_grade_pkey PRIMARY KEY (id)
);

create table if not exists dds.technologies (
	id int4 NOT NULL,
	technology text NULL,
	CONSTRAINT technologies_pkey PRIMARY KEY (id)
);

create table if not exists dds.technologies_employee_grade (
	id int4 NOT NULL,
	employee_id int4 NULL,
	dt date NULL,
	technology_id int4 NULL,
	grade_id int4 NULL,
	sort int4 NULL,
	highest_grade int4 NULL,
	CONSTRAINT technologies_employee_grade_pkey PRIMARY KEY (id)
);

create table if not exists dds.tools (
	id int4 NOT NULL,
	tool text NULL,
	CONSTRAINT tools_pkey PRIMARY KEY (id)
);

create table if not exists dds.tools_employee_grade (
	id int4 NOT NULL,
	employee_id int4 NULL,
	dt date NULL,
	tool_id int4 NULL,
	grade_id int4 NULL,
	sort int4 NULL,
	highest_grade int4 NULL,
	CONSTRAINT tools_employee_grade_pkey PRIMARY KEY (id)
);

create table if not exists dds.user_certificates (
	id int4 NOT NULL,
	employee_id int4 NULL,
	certificate_year int4 NULL,
	certificate_name text NULL,
	issuing_organization text NULL,
	quantity_employee_cer int4 NULL,
	CONSTRAINT user_certificates_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS dds.grades(
	id int4 PRIMARY KEY,
	grade varchar(20) NULL,
	sort int4 NULL
);