from invoke import task

@task
def start(ctx):
    ctx.run("python src/app.py")

@task
def test(ctx):
    ctx.run("pytest tests/")
    ctx.run("python -m tests.pathfinder_benchmark")