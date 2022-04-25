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

from typing import List

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
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

layout_margin = 4

font = 'Ubuntu Condensed Regular'

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

# 
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

##################################################
# Applications

mod = 'mod4'
terminal = 'alacritty'

####################

# DIR
file_manager = 'nemo'
# WEB
browser = 'google-chrome-stable'
messenger1 = 'whatsapp-nativefier'
messenger2 = 'caprine'
email_client = 'thunderbird'
password_manager = 'keepassxc'
music_playlist = 'google-chrome-stable https://www.youtube.com/playlist?list=PL14zqHuhShBB2_PRQOaD3imODj0Ejzjcv'
study_playlist = 'google-chrome-stable https://www.youtube.com/playlist?list=PLtAPmAYb-kX9AfgUB7s90ez_j8D-2avvC'
# DEV
text_editor  = 'subl'
# DOC
pdf_reader = 'qpdfview'
pomodoro_timer = 'pomotroid --no-sandbox'
# CLI
# OFF
task_manager = 'ao'
# MM_
photo_library = 'darktable'
# MON
system_monitor = 'gnome-system-monitor'
performance_controller = 'cpupower-gui'
system_monitor_cli = terminal + ' -e htop'
cpu_freq_monitor = terminal + ' -e watch -n1 "grep \"MHz\" /proc/cpuinfo"'
sensor_monitor = terminal + ' -e watch i8kctl' # ' -e watch sensors'
gpu_monitor = terminal + ' -e nvtop'
battery_monitor = terminal + ' -e battop'
# SYS
bluetooth_manager = 'blueman-manager'
volume_controller = 'pavucontrol'
# VM_
virtual_machine = 'vmware' # 'virtualbox'
# OTHERS
calculator = 'qalculate-gtk'
cli_fun = terminal + ' -e asciiquarium'

####################

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

# screenshot_clipboard = ' -o "%Y-%m-%d_%H-%M-%S.png" -e "xclip -selection clip -t image/png -i $f; mv $f ~/SSD1/Miscellaneous"'
screenshot_clipboard = ' -o "IMG_%Y%m%d_%H%M%S.png" -e "mv $f ~/SSD1/Miscellaneous"'
screen_recorder = 'sa.sy.bluerecorder'

change_dual_monitor_state = 'sh /home/tunx404/.scripts/change_dual_monitor_state.sh'
power_saving = 'sh /home/tunx404/.scripts/power_saving.sh '
performance_profile = 'cpupower-gui profile '

