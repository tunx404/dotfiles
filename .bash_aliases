##################################################
# Dotfiles

alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

alias adddot='~/.scripts/add_dotfiles.sh'
alias pushdot='~/.scripts/push_dotfiles.sh'

##################################################
# System

alias update-grub='sudo grub-mkconfig -o /boot/grub/grub.cfg'
alias pkgtop='pkgtop -pacman yay'
alias dd='sudo dd status=progress'
alias ssh='TERM=xterm-256color ssh'
alias genqtile='mkdir -p ~/Miscellaneous/Qtile && python ~/.config/qtile/gen-keybinding-img -c ~/.config/qtile/config.py -o ~/Miscellaneous/Qtile'

##################################################
# CMU

alias cmuvpn='sudo openconnect -u alehoang vpn.cmu.edu'

##################################################
# Update

alias removeorphans='pacman -Qtdq | sudo pacman -Rns -'
alias cleanpkg='sudo pacman -Scc && yay -Scc && rm -rf ~/.cache/yay && removeorphans'
alias cleandt='~/.config/darktable/purge_non_existing_images.sh --purge && darktable-generate-cache'
alias cleanall='cleanpkg && cleandt && conda clean -a'

alias updatepkg='sudo pacman -Syu && yay -Syu'
alias updateall='updatepkg'

##################################################
# Reset

alias resetlogid='sudo systemctl restart logid'
alias resetcuda='sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm'
alias resetserial='sudo chmod 666 /dev/ttyUSB0'

##################################################
# Projects

alias fintec='cd ~/Cloud/Google\ Drive\ 1/Projects/Fintecism/financialadvisor && conda activate fin && jupyter-lab'
alias frac='cd ~/Miscellaneous/fracture && jupyter-lab'

##################################################
# Applications

alias startdlna='minidlnad -f /home/$USER/.config/minidlna/minidlna.conf -P /home/$USER/.config/minidlna/minidlna.pid'
alias stopdlna='killall minidlnad'

##################################################
# Miscellaneous

alias mountmtp='aft-mtp-mount ~/MTP'
alias mountftp='curlftpfs 10.10.10.10/Gargoyle ~/Gargoyle -o'

alias exmonitor='xrandr --output DP-3 --mode 1920x1080 --pos 1920x0 --rotate normal'
