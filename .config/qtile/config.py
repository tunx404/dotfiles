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

import os
import re
import socket
import subprocess

##################################################
# Configurations

from colors import *

tunx404_font = 'Ubuntu Condensed Regular'

layout_margin = 4

bar_size = 24
# bar_margin = [0, 0, layout_margin, 0]
bar_margin = [layout_margin, layout_margin, layout_margin, layout_margin]
bar_background = tunx404_color_background
bar_opacity = 1

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

group_translated_names = {
    '': 'DIR',
    '': 'WEB',
    '': 'DEV',
    '': 'DOC',
    '': 'CLI',
    '': 'OFF',
    '': 'MM_',
    '': 'MON',
    '': 'SYS',
    '': 'VM_',
}

##################################################
# Applications

mod = 'mod4'
terminal = 'alacritty'

####################

# DIR
file_manager = 'nemo'
renamer = 'krename'
video_encoder = 'ghb'
file_backup = '/opt/freefilesync/FreeFileSync'
# WEB
browser = 'google-chrome-stable'
messenger1 = 'whatsapp-nativefier'
messenger2 = 'caprine'
email_client = 'thunderbird'
password_manager = 'keepassxc'
# music_playlist = 'google-chrome-stable https://www.youtube.com/playlist?list=PL14zqHuhShBB2_PRQOaD3imODj0Ejzjcv'
music_playlist = 'google-chrome-stable https://music.youtube.com/playlist?list=PL14zqHuhShBB2_PRQOaD3imODj0Ejzjcv'
study_playlist = 'google-chrome-stable https://www.youtube.com/playlist?list=PLtAPmAYb-kX9AfgUB7s90ez_j8D-2avvC'
# DEV
text_editor  = 'subl'
# DOC
pomodoro_timer = 'pomotroid --no-sandbox'
pdf_reader = 'qpdfview'
pdf_reader_2 = '/usr/bin/wpspdf'
spreadsheets = '/usr/bin/et'
writer = '/usr/bin/wps'
presentation = '/usr/bin/wpp'
# CLI
# OFF
task_manager = '/opt/kuro/Kuro.AppImage'
# MM_
photo_library = 'darktable'
# MON
system_monitor = 'gnome-system-monitor' # terminal + ' -e gtop'
system_monitor_cli = terminal + ' -e htop'
cpu_freq_monitor = terminal + ' -e watch -n1 "grep \"MHz\" /proc/cpuinfo"'
sensor_monitor = terminal + ' -e watch i8kctl' # ' -e watch sensors'
gpu_monitor = terminal + ' -e nvtop'
battery_monitor = terminal + ' -e battop'
# SYS
bluetooth_manager = 'blueman-manager'
volume_controller = 'pavucontrol'
# VM_
virtual_machines = 'virtualbox' # 'vmware'
# OTHERS
calculator = 'qalculate-gtk'
cli_fun = terminal + ' -e asciiquarium'
key_bindings = 'eog /home/tunx404/Cloud/Google\\ Drive\\ 1/Miscellaneous/Qtile/mod4.png'

####################

gui_launcher = 'ulauncher'
cli_launcher = 'dmenu-recent-aliases'
app_launcher = 'rofi -modi drun -show drun -display-drun "RUN"'
file_launcher = 'rofi -show find -modi find:~/.config/rofi/finder.sh'
window_switcher = 'rofi -show window'

change_wallpaper_all = 'nitrogen --set-zoom-fill --random --save /home/tunx404/.wallpapers/Ultra-wide'
change_wallpaper_1   = 'nitrogen --head=0 --set-zoom-fill --random --save /home/tunx404/.wallpapers/Wide'
change_wallpaper_2   = 'nitrogen --head=1 --set-zoom-fill --random --save /home/tunx404/.wallpapers/Wide'
change_wallpaper_3   = 'nitrogen --head=2 --set-zoom-fill --random --save /home/tunx404/.wallpapers/Wide'
change_wallpaper_dracula_1 = 'nitrogen --head=0 --set-zoom-fill --random --save /home/tunx404/.wallpapers/Wide/Dracula'
change_wallpaper_dracula_2 = 'nitrogen --head=1 --set-zoom-fill --random --save /home/tunx404/.wallpapers/Wide/Dracula'
change_wallpaper_dracula_3 = 'nitrogen --head=2 --set-zoom-fill --random --save /home/tunx404/.wallpapers/Wide/Dracula'

