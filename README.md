# flask-heroku-docker-yml

## commands

1. create heroku.yml

sections

## executed before container is run
setup:
  addons:
    - plan: heroku-postgresql
      as: DATABASE

  ## these env vars are available during runtime 
  config:
    S3_BUCKET: my-example-bucket

# builds any docker images
build:
  docker:
    web: Dockerfile
    worker: worker/Dockerfile

  ## these env vars are available during build time not runtime 
  config:
    ENV: development
    FOO: bar

## executed before container runs
release:
  command:
    - ./deployment-tasks.sh
  image: worker
  
## how to run container runs
run:
  web: python run.py
  worker: erl erlang-worker.erl
  asset-syncer:
    command:
      - python asset-syncer.py
    image: worker


2. docker create

3. heroku stack:set container --app appnamehere

4. git push heroku master

5. heroku open 

** Profile is not required