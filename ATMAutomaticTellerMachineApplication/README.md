# Create_Profile_and_Send_Email
The Script Is Simple an ATM Application .

## Step-1: Add Record Your Database Client User. Model Could Be Like This:
create table user_bank_info
(
	id serial not null,
	name varchar(50),
	surname varchar(50),
	email_address varchar(50),
	card_id int,
	balance int,
	created_at timestamp default now(),
	updated_at timestamp default now()
);

create unique index table_name_id_uindex
	on table_name (id);

alter table table_name
	add constraint table_name_pk
		primary key (id);


## Step-2: Run This Code

## Step-3: Select Your Process         
