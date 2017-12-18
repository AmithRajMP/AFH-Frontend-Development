from fabric.api import local, run, task, roles, put, env, sudo

env.user = 'ubuntu'
env.key_filename = 'prod-afhrk.key'
env.roledefs = {
    'dev': ['thesecurenode.com'],
    'prod': ['artforhumanity.in'],
}

@roles('prod')
@task
def update_code():
    run('cd /var/www/html')
    run('git pull origin master')