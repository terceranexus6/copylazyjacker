from fabric.api import sudo,run

def install_app():
    run('git clone https://github.com/terceranexus6/copylazyjacker')
    with cd('copylazyjacker')
        run('pip install -r requirements.txt')

def update_app():
    with cd('copylazyjacker')
        run('git pull')
        run('pip install -r requirements.txt')

def start_app():
    with cd('copylazyjacker/mapa/')
        run('sudo gunicorn -b 0.0.0.0:80 app:app —log-file=- &')
