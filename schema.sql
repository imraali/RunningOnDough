drop table if exists users;
create table users (
	name text primary key not null,
	flight text not null,
	transport text not null,
	food text not null,
    entertainment text not null,
    living text not null
);