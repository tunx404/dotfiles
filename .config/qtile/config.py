# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

##################################################

# python -m py_compile ~/.config/qtile/config.py

##################################################
# Imports

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal

import os
import re
import socket
import subprocess

##################################################
# Dracula Color Palette

color_dracula = {
    'Background':   '#282a36',
    'Current Line': '#44475a',
    'Foreground':   '#f8f8f2',
    'Comment':      '6272a4',
    'Cyan':         '#8be9fd',
    'Green':        '#50fa7b',
    'Orange':       '#ffb86c',
    'Pink':         '#ff79c6',
    'Purple':       '#bd93f9',
    'Red':          '#ff5555',
    'Yellow':       '#f1fa8c',
    'Transparent':  '#00000000',
}

##################################################
# Configurations

layout_margin = 2

font = 'Inconsolata for Powerline'

widget_background_color = None
# widget_background_color = color_dracula['Transparent']
# widget_background_color = color_dracula['Background']
widget_foreground_color = color_dracula['Foreground']
# widget_foreground_color = color_dracula['Red']

bar_size = 24
# bar_margin = [layout_margin, layout_margin, 0, layout_margin]
bar_margin = [0, 0, layout_margin, 0]
bar_background = color_dracula['Transparent']
# bar_background = color_dracula['Background']
bar_opacity = 1
# bar_opacity = 0.85

group_names = [
    '', # DIR
    '', # WEB
    '', # DEV
    '', # DOC
    '', # CLI
    '', # OFF
    '', # MM_
    '', # MON
    '', # SYS
    '', # VM_
]
# 

##################################################
# Applications

mod = 'mod4'

terminal = 'alacritty' # 'kitty'
system_info = terminal + ' -e neofetch'
cli_fun = terminal + ' -e asciiquarium'
calculator = 'galculator'
timer = 'pomotroid'

# DIR
file_manager = 'nemo'
# WEB
broswer = 'google-chrome-stable'
music_playlist = 'google-chrome-stable https://www.youtube.com/playlist?list=PL14zqHuhShBB2_PRQOaD3imODj0Ejzjcv'
# DEV
text_editor  = 'subl'
# DOC
pdf_reader = 'qpdfview'
# CLI
# OFF
# MM_
photo_library = 'darktable'
# MON
system_monitor = 'gnome-system-monitor'
performance_controller = 'cpupower-gui'
system_monitor_cli = terminal + ' -e htop'
cpu_freq = terminal + ' -e watch -n1 "grep \"MHz\" /proc/cpuinfo"'
sensor_monitor = terminal + ' -e watch i8kctl' # ' -e watch sensors'
gpu_monitor = terminal + ' -e nvtop'
# SYS
bluetooth_manager = 'blueman-manager'
volume_controller = 'pavucontrol'
# VM_
virtual_machine = 'virtualbox'

gui_launcher = 'ulauncher'
cli_launcher = 'dmenu_run'
app_launcher = 'rofi -modi drun -show drun -display-drun "RUN"'
file_launcher = 'rofi -show find -modi find:~/.config/rofi/finder.sh'
window_switcher = 'rofi -show window'

change_wallpaper_all = 'nitrogen --set-zoom-fill --random --save /home/tunx404/.wallpapers/Ultra-wide'
change_wallpaper_1   = 'nitrogen --head=0 --set-zoom-fill --random --save /home/tunx404/.wallpapers/Wide'
change_wallpaper_2   = 'nitrogen --head=1 --set-zoom-fill --random --save /home/tunx404/.wallpapers/Wide'
change_wallpaper_dracula_1 = 'nitrogen --head=0 --set-zoom-fill --random --save /home/tunx404/.wallpapers/Wide/Dracula'
change_wallpaper_dracula_2 = 'nitrogen --head=1 --set-zoom-fill --random --save /home/tunx404/.wallpapers/Wide/Dracula'

# screenshot_clipboard = ' -o "%Y-%m-%d_%H-%M-%S.png" -e "xclip -selection clip -t image/png -i $f; mv $f ~/Pictures"'
screenshot_clipboard = ' -o "%Y-%m-%d_%H-%M-%S.png" -e "mv $f ~/Pictures"'

change_dual_monitor_state = 'sh /home/tunx404/.config/qtile/change_dual_monitor_state.sh'

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##################################################
# Functions

