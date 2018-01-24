from fabric.api import sudo,run, cd

#meterse en el dir
def install_app():
    #directorio
    run('cd copylazyjacker/ && pip install -r requirements.txt')
    #checkear que sea la ultima version del playbook
    run('git pull')

def start_app():
    with cd('mapa')
        run('python app.py')
