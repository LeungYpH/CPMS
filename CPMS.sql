create table department(
        dept_name varchar(20) primary key ,
    building varchar(15)
);

create table manager(
    m_id varchar(8) primary key ,
    dept_name varchar(20) references department,
    phone varchar(11) check ( phone rlike '[1][35678][0-9]{9}')
);
create table region (
    area_id varchar(8) primary key ,
    location varchar(50),
    area numeric(10,2)
);
create table arrange(
  m_id varchar(20) references manager(m_id),
  a_id varchar(20) references region(area_id),
  primary key (m_id,a_id)
);
create table familia(
    family_name varchar(20) primary key
);
create table genus(
    genus_name varchar(20) primary key ,
    family_name varchar(20) references familia(family_name) on update cascade on delete cascade
);
create table species(
    species_name varchar(50) primary key ,
    genus_name varchar(20) references genus(genus_name) on update cascade on delete cascade ,
    desp varchar(150)
                    );
create table living(
    ID varchar(5),
    species_name varchar(50) references species(species_name) on update cascade on delete cascade ,
    area_id varchar(8) references region(area_id) on update cascade on delete cascade ,
    height numeric(5,2) check ( height>0 ),
    primary key (ID,species_name)
);

create procedure add_new_species(in familyName varchar(20),genusName varchar(20),speciesName varchar(20),introduction varchar(150))
begin
    if not familyName in (select family_name from familia)
        then insert into familia values (familyName);
    end if;
    if not genusName in (select genus_name from genus)
        then insert into genus values (genusName,familyName);
    end if;
    insert into species values (speciesName,genusName,introduction);

end;


insert into region (area_id, location, area)
values ('A00001','XiYuan Dormitory Area',2000000.34);
insert into region values ('A00002','First Teaching Building',165000.23);
insert into region values ('B00001','South-West Gate',15000.00);
insert into region values ('B00002','MingYuan Lake',150000.00);
insert into region values ('B00003','MingYuan Avenues',100000);
insert into region values ('C00001','BuGao Shan Mount',50000);
insert into region values ('B00004','Environment College',30000);
insert into region values ('C00002','Scenery Waterway',25000.00);
insert into region values ('C00003','Art Buildings',25000.00);
insert into region values ('A00003','DongYuan Dormitory Area',15000.00);
insert into region values ('B00005','East Gate',300000);
insert into region values ('B00006','South Gate',10000);
#桂花
insert into familia values ('Oleaceae');
insert into genus values ('Osmanthus Lour.','Oleaceae');
insert into species values ('Osmanthus sp.','Osmanthus Lour.','');

# 细叶榕
insert into familia values ('Moraceae Gaudich');
insert into genus values ('Ficus','Moraceae Gaudich');
insert into species values ('Ficus microcarpa','Ficus','');
#黄葛
insert into species values ('Ficus virens Aiton','Ficus','');
#蓝花楹
insert into familia values ('Bignoniaceae');
insert into genus values ('Jacaranda Juss.','Bignoniaceae');
insert into species values ('Jacaranda mimosifolia','Jacaranda Juss.','');
#白玉兰
insert into familia values ('Magnoliaceae');
insert into genus values ('Yulania','Magnoliaceae');
insert into species values ('Yulania denudata','Yulania Spach','');
#含笑花
insert into genus values ('Michelia','Magnoliaceae');
insert into species values ('Michelia figo','Michelia','');
#银杏
insert into familia values ('Ginkgoaceae');
insert into genus values ('Ginkgo L.','Ginkgoaceae');
insert into species values ('Ginkgo biloba','Ginkgo L.','');
#木本绣球
insert into familia values ('Caprifoliaceae');
insert into genus values ('Viburnum L.','Caprifoliaceae');
insert into species values ('Viburnum macrocephalum','Viburnum L.','');
#日本晚樱
insert into familia values('Rosaceae');
insert into genus values ('Prunus L.','Rosaceae');
insert into species values ('Prunus serrulata var.','Prunus L.','');
#垂丝海棠
insert into genus values('Malus Mill.','Rosaceae');
insert into species values ('Malus halliana Koehne','Malus Mill.','');

#桃花
insert into genus values ('Amygdalus','Rosaceae');
insert into species values ('Amygdalus persica','Amygdalus','');
#沙梨
insert into genus values ('Pyrus','Rosaceae');
insert into species values ('Pyrus pyrifolia','Pyrus','');