def app_to_group(group, app):
    def f(qtile):
        qtile.cmd_spawn(app)
        qtile.current_screen.set_group(qtile.groups[group_names.index(group)])
    return f

def screen_to_prev_group(qtile):
    i = qtile.groups.index(qtile.current_group)
    if i != 0:
        qtile.current_screen.set_group(qtile.groups[i - 1])

def screen_to_next_group(qtile):
    i = qtile.groups.index(qtile.current_group)
    if i + 1 != len(qtile.groups):
        qtile.current_screen.set_group(qtile.groups[i + 1])

def window_to_prev_group(qtile):
    i = qtile.groups.index(qtile.current_group)
    if i != 0:
        if qtile.current_window is not None:
            qtile.current_window.togroup(qtile.groups[i - 1].name)
        qtile.current_screen.set_group(qtile.groups[i - 1])

def window_to_next_group(qtile):
    i = qtile.groups.index(qtile.current_group)
    if i + 1 != len(qtile.groups):
        if qtile.current_window is not None:
            qtile.current_window.togroup(qtile.groups[i + 1].name)
        qtile.current_screen.set_group(qtile.groups[i + 1])

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

##################################################
# Key bindings

keys = [
    # Use xev to find key names

    ####################

    # Applications
    # DIR
    Key([mod], 'e',  lazy.function(app_to_group(group_names[0], file_manager)), desc='File manager'),
    # WEB
    Key([mod], 'c',  lazy.function(app_to_group(group_names[1], broswer)),      desc='Broswer'),
    Key([mod], 'u',  lazy.function(app_to_group(group_names[1], music_playlist)), desc='Music playlist'),
    # DEV
    Key([mod], 't',  lazy.function(app_to_group(group_names[2], text_editor)),  desc='Text editor'),
    # DOC
    Key([mod], 'f',  lazy.function(app_to_group(group_names[3], pdf_reader)),  desc='PDF reader'),
    # MM_
    Key([mod], 'i',  lazy.function(app_to_group(group_names[6], photo_library)),  desc='Photo library'),
    # MON
    Key([mod], 'm',  lazy.function(app_to_group(group_names[7], system_monitor)), desc='System monitor'),
    Key([mod], 'F9', lazy.function(app_to_group(group_names[7], performance_controller)), desc='Performance controller'),
    # SYS
    Key([mod], 'b',  lazy.function(app_to_group(group_names[8], bluetooth_manager)), desc='Bluetooth manager'),
    Key([mod], 'v',  lazy.function(app_to_group(group_names[8], volume_controller)), desc='Volume controller'),

    Key([mod, 'control', 'shift'], 'a',
        # DIR
        lazy.spawn(file_manager),
        # WEB
        lazy.spawn(broswer),
        # DEV
        lazy.spawn(text_editor),
        # DOC
        lazy.spawn(pdf_reader),
        # MON
        lazy.spawn(system_monitor),
        lazy.spawn(performance_controller),
        # SYS
        lazy.spawn(bluetooth_manager),
        lazy.spawn(volume_controller),
    desc='Open all'),

    # Launchers
    Key(['control', 'mod1'], 't', lazy.spawn(terminal), desc='Launch terminal'),
    Key([mod], 'Return', lazy.spawn(terminal), desc='Launch terminal'),
    Key([mod, 'shift'], 'Return', lazy.spawncmd(), desc='Spawn a command using a prompt widget'),

    # Key([mod], 'f', lazy.spawn(file_launcher), desc='File launcher'),
    
    Key([mod], 'r', lazy.spawn(app_launcher), desc='Application launcher'),
    Key([mod, 'shift'], 'r', lazy.spawn(cli_launcher), desc='CLI launcher'),
    Key(['control'], 'space', lazy.spawn(gui_launcher), desc='GUI launcher'),

    Key(['mod1'], 'Tab', lazy.spawn(window_switcher), desc='Switch window'),

    ####################

    # Switch between windows
    # Key([mod], 'h', lazy.layout.left(),  desc='Move focus to left'),
    # Key([mod], 'l', lazy.layout.right(), desc='Move focus to right'),
    # Key([mod], 'j', lazy.layout.down(),  desc='Move focus down'),
    # Key([mod], 'k', lazy.layout.up(),    desc='Move focus up'),

    # Key([mod], 'space', lazy.layout.next(), desc='Move window focus to other window'),

    Key([mod, 'control'], 'a', lazy.layout.left(),  desc='Move focus to left'),
    Key([mod, 'control'], 'd', lazy.layout.right(), desc='Move focus to right'),
    Key([mod, 'control'], 's', lazy.layout.down(),  desc='Move focus down'),
    Key([mod, 'control'], 'w', lazy.layout.up(),    desc='Move focus up'),

    Key([mod], 'q',     lazy.layout.next(), desc='Move window focus to other window'),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    # Key([mod, 'shift'], 'h', lazy.layout.shuffle_left(),  desc='Move window to the left'),
    # Key([mod, 'shift'], 'l', lazy.layout.shuffle_right(), desc='Move window to the right'),
    # Key([mod, 'shift'], 'j', lazy.layout.shuffle_down(),  desc='Move window down'),
    # Key([mod, 'shift'], 'k', lazy.layout.shuffle_up(),    desc='Move window up'),

    Key([mod, 'shift'], 'a', lazy.layout.shuffle_left(),  desc='Move window to the left'),
    Key([mod, 'shift'], 'd', lazy.layout.shuffle_right(), desc='Move window to the right'),
    Key([mod, 'shift'], 's', lazy.layout.shuffle_down(),  desc='Move window down'),
    Key([mod, 'shift'], 'w', lazy.layout.shuffle_up(),    desc='Move window up'),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # Key([mod, 'control'], 'h', lazy.layout.grow_left(),  desc='Grow window to the left'),
    # Key([mod, 'control'], 'l', lazy.layout.grow_right(), desc='Grow window to the right'),
    # Key([mod, 'control'], 'j', lazy.layout.grow_down(),  desc='Grow window down'),
    # Key([mod, 'control'], 'k', lazy.layout.grow_up(),    desc='Grow window up'),

    # Key([mod], 'n', lazy.layout.normalize(), desc='Reset all window sizes'),

    Key([mod], 'a', lazy.layout.grow_left(),  desc='Grow window to the left'),
    Key([mod], 'd', lazy.layout.grow_right(), desc='Grow window to the right'),
    Key([mod], 's', lazy.layout.grow_down(),  desc='Grow window down'),
    Key([mod], 'w', lazy.layout.grow_up(),    desc='Grow window up'),

    Key([mod], 'z', lazy.layout.normalize(), desc='Reset all window sizes'),

    ####################

    # Windows
    Key([mod], 'Up',   lazy.window.toggle_fullscreen(), desc='Fullscreen'),
    Key([mod], 'Down', lazy.window.toggle_floating(),   desc='Floating'),

    Key([mod, 'shift'],   'q', lazy.window.toggle_fullscreen(), desc='Fullscreen'),
    Key([mod, 'control'], 'q', lazy.window.toggle_floating(),   desc='Floating'),

    Key([mod, 'shift'], 'c', lazy.window.kill(), desc='Kill focused window'),

    # Toggle between different layouts as defined below
    Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with multiple stack panes
    # Key([mod, 'shift'], 'Return', lazy.layout.toggle_split(), desc='Toggle between split and unsplit sides of stack'),

    # Groups
    Key(['control', 'mod1'], 'Right', lazy.function(screen_to_next_group), desc='Switch to the next group'),
    Key(['control', 'mod1'], 'Left',  lazy.function(screen_to_prev_group), desc='Switch to the prev group'),

    Key(['control', 'shift', 'mod1'], 'Right', lazy.function(window_to_next_group), desc='Move window to the next group'),
    Key(['control', 'shift', 'mod1'], 'Left',  lazy.function(window_to_prev_group), desc='Move window to the prev group'),

    # Screens
    Key([mod], 'Right', lazy.to_screen(1), desc='Move focus to the next screen'),
    Key([mod], 'Left',  lazy.to_screen(0), desc='Move focus to the prev screen'),
    
    Key([mod, 'shift'], 'Right', lazy.function(window_to_next_screen),     lazy.to_screen(1), desc='Move window to the next screen'),
    Key([mod, 'shift'], 'Left',  lazy.function(window_to_previous_screen), lazy.to_screen(0), desc='Move window to the prev screen'),

    Key([mod, 'control'], 'Left',    lazy.spawn('xrandr --output DP-3  --mode 1920x1080 --pos 1920x0 --rotate left'),     desc='Rotate monitor 2 left'),
    Key([mod, 'control'], 'Right',   lazy.spawn('xrandr --output DP-3  --mode 1920x1080 --pos 1920x0 --rotate right'),    desc='Rotate monitor 2 right'),
    Key([mod, 'control'], 'Up',      lazy.spawn('xrandr --output DP-3  --mode 1920x1080 --pos 1920x0 --rotate normal'),   desc='Rotate monitor 2 normal'),
    Key([mod, 'control'], 'Down',    lazy.spawn('xrandr --output DP-3  --mode 1920x1080 --pos 1920x0 --rotate inverted'), desc='Rotate monitor 2 inverted'),

    Key([mod, 'control'], 'Return',  lazy.spawn('nitrogen --restore'), desc='Reset wallpaper'),

    Key([mod], 'p', lazy.spawn(change_dual_monitor_state), desc='Change dual monitor state'),

    # Wallpapers
    Key([mod, 'control'], 'grave', lazy.spawn(change_wallpaper_all), desc='Change wallpaper on both screen'),
    Key([mod, 'control'], '1',     lazy.spawn(change_wallpaper_1),   desc='Change wallpaper on screen 1'),
    Key([mod, 'control'], '2',     lazy.spawn(change_wallpaper_2),   desc='Change wallpaper on screen 2'),
    Key([mod, 'control'], '3',     lazy.spawn(change_wallpaper_dracula_1), lazy.spawn(change_wallpaper_dracula_2), desc='Change wallpaper to dracula'),

    # Screenshots
    Key([], 'Print', lazy.spawn('scrot' + screenshot_clipboard), desc='Screenshot (all)'),
    Key(['control'], 'Print', lazy.spawn('scrot -u' + screenshot_clipboard), desc='Screenshot (window)'),
    Key(['shift'], 'Print', lazy.spawn('scrot -s -f' + screenshot_clipboard), desc='Screenshot (area)'),

    ####################

    # System
    Key([mod, 'control', 'shift'], 'Delete', lazy.shutdown(), desc='Shutdown Qtile'),
    Key([mod, 'control', 'shift'], 'Escape', lazy.spawn('shutdown -h now'), desc='Shutdown'),
    Key([mod, 'control', 'shift'], 'End', lazy.spawn('reboot'), desc='Reboot'),
    Key([mod, 'control', 'shift'], 'l', lazy.spawn('systemctl suspend'), desc='Suspend'),
    Key([mod, 'control', 'shift'], 'h', lazy.spawn('systemctl hibernate'), desc='Hibernate'),

    # Qtile
    # Key([mod, 'control'], 'r', lazy.reload_config(), desc='Reload the config'),
    Key([mod, 'control'], 'r', lazy.restart(), desc='Reload the config'),

    # Fn keys
    Key([], 'XF86MonBrightnessUp',   lazy.spawn('brightnessctl set +10%')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl set 10%-')),

    Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer sset Master,0 5%-')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer sset Master,0 5%+')),
    Key([], 'XF86AudioMute',        lazy.spawn('amixer sset Master,0 toggle')),
    Key([], 'XF86AudioPlay',        lazy.spawn(
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify'
        '/org/mpris/MediaPlayer2'
        'org.mpris.MediaPlayer2.Player.PlayPause')
    ),

    Key([], 'XF86Calculator', lazy.spawn(calculator)),
]


