create schema if not exists stg;

create table if not exists stg.базы_данных (
	id int4 NOT NULL,
	название text NULL,
	активность text NULL,
	"Сорт." int8 NULL,
	"Дата изм." text NULL,
	CONSTRAINT базы_данных_pkey PRIMARY KEY (id)
);

create table if not exists stg.базы_данных_и_уровень_знаний_сотру (
	id int4 NOT NULL,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	"Базы данных" text NULL,
	дата text NULL,
	"Уровень знаний" text NULL,
	CONSTRAINT базы_данных_и_уровень_знаний_со_pkey PRIMARY KEY (id)
);

create table if not exists stg.инструменты (
	id int4 NOT NULL,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	CONSTRAINT инструменты_pkey PRIMARY KEY (id)
);

create table if not exists stg.инструменты_и_уровень_знаний_сотр (
	id int4 NOT NULL,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	дата text NULL,
	инструменты text NULL,
	"Уровень знаний" text NULL,
	CONSTRAINT инструменты_и_уровень_знаний_со_pkey PRIMARY KEY (id)
);

create table if not exists stg.образование_пользователей (
	id int4 NOT NULL,
	"User ID" text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	"Уровень образование" text NULL,
	"Название учебного заведения" text NULL,
	"Фиктивное название" text NULL,
	"Факультет, кафедра" text NULL,
	специальность text NULL,
	квалификация text NULL,
	"Год окончания" text NULL,
	CONSTRAINT образование_пользователей_pkey PRIMARY KEY (id)
);

create table if not exists stg.опыт_сотрудника_в_отраслях (
	id int4 NOT NULL,
	"User ID" text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	дата text NULL,
	отрасли text NULL,
	"Уровень знаний в отрасли" text NULL,
	CONSTRAINT опыт_сотрудника_в_отраслях_pkey PRIMARY KEY (id)
);

create table if not exists stg.опыт_сотрудника_в_предметных_обла (
	id int4 NOT NULL,
	"User ID" text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	дата text NULL,
	"Предментые области" text NULL,
	"Уровень знаний в предметной облас" text NULL,
	CONSTRAINT опыт_сотрудника_в_предметных_об_pkey PRIMARY KEY (id)
);

create table if not exists stg.отрасли (
	id int4 NOT NULL,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	CONSTRAINT отрасли_pkey PRIMARY KEY (id)
);

create table if not exists stg.платформы (
	id int4 NOT NULL,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	CONSTRAINT платформы_pkey PRIMARY KEY (id)
);

create table if not exists stg.платформы_и_уровень_знаний_сотруд (
	id int4 NOT NULL,
	"User ID" text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	дата text NULL,
	платформы text NULL,
	"Уровень знаний" text NULL,
	CONSTRAINT платформы_и_уровень_знаний_сотр_pkey PRIMARY KEY (id)
);

create table if not exists stg.предметная_область (
	id int4 NOT NULL,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	CONSTRAINT предметная_область_pkey PRIMARY KEY (id)
);

create table if not exists stg.сертификаты_пользователей (
	id int4 NOT NULL,
	"User ID" text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	"Год сертификата" text NULL,
	"Наименование сертификата" text NULL,
	"Организация, выдавшая сертификат" text NULL,
	CONSTRAINT сертификаты_пользователей_pkey PRIMARY KEY (id)
);

create table if not exists stg.сотрудники (
	id int4 NOT NULL,
	"Дата рождения" text NULL,
	активность text NULL,
	пол text NULL,
	фамилия text NULL,
	имя text NULL,
	"Последняя авторизация" text NULL,
	должность text NULL,
	цфо text NULL,
	"Дата регистрации" text NULL,
	"Дата изменения" text NULL,
	подразделения text NULL,
	"E-Mail" text NULL,
	логин text NULL,
	компания text NULL,
	"Город проживания" text NULL,
	CONSTRAINT сотрудники_pkey PRIMARY KEY (id)
);

create table if not exists stg.среды_разработки (
	id int4 NOT NULL,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	CONSTRAINT среды_разработки_pkey PRIMARY KEY (id)
);

create table if not exists stg.среды_разработки_и_уровень_знаний (
	id int4 NOT NULL,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	дата text NULL,
	"Среды разработки" text NULL,
	"Уровень знаний" text NULL,
	CONSTRAINT среды_разработки_и_уровень_знан_pkey PRIMARY KEY (id)
);

create table if not exists stg.технологии (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL
);

create table if not exists stg.технологии_и_уровень_знаний_сотру (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	дата text NULL,
	технологии text NULL,
	"Уровень знаний" text NULL
);

create table if not exists stg.типы_систем (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL
);

create table if not exists stg.типы_систем_и_уровень_знаний_сотру (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	дата text NULL,
	"Типы систем" text NULL,
	"Уровень знаний" text NULL
);

create table if not exists stg.уровень_образования (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL
);

create table if not exists stg.уровни_владения_ин_я (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL
);

create table if not exists stg.уровни_знаний (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL
);

create table if not exists stg.уровни_знаний_в_отрасли (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL
);

create table if not exists stg.уровни_знаний_в_предметной_област (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL
);

create table if not exists stg.фреймворки (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL
);

create table if not exists stg.фреймворки_и_уровень_знаний_сотру (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	дата text NULL,
	фреймворки text NULL,
	"Уровень знаний" text NULL
);

create table if not exists stg.языки (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL
);

create table if not exists stg.языки_программирования (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL
);

create table if not exists stg.языки_программирования_и_уровень (
	id int4 primary key,
	название text NULL,
	активность text NULL,
	"Сорт." text NULL,
	"Дата изм." text NULL,
	дата text NULL,
	"Языки программирования" text NULL,
	"Уровень знаний" text NULL
);