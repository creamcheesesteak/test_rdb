create table information(
    id text,
    name text
)

create table information(id text, name text);

insert into information(id, name)
    values('1', '홍길동');

insert into information(id, name)
    values('2', '장길산');

insert into information(name)
    values('정몽길');

select id, name from information
where id = '2';

select id, name from information
where id is null;

select id, name from information
where id != '2'; ---> 문자

where id != 2;
where id >= 2; ---> 숫자

where name like '홍길%';

insert into information(id, name)
    values('4', '비망록');

select id, name from information
where name like '길%';

select id, name from information
where id is null;


delete from information
where id is null;

select id, name from information

delete from information
where name like '%길%';

select id, name from information

delete from information

select id, name from information

drop table information
