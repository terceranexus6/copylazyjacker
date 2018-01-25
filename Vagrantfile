# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "azure"

  config.ssh.private_key_path = "~/.ssh/id_rsa"

  config.vm.provider :azure do |azure, override|
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    azure.vm_name = "lazyjacker"
    azure.resource_group_name= "juankers"
    azure.vm_image_urn = "Canonical:UbuntuServer:16.04-LTS:latest"
    azure.vm_size = "Basic_A0"
    azure.tcp_endpoints = "80"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "vvvvv"
    ansible.playbook = "playbook.yml"
    ansible.groups = {
      "app" => ["104.42.15.162"]
    }
  end

end
