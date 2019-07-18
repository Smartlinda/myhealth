CREATE TABLE "Patient" (
	"name" varchar(255) NOT NULL,
	"DOB" DATE NOT NULL,
	"sex" BOOLEAN,
	"tel_no" varchar(255) NOT NULL,
	"address" varchar(255) NOT NULL,
	"NIN" integer NOT NULL,
	CONSTRAINT "Patient_pk" PRIMARY KEY ("NIN")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Staff" (
	"ID" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	"tel_no" varchar(255) NOT NULL,
	"email" varchar(255) NOT NULL,
	"department" integer,
	"role" varchar(255) NOT NULL,
	"hospital" integer,
	CONSTRAINT "Staff_pk" PRIMARY KEY ("ID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Department" (
	"ID" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	"hospitalID" integer NOT NULL,
	"tel_no" varchar(255) NOT NULL,
	CONSTRAINT "Department_pk" PRIMARY KEY ("ID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Hospital" (
	"ID" serial NOT NULL,
	"name" varchar(255) NOT NULL,
	"address" varchar(255) NOT NULL,
	CONSTRAINT "Hospital_pk" PRIMARY KEY ("ID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Schedule" (
	"patient" integer NOT NULL,
	"date&time" timestamp NOT NULL,
	"ID" serial NOT NULL,
	"notes" varchar,
	"waiting time" TIME NOT NULL,
	CONSTRAINT "Schedule_pk" PRIMARY KEY ("ID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Medical supply" (
	"name" varchar(255) NOT NULL,
	"ID" integer NOT NULL,
	"stock" integer NOT NULL,
	CONSTRAINT "Medical supply_pk" PRIMARY KEY ("ID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "EHR" (
	"schedule" integer NOT NULL,
	"medicalSupply" integer NOT NULL,
	"amount" integer NOT NULL,
	CONSTRAINT "EHR_pk" PRIMARY KEY ("schedule","medicalSupply")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Lab test" (
	"ID" serial NOT NULL,
	"patient" integer NOT NULL,
	"doctor" integer NOT NULL,
	"name" varchar(255) NOT NULL,
	"conductor" integer NOT NULL,
	"report" TEXT NOT NULL,
	CONSTRAINT "Lab test_pk" PRIMARY KEY ("ID")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "OrderDetail" (
	"orderID" integer NOT NULL,
	"medicalSupply" integer NOT NULL,
	"amount" integer NOT NULL,
	CONSTRAINT "OrderDetail_pk" PRIMARY KEY ("orderID","medicalSupply")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "PHR" (
	"patient" integer NOT NULL,
	"weight" DECIMAL,
	"height" DECIMAL,
	"doctorID" integer,
	"disease" varchar(255) NOT NULL,
	CONSTRAINT "PHR_pk" PRIMARY KEY ("patient")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Disease" (
	"name" varchar NOT NULL,
	CONSTRAINT "Disease_pk" PRIMARY KEY ("name")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "Order" (
	"ID" serial NOT NULL,
	"datetime" timestamp NOT NULL,
	CONSTRAINT "Order_pk" PRIMARY KEY ("ID")
) WITH (
  OIDS=FALSE
);




ALTER TABLE "Staff" ADD CONSTRAINT "Staff_fk0" FOREIGN KEY ("department") REFERENCES "Department"("ID");
ALTER TABLE "Staff" ADD CONSTRAINT "Staff_fk1" FOREIGN KEY ("hospital") REFERENCES "Hospital"("ID");

ALTER TABLE "Department" ADD CONSTRAINT "Department_fk0" FOREIGN KEY ("hospitalID") REFERENCES "Hospital"("ID");


ALTER TABLE "Schedule" ADD CONSTRAINT "Schedule_fk0" FOREIGN KEY ("patient") REFERENCES "Patient"("NIN");


ALTER TABLE "EHR" ADD CONSTRAINT "EHR_fk0" FOREIGN KEY ("schedule") REFERENCES "Schedule"("ID");
ALTER TABLE "EHR" ADD CONSTRAINT "EHR_fk1" FOREIGN KEY ("medicalSupply") REFERENCES "Medical supply"("ID");

ALTER TABLE "Lab test" ADD CONSTRAINT "Lab test_fk0" FOREIGN KEY ("patient") REFERENCES "Patient"("NIN");
ALTER TABLE "Lab test" ADD CONSTRAINT "Lab test_fk1" FOREIGN KEY ("doctor") REFERENCES "Staff"("ID");
ALTER TABLE "Lab test" ADD CONSTRAINT "Lab test_fk2" FOREIGN KEY ("conductor") REFERENCES "Staff"("ID");

ALTER TABLE "OrderDetail" ADD CONSTRAINT "OrderDetail_fk0" FOREIGN KEY ("orderID") REFERENCES "Order"("ID");
ALTER TABLE "OrderDetail" ADD CONSTRAINT "OrderDetail_fk1" FOREIGN KEY ("medicalSupply") REFERENCES "Medical supply"("ID");

ALTER TABLE "PHR" ADD CONSTRAINT "PHR_fk0" FOREIGN KEY ("patient") REFERENCES "Patient"("NIN");
ALTER TABLE "PHR" ADD CONSTRAINT "PHR_fk1" FOREIGN KEY ("doctorID") REFERENCES "Staff"("ID");
ALTER TABLE "PHR" ADD CONSTRAINT "PHR_fk2" FOREIGN KEY ("disease") REFERENCES "Disease"("name");



