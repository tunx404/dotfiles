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
# Imports

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import re
import socket
import subprocess


##################################################
#Applications

mod          = 'mod4'
terminal     = 'alacritty'
broswer      = 'google-chrome-stable'
file_manager = 'nemo'
text_editor  = 'subl'
volume_controller = 'pavucontrol'
system_monitor = 'gnome-system-monitor'
system_monitor_cli = terminal + ' -e htop'
gpu_monitor = terminal + ' -e nvtop'
sensor_monitor = terminal + ' -e watch sensors'
# terminal     = guess_terminal()

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##################################################
# Key bindings

keys = [
    # System
    Key(['control', 'shift', 'mod1'], 'Delete', lazy.shutdown(), desc='Shutdown Qtile'),
    Key(['control', 'shift', 'mod1'], 'Escape', lazy.spawn('shutdown -h now'), desc='Shutdown'),
    Key(['control', 'shift', 'mod1'], 'End', lazy.spawn('reboot'), desc='Reboot'),
    Key(['control', 'shift', 'mod1'], 'l', lazy.spawn('systemctl suspend'), desc='Suspend'),
    Key(['control', 'shift', 'mod1'], 'h', lazy.spawn('systemctl hibernate'), desc='Hibernate'),

    # Fn keys
    Key([], 'XF86MonBrightnessUp',   lazy.spawn('brightnessctl set +10%')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('brightnessctl set 10%-')),

    Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer sset Master,0 5%-')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer sset Master,0 5%+')),
    Key([], 'XF86AudioMute',        lazy.spawn('amixer sset Master,0 toggle')),
    Key([], 'XF86AudioPlay',
        lazy.spawn(
            'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify'
            '/org/mpris/MediaPlayer2'
            'org.mpris.MediaPlayer2.Player.PlayPause')),

    # Qtile
    Key([mod, 'control'], 'r', lazy.restart(), desc='Reload the config'),

    # Applications
    Key([mod], 'e', lazy.spawn(file_manager), desc='File manager'),
    Key([mod], 't', lazy.spawn(text_editor),  desc='Text editor'),
    Key([mod], 'b', lazy.spawn(broswer),      desc='Broswer'),

    Key([], 'F9', lazy.spawn('cpupower-gui'), desc='cpupower-gui'),

    # Keyboard layouts
    Key([mod], 'space', lazy.widget['keyboardlayout'].next_keyboard(), desc='Next keyboard layout'),

    # Launcher
    Key([mod, 'control'], 'Return', lazy.spawn('dmenu_run'), desc='Launcher'),
    Key(['control'], 'space', lazy.spawn('ulauncher-toggle'), desc='Ulauncher'),

    # Switch monitor
    Key([mod], 'Right', lazy.to_screen(1), desc='Move focus to the next monitor'),
    Key([mod], 'Left',  lazy.to_screen(0), desc='Move focus to the prev monitor'),
    Key([mod, 'control', 'shift'], 'Left',  lazy.spawn('xrandr --output DP-3 --rotate left'),     desc='Rotate monitor 2 left'),
    Key([mod, 'control', 'shift'], 'Right', lazy.spawn('xrandr --output DP-3 --rotate right'),    desc='Rotate monitor 2 right'),
    Key([mod, 'control', 'shift'], 'Up',    lazy.spawn('xrandr --output DP-3 --rotate normal'),   desc='Rotate monitor 2 normal'),
    Key([mod, 'control', 'shift'], 'Down',  lazy.spawn('xrandr --output DP-3 --rotate inverted'), desc='Rotate monitor 2 inverted'),
    Key([mod, 'control', 'shift'], 'Return',  lazy.spawn('nitrogen --restore'), desc='Reset wallpaper'),

    ####################

    # Switch between windows
    Key([mod], 'h', lazy.layout.left(),  desc='Move focus to left'),
    Key([mod], 'l', lazy.layout.right(), desc='Move focus to right'),
    Key([mod], 'j', lazy.layout.down(),  desc='Move focus down'),
    Key([mod], 'k', lazy.layout.up(),    desc='Move focus up'),
    Key([mod], 'space', lazy.layout.next(), desc='Move window focus to other window'),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left(),  desc='Move window to the left'),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right(), desc='Move window to the right'),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down(),  desc='Move window down'),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up(),    desc='Move window up'),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, 'control'], 'h', lazy.layout.grow_left(),  desc='Grow window to the left'),
    Key([mod, 'control'], 'l', lazy.layout.grow_right(), desc='Grow window to the right'),
    Key([mod, 'control'], 'j', lazy.layout.grow_down(),  desc='Grow window down'),
    Key([mod, 'control'], 'k', lazy.layout.grow_up(),    desc='Grow window up'),
    Key([mod], 'n', lazy.layout.normalize(), desc='Reset all window sizes'),

    # # Toggle between split and unsplit sides of stack.
    # # Split = all windows displayed
    # # Unsplit = 1 window displayed, like Max layout, but still with
    # # multiple stack panes
    # Key([mod, 'shift'], 'Return', lazy.layout.toggle_split(),
    #     desc='Toggle between split and unsplit sides of stack'),
    Key([mod], 'Return', lazy.spawn(terminal), desc='Launch terminal'),

    # Toggle between different layouts as defined below
    Key([mod], 'Tab', lazy.next_layout(), desc='Toggle between layouts'),
    Key([mod], 'w', lazy.window.kill(), desc='Kill focused window'),

    # Key([mod, 'control'], 'r', lazy.reload_config(), desc='Reload the config'),
    Key([mod, 'control'], 'q', lazy.shutdown(), desc='Shutdown Qtile'),
    Key([mod], 'r', lazy.spawncmd(), desc='Spawn a command using a prompt widget'),
]


