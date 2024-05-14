config.load_autoconfig(False)
# Match with Xresources
base00 = "#101010"
base01 = "#d0484e"
base02 = "#25c192"
base03 = "#f28735"
base04 = "#49a6d0"
base05 = "#f74e8b"
base06 = "#d8a89a"
base07 = "#fdeadb"
base08 = "#121012"
base09 = "#c0383e"
base0A = "#15b082"
base0B = "#e27725"
base0C = "#3996c0"
base0D = "#f74e8b"
base0E = "#c8988a"
base0F = "#fdeadb"

# --- Completion widget ---

# May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = '#88fdeadb'
c.colors.completion.odd.bg = '#88101010'
c.colors.completion.even.bg = '#88100000'

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = base0F
c.colors.completion.category.bg = '#77101010'
c.colors.completion.category.border.top = '#8849a6d0'
c.colors.completion.category.border.bottom = '#8849a6d0'
c.colors.completion.item.selected.fg = base00
c.colors.completion.item.selected.bg = '#ccf74e8b'
c.colors.completion.item.selected.border.top = '#aaefdfef'
c.colors.completion.item.selected.border.bottom = '#bbe73d7b'
c.colors.completion.item.selected.match.fg = base0F
c.colors.completion.match.fg = base0A
# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = '#aaf28735'
# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = '#55101010'

# --- Context menu ---

c.colors.contextmenu.disabled.bg = '#77000000'
c.colors.contextmenu.disabled.fg = base01
# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = '#99101010'
c.colors.contextmenu.menu.fg =  base0F
c.colors.contextmenu.selected.bg = '#ddf74e8b'
c.colors.contextmenu.selected.fg = base00


# --- Downloads ---

c.colors.downloads.bar.bg = '#88101010'
c.colors.downloads.start.fg = base00
c.colors.downloads.start.bg = base0D
c.colors.downloads.start.fg = base0D
c.colors.downloads.start.bg = '#00101010'
c.colors.downloads.stop.fg = base0C
c.colors.downloads.stop.bg = '#77101010'
c.colors.downloads.error.fg = base09
c.colors.downloads.system.bg = 'hsv'

# --- Hints ---

c.colors.hints.fg = base0E
# Note that you can use a `rgba(...)` value for transparency.
c.colors.hints.bg = '#88101010'
c.colors.hints.match.fg = base05
c.colors.keyhint.fg = base05
# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = base05
c.colors.keyhint.bg = '#88101010'

# --- Messages ---

c.colors.messages.error.fg = base09
c.colors.messages.error.bg = '#66101010'
c.colors.messages.error.border = base09
c.colors.messages.warning.fg = base09
c.colors.messages.warning.bg = '#77101010'
c.colors.messages.warning.border = base09
c.colors.messages.info.fg = base01
c.colors.messages.info.bg = '#66101010'
c.colors.messages.info.border = '#99101010'


# --- Prompts ---

c.colors.prompts.fg = base0F
# Border used around UI elements in prompts.
c.colors.prompts.border = '#25c192'
c.colors.prompts.bg = '#ef101010'
c.colors.prompts.selected.bg = '#ef101010'
c.colors.prompts.selected.fg = base00
# --- Status bar ---

c.colors.statusbar.normal.fg = base05
c.colors.statusbar.normal.bg = '#88101010'
c.colors.statusbar.insert.fg = base08
c.colors.statusbar.insert.bg = '#aa25c192'
c.colors.statusbar.passthrough.fg = base0A
c.colors.statusbar.passthrough.bg = '#88101010'
# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = base0E
# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = '#88101010'
c.colors.statusbar.command.fg = base04
c.colors.statusbar.command.bg = '#88101004'
c.colors.statusbar.command.private.fg = base0E
c.colors.statusbar.command.private.bg = '#88101010'
c.colors.statusbar.caret.fg = base0D
c.colors.statusbar.caret.bg = '#77101010'
c.colors.statusbar.caret.selection.fg = base0D
c.colors.statusbar.caret.selection.bg = '#77101010'
c.colors.statusbar.progress.bg = base0D

# --- Status bar URL ---

c.colors.statusbar.url.fg = base05
c.colors.statusbar.url.error.fg = base08
# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = base0B
c.colors.statusbar.url.success.http.fg = base0C
c.colors.statusbar.url.success.https.fg = base0C
c.colors.statusbar.url.warn.fg = base09


# --- Tabs ---

c.colors.tabs.bar.bg = '#10101010'
c.colors.tabs.indicator.start = base03
c.colors.tabs.indicator.stop = base0B
c.colors.tabs.indicator.error = base08
c.colors.tabs.odd.fg = base02
c.colors.tabs.odd.bg = '#66101010'
c.colors.tabs.even.fg = base03
c.colors.tabs.even.bg = '#66101010'
c.colors.tabs.pinned.even.bg = '#66101002'
c.colors.tabs.pinned.even.fg = base00
c.colors.tabs.pinned.odd.bg = '#66101002'
c.colors.tabs.pinned.odd.fg = base00
c.colors.tabs.pinned.selected.even.bg = '#aaf74e8b'
c.colors.tabs.pinned.selected.even.fg = base00
c.colors.tabs.pinned.selected.odd.bg = '#aaf74e8b'
c.colors.tabs.pinned.selected.odd.fg = base00