##################################################
# Groups

# DIR
# WEB
# DEV
# DOC
# CLI
# OFF
# MM_
# MON
# SYS
# VM_

num_groups = 10

group_matches = [
    [Match(wm_class=['Nemo', 'Insync'])],
    [Match(wm_class=['Google-chrome', 'Opera', 'KeePassXC', 'qBittorrent', 'Caprine', 'Whatsapp-for-linux', 'Cisco AnyConnect Secure Mobility Client', 'Ao'])],
    [Match(wm_class=['Subl', 'pomotroid', 'jetbrains-studio'])],
    [Match(wm_class=['qpdfview', 'pdf'])],
    [Match(wm_class=[])],
    [Match(wm_class=['et', 'wps', 'wpp', 'Lifeograph'])],
    [Match(wm_class=['Darktable', 'vlc', 'Gimp-2.10', 'Spotify'])],
    [Match(wm_class=['Gnome-system-monitor', 'Cpupower-gui'])],
    [Match(wm_class=['Blueman-manager', 'Pavucontrol', 'Pamac-manager'])],
    [Match(wm_class=['VirtualBox Manager'])],
]

group_layouts = [
    'columns',
    'max',
    'columns',
    'columns',
    'ratiotile',
    'columns',
    'max',
    'ratiotile',
    'columns',
    'max',
]

