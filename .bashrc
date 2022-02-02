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
# source activate torch
# alias conda=~/miniconda3/bin/conda

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

export TUNX=$HOME/Miscellaneous

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

# 18786
export PEM_18786=/home/tunx404/.ssh/18786.pem
alias tunx='cd $HOME/Miscellaneous'
alias tunxj='cd $HOME/Miscellaneous && conda deactivate && jupyter-lab'
alias cdker='cd $HOME/18648/kernel'