# screenshot_clipboard = ' -o "%Y-%m-%d_%H-%M-%S.png" -e "xclip -selection clip -t image/png -i $f; mv $f ~/Miscellaneous"'
screenshot_clipboard = ' -o "IMG_%Y%m%d_%H%M%S.png" -e "mv $f ~/Miscellaneous"'
screen_recorder = 'sa.sy.bluerecorder'

change_multiple_monitor_setup = 'sh /home/tunx404/.scripts/change_multiple_monitor_setup.sh'
power_saving = 'sh /home/tunx404/.scripts/power_saving.sh '
performance_profile = 'cpupower-gui profile '

audio_play_pause = 'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause'
audio_next       = 'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next'
audio_prev       = 'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous'

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
    Key([mod], 'e', lazy.function(app_to_group(group_names[0], file_manager)), desc='File manager'),
    Key([mod], 'n', lazy.function(app_to_group(group_names[0], renamer)), desc='Renamer'),
    Key([mod], 'h', lazy.function(app_to_group(group_names[0], video_encoder)), desc='Video encoder'),
    Key([mod], 'b', lazy.function(app_to_group(group_names[0], file_backup)), desc='File backup'),
    # WEB
    Key([mod], 'c', lazy.function(app_to_group(group_names[1], browser)), desc='Browser'),
    Key([mod], 'k', lazy.function(app_to_group(group_names[1], password_manager)), desc='Password manager'),
    Key([mod], 'u', lazy.function(app_to_group(group_names[1], music_playlist)), desc='Music playlist'),
    Key([mod], 'y', lazy.function(app_to_group(group_names[1], study_playlist)), desc='Study with me playlist'),
    Key([mod], 'm', # lazy.function(app_to_group(group_names[1], messenger1)),
                    lazy.function(app_to_group(group_names[1], messenger2)), desc='Messenger'),
    # DEV
    Key([mod], 't', lazy.function(app_to_group(group_names[2], text_editor)), desc='Text editor'),
    # DOC
    Key([mod], 'f', lazy.function(app_to_group(group_names[3], pdf_reader)), desc='PDF reader'),
    Key([mod], 'o', lazy.function(app_to_group(group_names[3], pomodoro_timer)), desc='Pomodoro timer'),
    Key([mod], 'comma',      lazy.function(app_to_group(group_names[3], spreadsheets)), desc='Spreadsheets'),
    Key([mod], 'period',     lazy.function(app_to_group(group_names[3], writer)), desc='Writer'),
    Key([mod], 'slash',      lazy.function(app_to_group(group_names[3], presentation)), desc='Presentation'),
    Key([mod], 'semicolon',  lazy.function(app_to_group(group_names[3], pdf_reader_2)), desc='PDF reader 2'),
    # OFF
    Key([mod], 'g', lazy.function(app_to_group(group_names[5], task_manager)), desc='Task manager'),
    # MM_
    Key([mod], 'i', lazy.function(app_to_group(group_names[6], photo_library)), desc='Photo library'),
    # MON
    Key([mod, 'shift'], 'm', lazy.function(app_to_group(group_names[7], system_monitor)), desc='System: System monitor'),
    Key([mod, 'shift'], 'y', lazy.function(app_to_group(group_names[7], system_monitor_cli)), desc='System: System monitor CLI'),
    Key([mod, 'shift'], 'f', lazy.function(app_to_group(group_names[7], cpu_freq_monitor)), desc='System: CPU frequency monitor'),
    Key([mod, 'shift'], 'o', lazy.function(app_to_group(group_names[7], sensor_monitor)), desc='System: Sensor monitor'),
    Key([mod, 'shift'], 'g', lazy.function(app_to_group(group_names[7], gpu_monitor)), desc='System: GPU monitor'),
    Key([mod, 'shift'], 'b', lazy.function(app_to_group(group_names[7], battery_monitor)), desc='System: Battery monitor'),
    # SYS
    Key([mod], 'v', lazy.function(app_to_group(group_names[8], volume_controller)),
                    lazy.function(app_to_group(group_names[8], bluetooth_manager)), desc='Volume controller & Bluetooth manager'),
    # VM_
    Key([mod], 'j', lazy.function(app_to_group(group_names[9], virtual_machines)), desc='Virtual machines'),
    
    # OTHERS
    Key([mod], 'F1', lazy.spawn(key_bindings), desc='Key bindings'),
    Key([mod, 'shift', 'control'], 'z',
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
    Key([mod], 'q', lazy.spawn(terminal), desc='System: Launch terminal'),
    Key([mod], 'Return', lazy.spawn(terminal), desc='System: Launch terminal'),
    Key([mod], 'KP_Enter', lazy.spawn(terminal), desc='System: Launch terminal'),
    Key([mod, 'control'], 'r', lazy.spawncmd(), desc='System: Prompt'),
    Key([mod, 'shift'], 'r', lazy.spawn(cli_launcher), desc='System: CLI launcher'),
    #
    Key([mod], 'r', lazy.spawn(app_launcher), desc='System: Application launcher'),
    Key(['control'], 'space', lazy.spawn(gui_launcher), desc='System: GUI launcher'),

    ####################
    # Windows

    Key(['mod1'], 'Tab', lazy.layout.next(), desc='Move window focus to other window'),
    #
    Key([mod, 'shift'], 'a', lazy.layout.shuffle_left(),  desc='Move window to the left'),
    Key([mod, 'shift'], 'd', lazy.layout.shuffle_right(), desc='Move window to the right'),
    Key([mod, 'shift'], 's', lazy.layout.shuffle_down(),  desc='Move window down'),
    Key([mod, 'shift'], 'w', lazy.layout.shuffle_up(),    desc='Move window up'),
    #
    Key([mod], 'a', lazy.layout.grow_left(),  desc='Grow window to the left'),
    Key([mod], 'd', lazy.layout.grow_right(), desc='Grow window to the right'),
    Key([mod], 's', lazy.layout.grow_down(),  desc='Grow window down'),
    Key([mod], 'w', lazy.layout.grow_up(),    desc='Grow window up'),
    #
    Key([mod], 'z', lazy.layout.normalize(), desc='Reset all window sizes'),
    #
    Key([mod], 'Up',   lazy.window.toggle_fullscreen(), desc='Fullscreen'),
    Key([mod], 'Down', lazy.window.toggle_floating(),   desc='Floating'),
    #
    Key([mod, 'control'],   'q', lazy.window.toggle_fullscreen(), desc='Fullscreen'),
    Key([mod, 'shift'], 'q', lazy.window.toggle_floating(),   desc='Floating'),
    #
    Key([mod, 'shift'], 'c', lazy.window.kill(), desc='Kill focused window'),
    #
    Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),

    ####################

    # Groups
    Key([mod, 'control'], 'd', lazy.function(screen_to_next_group), desc='Switch to the next group'),
    Key([mod, 'control'], 'a', lazy.function(screen_to_prev_group), desc='Switch to the prev group'),
    Key([mod, 'control'], 'w', lazy.function(screen_to_next_group), desc='Switch to the next group'),
    Key([mod, 'control'], 's', lazy.function(screen_to_prev_group), desc='Switch to the prev group'),
    Key(['mod1', 'control'], 'Right', lazy.function(screen_to_next_group), desc='Switch to the next group'),
    Key(['mod1', 'control'], 'Left',  lazy.function(screen_to_prev_group), desc='Switch to the prev group'),
    #
    Key([mod, 'shift', 'control'], 'd', lazy.function(window_to_next_group), desc='Move window to the next group'),
    Key([mod, 'shift', 'control'], 'a', lazy.function(window_to_prev_group), desc='Move window to the prev group'),
    Key(['mod1', 'shift', 'control'], 'Right', lazy.function(window_to_next_group), desc='Move window to the next group'),
    Key(['mod1', 'shift', 'control'], 'Left', lazy.function(window_to_prev_group), desc='Move window to the prev group'),

    # Screens
    Key([mod, 'shift', 'control'], 'w', lazy.function(window_to_next_screen),     desc='Move window to the next screen'),
    Key([mod, 'shift', 'control'], 's', lazy.function(window_to_previous_screen), desc='Move window to the prev screen'),
    #
    Key([mod, 'control'], 'Left',  lazy.spawn('xrandr --output DP-3 --mode 1920x1080 --pos 3840x0 --rotate left'),
                                   lazy.spawn('nitrogen --restore'),
                                   desc='Rotate screen left'),
    Key([mod, 'control'], 'Right', lazy.spawn('xrandr --output DP-3 --mode 1920x1080 --pos 3840x0 --rotate right'),
                                   lazy.spawn('nitrogen --restore'),
                                   desc='Rotate screen right'),
    Key([mod, 'control'], 'Up',    lazy.spawn('xrandr --output DP-3 --mode 1920x1080 --pos 3840x0 --rotate normal'),
                                   lazy.spawn('nitrogen --restore'),
                                   desc='Rotate screen normal'),
    Key([mod, 'control'], 'Down',  lazy.spawn('xrandr --output DP-3 --mode 1920x1080 --pos 3840x0 --rotate inverted'),
                                   lazy.spawn('nitrogen --restore'),
                                   desc='Rotate screen inverted'),
    #
    Key([mod], 'p', lazy.spawn(change_multiple_monitor_setup), desc='Change multiple screen setup'),

    ####################

    # Wallpapers
    Key([mod, 'shift', 'control'], 'grave', lazy.spawn(change_wallpaper_all), desc='Change wallpaper on all screens'),
    Key([mod, 'control'],          'grave', lazy.spawn('nitrogen --restore'), desc='Reset screen wallpapers'),

    Key([mod, 'control'], '1',     lazy.spawn(change_wallpaper_1),   desc='Change wallpaper on screen 1'),
    Key([mod, 'control'], '2',     lazy.spawn(change_wallpaper_2),   desc='Change wallpaper on screen 2'),
    Key([mod, 'control'], '3',     lazy.spawn(change_wallpaper_3),   desc='Change wallpaper on screen 2'),
    #
    Key([mod, 'shift', 'control'], '1', lazy.spawn(change_wallpaper_dracula_1), desc='Change wallpaper on screen 1 to Dracula'),
    Key([mod, 'shift', 'control'], '2', lazy.spawn(change_wallpaper_dracula_2), desc='Change wallpaper on screen 2 to Dracula'),
    Key([mod, 'shift', 'control'], '3', lazy.spawn(change_wallpaper_dracula_3), desc='Change wallpaper on screen 3 to Dracula'),

    # Screenshots
    Key([],                   'Print', lazy.spawn('scrot' + screenshot_clipboard),       desc='Screenshot (all)'),
    Key(['control'],          'Print', lazy.spawn('scrot -u' + screenshot_clipboard),    desc='Screenshot (window)'),
    Key(['shift'],            'Print', lazy.spawn('scrot -s -f' + screenshot_clipboard), desc='Screenshot (area)'),
    Key(['shift', 'control'], 'Print', lazy.spawn(screen_recorder), desc='Screen recorder'),
    #
    Key([mod],                     'Print', lazy.spawn('scrot' + screenshot_clipboard),       desc='Screenshot (all)'),
    Key([mod, 'control'],          'Print', lazy.spawn('scrot -u' + screenshot_clipboard),    desc='Screenshot (window)'),
    Key([mod, 'shift'],            'Print', lazy.spawn('scrot -s -f' + screenshot_clipboard), desc='Screenshot (area)'),
    Key([mod, 'shift', 'control'], 'Print', lazy.spawn(screen_recorder),                      desc='Screen recorder'),
    #
    Key([mod],                     'x', lazy.spawn('scrot' + screenshot_clipboard),       desc='Screenshot (all)'),
    Key([mod, 'control'],          'x', lazy.spawn('scrot -u' + screenshot_clipboard),    desc='Screenshot (window)'),
    Key([mod, 'shift'],            'x', lazy.spawn('scrot -s -f' + screenshot_clipboard), desc='Screenshot (area)'),
    Key([mod, 'shift', 'control'], 'x', lazy.spawn(screen_recorder),                      desc='Screen recorder'),

    ####################

    # System
    Key([mod], 'l', lazy.spawn('loginctl lock-session'), desc='System: Lock'),
    #
    Key([mod, 'shift', 'control'], 'End', lazy.shutdown(), desc='System: Logout'),
    Key([mod, 'shift', 'control'], 'Escape', lazy.spawn('shutdown -h now'), desc='System: Shutdown'),
    Key([mod, 'shift', 'control'], 'Delete', lazy.spawn('reboot'), desc='System: Reboot'),
    Key([mod, 'shift', 'control'], 'l', lazy.spawn('systemctl suspend'), desc='System: Suspend'),
    Key([mod, 'shift', 'control'], 'h', lazy.spawn('systemctl hibernate'), desc='System: Hibernate'),
    #
    Key([mod, 'shift', 'control'], 'minus', lazy.spawn(power_saving + 'on'),  desc='System: Power saving on'),
    Key([mod, 'shift', 'control'], 'equal', lazy.spawn(power_saving + 'off'), desc='System: Power saving off'),

    # Qtile
    Key([mod, 'shift', 'control'], 'r', lazy.restart(), desc='System: Reload the config'),

    # Fn keys
    Key([], 'XF86MonBrightnessUp',   lazy.spawn('brightnessctl set +10%'), desc='System: Brightness up'),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl set 10%-'), desc='System: Brightness down'),

    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pulseaudio-ctl up 5'),   desc='System: Volume up'),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('pulseaudio-ctl down 5'), desc='System: Volume down'),
    Key([], 'XF86AudioMute',        lazy.spawn('pulseaudio-ctl mute'), desc='System: Mute'),

    Key([], 'XF86AudioPlay',        lazy.spawn(audio_play_pause), desc='Play/pause'),
    Key([], 'XF86AudioPrev',        lazy.spawn(audio_next),       desc='Next'),
    Key([], 'XF86AudioNext',        lazy.spawn(audio_prev),       desc='Previous'),

    Key([], 'XF86Calculator', lazy.spawn(calculator), desc='Calculator'),
]

