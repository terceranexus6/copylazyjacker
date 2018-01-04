# Lazy Hacker

This project pretends to offer a service similar to _metasploit_ which allows the user to scan a certain webpage looking for **vulnerabilities**. This tool is supposed to be user-friendly, in order to offer a  quick life-saver service for the ones who are not very related to security but even though concerned.

But remember! Don't rely your proffesional software security in fast scanning, ask a proffesional!

In the future we want to offer a higher scanning service with a curating tool for domains and certain organizations. **_Unsecure pages, beware!_**

# Internet Censorship app

This app provides an interactive internet censorhsip map which contains information about censorship in different countries.

This will ping to different webpages using proxies from different countries, trying to check if those pages are available for users in that country.

[![Made with HACKING and Open Source](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://www.gnu.org/licenses/gpl-3.0.en.html)

[![Build Status](https://travis-ci.org/terceranexus6/copylazyjacker.svg?branch=master)](https://travis-ci.org/terceranexus6/copylazyjacker)

Our service relies on:

- Python (Flask+scripts)
- Heroku
- now.sh + Dockerhub
- Azure client

## Python

Python will be used in Flask to provide a way of launching the app. The manage file will render the index. In the future I intend to extends the manage file in order to make a reliable MVC application, maybe using **Django** instead.

On the other hand I use python for a script that iterates a list of proxies and webpages and check their availability from different countries.

## Heroku

Heroku is used to deploy the app. This is the link:

Deployment https://copylazyjacker.herokuapp.com/

For this, I linked both the github repository with Heroku.

## Container

For containing I will be using now.sh and dockerhub.

Container: https://copylazyjacker-bdrfakgdkl.now.sh

Dockerfile en Dockerhub: https://hub.docker.com/r/terceranexus6/copylazyjacker

## Azure client + brew + vagrant

First I install [brew](https://docs.brew.sh/Installation.html) . Once it's installed I configure the [azure client](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) on it using `brew install azure-cli` as specified. For the virtual machine configuration I use a Vagrantfile specifying the details of the machine. 
