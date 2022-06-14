# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

##################################################
# IBus

export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus

##################################################
# DaVinci Resolve

export __NV_PRIME_RENDER_OFFLOAD=1
export __GLX_VENDOR_LIBRARY_NAME=nvidia

##################################################
# Conda

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/tunx404/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/tunx404/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/tunx404/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/tunx404/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# export PATH=~/miniconda3/bin:$PATH
# alias conda=~/miniconda3/bin/conda

conda activate torch

##################################################
# Kaggle

export PATH=~/.local/bin:$PATH

##################################################
# Prompt

eval "$(starship init bash)"

##################################################
# Dotfiles

alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

##################################################
# Fetch

# neofetch
paleofetch

##################################################
# Miscellaneous

alias resetlogid='sudo systemctl restart logid'

alias checkpower='cat /proc/acpi/bbswitch'

alias update-grub='sudo grub-mkconfig -o /boot/grub/grub.cfg'

alias updatepkg='sudo pacman -Syu && yay -Syu'
alias removeorphans='pacman -Qtdq | sudo pacman -Rns -'
alias cleanpkg='sudo pacman -Scc && yay -Scc && rm -rf ~/.cache/yay && removeorphans'

alias cleandt='~/.config/darktable/purge_non_existing_images.sh --purge && darktable-generate-cache'

alias cleanall='cleanpkg && cleandt && conda clean -a'

alias mountmtp='aft-mtp-mount ~/MTP'

alias adddot='~/.scripts/add_dotfiles.sh'
alias pushdot='~/.scripts/push_dotfiles.sh'

alias exmonitor='xrandr --output DP-3 --mode 1920x1080 --pos 1920x0 --rotate normal'

# CMU
alias cmuvpn='sudo openconnect -u alehoang vpn.cmu.edu'
alias ssh='TERM=xterm-256color ssh'
alias resetcuda='sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm'

alias fintec='cd $HOME/Cloud/Google\ Drive\ 1/Projects/Fintecism/financialadvisor && conda activate fin && jupyter-lab'

alias startdlna='minidlnad -f /home/$USER/.config/minidlna/minidlna.conf -P /home/$USER/.config/minidlna/minidlna.pid'
alias stopdlna='killall minidlnad'

alias mountftp='curlftpfs 10.10.10.10/Gargoyle ~/Gargoyle -o user=tunx404:x00rdsrw'

alias pkgtop='pkgtop -pacman yay'
