export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus

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

export HARCH=`echo $(uname -m) | sed "s/i./x/g"`
export PATH=/opt/gcc-linaro-4.9.4-2017.01-x86_64_arm-linux-gnueabi/bin:$PATH
export PATH=$HOME/bootimg-tools:$PATH
export CROSS_COMPILE=arm-linux-gnueabi- ARCH=arm
export CROSS_COMPILE=arm-linux-gnueabi- ARCH=arm
export CROSS_COMPILE=arm-linux-gnueabi- ARCH=arm
export HARCH=`echo $(uname -m) | sed "s/i./x/g"`
export CROSS_COMPILE=arm-linux-gnueabi- ARCH=arm
export PATH=$HOME/android-ndk-r9:$HOME/android-ndk-r9/toolchains/arm-linux-androideabi-4.8/prebuilt/linux-$HARCH/bin:$PATH
eval "$(starship init bash)"
export PATH=/opt/darktable/bin:$PATH
alias dotfiles="/usr/bin/git --git-dir=$HOME/.dotfiles.git/ --work-tree=$HOME"