prompt = "{0}@{1}: ".format(os.environ['USER'], socket.gethostname())

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
    # xev | grep 'keycode'

    ####################
    # Applications

    # DIR
    Key([mod], 'e',  lazy.function(app_to_group(group_names[0], file_manager)), desc='File manager'),
    # WEB
    Key([mod], 'c',  lazy.function(app_to_group(group_names[1], browser)),      desc='Browser'),
    # Key([mod], 'g',  lazy.function(app_to_group(group_names[1], email_client)), desc='Email client'),
    Key([mod], 'k',  lazy.function(app_to_group(group_names[1], password_manager)), desc='Password manager'),
    Key([mod], 'u',          lazy.function(app_to_group(group_names[1], music_playlist)), desc='Music playlist'),
    Key([mod, 'shift'], 'u', lazy.function(app_to_group(group_names[1], study_playlist)), desc='Study with me playlist'),
    Key([mod], 'm',  lazy.function(app_to_group(group_names[1], messenger1)), desc='Messenger'),
    # DEV
    Key([mod], 't',  lazy.function(app_to_group(group_names[2], text_editor)),  desc='Text editor'),
    # DOC
    Key([mod], 'f',  lazy.function(app_to_group(group_names[3], pdf_reader)),  desc='PDF reader'),
    Key([mod], 'o',  lazy.function(app_to_group(group_names[3], pomodoro_timer)),  desc='Pomodoro timer'),
    # OFF
    Key([mod], 'j',  lazy.function(app_to_group(group_names[5], pomodoro_timer)),  desc='Task manager'),
    # MM_
    Key([mod], 'i',  lazy.function(app_to_group(group_names[6], photo_library)),  desc='Photo library'),
    # MON
    Key([mod], 'y',  lazy.function(app_to_group(group_names[7], system_monitor)), desc='System monitor'),
    Key([mod], 'F9', lazy.function(app_to_group(group_names[7], performance_controller)), desc='Performance controller'),
    # SYS
    Key([mod], 'v',  lazy.function(app_to_group(group_names[8], volume_controller)),
                     lazy.function(app_to_group(group_names[8], bluetooth_manager)), desc='Volume controller & Bluetooth manager'),

    Key(['control', 'shift', 'mod1'], 'a',
        # DIR
        lazy.spawn(file_manager),
        # WEB
        # lazy.spawn(email_client),
        lazy.spawn(browser),
        # DEV
        lazy.spawn(text_editor),
        # DOC
        lazy.spawn(pdf_reader),
        lazy.spawn(pomodoro_timer),
        # OFF
        lazy.spawn(task_manager),
        # MON
        lazy.spawn(system_monitor),
        # SYS
        lazy.spawn(bluetooth_manager),
        lazy.spawn(volume_controller),
    desc='Open all'),

    # Launchers
    Key(['control', 'mod1'], 't', lazy.spawn(terminal), desc='Launch terminal'),
    Key([mod], 'Return', lazy.spawn(terminal), desc='Launch terminal'),
    Key([mod], 'KP_Enter', lazy.spawn(terminal), desc='Launch terminal'),
    Key([mod, 'shift'], 'Return', lazy.spawncmd(), desc='Spawn a command using a prompt widget'),

    # Key([mod], 'f', lazy.spawn(file_launcher), desc='File launcher'),
    
    Key([mod], 'r', lazy.spawn(app_launcher), desc='Application launcher'),
    Key([mod, 'shift'], 'r', lazy.spawn(cli_launcher), desc='CLI launcher'),
    Key(['control'], 'space', lazy.spawn(gui_launcher), desc='GUI launcher'),

    # Key(['mod1'], 'Tab', lazy.spawn(window_switcher), desc='Switch window'),

    ####################
    # Windows

    Key([mod], 'q', lazy.layout.next(), desc='Move window focus to other window'),
    Key(['mod1'], 'Tab', lazy.layout.next(), desc='Move window focus to other window'),

    Key([mod, 'shift'], 'a', lazy.layout.shuffle_left(),  desc='Move window to the left'),
    Key([mod, 'shift'], 'd', lazy.layout.shuffle_right(), desc='Move window to the right'),
    Key([mod, 'shift'], 's', lazy.layout.shuffle_down(),  desc='Move window down'),
    Key([mod, 'shift'], 'w', lazy.layout.shuffle_up(),    desc='Move window up'),

    Key([mod], 'a', lazy.layout.grow_left(),  desc='Grow window to the left'),
    Key([mod], 'd', lazy.layout.grow_right(), desc='Grow window to the right'),
    Key([mod], 's', lazy.layout.grow_down(),  desc='Grow window down'),
    Key([mod], 'w', lazy.layout.grow_up(),    desc='Grow window up'),

    Key([mod], 'z', lazy.layout.normalize(), desc='Reset all window sizes'),

    Key([mod], 'Up',   lazy.window.toggle_fullscreen(), desc='Fullscreen'),
    Key([mod], 'Down', lazy.window.toggle_floating(),   desc='Floating'),

    Key([mod, 'control'],   'q', lazy.window.toggle_fullscreen(), desc='Fullscreen'),
    Key([mod, 'shift'], 'q', lazy.window.toggle_floating(),   desc='Floating'),

    Key([mod, 'shift'], 'c', lazy.window.kill(), desc='Kill focused window'),

    Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),

    ####################

    # Groups
    Key(['control', 'mod1'], 'Right', lazy.function(screen_to_next_group), desc='Switch to the next group'),
    Key(['control', 'mod1'], 'Left',  lazy.function(screen_to_prev_group), desc='Switch to the prev group'),

    Key([mod, 'control'], 'w', lazy.function(screen_to_next_group), desc='Switch to the next group'),
    Key([mod, 'control'], 's', lazy.function(screen_to_prev_group), desc='Switch to the prev group'),

    Key(['control', 'shift', 'mod1'], 'Right', lazy.function(window_to_next_group), desc='Move window to the next group'),
    Key(['control', 'shift', 'mod1'], 'Left',  lazy.function(window_to_prev_group), desc='Move window to the prev group'),

    Key([mod, 'control', 'shift'], 'w', lazy.function(window_to_next_group), desc='Move window to the next group'),
    Key([mod, 'control', 'shift'], 's', lazy.function(window_to_prev_group), desc='Move window to the prev group'),

    # Screens
    Key([mod], 'Right', lazy.to_screen(1), desc='Move focus to the next screen'),
    Key([mod], 'Left',  lazy.to_screen(0), desc='Move focus to the prev screen'),

    Key([mod, 'control'], 'd', lazy.to_screen(1), desc='Move focus to the next screen'),
    Key([mod, 'control'], 'a', lazy.to_screen(0), desc='Move focus to the prev screen'),
    
    Key([mod, 'shift'], 'Right', lazy.function(window_to_next_screen),     lazy.to_screen(1), desc='Move window to the next screen'),
    Key([mod, 'shift'], 'Left',  lazy.function(window_to_previous_screen), lazy.to_screen(0), desc='Move window to the prev screen'),

    Key([mod, 'control', 'shift'], 'd', lazy.function(window_to_next_screen),     lazy.to_screen(1), desc='Move window to the next screen'),
    Key([mod, 'control', 'shift'], 'a', lazy.function(window_to_previous_screen), lazy.to_screen(0), desc='Move window to the prev screen'),

    Key([mod, 'control'], 'Left',  lazy.spawn('xrandr --output DP-3    --mode 1920x1080 --pos 1920x0 --rotate left'),
                                   lazy.spawn('nitrogen --restore'),
                                   desc='Rotate monitor 2 left'),
    Key([mod, 'control'], 'Right', lazy.spawn('xrandr --output DP-3    --mode 1920x1080 --pos 1920x0 --rotate right'),
                                   lazy.spawn('nitrogen --restore'),
                                   desc='Rotate monitor 2 right'),
    Key([mod, 'control'], 'Up',    lazy.spawn('xrandr --output DP-3    --mode 1920x1080 --pos 1920x0 --rotate normal'),
                                   lazy.spawn('nitrogen --restore'),
                                   desc='Rotate monitor 2 normal'),
    Key([mod, 'control'], 'Down',  lazy.spawn('xrandr --output DP-3    --mode 1920x1080 --pos 1920x0 --rotate inverted'),
                                   lazy.spawn('xrandr --output DP-1-3  --mode 1920x1080 --pos 1920x0 --rotate inverted'),
                                   lazy.spawn('nitrogen --restore'),
                                   desc='Rotate monitor 2 inverted'),

    Key([mod, 'control'], 'Return', lazy.spawn('nitrogen --restore'), desc='Reset wallpaper'),

    Key([mod], 'p', lazy.spawn(change_dual_monitor_state), desc='Change dual monitor state'),

    ####################

    # Wallpapers
    Key([mod, 'control'], 'grave', lazy.spawn(change_wallpaper_all), desc='Change wallpaper on both screen'),
    Key([mod, 'control'], '1',     lazy.spawn(change_wallpaper_1),   desc='Change wallpaper on screen 1'),
    Key([mod, 'control'], '2',     lazy.spawn(change_wallpaper_2),   desc='Change wallpaper on screen 2'),
    Key([mod, 'control'], '3',     lazy.spawn(change_wallpaper_dracula_1), lazy.spawn(change_wallpaper_dracula_2), desc='Change wallpaper to dracula'),

    # Screenshots
    Key([],          'Print', lazy.spawn('scrot' + screenshot_clipboard),       desc='Screenshot (all)'),
    Key(['control'], 'Print', lazy.spawn('scrot -u' + screenshot_clipboard),    desc='Screenshot (window)'),
    Key(['shift'],   'Print', lazy.spawn('scrot -s -f' + screenshot_clipboard), desc='Screenshot (area)'),
    Key(['control', 'shift'], 'Print', lazy.spawn(screen_recorder), desc='Screen recorder'),

    Key([],          'F9', lazy.spawn('scrot' + screenshot_clipboard),       desc='Screenshot (all)'),
    Key(['control'], 'F9', lazy.spawn('scrot -u' + screenshot_clipboard),    desc='Screenshot (window)'),
    Key(['shift'],   'F9', lazy.spawn('scrot -s -f' + screenshot_clipboard), desc='Screenshot (area)'),
    Key(['control', 'shift'], 'F9', lazy.spawn(screen_recorder), desc='Screen recorder'),

    Key([],          'XF86AudioNext', lazy.spawn('scrot' + screenshot_clipboard),       desc='Screenshot (all)'),
    Key(['control'], 'XF86AudioNext', lazy.spawn('scrot -u' + screenshot_clipboard),    desc='Screenshot (window)'),
    Key(['shift'],   'XF86AudioNext', lazy.spawn('scrot -s -f' + screenshot_clipboard), desc='Screenshot (area)'),
    Key(['control', 'shift'], 'XF86AudioNext', lazy.spawn(screen_recorder), desc='Screen recorder'),

    
    Key(['control'], 'Escape', lazy.spawn('scrot -u' + screenshot_clipboard),    desc='Screenshot (window)'),

    ####################

    # System
    Key([mod], 'l', lazy.spawn('loginctl lock-session'), desc='Lock screen'),
    Key([mod, 'control', 'shift'], 'End', lazy.shutdown(), desc='Shutdown Qtile'),
    Key([mod, 'control', 'shift'], 'Escape', lazy.spawn('shutdown -h now'), desc='Shutdown'),
    Key([mod, 'control', 'shift'], 'Delete', lazy.spawn('reboot'), desc='Reboot'),
    Key([mod, 'control', 'shift'], 'l', lazy.spawn('systemctl suspend'), desc='Suspend'),
    Key([mod, 'control', 'shift'], 'h', lazy.spawn('systemctl hibernate'), desc='Hibernate'),

    Key([mod, 'control', 'shift'], 'minus', lazy.spawn(power_saving + 'on'),  desc='Power saving on'),
    Key([mod, 'control', 'shift'], 'equal', lazy.spawn(power_saving + 'off'), desc='Power saving off'),

    Key([mod, 'control', 'shift'], '0', lazy.spawn(performance_profile + '08'), desc='Performance level 0'),
    Key([mod, 'control', 'shift'], '1', lazy.spawn(performance_profile + '16'), desc='Performance level 1'),
    Key([mod, 'control', 'shift'], '2', lazy.spawn(performance_profile + '26'), desc='Performance level 2'),
    Key([mod, 'control', 'shift'], '3', lazy.spawn(performance_profile + '36'), desc='Performance level 3'),
    Key([mod, 'control', 'shift'], '4', lazy.spawn(performance_profile + '45'), desc='Performance level 4'),
    Key([mod, 'control', 'shift'], '5', lazy.spawn(performance_profile + '45P'), desc='Performance level 5'),

    # Qtile
    # Key([mod, 'control'], 'r', lazy.reload_config(), desc='Reload the config'),
    Key([mod, 'control'], 'r', lazy.restart(), desc='Reload the config'),

    # Fn keys
    Key([], 'XF86MonBrightnessUp',   lazy.spawn('brightnessctl set +10%')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl set 10%-')),

    Key([], 'XF86AudioLowerVolume', lazy.spawn('pulseaudio-ctl down 5')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pulseaudio-ctl up 5')),
    Key([], 'XF86AudioMute',        lazy.spawn('pulseaudio-ctl mute')),
    Key([], 'XF86AudioPlay',        lazy.spawn(
        'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify'
        '/org/mpris/MediaPlayer2'
        'org.mpris.MediaPlayer2.Player.PlayPause')
    ),
    Key([], 'XF86AudioPrev', lazy.spawn('')),
    Key([], 'XF86AudioNext', lazy.spawn('')),

    Key([], 'XF86Calculator', lazy.spawn(calculator)),
]


##################################################
# Groups

num_groups = 10

# xprop
group_matches = [
    [Match(wm_class=['Nemo', 'Insync', 'Gprename'])],
    [Match(wm_class=['Google-chrome', 'Opera', 'KeePassXC', 'qBittorrent', 'Caprine', 'whatsapp-nativefier-d40211', 'Cisco AnyConnect Secure Mobility Client', 'Thunderbird'])],
    [Match(wm_class=['Subl', 'jetbrains-studio', 'code-oss', 'zoom'])],
    [Match(wm_class=['qpdfview', 'pdf', 'pomotroid'])],
    [Match(wm_class=[])],
    [Match(wm_class=['et', 'wps', 'wpp', 'Lifeograph', 'Ao'])],
    [Match(wm_class=['Darktable', 'Gimp-2.10', 'Spotify', 'Steam'])],
    [Match(wm_class=['Gnome-system-monitor', 'Cpupower-gui', 'Gnome-power-statistics'])],
    [Match(wm_class=['Blueman-manager', 'Pavucontrol', 'Pamac-manager'])],
    [Match(wm_class=['VirtualBox Manager', 'Vmware', 'TeamViewer'])],
]

group_layouts = [
    'columns',
    'max',
    'columns',
    'columns',
    'columns',
    'columns',
    'columns',
    'columns',
    'columns',
    'max',
]

groups = [Group(group_names[i], matches=group_matches[i], layout=group_layouts[i]) for i in range(num_groups)]

dgroups_app_rules = [
    Rule(Match(wm_class=['et', 'wps', 'wpp']), float=False, intrusive=True),
    ]

for k, group in zip(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], groups):
    keys.extend([
        Key([mod], k, lazy.group[group.name].toscreen(), desc='Switch to group {}'.format(group.name)),
        # Key([mod, 'shift'], k, lazy.window.togroup(group.name, switch_group=True), desc='Switch to & move focused window to group {}'.format(group.name))
        Key([mod, 'shift'], k, lazy.window.togroup(group.name, switch_group=False), desc='Move focused window to group {}'.format(group.name))
    ])

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
    # layout.Stack(**layout_config, num_stacks=2),
    # layout.Bsp(**layout_config),
    # layout.Matrix(**layout_config),
    # layout.MonadTall(**layout_config),
    # layout.MonadWide(**layout_config),
    # layout.RatioTile(**layout_config),
    # layout.Tile(**layout_config),
    # layout.TreeTab(**layout_config),
    # layout.VerticalTile(**layout_config),
    # layout.Zoomy(**layout_config),
    # layout.Floating(**layout_config),
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
            # text='',
            fontsize=12,
            # background=bg_color,
            # foreground=fg_color,
        )

    def separator_left(bg_color, fg_color):
        return widget.TextBox(
            text='|',
            # text='',
            fontsize=12,
            # background=bg_color,
            # foreground=fg_color,
        )

    widget_list = [
        widget.Image(
            filename='~/.config/qtile/icons/arch.png',
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
            # font=font,
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
            hide_unused=True,
        ),

        separator_left(widget_background_color, widget_foreground_color),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            scale=0.7,
        ),
        # widget.CurrentLayout(),

        separator_left(widget_background_color, widget_foreground_color),
        widget.TaskList(
            border=color_dracula['Foreground'],
            borderwidth=1,
            max_title_width=200,
            icon_size=16,
            margin=0,
        ),

        ####################

        separator_right(widget_background_color, widget_foreground_color),
        widget.OpenWeather(
            cityid='5206379',
            # https://openweathermap.org/city/5206379
            format='{temp}°{units_temperature} {humidity}% {weather_details}',
        ),

        # separator_right(widget_background_color, widget_foreground_color),
        # widget.CPUGraph(
        #     **graph_config,
        #     mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(cpu_freq_monitor)},
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
            format='{load_percent}%',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(cpu_freq_monitor)},
        ),

        separator_right(widget_background_color, widget_foreground_color),
        widget.Memory(
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(system_monitor_cli)},
        ),

        separator_right(widget_background_color, widget_foreground_color),
        widget.Net(
            interface='wlan0',
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
        widget.PulseVolume(
            limit_max_volume=True,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(volume_controller)},
        ),

        separator_right(widget_background_color, widget_foreground_color),
        widget.Battery(
            format='{char} {percent:2.0%} {watt:.2f} W', # '{char} {percent:2.0%} {hour:d}:{min:02d} {watt:.2f} W'
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(battery_monitor)},
            update_interval=10,
        ),

        separator_right(widget_background_color, widget_foreground_color),
        widget.Systray(
            icon_size=16,
        ),

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
        # widget.Chord(
        #     chords_colors={
        #         'launch': ('#ff0000', '#ffffff'),
        #     },
        #     name_transform=lambda name: name.upper(),
        # ),
        # widget.QuickExit(),
    ]
    return widget_list
    
widget_list1 = init_widget_list()
widget_list2 = init_widget_list()[:-3] + init_widget_list()[-1:]

widget_defaults = dict(
    font=font,
    fontsize=12,
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
    subprocess.call([home + '/.scripts/autostart.sh'])


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
