create database lms;
show databases;
drop database lms;
use lms;
create table Books(BookID varchar(255),BookName varchar(255),AuthorName varchar(255),primary key(BookID));
insert into Books values("B001","Murder In Mesopotamia","Agatha Christie");
select *from Books;
update Books set BookName="Death on the Nile" where BookID="B002";
delete from Books where BookID="B001";

create table Students(StudentID varchar(255),StudentPass varchar(255),primary key(StudentID));
insert into Students values("saurabh@mylibrary.com","saurabh10");
delete from Students where StudentID="shikha@mylibarary.com"
select *from Students;

create table Librarian(LibID varchar(255),LibPass varchar(255),primary key(LibID));
insert into Librarian values("mohan@mylibrary.com","adminmohan");
select * from Librarian;

create table Issued(DateofIssue varchar(255),BookID varchar(255),StudentID varchar(255),primary key(DateofIssue));
insert into Issued values("2022-10-28 20:50:25.7686","B002","shikha@mylibrary.com");
select *from Issued;