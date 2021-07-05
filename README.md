# API of Regional Teaching Materials Creation Support System
- あらかじめ[initialize.sql](https://www.dropbox.com/s/hasejghph32e0z6/initialize.sql?dl=0)を`/mysql/sqls`に格納し，`docker-compose up -d`する
- Dockerを立ち上げた後，mysqlの権限周りを設定する必要があるかも？？
- 続けて以下を実行
```
$docker-compose exec mysql mysql -u root -ppassword
$mysql> create database Research_system;
$mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
$mysql> ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'password';

$docker-compose exec mysql bash
$cd docker-entrypoint-initdb.d
$mysql -u root -ppassword -D Research_system < initialize.sql
```
