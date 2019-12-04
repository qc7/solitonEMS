BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "leave_annual_planner" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"leave_year"	varchar(5) NOT NULL,
	"date_from"	date NOT NULL,
	"date_to"	date NOT NULL,
	"status"	varchar(15) NOT NULL,
	"employee_id"	integer NOT NULL,
	"leave_id"	integer NOT NULL,
	FOREIGN KEY("leave_id") REFERENCES "leave_leave_types"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "role_solitonuser" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"middleName"	varchar(20) NOT NULL,
	"password_change"	varchar(10) NOT NULL,
	"employee_id"	integer NOT NULL UNIQUE,
	"soliton_role_id"	integer NOT NULL,
	"user_id"	integer NOT NULL UNIQUE,
	"soliton_department_id"	integer NOT NULL,
	"soliton_team_id"	integer NOT NULL,
	FOREIGN KEY("soliton_department_id") REFERENCES "employees_departments"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("soliton_role_id") REFERENCES "role_solitonrole"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("soliton_team_id") REFERENCES "employees_teams"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "employees_employee" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"first_name"	varchar(30) NOT NULL,
	"last_name"	varchar(30) NOT NULL,
	"basic_salary"	varchar(20) NOT NULL,
	"grade"	varchar(3) NOT NULL,
	"gender"	varchar(10) NOT NULL,
	"start_date"	date NOT NULL,
	"marital_status"	varchar(10) NOT NULL,
	"dob"	date NOT NULL,
	"nationality"	varchar(20) NOT NULL,
	"nssf_no"	varchar(20) NOT NULL,
	"telephone_no"	varchar(20) NOT NULL,
	"residence_address"	varchar(20) NOT NULL,
	"national_id"	varchar(20) NOT NULL,
	"ura_tin"	varchar(20) NOT NULL,
	"image_url"	varchar(20) NOT NULL,
	"leave_balance"	integer NOT NULL,
	"leave_status"	varchar(45) NOT NULL
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "role_notification" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"message"	text NOT NULL,
	"date_time"	datetime NOT NULL,
	"status"	varchar(10) NOT NULL,
	"user_id"	integer NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "role_solitonuser"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "role_solitonrole" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS "payroll_payroll" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"employee_nssf"	varchar(15) NOT NULL,
	"employer_nssf"	varchar(15) NOT NULL,
	"gross_salary"	varchar(15) NOT NULL,
	"net_salary"	varchar(15) NOT NULL,
	"paye"	varchar(20) NOT NULL,
	"total_nssf_contrib"	varchar(20) NOT NULL,
	"total_statutory"	varchar(20) NOT NULL,
	"overtime"	varchar(20) NOT NULL,
	"bonus"	varchar(20) NOT NULL,
	"sacco_deduction"	varchar(20) NOT NULL,
	"damage_deduction"	varchar(20) NOT NULL,
	"prorate"	varchar(20) NOT NULL,
	"employee_id"	integer NOT NULL,
	"payroll_record_id"	integer NOT NULL,
	FOREIGN KEY("employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("payroll_record_id") REFERENCES "payroll_payrollrecord"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "payroll_payrollrecord" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"year"	varchar(20) NOT NULL,
	"month"	varchar(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS "leave_leaveapplication" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"apply_date"	date NOT NULL,
	"start_date"	date NOT NULL,
	"end_date"	date NOT NULL,
	"no_of_days"	integer NOT NULL,
	"supervisor"	varchar(45) NOT NULL,
	"sup_Status"	varchar(15) NOT NULL,
	"hod"	varchar(45) NOT NULL,
	"hod_status"	varchar(15) NOT NULL,
	"hr"	varchar(45) NOT NULL,
	"hr_status"	varchar(15) NOT NULL,
	"app_status"	varchar(10) NOT NULL,
	"remarks"	text NOT NULL,
	"balance"	integer NOT NULL,
	"employee_id"	integer NOT NULL,
	"leave_type_id"	integer NOT NULL,
	FOREIGN KEY("employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("leave_type_id") REFERENCES "leave_leave_types"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "leave_leave_types" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"leave_type"	varchar(45) NOT NULL,
	"leave_days"	integer NOT NULL,
	"description"	text NOT NULL
);
CREATE TABLE IF NOT EXISTS "leave_holidays" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"holiday_date"	date NOT NULL,
	"holiday_name"	varchar(50) NOT NULL,
	"duration"	varchar(15) NOT NULL
);
CREATE TABLE IF NOT EXISTS "leave_approval_path" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"path_name"	varchar(45) NOT NULL,
	"required"	bool NOT NULL,
	"first_approval"	varchar(45) NOT NULL,
	"second_approval"	varchar(45) NOT NULL,
	"third_approval"	varchar(45) NOT NULL,
	"fourth_approval"	varchar(45) NOT NULL
);
CREATE TABLE IF NOT EXISTS "employees_bankdetail" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name_of_bank"	varchar(20) NOT NULL,
	"branch"	varchar(20) NOT NULL,
	"bank_account"	varchar(20) NOT NULL,
	"employee_id"	integer NOT NULL UNIQUE,
	FOREIGN KEY("employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "employees_organisationdetail" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"department_id"	integer NOT NULL,
	"employee_id"	integer NOT NULL UNIQUE,
	"position_id"	integer NOT NULL,
	"team_id"	integer NOT NULL,
	FOREIGN KEY("department_id") REFERENCES "employees_departments"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("position_id") REFERENCES "employees_job_titles"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("team_id") REFERENCES "employees_teams"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "employees_beneficiary" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(40) NOT NULL,
	"relationship"	varchar(40) NOT NULL,
	"mobile_number"	varchar(40) NOT NULL,
	"percentage"	varchar(40) NOT NULL,
	"employee_id"	integer NOT NULL,
	FOREIGN KEY("employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "employees_certification" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"institution"	varchar(100) NOT NULL,
	"name"	varchar(100) NOT NULL,
	"year_completed"	varchar(4) NOT NULL,
	"grade"	varchar(20) NOT NULL,
	"employee_id"	integer NOT NULL,
	FOREIGN KEY("employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "employees_deduction" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(20) NOT NULL,
	"amount"	integer NOT NULL,
	"employee_id"	integer NOT NULL,
	FOREIGN KEY("employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "employees_dependant" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(40) NOT NULL,
	"dob"	date NOT NULL,
	"gender"	varchar(40) NOT NULL,
	"employee_id"	integer NOT NULL,
	FOREIGN KEY("employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "employees_emergencycontact" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(40) NOT NULL,
	"relationship"	varchar(40) NOT NULL,
	"mobile_number"	varchar(50) NOT NULL,
	"email"	varchar(40) NOT NULL,
	"employee_id"	integer NOT NULL,
	FOREIGN KEY("employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "employees_leave" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"designation"	varchar(20) NOT NULL,
	"nin"	varchar(30) NOT NULL,
	"department"	varchar(15) NOT NULL,
	"apply_date"	date NOT NULL,
	"_year"	varchar(4) NOT NULL,
	"start_date"	date NOT NULL,
	"end_date"	date NOT NULL,
	"supervisor"	varchar(45) NOT NULL,
	"sup_Status"	varchar(15) NOT NULL,
	"hod"	varchar(45) NOT NULL,
	"hod_status"	varchar(15) NOT NULL,
	"Employee_id"	integer NOT NULL,
	FOREIGN KEY("Employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "employees_spouse" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(40) NOT NULL,
	"national_id"	varchar(40) NOT NULL,
	"dob"	date NOT NULL,
	"occupation"	varchar(40) NOT NULL,
	"telephone"	varchar(40) NOT NULL,
	"nationality"	varchar(40) NOT NULL,
	"passport_number"	varchar(40) NOT NULL,
	"alien_certificate_number"	varchar(40) NOT NULL,
	"immigration_file_number"	varchar(40) NOT NULL,
	"employee_id"	integer NOT NULL,
	FOREIGN KEY("employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "employees_teams" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(45) NOT NULL,
	"supervisors"	varchar(45) NOT NULL,
	"status"	varchar(15) NOT NULL,
	"department_id"	integer NOT NULL,
	FOREIGN KEY("department_id") REFERENCES "employees_departments"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "employees_homeaddress" (
	"employee_id"	integer NOT NULL,
	"district"	varchar(20) NOT NULL,
	"division"	varchar(20) NOT NULL,
	"county"	varchar(20) NOT NULL,
	"sub_county"	varchar(20) NOT NULL,
	"parish"	varchar(20) NOT NULL,
	"village"	varchar(20) NOT NULL,
	"address"	varchar(20) NOT NULL,
	"telephone"	varchar(20) NOT NULL,
	FOREIGN KEY("employee_id") REFERENCES "employees_employee"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("employee_id")
);
CREATE TABLE IF NOT EXISTS "employees_job_titles" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"title"	varchar(45) NOT NULL,
	"positions"	integer NOT NULL
);
CREATE TABLE IF NOT EXISTS "employees_departments" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(45) NOT NULL,
	"hod"	varchar(45) NOT NULL,
	"status"	varchar(15) NOT NULL
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(150) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"first_name"	varchar(30) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"last_name"	varchar(150) NOT NULL
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag">=0),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL
);
INSERT INTO "leave_annual_planner" ("id","leave_year","date_from","date_to","status","employee_id","leave_id") VALUES (1,'2019','2019-08-26','2019-08-30','Pending',5,1),
 (2,'2019','2019-12-23','2019-12-27','Pending',5,1),
 (3,'2019','2019-11-04','2019-11-08','Pending',5,1),
 (4,'2019','2019-08-06','2019-08-10','Pending',5,1);
INSERT INTO "role_solitonuser" ("id","middleName","password_change","employee_id","soliton_role_id","user_id","soliton_department_id","soliton_team_id") VALUES (1,'','',1,1,1,1,1),
 (2,'','',2,3,2,1,1),
 (3,'','',3,4,3,1,1),
 (4,'','',4,2,4,1,1),
 (5,'','',5,3,5,1,1);
INSERT INTO "employees_employee" ("id","first_name","last_name","basic_salary","grade","gender","start_date","marital_status","dob","nationality","nssf_no","telephone_no","residence_address","national_id","ura_tin","image_url","leave_balance","leave_status") VALUES (1,'Kennedy','Mutua','3000000','A','Male','2019-07-31','Married','2019-07-31','Ugandan','6564','0781515','Kampala','44689','89415','asdasdas',21,'At Work'),
 (2,'John ','Nsimbi','3000000','2','Male','2011-08-19','Single','1992-08-19','Ugandan','34567890','3476890','Makindye','234567890','4657890','',18,'At Work'),
 (3,'Nansukusa','Yudaya','25000000','B','Female','2011-08-19','Married','1992-08-19','Ugandan','498','04865646','Kampala','845','432','',21,'At Work'),
 (4,'Omar','Derow','5000000','A','Male','2011-08-19','Married','1992-08-19','Kenyan','4856','075645','Kampala','495623','89556','',21,'At Work'),
 (5,'Benard','Baliddawa','1000000','D','Male','2011-08-19','Single','1992-08-19','Ugandan','4522','07546456','Kampala','74565','78452','',21,'At Work');
INSERT INTO "django_session" ("session_key","session_data","expire_date") VALUES ('ffzusfmi5v2opu64e5tjasvpnsdmz9rl','YjM5MDhiOTFmZTk3MjA3ZTlkNzlkNTZiN2YzOGUzY2FjZjFkOWQwZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1M2ExZTMzMzFiOWQ5MGVhNGI1Y2NiMjAwNjdhYTYzOTFkN2Y2M2JiIn0=','2019-08-20 12:08:23.444932'),
 ('skexni6gmp2o0httpnqhs6ndjrznc4n4','N2NhZjJmODMyNWY1MGNkZTYxODI0MDkwZTVkYzVlMGNlY2IxOTc0Yzp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5OTQyNGNlM2NkYmM3MjIxMzFlMWRiNzExNThlMGQzMGI5NzhhZDNlIn0=','2019-09-03 14:25:14.826869');
INSERT INTO "role_solitonrole" ("id","name") VALUES (1,'HR'),
 (2,'HOD'),
 (3,'Employee'),
 (4,'Supervisor');
INSERT INTO "payroll_payroll" ("id","employee_nssf","employer_nssf","gross_salary","net_salary","paye","total_nssf_contrib","total_statutory","overtime","bonus","sacco_deduction","damage_deduction","prorate","employee_id","payroll_record_id") VALUES (1,'157500.0','315000.0','3150000','2145500','847000.0','472500','1319500','0.0','0.0','0.0','0.0','0.0',1,1),
 (2,'236250.0','472500.0','4725000.0','3169250','1319500.0','708750','2028250','0.0','1575000.0','0.0','0.0','0.0',1,2),
 (3,'157500.0','315000.0','3150000','2145500','847000.0','472500','1319500','0.0','0.0','0.0','0.0','0.0',1,3),
 (4,'157500.0','315000.0','3150000','2085500','847000.0','472500','1319500','0.0','0.0','60000','0.0','0.0',2,3),
 (5,'163179','326358','3263581','2219327','881074','489537','1370611','113581','0.0','0.0','0.0','0.0',1,4),
 (6,'157500.0','315000.0','3150000','2085500','847000.0','472500','1319500','0.0','0.0','60000','0.0','0.0',2,4),
 (7,'1257500.0','2515000.0','25150000','16445500','7447000.0','3772500','11219500','0.0','0.0','0.0','0.0','0.0',3,4),
 (8,'257500.0','515000.0','5150000','3445500','1447000.0','772500','2219500','0.0','0.0','0.0','0.0','0.0',4,4),
 (9,'57500.0','115000.0','1150000','845500','247000.0','172500','419500','0.0','0.0','0.0','0.0','0.0',5,4),
 (10,'236250.0','472500.0','4725000.0','3169250','1319500.0','708750','2028250','0.0','1575000.0','0.0','0.0','0.0',1,5),
 (11,'236250.0','472500.0','4725000.0','3109250','1319500.0','708750','2028250','0.0','1575000.0','60000','0.0','0.0',2,5),
 (12,'1886250.0','3772500.0','37725000.0','24619250','11219500.0','5658750','16878250','0.0','12575000.0','0.0','0.0','0.0',3,5),
 (13,'386250.0','772500.0','7725000.0','5119250','2219500.0','1158750','3378250','0.0','2575000.0','0.0','0.0','0.0',4,5),
 (14,'86250.0','172500.0','1725000.0','1219250','419500.0','258750','678250','0.0','575000.0','0.0','0.0','0.0',5,5);
INSERT INTO "payroll_payrollrecord" ("id","year","month") VALUES (1,'2019','January'),
 (2,'2019','July'),
 (3,'2019','March'),
 (4,'2019','July'),
 (5,'2019','August');
INSERT INTO "leave_leaveapplication" ("id","apply_date","start_date","end_date","no_of_days","supervisor","sup_Status","hod","hod_status","hr","hr_status","app_status","remarks","balance","employee_id","leave_type_id") VALUES (1,'2019-07-31','2019-08-04','2019-08-06',3,'Nansukusa Yudaya','Approved','Omar Derow','Approved','Kennedy Mutua','Approved','Approved','',18,2,1),
 (8,'2019-08-05','2019-08-05','2019-08-07',8,'','Pending','','Pending','','Pending','Pending','',21,5,1),
 (9,'2019-08-05','2019-08-06','2019-08-08',7,'','Pending','','Pending','','Pending','Pending','',21,5,1),
 (10,'2019-08-05','2019-08-15','2019-08-19',10,'','Pending','','Pending','','Pending','Pending','',21,5,1);
INSERT INTO "leave_leave_types" ("id","leave_type","leave_days","description") VALUES (1,'Annual',21,'fsdfdsf'),
 (2,'Maternity',60,'dasdf'),
 (3,'Paternity',10,'ergerg');
INSERT INTO "leave_holidays" ("id","holiday_date","holiday_name","duration") VALUES (1,'2019-08-09','EID','1'),
 (2,'2019-08-03','Labor Day','1');
INSERT INTO "employees_bankdetail" ("id","name_of_bank","branch","bank_account","employee_id") VALUES (1,'Stambic Bank','Nakasero','234576890978',2);
INSERT INTO "employees_organisationdetail" ("id","department_id","employee_id","position_id","team_id") VALUES (1,1,1,1,1),
 (2,2,2,2,1),
 (3,2,3,2,1),
 (4,2,4,2,1),
 (5,2,5,2,1);
INSERT INTO "employees_beneficiary" ("id","name","relationship","mobile_number","percentage","employee_id") VALUES (1,'Alice Nalumu','Daughter','34567890','80%',2);
INSERT INTO "employees_certification" ("id","institution","name","year_completed","grade","employee_id") VALUES (1,'Uganda Christian University','Bachelor of Information Technology','2012','Second Class Upper',2),
 (2,'Makerere','Masters','2018','A',2),
 (3,'Makerere','Degree','2010','A',1);
INSERT INTO "employees_deduction" ("id","name","amount","employee_id") VALUES (1,'Sacco',60000,2);
INSERT INTO "employees_dependant" ("id","name","dob","gender","employee_id") VALUES (1,'Fresh Kid','2000-08-19','Male',2);
INSERT INTO "employees_emergencycontact" ("id","name","relationship","mobile_number","email","employee_id") VALUES (1,'Peter Walusimbi','Brother','234567890','peter@something.com',2);
INSERT INTO "employees_spouse" ("id","name","national_id","dob","occupation","telephone","nationality","passport_number","alien_certificate_number","immigration_file_number","employee_id") VALUES (1,'Teddy Nansikombi','35476890','1992-08-19','Accountant','35467890','Ugandan','3546789','34576890','34576890-0',2);
INSERT INTO "employees_teams" ("id","name","supervisors","status","department_id") VALUES (1,'HR','Kennedy','Active',1),
 (2,'Finance','BenardBaliddawa','Active',2),
 (3,'Finance','BenardBaliddawa','Active',2);
INSERT INTO "employees_homeaddress" ("employee_id","district","division","county","sub_county","parish","village","address","telephone") VALUES (2,'Kamapala','Wakiso','Entebbe','Nabweru','Wakiso','Wakiso','Wakiso','34567890');
INSERT INTO "employees_job_titles" ("id","title","positions") VALUES (1,'HR',2),
 (2,'Software Developer',3),
 (4,'Accountant',6);
INSERT INTO "employees_departments" ("id","name","hod","status") VALUES (1,'HR & Admin','Kennedy Mutua','Active'),
 (2,'Finance and Procurement','Kennedy Mutua','Active');
INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","first_name","email","is_staff","is_active","date_joined","last_name") VALUES (1,'pbkdf2_sha256$150000$7jjTNWMhVmED$w15/Z4I8NrEVI97vB1P/7NCapa9esx36Sn+fGE5rPOg=','2019-08-20 13:17:24.913780',1,'hr','','',1,1,'2019-07-31 07:21:05.843726',''),
 (2,'pbkdf2_sha256$150000$csx3nTcT58E9$QOEdUnlR1UDg0cGDFcU2jryXUIanYrh65wD+1OtDERE=','2019-08-02 14:48:21.390184',0,'nsimbi','','',0,1,'2019-07-31 08:32:02.630947',''),
 (3,'pbkdf2_sha256$150000$toGXkzPNgnGX$gnK4/2DQc9GmcWJcgMmMgglXivCMbq30AtzlhmUpCUg=','2019-08-05 06:03:52.363479',0,'yudaya','','',0,1,'2019-07-31 08:41:37.802700',''),
 (4,'pbkdf2_sha256$150000$HP6vYCGX2xRi$HQhflgLl8CSSVUk5UBkosIhutwk7tCX8rYPXbfDqWDo=','2019-07-31 08:49:28.439613',0,'omar','','',0,1,'2019-07-31 08:42:06.595637',''),
 (5,'pbkdf2_sha256$150000$WVlu5myoBfrY$QH5Z8gDE0vJZYQIidvT2Xd/OU1tyrIXq7Gz6neheudQ=','2019-08-20 14:25:14.741724',0,'beno','','',0,1,'2019-08-05 05:34:32.896680','');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (1,1,'add_departments','Can add departments'),
 (2,1,'change_departments','Can change departments'),
 (3,1,'delete_departments','Can delete departments'),
 (4,1,'view_departments','Can view departments'),
 (5,2,'add_employee','Can add employee'),
 (6,2,'change_employee','Can change employee'),
 (7,2,'delete_employee','Can delete employee'),
 (8,2,'view_employee','Can view employee'),
 (9,3,'add_job_titles','Can add job_ titles'),
 (10,3,'change_job_titles','Can change job_ titles'),
 (11,3,'delete_job_titles','Can delete job_ titles'),
 (12,3,'view_job_titles','Can view job_ titles'),
 (13,4,'add_homeaddress','Can add home address'),
 (14,4,'change_homeaddress','Can change home address'),
 (15,4,'delete_homeaddress','Can delete home address'),
 (16,4,'view_homeaddress','Can view home address'),
 (17,5,'add_teams','Can add teams'),
 (18,5,'change_teams','Can change teams'),
 (19,5,'delete_teams','Can delete teams'),
 (20,5,'view_teams','Can view teams'),
 (21,6,'add_spouse','Can add spouse'),
 (22,6,'change_spouse','Can change spouse'),
 (23,6,'delete_spouse','Can delete spouse'),
 (24,6,'view_spouse','Can view spouse'),
 (25,7,'add_leave','Can add leave'),
 (26,7,'change_leave','Can change leave'),
 (27,7,'delete_leave','Can delete leave'),
 (28,7,'view_leave','Can view leave'),
 (29,8,'add_emergencycontact','Can add emergency contact'),
 (30,8,'change_emergencycontact','Can change emergency contact'),
 (31,8,'delete_emergencycontact','Can delete emergency contact'),
 (32,8,'view_emergencycontact','Can view emergency contact'),
 (33,9,'add_dependant','Can add dependant'),
 (34,9,'change_dependant','Can change dependant'),
 (35,9,'delete_dependant','Can delete dependant'),
 (36,9,'view_dependant','Can view dependant'),
 (37,10,'add_deduction','Can add deduction'),
 (38,10,'change_deduction','Can change deduction'),
 (39,10,'delete_deduction','Can delete deduction'),
 (40,10,'view_deduction','Can view deduction'),
 (41,11,'add_certification','Can add certification'),
 (42,11,'change_certification','Can change certification'),
 (43,11,'delete_certification','Can delete certification'),
 (44,11,'view_certification','Can view certification'),
 (45,12,'add_beneficiary','Can add beneficiary'),
 (46,12,'change_beneficiary','Can change beneficiary'),
 (47,12,'delete_beneficiary','Can delete beneficiary'),
 (48,12,'view_beneficiary','Can view beneficiary'),
 (49,13,'add_organisationdetail','Can add organisation detail'),
 (50,13,'change_organisationdetail','Can change organisation detail'),
 (51,13,'delete_organisationdetail','Can delete organisation detail'),
 (52,13,'view_organisationdetail','Can view organisation detail'),
 (53,14,'add_bankdetail','Can add bank detail'),
 (54,14,'change_bankdetail','Can change bank detail'),
 (55,14,'delete_bankdetail','Can delete bank detail'),
 (56,14,'view_bankdetail','Can view bank detail'),
 (57,15,'add_payrollrecord','Can add payroll record'),
 (58,15,'change_payrollrecord','Can change payroll record'),
 (59,15,'delete_payrollrecord','Can delete payroll record'),
 (60,15,'view_payrollrecord','Can view payroll record'),
 (61,16,'add_payroll','Can add payroll'),
 (62,16,'change_payroll','Can change payroll'),
 (63,16,'delete_payroll','Can delete payroll'),
 (64,16,'view_payroll','Can view payroll'),
 (65,17,'add_approval_path','Can add approval_ path'),
 (66,17,'change_approval_path','Can change approval_ path'),
 (67,17,'delete_approval_path','Can delete approval_ path'),
 (68,17,'view_approval_path','Can view approval_ path'),
 (69,18,'add_holidays','Can add holidays'),
 (70,18,'change_holidays','Can change holidays'),
 (71,18,'delete_holidays','Can delete holidays'),
 (72,18,'view_holidays','Can view holidays'),
 (73,19,'add_leave_types','Can add leave_ types'),
 (74,19,'change_leave_types','Can change leave_ types'),
 (75,19,'delete_leave_types','Can delete leave_ types'),
 (76,19,'view_leave_types','Can view leave_ types'),
 (77,20,'add_leaveapplication','Can add leave application'),
 (78,20,'change_leaveapplication','Can change leave application'),
 (79,20,'delete_leaveapplication','Can delete leave application'),
 (80,20,'view_leaveapplication','Can view leave application'),
 (81,21,'add_solitonrole','Can add soliton role'),
 (82,21,'change_solitonrole','Can change soliton role'),
 (83,21,'delete_solitonrole','Can delete soliton role'),
 (84,21,'view_solitonrole','Can view soliton role'),
 (85,22,'add_solitonuser','Can add soliton user'),
 (86,22,'change_solitonuser','Can change soliton user'),
 (87,22,'delete_solitonuser','Can delete soliton user'),
 (88,22,'view_solitonuser','Can view soliton user'),
 (89,23,'add_notification','Can add notification'),
 (90,23,'change_notification','Can change notification'),
 (91,23,'delete_notification','Can delete notification'),
 (92,23,'view_notification','Can view notification'),
 (93,24,'add_logentry','Can add log entry'),
 (94,24,'change_logentry','Can change log entry'),
 (95,24,'delete_logentry','Can delete log entry'),
 (96,24,'view_logentry','Can view log entry'),
 (97,25,'add_permission','Can add permission'),
 (98,25,'change_permission','Can change permission'),
 (99,25,'delete_permission','Can delete permission'),
 (100,25,'view_permission','Can view permission'),
 (101,26,'add_group','Can add group'),
 (102,26,'change_group','Can change group'),
 (103,26,'delete_group','Can delete group'),
 (104,26,'view_group','Can view group'),
 (105,27,'add_user','Can add user'),
 (106,27,'change_user','Can change user'),
 (107,27,'delete_user','Can delete user'),
 (108,27,'view_user','Can view user'),
 (109,28,'add_contenttype','Can add content type'),
 (110,28,'change_contenttype','Can change content type'),
 (111,28,'delete_contenttype','Can delete content type'),
 (112,28,'view_contenttype','Can view content type'),
 (113,29,'add_session','Can add session'),
 (114,29,'change_session','Can change session'),
 (115,29,'delete_session','Can delete session'),
 (116,29,'view_session','Can view session'),
 (117,30,'add_annual_planner','Can add annual_planner'),
 (118,30,'change_annual_planner','Can change annual_planner'),
 (119,30,'delete_annual_planner','Can delete annual_planner'),
 (120,30,'view_annual_planner','Can view annual_planner');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (1,'employees','departments'),
 (2,'employees','employee'),
 (3,'employees','job_titles'),
 (4,'employees','homeaddress'),
 (5,'employees','teams'),
 (6,'employees','spouse'),
 (7,'employees','leave'),
 (8,'employees','emergencycontact'),
 (9,'employees','dependant'),
 (10,'employees','deduction'),
 (11,'employees','certification'),
 (12,'employees','beneficiary'),
 (13,'employees','organisationdetail'),
 (14,'employees','bankdetail'),
 (15,'payroll','payrollrecord'),
 (16,'payroll','payroll'),
 (17,'leave','approval_path'),
 (18,'leave','holidays'),
 (19,'leave','leave_types'),
 (20,'leave','leaveapplication'),
 (21,'role','solitonrole'),
 (22,'role','solitonuser'),
 (23,'role','notification'),
 (24,'admin','logentry'),
 (25,'auth','permission'),
 (26,'auth','group'),
 (27,'auth','user'),
 (28,'contenttypes','contenttype'),
 (29,'sessions','session'),
 (30,'leave','annual_planner');
INSERT INTO "django_admin_log" ("id","action_time","object_id","object_repr","change_message","content_type_id","user_id","action_flag") VALUES (1,'2019-07-31 07:26:39.009026','1','Kennedy Mutua','[{"added": {}}]',2,1,1),
 (2,'2019-07-31 07:27:06.581812','1','HR','[{"added": {}}]',21,1,1),
 (3,'2019-07-31 07:27:14.683770','2','HOD','[{"added": {}}]',21,1,1),
 (4,'2019-07-31 07:27:30.094384','3','Employee','[{"added": {}}]',21,1,1),
 (5,'2019-07-31 07:27:38.926822','4','Supervisor','[{"added": {}}]',21,1,1),
 (6,'2019-07-31 07:27:55.743424','1','hr','[{"added": {}}]',22,1,1),
 (7,'2019-07-31 07:55:57.712239','1','Teams object (1)','[{"added": {}}]',5,1,1),
 (8,'2019-07-31 07:56:27.375138','1','HR HR & Admin','[{"added": {}}]',13,1,1),
 (9,'2019-07-31 08:32:03.049870','2','nsimbi','[{"added": {}}]',27,1,1),
 (10,'2019-07-31 08:32:55.385520','2','nsimbi','[{"added": {}}]',22,1,1),
 (11,'2019-07-31 08:41:38.238535','3','yudaya','[{"added": {}}]',27,1,1),
 (12,'2019-07-31 08:42:07.016511','4','omar','[{"added": {}}]',27,1,1),
 (13,'2019-07-31 08:42:37.190581','3','yudaya','[{"added": {}}]',22,1,1),
 (14,'2019-07-31 08:42:46.934889','4','omar','[{"added": {}}]',22,1,1),
 (15,'2019-08-05 05:34:33.414473','5','beno','[{"added": {}}]',27,1,1),
 (16,'2019-08-05 05:35:26.930269','5','beno','[{"added": {}}]',22,1,1),
 (17,'2019-08-05 07:07:06.233830','5','Software Developer Finance and Procurement','[{"added": {}}]',13,1,1);
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (1,'contenttypes','0001_initial','2019-07-31 07:17:35.102587'),
 (2,'auth','0001_initial','2019-07-31 07:17:35.214798'),
 (3,'admin','0001_initial','2019-07-31 07:17:35.312705'),
 (4,'admin','0002_logentry_remove_auto_add','2019-07-31 07:17:35.412948'),
 (5,'admin','0003_logentry_add_action_flag_choices','2019-07-31 07:17:35.509441'),
 (6,'contenttypes','0002_remove_content_type_name','2019-07-31 07:17:35.633111'),
 (7,'auth','0002_alter_permission_name_max_length','2019-07-31 07:17:35.727855'),
 (8,'auth','0003_alter_user_email_max_length','2019-07-31 07:17:35.830956'),
 (9,'auth','0004_alter_user_username_opts','2019-07-31 07:17:35.936729'),
 (10,'auth','0005_alter_user_last_login_null','2019-07-31 07:17:36.072155'),
 (11,'auth','0006_require_contenttypes_0002','2019-07-31 07:17:36.186611'),
 (12,'auth','0007_alter_validators_add_error_messages','2019-07-31 07:17:36.292364'),
 (13,'auth','0008_alter_user_username_max_length','2019-07-31 07:17:36.400093'),
 (14,'auth','0009_alter_user_last_name_max_length','2019-07-31 07:17:36.503819'),
 (15,'auth','0010_alter_group_name_max_length','2019-07-31 07:17:36.607574'),
 (16,'auth','0011_update_proxy_permissions','2019-07-31 07:17:36.749074'),
 (17,'employees','0001_initial','2019-07-31 07:17:37.147987'),
 (18,'employees','0002_auto_20190731_1016','2019-07-31 07:17:37.554366'),
 (19,'leave','0001_initial','2019-07-31 07:17:37.740332'),
 (20,'payroll','0001_initial','2019-07-31 07:17:37.850921'),
 (21,'role','0001_initial','2019-07-31 07:17:38.026502'),
 (22,'sessions','0001_initial','2019-07-31 07:17:38.118183'),
 (23,'employees','0003_remove_employee_team','2019-07-31 07:25:14.127957'),
 (24,'role','0002_auto_20190805_1147','2019-08-05 08:48:10.796629'),
 (25,'leave','0002_annual_planner','2019-08-19 09:23:38.301878'),
 (26,'leave','0003_annual_planner_leave','2019-08-20 12:49:50.487162');
CREATE INDEX IF NOT EXISTS "leave_annual_planner_leave_id_1519ac29" ON "leave_annual_planner" (
	"leave_id"
);
CREATE INDEX IF NOT EXISTS "leave_annual_planner_employee_id_a9f9544d" ON "leave_annual_planner" (
	"employee_id"
);
CREATE INDEX IF NOT EXISTS "role_solitonuser_soliton_team_id_9e5f463b" ON "role_solitonuser" (
	"soliton_team_id"
);
CREATE INDEX IF NOT EXISTS "role_solitonuser_soliton_department_id_b55995a5" ON "role_solitonuser" (
	"soliton_department_id"
);
CREATE INDEX IF NOT EXISTS "role_solitonuser_soliton_role_id_066c675c" ON "role_solitonuser" (
	"soliton_role_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "role_notification_user_id_183cc26e" ON "role_notification" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "payroll_payroll_payroll_record_id_ff8524fc" ON "payroll_payroll" (
	"payroll_record_id"
);
CREATE INDEX IF NOT EXISTS "payroll_payroll_employee_id_cd24ccf6" ON "payroll_payroll" (
	"employee_id"
);
CREATE INDEX IF NOT EXISTS "leave_leaveapplication_leave_type_id_0e9fc30d" ON "leave_leaveapplication" (
	"leave_type_id"
);
CREATE INDEX IF NOT EXISTS "leave_leaveapplication_employee_id_e0f6bce9" ON "leave_leaveapplication" (
	"employee_id"
);
CREATE INDEX IF NOT EXISTS "employees_organisationdetail_team_id_449692a2" ON "employees_organisationdetail" (
	"team_id"
);
CREATE INDEX IF NOT EXISTS "employees_organisationdetail_position_id_22e59f1a" ON "employees_organisationdetail" (
	"position_id"
);
CREATE INDEX IF NOT EXISTS "employees_organisationdetail_department_id_63394300" ON "employees_organisationdetail" (
	"department_id"
);
CREATE INDEX IF NOT EXISTS "employees_beneficiary_employee_id_d1ce05bb" ON "employees_beneficiary" (
	"employee_id"
);
CREATE INDEX IF NOT EXISTS "employees_certification_employee_id_d87763ff" ON "employees_certification" (
	"employee_id"
);
CREATE INDEX IF NOT EXISTS "employees_deduction_employee_id_fbad5973" ON "employees_deduction" (
	"employee_id"
);
CREATE INDEX IF NOT EXISTS "employees_dependant_employee_id_b1af3424" ON "employees_dependant" (
	"employee_id"
);
CREATE INDEX IF NOT EXISTS "employees_emergencycontact_employee_id_e77ac0fd" ON "employees_emergencycontact" (
	"employee_id"
);
CREATE INDEX IF NOT EXISTS "employees_leave_Employee_id_b5fad2ac" ON "employees_leave" (
	"Employee_id"
);
CREATE INDEX IF NOT EXISTS "employees_spouse_employee_id_0bc8813b" ON "employees_spouse" (
	"employee_id"
);
CREATE INDEX IF NOT EXISTS "employees_teams_department_id_6b4c1ca5" ON "employees_teams" (
	"department_id"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
COMMIT;
