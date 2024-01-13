execute pathogen#infect()
set omnifunc=syntaxcomplete#Complete
syntax on
filetype plugin indent on 
set number
filetype off
set tabstop=2
set shiftwidth=2
set ruler
set ai
set hlsearch
highlight Comment ctermfg=green
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'xuhdev/vim-latex-live-preview'
Plugin 'davidhalter/jedi-vim'
Plugin 'scrooloose/nerdtree'
Plugin 'tpope/vim-fugitive'
Plugin 'sheerun/vim-polyglot'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'scrooloose/nerdcommenter'
Plugin 'mattn/emmet-vim'
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'
"color 
Plugin 'bignimbus/pop-punk.vim'

colorscheme pop-punk


call vundle#end()            " required
filetype plugin indent on    "
let g:airline_powerline_fonts = 1
if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif
let g:airline_symbols.space = "\ua0"
let g:airline_left_sep=''
let g:airline_right_sep=''

"pop punk
" pop-punk ANSI colors for vim terminal
let g:terminal_ansi_colors = pop_punk#AnsiColors()

" for the airline theme - note the underscore instead of the hyphen
let g:airline_theme = 'pop_punk'

" for lightline theme - this needs underscore too
"let g:lightline.colorscheme = 'pop_punk'

"autopreview LaTeX
map C :! pdflatex %<CR><CR>
map S :! zathura $(echo % \| sed 's/tex$/pdf/') & disown<CR><CR>
let g:livepreview_previewer = 'zathura'
let g:livepreview_use_biber = 1
let g:livepreview_cursorhold_recompile = 0

" unicode symbols

let g:airline_left_sep = '»'
let g:airline_left_sep = '▶'
let g:airline_right_sep = '«'
let g:airline_right_sep = '◀'
let g:airline_symbols.linenr = '␊'
let g:airline_symbols.linenr = '␤'
let g:airline_symbols.linenr = '¶'
let g:airline_symbols.branch = '⎇'
let g:airline_symbols.paste = 'ρ'
let g:airline_symbols.paste = 'Þ'
let g:airline_symbols.paste = '∥'
let g:airline_symbols.whitespace = 'Ξ'

" airline symbols
let g:airline_left_sep = ''
let g:airline_left_alt_sep = ''
let g:airline_right_sep = ''
let g:airline_right_alt_sep = ''
let g:airline_symbols.branch = ''
let g:airline_symbols.readonly = ''
let g:airline_symbols.linenr = ''

" Nerd Tree 
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>

"jedi vim
let g:jedi#auto_initialization = 1
"Compile document, be it groff/LaTeX/markdown/etc.
map <leader>c :w! \| !compiler "%:p"<CR>
