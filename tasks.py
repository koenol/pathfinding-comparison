from invoke import task

@task
def start(ctx):
    ctx.run("python src/app.py")

@task
def test(ctx):
    ctx.run("pytest tests/")

@task
def perf_test(ctx):
    ctx.run("python -m tests.pathfinder_benchmark")