create schema if not exists err_log;

create table if not exists err_log.err_log_t(
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    v_step TEXT,
	err text
);