##################################################
# Groups

num_groups = 10

# xprop
group_matches = [
    [Match(wm_class=['Nemo', 'Insync', 'krename', "FreeFileSync"])],
    [Match(wm_class=['Google-chrome', 'Opera', 'KeePassXC', 'qBittorrent', 'Caprine', 'whatsapp-nativefier-d40211', 'Cisco AnyConnect Secure Mobility Client', 'Thunderbird'])],
    [Match(wm_class=['Subl', 'jetbrains-studio', 'code-oss', 'sun-awt-X11-XFramePeer'])],
    [Match(wm_class=['qpdfview', 'pdf', 'pomotroid', 'zoom'])],
    [Match(wm_class=[])],
    [Match(wm_class=['et', 'wps', 'wpp', 'Lifeograph', 'kuro'])],
    [Match(wm_class=['Darktable', 'Gimp-2.10', 'Spotify', 'Steam', 'resolve', 'csgo_linux64', 'hl2_linux'])],
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
# for k, group in zip(['1', '2', '3', '4', '5', '6', '7', '8', '9', 'grave'], groups):
    keys.extend([
        Key([mod], k, lazy.group[group.name].toscreen(), desc='Switch to group {}'.format(group_translated_names[group.name])),
        # Key([mod, 'shift'], k, lazy.window.togroup(group.name, switch_group=True), desc='Switch to & move focused window to group {}'.format(group_translated_names[group.name]))
        Key([mod, 'shift'], k, lazy.window.togroup(group.name, switch_group=False), desc='Move focused window to group {}'.format(group_translated_names[group.name]))
    ])

##################################################
# Layouts

layout_config = {
    'border_width': 2,
    'margin': layout_margin,
    'border_focus': tunx404_color_red,
    'border_normal': tunx404_color_background_2,
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

def init_widget_list():
    def separator(direction, color):
        if direction == 'right':
            text = ''
        else:
            text = ''

        if color == 1:
            background = tunx404_color_background_2
            foreground = tunx404_color_background
        else:
            background = tunx404_color_background
            foreground = tunx404_color_background_2

        return widget.TextBox(
            text=text,
            # font='meslolgs',
            fontsize=18,
            background=background,
            foreground=foreground,
            padding=0,
        )

    widget_list = [
        widget.Image(
            filename='~/.config/qtile/icons/arch.png',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(cli_fun)},
            margin=4,
            background=tunx404_color_background_2,
        ),
        widget.Prompt(
            prompt=prompt,
        ),
        separator(direction='left', color=2),

        widget.GroupBox(
            fontsize=28,
            active=tunx404_color_foreground,
            block_highlight_text_color=tunx404_color_foreground,
            highlight_color=tunx404_color_red,
            highlight_method='line',
            this_current_screen_border=tunx404_color_foreground,
            this_screen_border=tunx404_color_foreground_2,
            other_current_screen_border=tunx404_color_foreground,
            other_screen_border=tunx404_color_foreground_2,
            hide_unused=True,
            background=tunx404_color_background,

        ),
        separator(direction='left', color=1),

        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            scale=0.7,
            background=tunx404_color_background_2,
        ),
        separator(direction='left', color=2),

        widget.TaskList(
            border=tunx404_color_foreground,
            borderwidth=1,
            max_title_width=200,
            icon_size=16,
            margin=0,
            background=tunx404_color_background,
        ),

        ####################

        separator(direction='right', color=2),
        widget.TextBox(text='', fontsize=20, background=tunx404_color_background_2),
        widget.OpenWeather(
            cityid='5206379', # https://openweathermap.org/city/5206379
            format='{temp}°{units_temperature} {humidity}% {weather_details}',
            background=tunx404_color_background_2
        ),

        separator(direction='right', color=1),
        widget.TextBox(text='', fontsize=20, background=tunx404_color_background),
        widget.CPU(
            format='{load_percent}%',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(cpu_freq_monitor)},
            background=tunx404_color_background
        ),

        separator(direction='right', color=2),
        widget.TextBox(text='', fontsize=20, background=tunx404_color_background_2),
        widget.Memory(
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(system_monitor_cli)},
            background=tunx404_color_background_2
        ),

        separator(direction='right', color=1),
        widget.TextBox(text='', fontsize=20, background=tunx404_color_background),
        widget.Net(
            interface='wlan0',
            format='{down} ↓↑ {up}',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(system_monitor)},
            background=tunx404_color_background
        ),

        separator(direction='right', color=2),
        widget.TextBox(text='', fontsize=14, background=tunx404_color_background_2),
        widget.ThermalSensor(
            foreground=tunx404_color_foreground,
            foreground_alert=tunx404_color_red,
            tag_sensor='Package id 0',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(sensor_monitor)},
            background=tunx404_color_background_2
        ),

        separator(direction='right', color=1),
        widget.TextBox(text='', fontsize=14, background=tunx404_color_background),
        widget.NvidiaSensors(
            foreground=tunx404_color_foreground,
            foreground_alert=tunx404_color_red,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(gpu_monitor)},
            background=tunx404_color_background
        ),

        separator(direction='right', color=2),
        widget.TextBox(text='', fontsize=20, background=tunx404_color_background_2),
        widget.PulseVolume(
            limit_max_volume=True,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(volume_controller)},
            background=tunx404_color_background_2
        ),

        separator(direction='right', color=1),
        widget.TextBox(text='', fontsize=14, background=tunx404_color_background),
        widget.Battery(
            format='{char} {percent:2.0%} {watt:.2f} W',
            # format='{char} {percent:2.0%} {hour:d}:{min:02d} {watt:.2f} W',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(battery_monitor)},
            update_interval=10,
            background=tunx404_color_background
        ),

        separator(direction='right', color=2),
        widget.TextBox(text='', fontsize=20, background=tunx404_color_background_2),
        widget.Clock(
            format="%a %d/%m %H:%M:%S",
            background=tunx404_color_background_2
        ),

        separator(direction='right', color=1),
        widget.Systray(
            icon_size=16,
            background=tunx404_color_background
        ),
    ]
    return widget_list
    
widget_list1 = init_widget_list()
widget_list2 = init_widget_list()[:-2]
widget_list3 = init_widget_list()[:-2]

widget_defaults = dict(
    font=tunx404_font,
    fontsize=12,
    padding=3,
    background=None,
    foreground=tunx404_color_foreground,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(top=bar.Bar(widgets=widget_list1, size=bar_size, background=bar_background, margin=bar_margin, opacity=bar_opacity)),
    Screen(top=bar.Bar(widgets=widget_list2, size=bar_size, background=bar_background, margin=bar_margin, opacity=bar_opacity)),
    Screen(top=bar.Bar(widgets=widget_list3, size=bar_size, background=bar_background, margin=bar_margin, opacity=bar_opacity)),
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