#桂花
insert into living values('0001','Osmanthus sp.','A00001',3.2);
insert into living values('0002','Osmanthus sp.','A00001',2.13);
insert into living values('0003','Osmanthus sp.','A00001',3.22);
insert into living values('0004','Osmanthus sp.','A00001',3.02);
insert into living values('0005','Osmanthus sp.','A00001',2.92);
insert into living values('0006','Osmanthus sp.','A00001',2.72);
insert into living values('0007','Osmanthus sp.','A00001',2.62);
insert into living values('0008','Osmanthus sp.','A00002',3.12);
insert into living values('0009','Osmanthus sp.','A00002',2.87);
insert into living values('0010','Osmanthus sp.','A00002',3.12);
insert into living values('0011','Osmanthus sp.','B00006',3.3);
insert into living values('0012','Osmanthus sp.','B00006',2.92);
insert into living values('0013','Osmanthus sp.','B00006',3.03);
insert into living values('0014','Osmanthus sp.','B00006',3.00);
insert into living values('0015','Osmanthus sp.','B00005',3.12);
insert into living values('0016','Osmanthus sp.','B00005',2.92);
insert into living values('0017','Osmanthus sp.','B00005',2.21);
insert into living values('0018','Osmanthus sp.','B00005',2.23);
insert into living values('0019','Osmanthus sp.','B00003',2.12);
insert into living values('0020','Osmanthus sp.','B00003',2.42);
insert into living values('0021','Osmanthus sp.','B00003',2.53);
insert into living values('0022','Osmanthus sp.','B00003',2.28);
insert into living values('0023','Osmanthus sp.','B00003',3.48);
insert into living values('0024','Osmanthus sp.','B00001',2.86);
insert into living values('0025','Osmanthus sp.','B00001',3.27);
insert into living values('0026','Osmanthus sp.','B00001',3.25);
insert into living values('0027','Osmanthus sp.','B00001',3.02);
#细叶榕
insert into living values('0001','Ficus microcarpa','A00003',4.2);
insert into living values('0002','Ficus microcarpa','A00003',5.13);
insert into living values('0003','Ficus microcarpa','A00003',5.22);
insert into living values('0004','Ficus microcarpa','A00003',4.62);
insert into living values('0005','Ficus microcarpa','A00003',5.92);
insert into living values('0006','Ficus microcarpa','A00002',3.72);
insert into living values('0007','Ficus microcarpa','A00002',5.62);
insert into living values('0008','Ficus microcarpa','A00002',4.12);
insert into living values('0009','Ficus microcarpa','A00002',5.87);
insert into living values('0010','Ficus microcarpa','A00002',5.12);
insert into living values('0011','Ficus microcarpa','B00001',6.3);
insert into living values('0012','Ficus microcarpa','B00001',4.92);
insert into living values('0013','Ficus microcarpa','B00001',6.03);
insert into living values('0014','Ficus microcarpa','B00001',5.00);
insert into living values('0015','Ficus microcarpa','B00001',5.12);
insert into living values('0016','Ficus microcarpa','B00005',4.92);
insert into living values('0017','Ficus microcarpa','B00005',6.21);
insert into living values('0018','Ficus microcarpa','B00005',5.23);
insert into living values('0019','Ficus microcarpa','B00003',6.12);
insert into living values('0020','Ficus microcarpa','C00001',4.42);
insert into living values('0021','Ficus microcarpa','C00001',5.53);
insert into living values('0022','Ficus microcarpa','C00001',6.28);
insert into living values('0023','Ficus microcarpa','C00001',4.48);
insert into living values('0024','Ficus microcarpa','C00001',6.86);
insert into living values('0025','Ficus microcarpa','C00001',4.27);
insert into living values('0026','Ficus microcarpa','C00002',6.25);
insert into living values('0027','Ficus microcarpa','C00002',4.42);
insert into living values('0028','Ficus microcarpa','C00002',4.22);
insert into living values('0029','Ficus microcarpa','C00002',5.02);
insert into living values('0030','Ficus microcarpa','C00002',3.02);
#黄葛
insert into living values('0001','Ficus virens Aiton','A00001',6.2);
insert into living values('0002','Ficus virens Aiton','A00001',6.13);
insert into living values('0003','Ficus virens Aiton','A00001',3.22);
insert into living values('0004','Ficus virens Aiton','A00001',3.02);
insert into living values('0005','Ficus virens Aiton','A00001',2.92);
insert into living values('0006','Ficus virens Aiton','A00001',2.72);
insert into living values('0007','Ficus virens Aiton','A00001',2.62);
insert into living values('0008','Ficus virens Aiton','A00002',3.12);
insert into living values('0009','Ficus virens Aiton','A00002',2.87);
insert into living values('0010','Ficus virens Aiton','A00002',3.12);
insert into living values('0011','Ficus virens Aiton','B00003',5.12);
insert into living values('0012','Ficus virens Aiton','B00003',5.42);
insert into living values('0013','Ficus virens Aiton','B00003',5.53);
insert into living values('0014','Ficus virens Aiton','B00003',5.28);
insert into living values('0015','Ficus virens Aiton','B00003',5.48);
insert into living values('0016','Ficus virens Aiton','B00002',4.86);
insert into living values('0017','Ficus virens Aiton','B00002',4.27);
insert into living values('0018','Ficus virens Aiton','B00002',4.25);
insert into living values('0019','Ficus virens Aiton','B00002',4.02);
#蓝花楹
insert into living values ('0001','Jacaranda mimosifolia','B00001',8.63);
insert into living values ('0002','Jacaranda mimosifolia','B00001',9.13);
insert into living values ('0003','Jacaranda mimosifolia','B00001',9.23);
insert into living values ('0004','Jacaranda mimosifolia','B00001',9.04);
insert into living values ('0005','Jacaranda mimosifolia','B00001',8.73);
insert into living values ('0006','Jacaranda mimosifolia','B00001',8.79);
insert into living values ('0007','Jacaranda mimosifolia','B00001',8.13);
insert into living values ('0008','Jacaranda mimosifolia','B00001',10.13);
insert into living values ('0009','Jacaranda mimosifolia','B00001',9.83);
insert into living values ('0010','Jacaranda mimosifolia','B00001',9.78);
insert into living values ('0011','Jacaranda mimosifolia','B00001',9.56);
insert into living values ('0012','Jacaranda mimosifolia','B00001',8.93);
insert into living values ('0013','Jacaranda mimosifolia','B00001',9.33);
# 玉兰
insert into living values ('0001','Yulania denudata','B00003',10.86);
insert into living values ('0002','Yulania denudata','B00003',11.82);
insert into living values ('0003','Yulania denudata','B00003',10.53);
insert into living values ('0004','Yulania denudata','B00003',11.44);
insert into living values ('0005','Yulania denudata','A00001',11.32);
insert into living values ('0006','Yulania denudata','A00001',10.97);
insert into living values ('0007','Yulania denudata','A00001',10.69);
insert into living values ('0008','Yulania denudata','A00001',11.01);
#含笑
insert into living values('0001','Michelia figo','A00002',2.03);
insert into living values('0002','Michelia figo','A00002',2.23);
insert into living values('0003','Michelia figo','A00002',2.41);
insert into living values('0004','Michelia figo','A00002',2.32);
insert into living values('0005','Michelia figo','A00002',2.25);
#银杏
insert into living values('0001','Ginkgo biloba','A00002',13.2);
insert into living values('0002','Ginkgo biloba','A00002',12.13);
insert into living values('0003','Ginkgo biloba','A00002',13.22);
insert into living values('0004','Ginkgo biloba','A00002',13.02);
insert into living values('0005','Ginkgo biloba','A00002',12.92);
insert into living values('0006','Ginkgo biloba','A00002',12.72);
insert into living values('0007','Ginkgo biloba','A00002',12.62);
insert into living values('0008','Ginkgo biloba','A00002',13.12);
insert into living values('0009','Ginkgo biloba','A00002',12.87);
insert into living values('0010','Ginkgo biloba','A00002',13.12);
insert into living values('0011','Ginkgo biloba','B00006',11.3);
insert into living values('0012','Ginkgo biloba','B00006',12.92);
insert into living values('0013','Ginkgo biloba','B00006',13.03);
insert into living values('0014','Ginkgo biloba','B00006',13.00);
insert into living values('0015','Ginkgo biloba','B00006',13.12);
insert into living values('0016','Ginkgo biloba','B00005',11.92);
insert into living values('0017','Ginkgo biloba','B00005',12.21);
insert into living values('0018','Ginkgo biloba','B00005',12.123);
insert into living values('0019','Ginkgo biloba','B00003',12.12);
insert into living values('0020','Ginkgo biloba','B00003',12.42);
insert into living values('0021','Ginkgo biloba','B00003',12.53);
insert into living values('0022','Ginkgo biloba','B00003',12.28);
insert into living values('0023','Ginkgo biloba','B00003',13.48);
insert into living values('0024','Ginkgo biloba','B00003',12.86);
insert into living values('0025','Ginkgo biloba','B00001',13.27);
insert into living values('0026','Ginkgo biloba','B00001',13.25);
insert into living values('0027','Ginkgo biloba','B00001',13.02);
insert into living values('0028','Ginkgo biloba','B00001',13.02);
insert into living values('0029','Ginkgo biloba','B00001',13.02);
insert into living values('0030','Ginkgo biloba','B00003',13.02);
insert into living values('0031','Ginkgo biloba','B00003',13.02);
insert into living values('0032','Ginkgo biloba','B00003',13.02);
insert into living values('0033','Ginkgo biloba','B00003',13.02);
insert into living values('0034','Ginkgo biloba','B00003',13.02);
insert into living values('0035','Ginkgo biloba','B00003',13.02);
insert into living values('0036','Ginkgo biloba','B00003',13.02);
insert into living values('0037','Ginkgo biloba','B00003',13.02);
insert into living values('0038','Ginkgo biloba','B00003',13.02);
insert into living values('0039','Ginkgo biloba','B00003',13.02);
insert into living values('0040','Ginkgo biloba','B00003',13.02);
insert into living values('0041','Ginkgo biloba','B00003',13.02);
insert into living values('0042','Ginkgo biloba','B00003',13.02);
insert into living values('0043','Ginkgo biloba','B00003',13.02);
insert into living values('0044','Ginkgo biloba','B00003',13.02);
insert into living values('0045','Ginkgo biloba','B00003',13.02);
insert into living values('0046','Ginkgo biloba','B00003',13.02);
insert into living values('0047','Ginkgo biloba','B00003',13.02);
insert into living values('0048','Ginkgo biloba','B00003',13.02);
#木本绣球
insert into living values ('0001','Viburnum macrocephalum','A00001',5.2);
insert into living values ('0002','Viburnum macrocephalum','A00001',5.02);
insert into living values ('0003','Viburnum macrocephalum','A00001',5.12);
#日本晚樱
insert into living values ('0001','Prunus serrulata var.','A00001',4.12);
insert into living values ('0002','Prunus serrulata var.','A00001',4.22);
insert into living values ('0003','Prunus serrulata var.','A00001',4.31);
insert into living values ('0004','Prunus serrulata var.','A00001',4.25);
insert into living values ('0005','Prunus serrulata var.','A00001',4.53);
insert into living values ('0006','Prunus serrulata var.','B00004',4.12);
insert into living values ('0007','Prunus serrulata var.','B00004',4.12);
insert into living values ('0008','Prunus serrulata var.','B00004',4.42);
insert into living values ('0009','Prunus serrulata var.','B00004',4.25);
#垂丝海棠
insert into living values ('0001','Malus halliana Koehne','B00002',3.34);
insert into living values ('0002','Malus halliana Koehne','B00002',3.34);
insert into living values ('0003','Malus halliana Koehne','B00002',3.34);
insert into living values ('0004','Malus halliana Koehne','B00002',3.34);
insert into living values ('0005','Malus halliana Koehne','B00002',3.34);
insert into living values ('0006','Malus halliana Koehne','B00002',3.34);
insert into living values ('0007','Malus halliana Koehne','B00005',3.34);
insert into living values ('0008','Malus halliana Koehne','B00005',3.34);
insert into living values ('0009','Malus halliana Koehne','B00005',3.34);
insert into living values ('00010','Malus halliana Koehne','B00005',3.34);
#桃花
insert into living values ('0001','Pyrus pyrifolia','B00002',4.24);
insert into living values ('0002','Pyrus pyrifolia','B00002',4.14);
insert into living values ('0003','Pyrus pyrifolia','B00002',4.01);
insert into living values ('0004','Pyrus pyrifolia','B00002',3.74);
