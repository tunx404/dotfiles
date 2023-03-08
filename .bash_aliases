##################################################
# Dotfiles

alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles-ubuntu/ --work-tree=$HOME'
alias dotstatus='dotfiles status'

alias dotadd='~/.scripts/add_dotfiles.sh'
alias dotpush='~/.scripts/push_dotfiles.sh'

alias dotupdate='cd ~/SSD/Applications/Git/dotfiles && git pull'

##################################################
# System

alias cleanpkg='sudo apt --purge autoremove && sudo apt clean'
alias cleanconda='conda clean -a'
alias cleanall='cleanconda && cleanpkg'

alias checkppa='ls /etc/apt/sources.list.d'
alias checksource='cat /etc/apt/sources.list'

alias updatepkg='sudo apt update && sudo apt upgrade'
alias updateall='updatepkg'

alias dd='sudo dd status=progress'

alias ssh='TERM=xterm-256color ssh'

alias blup='sudo brightnessctl set +10%'
alias bldown='sudo brightnessctl set 10%-'

alias hbn='sudo systemctl hibernate'

alias python='python3'

alias setpem='sudo chown -R anhlh33 ./'

alias exmonitor='xrandr --output HDMI-0 --mode 2560x1440 --pos 1920x0 --rotate normal'
alias exmonitorfhd='xrandr --output HDMI-0 --mode 1920x1080 --pos 1920x0 --rotate normal'

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

##################################################
# Projects

alias fintec='cd ~/Cloud/Google\ Drive\ 1/Projects/Fintecism/financialadvisor && conda activate fin && jupyter-lab'

alias makevideo='ffmpeg -framerate 24 -pattern_type glob -i "*.png" -c:v libx264 -pix_fmt yuv420p -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" 0.mp4'

##################################################
# VinAI

alias z43='ssh z43'

alias mountz43='sshfs z43:/home/ubuntuz43 /home/anhlh33/SSHFS/z43'
alias mountnouvohcm='sshfs nouvo-hcm:/home/ubuntu /home/anhlh33/SSHFS/nouvo-hcm'
alias mountnouvo='sshfs nouvo:/home/ubuntu /home/anhlh33/SSHFS/nouvo'