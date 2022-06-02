from invoke import task

@task
def cleanup(c):
    cmd = 'rm -rf dist build'
    c.run(cmd)
    print('cleanup: done')

@task(cleanup)
def sdist(c):
    cmd = 'python setup.py sdist'
    c.run(cmd)

@task(sdist)
def bdist_wheel(c):
    cmd = 'python setup.py bdist_wheel'
    c.run(cmd)

@task(sdist, build_wheel)
def upload(c):
    cmd = 'twine upload --repository pypi dist/*'
    c.run(cmd)