# --- Selected tabs ---
c.colors.tabs.selected.odd.fg = base0A
c.colors.tabs.selected.odd.bg = '#77101010'
c.colors.tabs.selected.even.fg = base0A
c.colors.tabs.selected.even.bg = '#77101010'
# Default page background when there is none
c.colors.webpage.bg = base0F





# --- Fonts ---

c.fonts.default_family = 'Space Mono Nerd Font'
c.fonts.default_size = '10pt'
c.fonts.messages.error = '10pt Space Mono'
c.fonts.messages.info = '10pt Space Mono Nerd Font'
c.fonts.messages.warning = '10pt Space Mono Nerd Font'
c.fonts.statusbar = '10pt Space Mono Nerd Font'
c.fonts.downloads = '10pt Space Mono Nerd Font'
c.fonts.prompts = '10pt Space Mono Nerd Font'
c.fonts.keyhint = '10pt Space Mono Nerd Font'
c.fonts.hints = '10pt Space Mono Nerd Font'
c.fonts.contextmenu = '10pt Space Mono Nerd Font'
c.fonts.completion.category = 'bold 10pt Space Mono Nerd Font'
c.fonts.completion.entry = '10pt Space Mono Nerd Font'
c.fonts.tabs.selected = 'italic 10pt Space Mono Nerd Font'
c.fonts.tabs.unselected = '10pt Space Mono Nerd Font'
c.fonts.messages.info = 'italic 10pt Space Mono Nerd Font'
c.fonts.messages.error = 'italic 10pt Space Mono Nerd Font'
c.fonts.messages.warning = 'italic 10pt Space Mono Nerd Font'




# --- Appearance ---

c.hints.padding = {
            "left": 4,
            "right": 4,
            "top": 3,
            "bottom": 4
            }

c.colors.completion.fg = '#efefef'
c.colors.downloads.start.fg = '#bbd0484e'
c.colors.downloads.start.bg = '#00101010'
c.colors.downloads.stop.bg = '#00101010'
c.colors.downloads.stop.fg = '#ee25c192'

c.tabs.padding = {
            "left": 3,
             "right": 3,
             "top": 3,
             "bottom": 4
             }
c.tabs.title.format = "{audio}{current_title}"
c.window.title_format = "{perc}{current_title}"
c.tabs.last_close = "close"
c.tabs.indicator.width = 0
c.tabs.favicons.scale = 1.4
c.tabs.show_switching_delay = 700

# --- Preferences ---

c.completion.height = "30%"
c.downloads.location.directory = "/home/cs/dow"
c.downloads.location.prompt = False
c.prompt.filebrowser = False
c.input.insert_mode.auto_load = True
c.input.insert_mode.auto_leave = True
c.downloads.prevent_mixed_content = True
c.downloads.position = 'bottom'
c.window.transparent = True
c.content.notifications.enabled = True
c.content.webgl = True
c.content.pdfjs = True
c.content.xss_auditing = False
c.content.local_content_can_access_remote_urls = True
c.content.plugins = True
c.content.tls.certificate_errors = "load-insecurely"
c.content.geolocation = False
c.hints.radius = 7
c.hints.uppercase = True


# --- Search engines ---

#c.url.start_pages = ["file:///home/cs/.config/qutebrowser/index.html"]
c.url.searchengines = { 'DEFAULT': 'https://duckduckgo.com/?ia=web&q={}', '!a': 'https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}', '!g': 'https://google.com/search?hl=en&q={}', '!i': 'https://google.com/search?hl=en&tbm=isch&q={}', '!m': 'https://google.com/maps?q={}', '!w': 'https://en.wikipedia.org/w/index.php?title=Special%3ASearch&search={}', '!h': 'https://github.com/search?q={}', '!i': 'https://yewtu.be/search?q={}', '!y': 'https://youtube.com/results?search_query={}'}

c.fileselect.handler = 'external'
#c.fileselect.single_file.command = ['st', '-e', 'ranger', '--choosefile={}']
c.fileselect.single_file.command = ['foot', '-e', 'nnn', '-d', '-l', '2', '-U', '-D', '-R', '-p', '{}']
#c.fileselect.multiple_files.command = ['st', '-e', 'ranger', '--choosefiles={}']
c.fileselect.multiple_files.command = ['foot', '-e', 'nnn', '-d', '-l', '2', '-U', '-D', '-R', '-p', '{}']

config.bind('<Ctrl+/>', 'hint links spawn --detach mpv {hint-url}')
# --- Keybindings: Bookmarks ---
config.bind(',2', 'open https://yt.funami.tech/feed/subscriptions')
config.bind(',3', 'open https://proton.me')
config.bind(',4', 'open https://thepiratebay.org')
config.bind(',5', 'open https://boards.4channel.org/g/catalog')
config.bind(',6', 'open https://news.ycombinator.com/news')
config.bind(',7', 'open https://old.reddit.com')
config.bind(',8', 'open https://lainchan.org')
config.bind(',-', 'open https://app.element.io/#/welcome')
config.bind(',=', 'open https://en.wikipedia.org/wiki/Main_Page')
