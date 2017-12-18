from fabric.api import local, run, task, roles, put, env, sudo
from fabric.context_managers import cd

env.user = 'ubuntu'
env.key_filename = 'prod-afhrk.key'
env.roledefs = {
    'dev': ['thesecurenode.com'],
    'prod': ['artforhumanity.in'],
}

@roles('prod')
@task
def update_code():
    with cd('/var/www/html/'):
        run('git pull gitlab master')