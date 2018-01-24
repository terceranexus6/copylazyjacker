from fabric.api import sudo,run

#clonar, instalar pip, meterse en el dir
def install_app():
    #descargar repositorio
    run('git clone https://github.com/terceranexus6/copylazyjacker')

    #instalamos pip
    run('sudo apt-get install -y python-pip')

    #directorio
    run('cd copylazyjacker/ && pip install -r requirements.txt')

#borrar repositorio
def borrar_repo():
    run('sudo rm -rf ./copylazyjacker')
