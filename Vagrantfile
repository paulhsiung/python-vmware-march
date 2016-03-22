VAGRANTFILE_API_VERSION = "2"

$setupscript = <<END
sudo chown -R vagrant:vagrant /usr/local/

# install virtualenv
pip install virtualenv virtualenvwrapper
END

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    hostname = "di_python.box"

    # Box
    config.vm.box = "ubuntu/trusty64"

    config.vm.provider :virtualbox do |v|
        v.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
        v.customize ["modifyvm", :id, "--memory", 2048]
    end

    # Shared folders
    config.vm.synced_folder ".", "/local"

    # Setup
    config.vm.provision :shell, :inline => "touch .hushlogin"  # turn off our banner
    config.vm.provision :shell, :inline => "hostnamectl set-hostname #{hostname}"
    config.vm.provision :shell, :inline => "apt-get update --fix-missing"
    config.vm.provision :shell, :inline => "apt-get install -q -y g++ git curl tree nano python-dev python python-pip"

    # install python pip dependencies
    config.vm.provision :shell, inline: $setupscript

end