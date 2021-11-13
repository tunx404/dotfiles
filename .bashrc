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
export PATH=/opt/gcc-linaro-4.9.4-2017.01-x86_64_arm-linux-gnueabi/bin:$PATH
export PATH=$HOME/bootimg-tools:$PATH
export CROSS_COMPILE=arm-linux-gnueabi- ARCH=arm
export HARCH=`echo $(uname -m) | sed "s/i./x/g"`
export PATH=$HOME/android-ndk-r9:$HOME/android-ndk-r9/toolchains/arm-linux-androideabi-4.8/prebuilt/linux-$HARCH/bin:$PATH

export ANDROID_RAMDISK=~/nakasi-jdq39/boot-img/boot.img-ramdisk-root.gz
export ANDROID_KERNEL=~/kernel/arch/arm/boot/zImage


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

alias tunx='cd $HOME/Miscellaneous'
export TUNX=$HOME/Miscellaneous
alias cmuvpn='sudo openconnect -u alehoang vpn.cmu.edu'
alias tunxj='cd $HOME/Miscellaneous && conda deactivate && jupyter-lab'

alias dng='WINEPREFIX=$HOME/.wine-dng wine "$HOME/.wine-dng/drive_c/Program Files/Adobe/Adobe DNG Converter/Adobe DNG Converter.exe"'
alias dng-wine='WINEPREFIX=$HOME/.wine-dng wine'
alias dng-cfg='WINEPREFIX=$HOME/.wine-dng winecfg'