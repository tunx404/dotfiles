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

alias cmuvpn='sudo openconnect -u alehoang vpn.cmu.edu'

alias dng='WINEPREFIX=$HOME/.wine-dng wine "$HOME/.wine-dng/drive_c/Program Files/Adobe/Adobe DNG Converter/Adobe DNG Converter.exe"'
alias dng-wine='WINEPREFIX=$HOME/.wine-dng wine'
alias dng-cfg='WINEPREFIX=$HOME/.wine-dng winecfg'

alias resetcuda='sudo rmmod nvidia_uvm && sudo modprobe nvidia_uvm'
alias resetlogid='sudo systemctl restart logid'

alias checkpower='cat /proc/acpi/bbswitch'

alias update-grub='sudo grub-mkconfig -o /boot/grub/grub.cfg'

alias removeorphans='pacman -Qtdq | sudo pacman -Rns -'
alias cleanpkg='sudo pacman -Scc && yay -Scc && rm -rf ~/.cache/yay && removeorphans'
alias updatepkg='sudo pacman -Syu && yay -Syu'

alias cleandt='~/.config/darktable/purge_non_existing_images.sh --purge && darktable-generate-cache'

alias mountmtp='aft-mtp-mount ~/Quest2'

alias adddot='~/.scripts/add_dotfiles.sh'
alias pushdot='~/.scripts/push_dotfiles.sh'

alias ohmonitor='xrandr --output DP-3 --mode 1680x1050 --pos 1920x0 --rotate normal'

alias ssh='TERM=xterm-256color ssh'

# 18744
alias cdav='cd $HOME/Miscellaneous/18744'

# 18646
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/cppunit/lib