##################################################
# Groups

groups = [Group(i) for i in '12345678']

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc='Switch to group {}'.format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        # Key([mod, 'shift'], i.name, lazy.window.togroup(i.name, switch_group=True),
        #     desc='Switch to & move focused window to group {}'.format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        Key([mod, 'shift'], i.name, lazy.window.togroup(i.name),
            desc='move focused window to group {}'.format(i.name)),
    ])


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
# Layouts

layout_theme = {'border_width': 2,
                'margin': 4,
                'border_focus': color_dracula['Comment'],
                'border_normal': color_dracula['Current Line']
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    layout.RatioTile(**layout_theme),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(**layout_theme)
]


##################################################
# Screens

# widget_background_color = color_dracula['Background']
widget_background_color = color_dracula['Transparent']
# widget_background_color = color_dracula['Red']
widget_foreground_color = color_dracula['Foreground']
# widget_foreground_color = color_dracula['Red']
widget_color = color_dracula['Transparent']
# widget_color = color_dracula['Current Line']

def init_widget_list():
    def separator_right(bg_color, fg_color):
        return widget.TextBox(
                        text='\\',
                        fontsize=20,
                        font='Inconsolata for Powerline',
                        background=bg_color,
                        foreground=fg_color)

    def separator_left(bg_color, fg_color):
        return widget.TextBox(
                        text='/',
                        fontsize=20,
                        font='Inconsolata for Powerline',
                        background=bg_color,
                        foreground=fg_color)

    widget_list = [
        widget.Image(
            filename='~/.config/qtile/icons/240px-Faenza-start-here-archlinux-symbolic.svg.png',
            scale='false',
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(terminal)}
            ),
        widget.Prompt(
            prompt=prompt,
            font='Inconsolata for Powerline',
            padding=10,
            ),

        separator_left(widget_background_color, widget_foreground_color),

        widget.GroupBox(
            font='Inconsolata SemiBold',
            fontsize=14,
            active=color_dracula['Foreground'],
            inactive=color_dracula['Current Line'],
            block_highlight_text_color=color_dracula['Foreground'],
            highlight_color=color_dracula['Current Line'],
            highlight_method='line',
            this_current_screen_border=color_dracula['Foreground'],
            this_screen_border=color_dracula['Comment'],
            other_current_screen_border=color_dracula['Foreground'],
            other_screen_border=color_dracula['Comment'],
            hide_unused=True,
            ),

        separator_left(widget_background_color, widget_foreground_color),

        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            padding=0,
            scale=0.7
            ),
        widget.CurrentLayout(
            padding=5
            ),

        separator_left(widget_background_color, widget_foreground_color),

        widget.TaskList(
            border=widget_foreground_color,
            borderwidth=1,
            max_title_width=200,
        ),

        ##########

        # widget.Spacer(),

        ##########

        # widget.Notify(
        #     background=color_dracula['Red'],
        #     max_chars=100,
        # ),

        separator_right(widget_background_color, widget_foreground_color),
        
        widget.OpenWeather(
            cityid='5206379',
            format='{main_temp}°{units_temperature} {humidity}% {weather_details}',
        ),

        separator_right(widget_background_color, widget_foreground_color),
        
        widget.Pomodoro(
            color_active=color_dracula['Red'],
            color_break=color_dracula['Green'],
            color_inactive=color_dracula['Foreground'],
        ),

        separator_right(widget_background_color, widget_foreground_color),
        
        widget.CPU(
            line_width=1,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(system_monitor_cli)},
        ),

        separator_right(widget_background_color, widget_foreground_color),
        
        widget.Memory(
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(system_monitor_cli)},
            padding=5
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

        widget.Battery(
            format='{percent:2.0%}',
        ),

        separator_right(widget_background_color, widget_foreground_color),

        widget.Volume(
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(volume_controller)},
        ),

        separator_right(widget_background_color, widget_foreground_color),

        widget.Systray(
        ),

        separator_right(widget_background_color, widget_foreground_color),

        widget.Clock(
            format="%a %d/%m %H:%M:%S"
        ),

        # widget.Backlight(),
        # widget.LaunchBar(progs=[('thunderbird', 'thunderbird -safe-mode', 'launch thunderbird in safe mode')]),
        # widget.AGroupBox(),
        # widget.WindowTabs(),
        # widget.StatusNotifier(),
        # widget.WidgetBox(widgets=[
        #         widget.TextBox(text="This widget is in the box"),
        #         widget.Memory()
        #     ]
        # ),
        # widget.CPUGraph(),
        # widget.MemoryGraph(),
        # widget.NetGraph(),
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
widget_list2 = init_widget_list()[:-3]+ init_widget_list()[-2:]

widget_defaults = dict(
    font='Inconsolata for Powerline',
    fontsize=14,
    padding=3,
    background=widget_background_color,
)
# widget_defaults = dict(
#     font='sans',
#     fontsize=12,
#     padding=3,
# )
extension_defaults = widget_defaults.copy()

screens = [
    Screen(top=bar.Bar(widgets=widget_list1, size=24, background=widget_color)),
    Screen(top=bar.Bar(widgets=widget_list2, size=24, background=widget_color)),
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