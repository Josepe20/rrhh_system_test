CREATE TABLE rrhh.departments (
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR NOT NULL,
	"status" BOOLEAN NOT NULL
);


CREATE TABLE rrhh.job_positions (
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR NOT NULL,
	"status" BOOLEAN NOT NULL
);

---------------------
CREATE TABLE rrhh.employees (
	"id" SERIAL PRIMARY KEY,
	"first_name" VARCHAR NOT NULL,
	"last_name" VARCHAR NOT NULL,
	"address" VARCHAR NOT NULL,
	"birth_date" DATE NOT NULL,
	"department_id" INTEGER,
	"job_position_id" INTEGER,
	CONSTRAINT fk_department FOREIGN KEY(department_id) REFERENCES rrhh.departments(id),
	CONSTRAINT fk_job_position FOREIGN KEY(job_position_id) REFERENCES rrhh.job_positions(id)
);

-- Elimina las restricciones existentes
ALTER TABLE rrhh.employees DROP CONSTRAINT fk_department;
ALTER TABLE rrhh.employees DROP CONSTRAINT fk_job_position;


-- Agregar la restricción de clave foránea con ON DELETE CASCADE para department_id
ALTER TABLE rrhh.employees
ADD CONSTRAINT fk_department
FOREIGN KEY (department_id) REFERENCES rrhh.departments(id) ON DELETE CASCADE;

-- Agregar la restricción de clave foránea con ON DELETE CASCADE para job_position_id
ALTER TABLE rrhh.employees
ADD CONSTRAINT fk_job_position
FOREIGN KEY (job_position_id) REFERENCES rrhh.job_positions(id) ON DELETE CASCADE;
--


-- Agregar índices para mejorar las búsquedas
CREATE INDEX idx_department_id ON rrhh.employees(department_id);
CREATE INDEX idx_job_position_id ON rrhh.employees(job_position_id);
CREATE INDEX idx_last_name ON rrhh.employees(last_name);


------------------------- Insert de datos para desarrollo ---------------------------
-- Usamos WITH para crear la CTE y realizar todas las inserciones en un solo bloque
WITH inserted_departments AS (
    -- Insertamos 5 departamentos
    INSERT INTO rrhh.departments (name, status)
    VALUES 
        ('Human Resources', TRUE),
        ('Marketing', TRUE),
        ('Finance', TRUE),
        ('IT', TRUE),
        ('Operations', TRUE)
    RETURNING id
),
inserted_job_positions AS (
    -- Insertamos 5 posiciones laborales
    INSERT INTO rrhh.job_positions (name, status)
    VALUES
        ('Manager', TRUE),
        ('Senior Developer', TRUE),
        ('Junior Developer', TRUE),
        ('Data Analyst', TRUE),
        ('Accountant', TRUE)
    RETURNING id
)
-- Ahora insertamos los empleados con las FK de los departamentos y las posiciones laborales
INSERT INTO rrhh.employees (first_name, last_name, address, birth_date, department_id, job_position_id)
VALUES
    ('John', 'Doe', '1234 Elm Street', '1990-01-15', 
     (SELECT id FROM inserted_departments LIMIT 1 OFFSET 0), 
     (SELECT id FROM inserted_job_positions LIMIT 1 OFFSET 0)),
    ('Jane', 'Smith', '5678 Oak Avenue', '1985-06-30', 
     (SELECT id FROM inserted_departments LIMIT 1 OFFSET 1), 
     (SELECT id FROM inserted_job_positions LIMIT 1 OFFSET 1)),
    ('Alice', 'Johnson', '9876 Pine Road', '1993-03-12', 
     (SELECT id FROM inserted_departments LIMIT 1 OFFSET 2), 
     (SELECT id FROM inserted_job_positions LIMIT 1 OFFSET 2)),
    ('Bob', 'Brown', '5432 Maple Lane', '1988-08-22', 
     (SELECT id FROM inserted_departments LIMIT 1 OFFSET 3), 
     (SELECT id FROM inserted_job_positions LIMIT 1 OFFSET 3)),
    ('Charlie', 'Wilson', '1111 Cedar Blvd', '1992-12-05', 
     (SELECT id FROM inserted_departments LIMIT 1 OFFSET 4), 
     (SELECT id FROM inserted_job_positions LIMIT 1 OFFSET 4));


--- Select de datos
select * from rrhh.departments d;
select * from rrhh.job_positions jp;
select * from rrhh.employees e;

---delete from rrhh.employees e where e.first_name = 'Jose';


----
SELECT
    conname AS constraint_name,
    conrelid::regclass AS table_name,
    a.attname AS column_name,
    pg_catalog.pg_get_constraintdef(c.oid, true) as definition
FROM pg_constraint c
JOIN pg_attribute a ON a.attnum = ANY(c.conkey)
WHERE conrelid = 'rrhh.employees'::regclass;




-- SELECT * FROM public.alembic_version;
-- DELETE FROM alembic_version;

