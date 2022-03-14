#!/bin/env bash

passwdhome(){
	if grep -Fq ':/var/home' /etc/passwd
	then
		cp /etc/passwd /etc/passwd.backup
		sed -i 's|:/var/home|:/home|' /etc/passwd
	fi
}

checksymlink(){
	if ! [[ $(readlink "/snap") == "/var/lib/snapd/snap" ]]
	then
		ln -sf '/var/lib/snapd/snap/' '/snap/' | systemd-cat -t snapd-ostree.service -p info
		checksymlink
	fi
}

chattr -i /
checksymlink
passedhome
chattr +i /
