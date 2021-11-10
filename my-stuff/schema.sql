CREATE TABLE IF NOT EXISTS rain (
	timestamp NUMBER PRIMARY KEY NOT NULL
);

CREATE TABLE IF NOT EXISTS onboard (
	timestamp NUMBER PRIMARY KEY NOT NULL,
    cpu_temp NUMBER,
    gpu_temp NUMBER,
    mem_usage NUMBER,
    cpu_usage NUMBER
);
