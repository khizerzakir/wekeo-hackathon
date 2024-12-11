### Local environment setup
This application was built using python language and must be used during the WEkEO hackathon session. Application uses pipenv virtual environment. In order to run application make sure you have installed next packages:
1. python
2. pip
3. pipenv

Running application requires switching to virtual environment and installing required dependencies
```shell
pipenv shell
```
```shell
pipenv install
```
After finishing of the dependencies installation just run this application
```shell
python main.py
```
### Data base setup.
Application directly interacts with the data base in order to obtain drops and calculate their next position. You can use either local data base setup or remote database. To adjust data base connection edit `config.ini` file
```ini
[database]
host=localhost
database=postgres
user=postgres
password=P@ssw0rc!
```
#### Local data base setup
To spin up local database it is recommended to use docker container and docker compose plugin to easily maintain setup. Here is provided docker compose file for local data base setup:
```yaml
services:
  postgis:
    image: postgis/postgis:latest
    container_name: postgis
    restart: always
    environment:
      POSTGRES_USER: postgres           
      POSTGRES_PASSWORD: P@ssw0rc!   
      POSTGRES_DB: postgres         
    ports:
      - "5432:5432"                
    volumes:
      - postgis_data:/var/lib/postgresql/data
    networks:
      cluster:
        ipv4_address: 111.222.33.2
volumes:
  postgis_data:
    driver: local
    driver_opts:
      o: bind
      type: none
      device: ./data/postgis_data
networks:
  cluster:
    ipam:
      config:
        - subnet: 111.222.33.0/24
```
> Do not forget to create `./data/postgis_data` file in folder where docker compose file is located. This folder will be used to mount volume from container in order to persist data 