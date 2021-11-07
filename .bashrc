#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

# IBus
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus

# Conda
export PATH=~/miniconda3/bin:$PATH
# source activate torch

# Kaggle
export PATH=~/.local/bin:$PATH

# 18648
export HARCH=`echo $(uname -m) | sed "s/i./x/g"`
export PATH=/opt/gcc-linaro-4.9.4-2017.01-x86_64_arm-linux-gnueabi/bin:$PATH
export PATH=$HOME/bootimg-tools:$PATH
export CROSS_COMPILE=arm-linux-gnueabi- ARCH=arm
export HARCH=`echo $(uname -m) | sed "s/i./x/g"`
export PATH=$HOME/android-ndk-r9:$HOME/android-ndk-r9/toolchains/arm-linux-androideabi-4.8/prebuilt/linux-$HARCH/bin:$PATH

export ANDROID_RAMDISK=~/nakasi-jdq39/boot-img/boot.img-ramdisk-root.gz
export ANDROID_KERNEL=~/kernel/arch/arm/boot/zImage

# Prompt
eval "$(starship init bash)"

# Dotfiles
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

# neofetch
paleofetch

# Miscellaneous
export TUNX=~/SSD1/Miscellaneous