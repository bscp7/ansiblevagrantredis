Vagrant.configure("2") do |config|
 config.vm.define "hostA" do |hostA|
   hostA.vm.box = "ubuntu/trusty32"
   hostA.vm.hostname = 'Ubuntu-A'
   config.vm.provider "virtualbox" do |v|
     v.memory = 512
     v.cpus = 2
   end
   config.vm.network "private_network", type: "dhcp"
  end 
 config.vm.define "hostB" do |hostB|  
   hostB.vm.box = "ubuntu/trusty32"  
   hostB.vm.hostname = 'Ubuntu-B'
   config.vm.provider "virtualbox" do |v|
     v.memory = 512
     v.cpus = 2
   end
   config.vm.network "private_network", type: "dhcp"
 end 
end