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
def bdistwheel(c):
    cmd = 'python setup.py bdist_wheel'
    c.run(cmd)

@task(sdist, bdistwheel)
def upload(c):
    cmd = 'twine upload --repository pypi dist/*'
    c.run(cmd)


@task
def check_memory_usage(c):
    from jp_prefecture import jp_prefectures as jp
    from jp_prefecture.jp_cities import jp_cities as city
    from pympler import asizeof

    print('Memory Usage:')
    print(f"""
jp_prefecture: {asizeof.asizeof(jp)/1024:5.2f} KB.
    jp_cities: {asizeof.asizeof(city)/1024:5.2f} KB.
""")
