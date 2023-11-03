##################################################
# Dotfiles

alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles --work-tree=$HOME'
alias dotstatus='dotfiles status'

alias adddot='~/.scripts/add_dotfiles.sh'
alias pushdot='~/.scripts/push_dotfiles.sh'

##################################################
# Monitor

alias resetmonitor='xrandr --output HDMI-0 --auto --right-of eDP-1-1 --scale 1x1 --rotate normal'

alias exmonitorcf='xrandr --output DP-1-1 --mode 1920x1080 --pos 1920x0 --rotate normal'
alias exmonitorcfr='xrandr --output DP-1-1 --mode 1920x1080 --pos 1920x0 --rotate right'
alias exmonitorcfl='xrandr --output DP-1-1 --mode 1920x1080 --pos 1920x0 --rotate left'
alias exmonitorc2='xrandr --output DP-1-1 --mode 2560x1440 --pos 1920x0 --rotate normal'
alias exmonitorc4='xrandr --output DP-1-1 --mode 3840x2160 --pos 1920x0 --rotate normal'

alias exmonitorhf='xrandr --output HDMI-0 --mode 1920x1080 --pos 1920x0 --scale 1x1 --rotate normal'
alias exmonitorh2='xrandr --output HDMI-0 --mode 2560x1440 --pos 1920x0 --scale 1x1 --rotate left'
alias exmonitorh4='xrandr --output HDMI-0 --mode 3840x2160 --pos 1920x0 --scale 1x1 --rotate normal'

##################################################
# System

alias removeorphans=''
alias cleanpkg='sudo apt --purge autoremove && sudo apt clean'
alias cleanfp='flatpak uninstall --unused'
alias cleanconda='rm -rf ~/.cache/pip && conda clean -a'
alias cleandocker='docker image prune'
alias cleanvscode='rm -rf /home/anhlh33/.cache/vscode-cpptools'
alias cleanall='cleanconda && cleanpkg && cleandocker && cleanfp && cleanvscode'

alias updatepkg='sudo apt update && sudo apt upgrade'
alias updateall='updatepkg'

alias checkppa='cd /etc/apt/sources.list'
alias checksource='cat /etc/apt/sources.list'
alias editsource='sudo nano /etc/apt/sources.list'

alias dd='sudo dd status=progress'
alias ssh='TERM=xterm-256color ssh'

alias blup='sudo brightnessctl set +10%'
alias bldown='sudo brightnessctl set 10%-'

alias python='python3'

alias hbn='sudo systemctl hibernate'

alias setpem='sudo chown -R anhlh33 ./'

alias limittemp='sudo undervolt -v --temp 95 --core -0 --cache -0 --gpu -0'

alias cpufreq='watch -n1 "grep \"MHz\" /proc/cpuinfo"'

alias testqtile='python3.9 -m py_compile ~/.config/qtile/config.py'

alias resetsound='pulseaudio -k'

alias checkssdtemp='sudo smartctl -a /dev/sda | grep -e "Device Model" -e "Temperature" && echo "" && sudo smartctl -a /dev/nvme0n1 | grep -e "Model Number" -e "Temperature:"'

##################################################
# Reset

alias runlogid='sudo logid -c /home/anhlh33/.config/logid/logid.cfg'
alias resetlogid='sudo systemctl restart logid'
alias resetcuda='sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm'
alias resetserial='sudo chmod 666 /dev/ttyUSB0'
# alias resetserial='sudo chmod a+rw /dev/ttyUSB0'

##################################################
# Applications

alias startdlna='minidlnad -f /home/$USER/.config/minidlna/minidlna.conf -P /home/$USER/.config/minidlna/minidlna.pid'
alias stopdlna='killall minidlnad'

alias sshot='scrot -s IMG_%Y%m%d_%H%M%S.png -e '\''mv $f ~/Miscellaneous'\'
alias genqtile='mkdir -p ~/Cloud/Google\ Drive\ 1/Miscellaneous/Qtile && python3.9 ~/.config/qtile/gen-keybinding-img -c ~/.config/qtile/config.py -o ~/Cloud/Google\ Drive\ 1/Miscellaneous/Qtile'

alias duall='du -hcs .[^.]*'

##################################################
# Miscellaneous

