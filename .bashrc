# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

##################################################
# 0bash_aliases

if [ -f ~/.bash_aliases ]; then
. ~/.bash_aliases
fi

##################################################
# IBus

export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus

##################################################
# Conda

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/tunx404/.miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/tunx404/.miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/tunx404/.miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/tunx404/.miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# conda activate torch

##################################################
# Kaggle

export PATH=~/.local/bin:$PATH

##################################################
# Prompt

eval "$(starship init bash)"

##################################################
# Fetch

# neofetch
paleofetch

##################################################
# MATLAB

export LD_PRELOAD=/lib64/libfreetype.so

# ##################################################
# # ROS

# source /opt/ros/noetic/setup.bash

# ##################################################
# # DaVinci Resolve

# export __NV_PRIME_RENDER_OFFLOAD=1
# export __GLX_VENDOR_LIBRARY_NAME=nvidia
