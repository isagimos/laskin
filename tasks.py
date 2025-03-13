from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/ui/user_interface.py", pty=True)