##################################################
# Dotfiles

alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles --work-tree=$HOME'
alias dotstatus='dotfiles status'

alias adddot='~/.scripts/add_dotfiles.sh'
alias pushdot='~/.scripts/push_dotfiles.sh'

##################################################
# Monitor

alias exmonitor='xrandr --output DP-3 --mode 1920x1080 --pos 1920x0 --rotate normal'
alias exmonitortop='xrandr --output DP1 --mode 1920x1080 --pos 0x-1080 --rotate normal'

alias exmonitorhub='xrandr --output DP-1 --mode 1920x1080 --pos 1920x0 --rotate normal'
alias exmonitorhubtop='xrandr --output DP-1 --mode 1920x1080 --pos 0x-1080 --rotate normal'

##################################################
# System

alias removeorphans='pacman -Qtdq | sudo pacman -Rns -'
alias cleanpkg='sudo pacman -Scc && yay -Scc && rm -rf ~/.cache/yay && removeorphans'
alias cleandt='~/.config/darktable/purge_non_existing_images.sh --purge && darktable-generate-cache'
alias cleanconda='conda clean -a'
alias cleanall='cleanconda && cleanpkg'

alias searchpkg='pacman -Qsq'
alias removepkg='sudo pacman -Rsun '
alias updatepkg='sudo pacman -Syu && yay -Syu'
alias updateall='updatepkg'

alias editpacman='sudo subl /etc/pacman.conf'

alias update-grub='sudo grub-mkconfig -o /boot/grub/grub.cfg'
alias pkgtop='pkgtop -pacman yay'

alias dd='sudo dd status=progress'
alias ssh='TERM=xterm-256color ssh'

alias hbn='sudo systemctl hibernate'

alias setpem='sudo chown -R tunx404 ./'

##################################################
# Reset

alias runlogid='sudo logid -c /home/anhlh33/.config/logid/logid.cfg'
alias resetlogid='sudo systemctl restart logid'
alias resetcuda='sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm'
alias resetserial='sudo chmod 666 /dev/ttyUSB0'

##################################################
# Applications

alias startdlna='minidlnad -f /home/$USER/.config/minidlna/minidlna.conf -P /home/$USER/.config/minidlna/minidlna.pid'
alias stopdlna='killall minidlnad'

alias sshot='scrot -s IMG_%Y%m%d_%H%M%S.png -e '\''mv $f ~/Miscellaneous'\'
alias genqtile='mkdir -p ~/Cloud/Google\ Drive\ 1/Miscellaneous/Qtile && python ~/.config/qtile/gen-keybinding-img -c ~/.config/qtile/config.py -o ~/Cloud/Google\ Drive\ 1/Miscellaneous/Qtile'

##################################################
# Miscellaneous

alias mountmtp='aft-mtp-mount ~/MTP'
alias mountftp='curlftpfs 10.10.10.10/Gargoyle ~/Gargoyle -o'

alias exmonitor='xrandr --output HDMI-1-0 --mode 1920x1080 --pos 1920x0 --rotate normal'

alias updatedot='cd ~/SSD/Applications/Git/dotfiles && git pull'