groups = [Group(group_names[i], matches=group_matches[i], layout=group_layouts[i]) for i in range(num_groups)]

for k, group in zip(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], groups):
    keys.extend([
        Key([mod], k, lazy.group[group.name].toscreen(), desc='Switch to group {}'.format(group.name)),
        Key([mod, 'shift'], k, lazy.window.togroup(group.name, switch_group=True), desc='Switch to & move focused window to group {}'.format(group.name))
    ])

# groups = [Group(i) for i in '123456789']

# https://docs.qtile.org/en/stable/manual/config/groups.html
# from libqtile.dgroups import simple_key_binder
# dgroups_key_binder = simple_key_binder('mod4')

# for i in groups:
#     keys.extend([
#         # mod1 + letter of group = switch to group
#         Key([mod], i.name, lazy.group[i.name].toscreen(),
#             desc='Switch to group {}'.format(i.name)),

#         # mod1 + shift + letter of group = switch to & move focused window to group
#         Key([mod, 'shift'], i.name, lazy.window.togroup(i.name, switch_group=True),
#             desc='Switch to & move focused window to group {}'.format(i.name)),
#         # Or, use below if you prefer not to switch to that group.
#         # # mod1 + shift + letter of group = move focused window to group
#         # Key([mod, 'shift'], i.name, lazy.window.togroup(i.name),
#         #     desc='move focused window to group {}'.format(i.name)),
#     ])

