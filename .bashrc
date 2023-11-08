# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

##################################################
# bash_aliases

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

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

##################################################
# Prompt

eval "$(starship init bash)"

##################################################
# Fetch

paleofetch

##################################################
# Applications

# IBus
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus

