<!--
    Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with < this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
-->


# TRAILS: A Database Native Model Selection System

![image-20230702035806963](internal/ml/model_selection/documents/imgs/image-20230702035806963.png)

# Build & Run examples

## PyTorch + PostgreSQL

```bash
# Remove existing one if there is 
docker rm -f trails
# Create project folder.
mkdir project && cd project
# Download the Dockerile.
wget -O Dockerfile https://raw.githubusercontent.com/NLGithubWP/Trails/main/torch.psql.Dockerfile

# Build Dockerile and run the docker.
docker build -t trails .
docker run -d --name trails --network="host" trails
# Wait for 5 mins, monitor the logs until it shows "Done!", then exit the monitor
docker logs -f trails

# Connect to the pg server and use pg_extension database.
docker exec -it trails bash
psql -h localhost -p 28814 -U postgres
\c pg_extension

# Test coordinator
SELECT coordinator('0.08244', '168.830156', '800', false, '/project/Trails/internal/ml/model_selection/config.ini');
# Run an example, wait one min, it will run filtering + refinemnt + training the selected model.
CALL model_selection_end2end('frappe_train', ARRAY['col1', 'col2', 'col3', 'col4','col5','col6','col7','col8','col9','col10', 'label'], '10', '/project/Trails/internal/ml/model_selection/config.ini');

# In other terminal, monitor the running process
docker exec -it trails_polardb bash
tail -f /home/postgres/.pgrx/data-14/trails_log_folder/<log_file_name>
```
## PyTorch + PolarDB

```bash
# Remove existing one if there is 
docker rm -f trails_polardb
# Create project folder.
mkdir project_polardb && cd project_polardb
# Download the Dockerile.
wget -O Dockerfile https://raw.githubusercontent.com/NLGithubWP/Trails/main/torch.polarDB.Dockerfile

# Build Dockerile and run the docker.
docker build -t trails_polardb .
docker run -d --name trails_polardb  trails_polardb
# Monitor the logs until the setup step is done.
docker logs -f trails_polardb
# Run a setup script
docker exec trails_polardb /bin/bash -c "/home/postgres/Trails/init_polardb.sh"

# Connect to the primary pg server and use pg_extension database.
docker exec -it trails_polardb bash
psql -h localhost -p 5432 -U postgres 
\c pg_extension

# Test coordinator
SELECT coordinator('0.08244', '168.830156', '800', false, '/home/postgres/Trails/internal/ml/model_selection/config.ini');
# Run an example, wait one min, it will run filtering + refinemnt + training the selected model.
CALL model_selection_end2end('frappe_train', ARRAY['col1', 'col2', 'col3', 'col4','col5','col6','col7','col8','col9','col10', 'label'], '10', '/home/postgres/Trails/internal/ml/model_selection/config.ini');

# In other terminal, monitor the running process
docker exec -it trails_polardb bash
tail -f /var/polardb/primary_datadir/trails_log_folder/<log_file_name>
```

## Singa + PostgreSQL

```bash
# Remove existing one if there is 
docker rm -f singa_trails
# Create project folder.
mkdir project && cd project
# Download the Dockerile.
wget -O Dockerfile  ??

# Build Dockerile and run the docker.
docker build -t singa_trails .
docker run -d --name singa_trails singa_trails
# Wait for 5 mins, monitor the logs until it shows "Done!", then exit the monitor
docker logs -f singa_trails

# Connect to the pg server and use pg_extension database.
docker exec -it singa_trails bash
psql -h localhost -p 28814 -U postgres
\c pg_extension

# Test coordinator
SELECT coordinator('0.08244', '168.830156', '800', false, '/project/Trails/internal/ml/model_selection/config.ini');
# Run an example, wait one min, it will run filtering + refinemnt + training the selected model.
CALL model_selection_end2end('frappe_train', ARRAY['col1', 'col2', 'col3', 'col4','col5','col6','col7','col8','col9','col10', 'label'], '10', '/project/Trails/internal/ml/model_selection/config.ini');

# In other terminal, monitor the running process
docker exec -it trails_polardb bash
tail -f /home/postgres/.pgrx/data-14/trails_log_folder/<log_file_name>
```



```bash
# Test the basic functions 
python3 ./internal/ml/model_selection/exps/4.seq_score_online.py   --embedding_cache_filtering=True   --models_explore=10   --tfmem=synflow   --log_name=score_based   --search_space=mlp_sp   --num_layers=4   --hidden_choice_len=20   --base_dir=./dataset   --num_labels=2   --device=cpu   --batch_size=32   --dataset=frappe   --nfeat=5500   --nfield=10   --nemb=10   --workers=0   --result_dir=./exp_result/   --log_folder=log_foler

python3 ./internal/ml/model_selection/exps/0.train_one_model.py --log_name=train_log --search_space=mlp_sp --base_dir=./dataset --num_labels=2 --device=cpu --batch_size=10 --lr=0.01 --epoch=5 --iter_per_epoch=2000 --dataset=frappe --nfeat=5500 --nfield=10 --nemb=10 --workers=0 --result_dir=./exp_result/   --log_folder=log_foler

python3 internal/ml/model_selection/pg_interface.py
```

## Singa + PolarDB

```bash
# Remove existing one if there is 
docker rm -f trails_singa_polardb
# Create project folder.
mkdir project_polardb_singa && cd project_polardb_singa
# Download the Dockerile.
wget -O Dockerfile ???

# Build Dockerile and run the docker.
docker build -t trails_singa_polardb .
docker run -d --name trails_singa_polardb  trails_singa_polardb
# Monitor the logs until the setup step is done.
docker logs -f trails_singa_polardb
# Run a setup script
docker exec trails_singa_polardb /bin/bash -c "/home/postgres/Trails/init_polardb.sh"

# Connect to the primary pg server and use pg_extension database.
docker exec -it trails_singa_polardb bash
psql -h localhost -p 5432 -U postgres 
\c pg_extension

# Test coordinator
SELECT coordinator('0.08244', '168.830156', '800', false, '/home/postgres/Trails/internal/ml/model_selection/config.ini');
# Run an example, wait one min, it will run filtering + refinemnt + training the selected model.
CALL model_selection_end2end('frappe_train', ARRAY['col1', 'col2', 'col3', 'col4','col5','col6','col7','col8','col9','col10', 'label'], '10', '/home/postgres/Trails/internal/ml/model_selection/config.ini');

# In other terminal, monitor the running process
docker exec -it trails_singa_polardb bash
tail -f /var/polardb/primary_datadir/trails_log_folder/<log_file_name>
```

# Reproduce the result

Document is at [here](https://github.com/NLGithubWP/Trails/blob/main/internal/ml/model_selection/documents/README.md)