alias mountmtp='aft-mtp-mount ~/MTP'
alias mountftp='curlftpfs 10.10.10.10/Gargoyle ~/Gargoyle -o'

##################################################
# Git

alias gl='git log'
alias gf='git fetch --prune --prune-tags && git status'
alias gs='git status'

function gcp () {
    git commit -m "$1"
}

##################################################
# VinAI

alias sshfs='sshfs -o reconnect,ServerAliveInterval=15,ServerAliveCountMax=3'

alias z43='ssh z43'
alias rs720='ssh rs720'

alias mountz43='sshfs -o reconnect,ServerAliveInterval=15,ServerAliveCountMax=3 z43:/home/ubuntuz43 /home/anhlh33/SSHFS/z43'
alias mountnouvohcm='sshfs -o reconnect,ServerAliveInterval=15,ServerAliveCountMax=3 nouvo-hcm:/home/ubuntu /home/anhlh33/SSHFS/nouvo-hcm'
alias mountnouvo='sshfs -o reconnect,ServerAliveInterval=15,ServerAliveCountMax=3 nouvo:/home/ubuntu /home/anhlh33/SSHFS/nouvo'
alias mountrs720='sshfs -o reconnect,ServerAliveInterval=15,ServerAliveCountMax=3 rs720:/home/rs720 /home/anhlh33/SSHFS/rs720'
alias mountfaceid-dev='sshfs -o reconnect,ServerAliveInterval=15,ServerAliveCountMax=3 faceid-dev:/home/ubuntu /home/anhlh33/SSHFS/faceid-dev'
alias mountisilon='sshfs -o reconnect,ServerAliveInterval=15,ServerAliveCountMax=3 dgx-truongsa:/guardpro /home/anhlh33/SSHFS/isilon'
alias mountmac='sshfs -o reconnect,ServerAliveInterval=15,ServerAliveCountMax=3 mac:/Users/lehoanganh /home/anhlh33/SSHFS/mac'

alias umountz43='sudo umount ~/SSHFS/z43'
alias umountrs720='sudo umount ~/SSHFS/rs720'
alias umountall='for dir_path in ~/SSHFS/*; do sudo umount -f $dir_path; done'

alias rungpu='/home/anhlh33/Serving/docker/run_docker.sh'
alias testgpu='docker start test_gpu && docker exec -it test_gpu bash'
alias delgpu='docker stop test_gpu && docker rm test_gpu'

alias runsdk='/home/anhlh33/Serving/docker/SDK/run_docker_sdk.sh'
alias testsdk='docker start test_gpu_sdk && docker exec -it test_gpu_sdk bash'
alias delsdk='docker stop test_gpu_sdk && docker rm test_gpu_sdk'

alias runfaceid='/home/anhlh33/cctv-faceid-demo/docker/run_docker.sh'
alias testfaceid='docker start faceid_demo && docker exec -it faceid_demo bash'
alias delfaceid='docker stop faceid_demo && docker rm faceid_demo'

alias runandroid='cd /home/anhlh33/Git/guardpro-android-sdk && ./docker/run_docker.sh'
alias testandroid='docker start guardpro-android-sdk && docker exec -it guardpro-android-sdk bash'
alias delandroid='docker stop guardpro-android-sdk && docker rm guardpro-android-sdk'
alias testruntime='/home/anhlh33/Git/guardpro-android-sdk/docker/run_docker_runtime.sh'

alias startvm='/home/anhlh33/SSD2/Backups/VMs/macOS-Simple-KVM/basic.sh'

alias startandroid='/home/anhlh33/VinAI/Portable/android-studio/bin/studio.sh'

alias startmongo='sudo mongod --dbpath /var/lib/mongo'

alias convertpaddle='python3.9 -m paddle_serving_client.convert --dirname inference_model --model_filename model.pdmodel --params_filename model.pdiparams --serving_server serving_server --serving_client serving_client'

alias rtspserver='RTSP_RTSPADDRESS="127.0.0.1:8556" ~/Portable/Linux/RTSP/rtsp-simple-server'

alias makej='make -j$(nproc)'

alias makevideo='ffmpeg -framerate 24 -pattern_type glob -i "*.png" -c:v libx264 -pix_fmt yuv420p -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" 0.mp4'

alias startcompose='docker compose up'
alias stopcompose='docker compose down --rmi local'