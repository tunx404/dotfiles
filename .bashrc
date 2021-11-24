#
# ~/.bashrc
#

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
# 18648

export HARCH=`echo $(uname -m) | sed "s/i./x/g"`
export PATH=$HOME/18648/gcc-linaro-4.9.4-2017.01-x86_64_arm-linux-gnueabi/bin:$PATH
export PATH=$HOME/18648/bootimg-tools:$PATH
export CROSS_COMPILE=arm-linux-gnueabi- ARCH=arm

export PATH=$HOME/18648/android-ndk-r9:$HOME/18648/android-ndk-r9/toolchains/arm-linux-androideabi-4.8/prebuilt/linux-$HARCH/bin:$PATH

export ANDROID_RAMDISK=$HOME/18648/nakasi-jdq39/boot-img/boot.img-ramdisk-root.gz
export ANDROID_KERNEL=$HOME/18648/kernel/arch/arm/boot/zImage


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

alias updategrub='sudo grub-mkconfig -o /boot/grub/grub.cfg'
alias removeorphans='pacman -Qtdq | sudo pacman -Rns -'
alias cleanpkg='sudo pacman -Scc && yay -Scc && rm -rf ~/.cache/yay && removeorphans'
alias updatepkg='sudo pacman -Syu && yay -Syu'

# 18786
export PEM_18786=/home/tunx404/.ssh/18786.pem
alias tunx='cd $HOME/Miscellaneous'
alias tunxj='cd $HOME/Miscellaneous && conda deactivate && jupyter-lab'
alias cdker='cd $HOME/18648/kernel'

# 18648
alias buildjni='cd $HOME/18648/taskmon/energymon/TaskMon/app/src/main && ndk-build'
alias buildkernel='cd $HOME/18648/kernel && make oldconfig && make -j12 && file arch/arm/boot/compressed/vmlinux'
alias cdkernel='cd $HOME/18648/kernel' # && git status'
alias cdmon='cd $HOME/18648/taskmon' # && git status'
