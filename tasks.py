from invoke import task


@task
def build(c):
    c.run("docker-compose build")


@task
def start(c):
    c.run("docker-compose up -d")


@task
def stop(c):
    c.run("docker-compose stop")


@task
def shell(c):
    c.run("docker-compose run --rm backend python manage.py shell -i ipython", pty=True)


@task
def makemigrations(c, args=""):
    c.run(f"docker-compose run --rm backend python manage.py makemigrations {args}")


@task
def migrate(c):
    c.run("docker-compose run --rm backend python manage.py migrate")


@task
def collectstatic(c):
    c.run("docker-compose run --rm backend python manage.py collectstatic --noinput")


@task
def tests(c):
    c.run("pytest tests/")


@task
def quality(c):
    c.run("docker-compose run --rm backend black .")
    c.run("docker-compose run --rm backend flake8 .")


@task
def quality_check(c):
    c.run("docker-compose run --rm backend black . --check")
    c.run("docker-compose run --rm backend flake8 .")


@task(build, migrate)
def setup_dev(c):
    pass


@task
def add_dep(c, dependency):
    c.run("docker-compose run --rm backend poetry add " + dependency)


@task
def add_dev_dep(c, dependency):
    c.run("docker-compose run --rm backend poetry add -D " + dependency)
