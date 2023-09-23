feh --bg-fill  /home/cs/dow/bkg.jpg  /home/cs/dow/black.jpg &
picom &
slstatus &
#dwmblocks &
setxkbmap de &
xset s off &
xset s noblank &
xset -dpms &
xrdb -merge ~/.Xresources &
xrandr --output DisplayPort-1 --mode 1920x1080 --rotate left &
exec dbus-launch --exit-with-session dwm