##################################################
# Layouts

layout_config = {'border_width': 2,
                'margin': layout_margin,
                # 'border_focus': color_dracula['Comment'],
                'border_focus': color_dracula['Foreground'],
                # 'border_normal': color_dracula['Current Line'],
                'border_normal': color_dracula['Comment'],
}

layouts = [
    layout.Columns(
        **layout_config,
        border_on_single=True,
    ),
    layout.Max(**layout_config),
    layout.Stack(**layout_config, num_stacks=2),
    layout.Bsp(**layout_config),
    layout.Matrix(**layout_config),
    layout.MonadTall(**layout_config),
    layout.MonadWide(**layout_config),
    layout.RatioTile(**layout_config),
    layout.Tile(**layout_config),
    layout.TreeTab(**layout_config),
    layout.VerticalTile(**layout_config),
    layout.Zoomy(**layout_config),
    layout.Floating(**layout_config),
]


##################################################
# Screens

# sudo subl /lib/python3.9/site-packages/libqtile/widget/graph.py
graph_config = dict(
    border_color=widget_foreground_color,
    border_width=1,
    fill_color=widget_foreground_color,
    graph_color=widget_foreground_color,
    line_width=1,
    samples=60,
)

def init_widget_list():
    def separator_right(bg_color, fg_color):
        return widget.TextBox(
            text='|',
            fontsize=16,
            # background=bg_color,
            # foreground=fg_color,
        )

    def separator_left(bg_color, fg_color):
        return widget.TextBox(
            text='|',
            fontsize=16,
            # background=bg_color,
            # foreground=fg_color,
        )

    widget_list = [
        widget.Image(
            filename='~/.config/qtile/icons/Manjaro_logo_white.png',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(cli_fun)},
            margin=4,
        ),
        widget.Prompt(
            prompt=prompt,
            font='Inconsolata for Powerline',
        ),

        separator_left(widget_background_color, widget_foreground_color),
        widget.GroupBox(
            # font='Inconsolata SemiBold',
            fontsize=28,
            # active=color_dracula['Foreground'],
            # inactive=color_dracula['Current Line'],
            block_highlight_text_color=color_dracula['Foreground'],
            # highlight_color=color_dracula['Current Line'],
            # highlight_color=color_dracula['Comment'],
            highlight_color=color_dracula['Red'],
            highlight_method='line',
            this_current_screen_border=color_dracula['Foreground'],
            this_screen_border=color_dracula['Current Line'],
            other_current_screen_border=color_dracula['Foreground'],
            other_screen_border=color_dracula['Current Line'],
            # hide_unused=True,
        ),

        separator_left(widget_background_color, widget_foreground_color),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            scale=0.7,
        ),
        widget.CurrentLayout(),

        separator_left(widget_background_color, widget_foreground_color),
        widget.TaskList(
            border=color_dracula['Foreground'],
            borderwidth=1,
            max_title_width=200,
            icon_size=16,
            margin=1,
        ),

        ####################

        separator_right(widget_background_color, widget_foreground_color),
        widget.OpenWeather(
            cityid='5206379',
            format='{temp}°{units_temperature} {humidity}% {weather_details}',
        ),

        # separator_right(widget_background_color, widget_foreground_color),
        # widget.CPUGraph(
        #     **graph_config,
        #     mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(cpu_freq)},
        # ),
        
        # separator_right(widget_background_color, widget_foreground_color),
        # widget.MemoryGraph(
        #     **graph_config,
        #     mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(system_monitor_cli)},
        # ),
        
        # separator_right(widget_background_color, widget_foreground_color),
        # widget.NetGraph(
        #     **graph_config,
        #     mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(system_monitor)},
        #     bandwidth_type='down',
        # ),

        # separator_right(widget_background_color, widget_foreground_color),
        # widget.NetGraph(
        #     **graph_config,
        #     mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(system_monitor)},
        #     bandwidth_type='up',
        # ),

        separator_right(widget_background_color, widget_foreground_color),
        widget.CPU(
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(system_monitor_cli)},
        ),

        separator_right(widget_background_color, widget_foreground_color),
        widget.Memory(
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(system_monitor_cli)},
        ),

        separator_right(widget_background_color, widget_foreground_color),
        widget.Net(
            interface='wlo1',
            format='{down} ↓↑ {up}',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(system_monitor)},
        ),

        separator_right(widget_background_color, widget_foreground_color),
        widget.ThermalSensor(
            tag_sensor='Package id 0',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(sensor_monitor)},
        ),

        separator_right(widget_background_color, widget_foreground_color),
        widget.NvidiaSensors(
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(gpu_monitor)},
        ),

        separator_right(widget_background_color, widget_foreground_color),
        widget.Volume(
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(volume_controller)},
        ),

        separator_right(widget_background_color, widget_foreground_color),
        widget.Systray(),

        separator_right(widget_background_color, widget_foreground_color),
        widget.Clock(
            format="%a %d/%m %H:%M:%S",
        ),

        # widget.Backlight(),
        # widget.LaunchBar(progs=[('thunderbird', 'thunderbird -safe-mode', 'launch thunderbird in safe mode')]),
        # widget.AGroupBox(),
        # widget.WindowTabs(),
        # widget.WidgetBox(widgets=[
        #         widget.TextBox(text="This widget is in the box"),
        #         widget.Memory()
        #     ]
        # ),
        # widget.HDDBusyGraph(),
        # widget.CheckUpdates(
        #     background=widget_background_color,
        #     update_interval=600,
        #     mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal + ' -e sudo pacman -Syyu')},
        # ),
        # widget.CapsNumLockIndicator(
        #     background=widget_background_color,
        # ),

        ####################

        # widget.CurrentLayout(),
        # widget.GroupBox(),
        # widget.Prompt(),
        # widget.WindowName(),
        # widget.Chord(
        #     chords_colors={
        #         'launch': ('#ff0000', '#ffffff'),
        #     },
        #     name_transform=lambda name: name.upper(),
        # ),
        # widget.TextBox('default config', name='default'),
        # widget.TextBox('Press &lt;M-r&gt; to spawn', foreground='#d75f5f'),
        # widget.Systray(),
        # widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
        # widget.QuickExit(),
    ]
    return widget_list
    
widget_list1 = init_widget_list()
widget_list2 = init_widget_list()[:-3] + init_widget_list()[-1:]

widget_defaults = dict(
    font=font,
    fontsize=14,
    padding=3,
    background=widget_background_color,
    foreground=widget_foreground_color,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(top=bar.Bar(widgets=widget_list1, size=bar_size, background=bar_background, margin=bar_margin, opacity=bar_opacity)),
    Screen(top=bar.Bar(widgets=widget_list2, size=bar_size, background=bar_background, margin=bar_margin, opacity=bar_opacity)),
]


##################################################
# Startup commands

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


##################################################
# Others

# Drag floating layouts.
mouse = [
    Drag([mod],  'Button1', lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod],  'Button3', lazy.window.set_size_floating(),     start=lazy.window.get_size()),
    Click([mod], 'Button2', lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = 'smart'
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = 'LG3D'
