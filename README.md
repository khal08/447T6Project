install requirements for db

Configure database (must be done for each persons system as this program is hosted locally):

1. mysql -u root
2. [If you have an 'admin' user skip this step]: CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
3. CREATE DATABASE vax_data;
4. exit sql, start another terminal and type "from App import db"
5. db.create_all() 
5a. Right now there is a small error with the database needing a length count defined in the constructor that it is currently not accepting, but working on it
