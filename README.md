# Lazy Hacker

This project pretends to offer a service similar to _metasploit_ which allows the user to scan a certain webpage looking for **vulnerabilities**. This tool is supposed to be user-friendly, in order to offer a  quick life-saver service for the ones who are not very related to security but even though concerned.

But remember! Don't rely your proffesional software security in fast scanning, ask a proffesional!

In the future we want to offer a higher scanning service with a curating tool for domains and certain organizations. **_Unsecure pages, beware!_**

# Internet Censorship app

This app provides an interactive internet censorhsip map which contains information about censorship in different countries.

This will ping to different webpages using proxies from different countries, trying to check if those pages are available for users in that country.

[![Made with HACKING and Open Source](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://www.gnu.org/licenses/gpl-3.0.en.html)

## Continuous integration:

[![Build Status](https://travis-ci.org/terceranexus6/copylazyjacker.svg?branch=master)](https://travis-ci.org/terceranexus6/copylazyjacker)

![](https://github.com/terceranexus6/copylazyjacker/blob/master/images/photo_2018-01-23_11-18-54.jpg?raw=true)

Our service relies on:

- Python (Flask+scripts)
- Heroku
- now.sh + Dockerhub
- Azure client

## Python

![](https://github.com/terceranexus6/copylazyjacker/blob/master/images/photo_2018-01-23_11-19-02.jpg?raw=true)

Python will be used in Flask to provide a way of launching the app. The manage file will render the index. In the future I intend to extends the manage file in order to make a reliable MVC application, maybe using **Django** instead.

On the other hand I use python for a script that iterates a list of proxies and webpages and check their availability from different countries.

## Heroku

![](https://github.com/terceranexus6/copylazyjacker/blob/master/images/photo_2018-01-23_11-19-07.jpg?raw=true)

Heroku is used to deploy the app. This is the link:

Deployment https://copylazyjacker.herokuapp.com/

For this, I linked both the github repository with Heroku.

## Container

![](https://github.com/terceranexus6/copylazyjacker/blob/master/images/photo_2018-01-23_11-18-32.jpg?raw=true)

For containing I will be using now.sh and dockerhub.

Container: https://copylazyjacker-bdrfakgdkl.now.sh

Dockerfile en Dockerhub: https://hub.docker.com/r/terceranexus6/copylazyjacker

## Azure + vagrant

![](https://github.com/terceranexus6/copylazyjacker/blob/master/images/photo_2018-01-23_11-18-52.jpg?raw=true)

For deployment using virtual machine, I will be configuring vagrant and Azure-cli.

First of all I have to register in azure. Once it's done, I install vagrant:

`sudo apt-get install vagrant`

After installing vagrant, I install the azure-cli plugin for vagrant:

`vagrant box add azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure`
`vagrant plugin install vagrant-azure`

Now I logged in in azure using:

`az login`

I initialize vagrant using:

`vagrant init ubuntu/xenial64`

Now I create the azure app:

`az ad sp create-for-rbac --name {appName} --password "{strong password}"`

If permmision error appears, check in the azure platform for the permmision settings, as specified in [here](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-create-service-principal-portal#required-permissions).

Once it's done, we look for the subscription id here:

`az account list --output table `

now we export to the Vagrantfile the login data using:

```
export AZURE_TENANT_ID={tenant id}
export AZURE_CLIENT_ID={AppId}
export AZURE_SUBSCRIPTION_ID={subscription id}
export AZURE_CLIENT_SECRET={strong password}
```
And we raise the vagrant

`vagrant up --provider=azure`

Now we wanted to use Ansible and Fabric, **what do we need to change?**

In the Vagrantfile we add:

```
config.vm.provision "ansible" do |ansible|
  ansible.become = true
  ansible.verbose = "v"
  ansible.playbook = "playbook.yml"
end
```

And we write the `playbook.yml`. I decided to add the update, git and python installation in the playbook so not needed to rewrite it in the Fabric file `fabfile.py`, in which I included a `cd` function and `git pull` apart from the application start. 
