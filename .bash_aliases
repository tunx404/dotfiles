##################################################
# Dotfiles

alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles --work-tree=$HOME'
alias dotstatus='dotfiles status'

alias adddot='~/.scripts/add_dotfiles.sh'
alias pushdot='~/.scripts/push_dotfiles.sh'

##################################################
# Monitor

alias resetmonitor='xrandr --output eDP-1-1 --mode 1920x1080 --pos 0x0 --rotate normal --output DP-1-1 --auto --right-of eDP-1-1 --output HDMI-0 --auto --right-of DP-1-1 --rotate left'

alias exmonitorcf='xrandr --output DP-1-1 --mode 1920x1080 --pos 1920x0 --rotate normal'
alias exmonitorcfr='xrandr --output DP-1-1 --mode 1920x1080 --pos 1920x0 --rotate right'
alias exmonitorcfl='xrandr --output DP-1-1 --mode 1920x1080 --pos 1920x0 --rotate left'
alias exmonitorc2='xrandr --output DP-1-1 --mode 2560x1440 --pos 1920x0 --rotate normal'
alias exmonitorc4='xrandr --output DP-1-1 --mode 3840x2160 --pos 1920x0 --rotate normal'

# alias exmonitorh2='xrandr --output HDMI-0 --mode 2560x1440 --pos 4480x0 --rotate normal'
# alias exmonitorh2l='xrandr --output HDMI-0 --mode 2560x1440 --pos 4480x0 --rotate left'
alias exmonitorh2='xrandr --output HDMI-0 --mode 2560x1440 --pos 5760x0 --rotate normal'
alias exmonitorh2l='xrandr --output HDMI-0 --mode 2560x1440 --pos 5760x0 --rotate left'

##################################################
# System

alias removeorphans=''
alias cleanpkg='sudo apt --purge autoremove && sudo apt clean'
alias cleandt=''
alias cleanconda='ls' # 'conda clean -a'
alias cleandocker='docker image prune'
alias cleanall='cleanconda && cleanpkg && cleandocker'

alias updatepkg='sudo apt update && sudo apt upgrade'
alias updateall='updatepkg'

alias checkppa='cd /etc/apt/sources.list'
alias checksource='cat /etc/apt/sources.list'

alias dd='sudo dd status=progress'
alias ssh='TERM=xterm-256color ssh'

alias blup='sudo brightnessctl set +10%'
alias bldown='sudo brightnessctl set 10%-'

alias python='python3'

alias hbn='sudo systemctl hibernate'

alias setpem='sudo chown -R anhlh33 ./'

alias limittemp='sudo undervolt -v --temp 95 --core -0 --cache -0 --gpu -0'

alias cpufreq='watch -n1 "grep \"MHz\" /proc/cpuinfo"'

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
alias mountrs720='sshfs rs720:/home/rs720 /home/anhlh33/SSHFS/rs720'

alias testgpu='docker exec -it test_gpu bash'

alias anhlh33_deepstream='docker exec -it anhlh33_deepstream bash'

alias rtspserver='RTSP_RTSPADDRESS="127.0.0.1:8556" ~/Portable/Linux/RTSP/rtsp-simple-server'