CREATE TABLE [metaDb_metaobj] (
  [id] integer  PRIMARY KEY NOT NULL,
  [code] varchar(50)  NULL,
  [objType] varchar(50)  NOT NULL,
  [category] varchar(50)  NULL,
  [alias] varchar(50)  NULL,
  [physicalName] varchar(200)  NULL,
  [description] varchar(200)  NULL
);

CREATE TABLE metaDb_domain (
     metaobj_ptr_id  integer NOT NULL PRIMARY KEY,
     origin  varchar(50),
     superDomain_id  integer
);

CREATE TABLE metaDb_model (
     metaobj_ptr_id  integer NOT NULL PRIMARY KEY,
     modelPrefix  varchar(50),
     idModel  varchar(50),
     idRef  varchar(50),
     domain_id  integer NOT NULL,
     superModel  varchar(50)
);


CREATE TABLE metaDb_concept (
    metaobj_ptr_id integer NOT  NULL PRIMARY KEY ,
    model_id integer NOT NULL ,
    superConcept varchar(50)
);

CREATE TABLE metaDb_property (
     metaobj_ptr_id  integer NOT NULL PRIMARY KEY ,
     baseType  varchar(50),
     length  integer,
     decLength  integer,
     isNullable  integer NOT NULL,
     isRequired  integer NOT NULL,
     isSensitive  integer NOT NULL,
     isEssential  integer NOT NULL,
     isUnique  integer NOT NULL,
     isForeign  integer NOT NULL,
     foreignConcept  varchar(200),
     conceptPosition  integer,
     defaultValue  varchar(50),
     derivationType  varchar(50),
     derivationRule  varchar(50),
     derivationConcept  varchar(200),
     derivationProperty  varchar(200),
     concept_id  integer NOT NULL ,
     superProperty  varchar(50)
);

CREATE TABLE metaDb_relationship (
     metaobj_ptr_id  integer NOT NULL PRIMARY KEY ,
     baseMin  varchar(50),
     baseMax  varchar(50),
     refMin  varchar(50),
     refMax  varchar(50),
     concept_id  integer NOT NULL ,
     baseConcept  varchar(50)
);


CREATE TABLE metaDb_udp (
     id  integer NOT NULL PRIMARY KEY,
     code  varchar(50) NOT NULL,
     value  varchar(50),
     metaObj_id  integer NOT NULL
);
