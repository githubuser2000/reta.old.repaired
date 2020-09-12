let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <expr> <Down> pumvisible() ? "\" : "\<Down>"
inoremap <expr> <Up> pumvisible() ? "\" : "\<Up>"
imap <Nul> <C-Space>
imap <C-R>	 <Plug>snipMateShow
inoremap <expr> <S-Tab> pumvisible() ? "\" : "\<S-Tab>"
inoremap <silent> <C-Tab> =UltiSnips#ListSnippets()
inoremap <silent> <Plug>(fzf-maps-i) :call fzf#vim#maps('i', 0)
inoremap <expr> <Plug>(fzf-complete-buffer-line) fzf#vim#complete#buffer_line()
inoremap <expr> <Plug>(fzf-complete-line) fzf#vim#complete#line()
inoremap <expr> <Plug>(fzf-complete-file-ag) fzf#vim#complete#path('ag -l -g ""')
inoremap <expr> <Plug>(fzf-complete-file) fzf#vim#complete#path("find . -path '*/\.*' -prune -o -type f -print -o -type l -print | sed 's:^..::'")
inoremap <expr> <Plug>(fzf-complete-path) fzf#vim#complete#path("find . -path '*/\.*' -prune -o -print | sed '1d;s:^..::'")
inoremap <expr> <Plug>(fzf-complete-word) fzf#vim#complete#word()
inoremap <silent> <Plug>snipMateShow =snipMate#ShowAvailableSnips()
inoremap <silent> <Plug>snipMateBack =snipMate#BackwardsSnippet()
inoremap <silent> <Plug>snipMateTrigger =snipMate#TriggerSnippet(1)
inoremap <silent> <Plug>snipMateNextOrTrigger =snipMate#TriggerSnippet()
inoremap <silent> <Plug>NERDCommenterInsert  <BS>:call NERDComment('i', "insert")
imap <C-G>S <Plug>ISurround
imap <C-G>s <Plug>Isurround
imap <C-S> <Plug>Isurround
inoremap <silent> <Plug>(ale_complete) :ALEComplete
imap <F5> <Plug>ToggleBackground
snoremap <silent>  "_c
nnoremap  
xnoremap <silent> 	 :call UltiSnips#SaveLastVisualSelection()gvs
snoremap <silent> 	 :call UltiSnips#ExpandSnippet()
nnoremap <NL> <NL>
nnoremap  
nnoremap  
nnoremap <silent>  :CtrlP
snoremap  "_c
nnoremap   za
vnoremap // y/\V=escape(@",'/\')
map Q gq
xmap S <Plug>VSurround
nnoremap \d :YcmShowDetailedDiagnostic
nmap \ca <Plug>NERDCommenterAltDelims
xmap \cu <Plug>NERDCommenterUncomment
nmap \cu <Plug>NERDCommenterUncomment
xmap \cb <Plug>NERDCommenterAlignBoth
nmap \cb <Plug>NERDCommenterAlignBoth
xmap \cl <Plug>NERDCommenterAlignLeft
nmap \cl <Plug>NERDCommenterAlignLeft
nmap \cA <Plug>NERDCommenterAppend
xmap \cy <Plug>NERDCommenterYank
nmap \cy <Plug>NERDCommenterYank
xmap \cs <Plug>NERDCommenterSexy
nmap \cs <Plug>NERDCommenterSexy
xmap \ci <Plug>NERDCommenterInvert
nmap \ci <Plug>NERDCommenterInvert
nmap \c$ <Plug>NERDCommenterToEOL
xmap \cn <Plug>NERDCommenterNested
nmap \cn <Plug>NERDCommenterNested
xmap \cm <Plug>NERDCommenterMinimal
nmap \cm <Plug>NERDCommenterMinimal
xmap \c  <Plug>NERDCommenterToggle
nmap \c  <Plug>NERDCommenterToggle
xmap \cc <Plug>NERDCommenterComment
nmap \cc <Plug>NERDCommenterComment
nmap \w\m <Plug>VimwikiMakeTomorrowDiaryNote
nmap \w\y <Plug>VimwikiMakeYesterdayDiaryNote
nmap \w\t <Plug>VimwikiTabMakeDiaryNote
nmap \w\w <Plug>VimwikiMakeDiaryNote
nmap \w\i <Plug>VimwikiDiaryGenerateLinks
nmap \wi <Plug>VimwikiDiaryIndex
nmap \ws <Plug>VimwikiUISelect
nmap \wt <Plug>VimwikiTabIndex
nmap \ww <Plug>VimwikiIndex
map \g :YcmCompleter GoToDefinitionElseDeclaration
vmap ]f :call PythonDec("function", 1)
vmap ]F :call PythonDec("function", -1)
vmap ]j :call PythonDec("class", 1)
vmap ]J :call PythonDec("class", -1)
vmap ]u :call PythonUncommentSelection()
vmap ]# :call PythonCommentSelection()
vmap ]> >
vmap ]< <
vmap ]e :PEoBm'gv``
vmap ]t :PBOBm'gv``
nmap ]f :call PythonDec("function", 1)
omap ]f :call PythonDec("function", 1)
nmap ]F :call PythonDec("function", -1)
omap ]F :call PythonDec("function", -1)
nmap ]j :call PythonDec("class", 1)
omap ]j :call PythonDec("class", 1)
nmap ]J :call PythonDec("class", -1)
omap ]J :call PythonDec("class", -1)
nmap ]u :call PythonUncommentSelection()
omap ]u :call PythonUncommentSelection()
nmap ]# :call PythonCommentSelection()
omap ]# :call PythonCommentSelection()
nmap ]> ]tV]e>
omap ]> ]tV]e>
nmap ]< ]tV]e<
omap ]< ]tV]e<
nmap ]e :PEoB
omap ]e :PEoB
nmap ]t :PBoB
omap ]t :PBoB
map ]v ]tV]e
map ]c :call PythonSelectObject("class")
map ]d :call PythonSelectObject("function")
map ]<Up> :call PythonNextLine(-1)
map ]<Down> :call PythonNextLine(1)
nmap cS <Plug>CSurround
nmap cs <Plug>Csurround
nmap ds <Plug>Dsurround
vmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
xmap gS <Plug>VgSurround
nmap ySS <Plug>YSsurround
nmap ySs <Plug>YSsurround
nmap yss <Plug>Yssurround
nmap yS <Plug>YSurround
nmap ys <Plug>Ysurround
nmap <F9> :set rnu
nmap <F7> :GutentagsUpdate!
nmap <F3> :colorscheme embark
smap <S-Tab> <Plug>snipMateBack
vnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(netrw#GX(),netrw#CheckIfRemote(netrw#GX()))
snoremap <C-R> "_c
snoremap <silent> <C-H> "_c
snoremap <silent> <Del> "_c
snoremap <silent> <BS> "_c
snoremap <silent> <C-Tab> :call UltiSnips#ListSnippets()
onoremap <silent> <Plug>(fzf-maps-o) :call fzf#vim#maps('o', 0)
xnoremap <silent> <Plug>(fzf-maps-x) :call fzf#vim#maps('x', 0)
nnoremap <silent> <Plug>(fzf-maps-n) :call fzf#vim#maps('n', 0)
snoremap <silent> <Plug>snipMateBack a=snipMate#BackwardsSnippet()
snoremap <silent> <Plug>snipMateNextOrTrigger a=snipMate#TriggerSnippet()
nnoremap <silent> <C-P> :CtrlP
xnoremap <silent> <Plug>NERDCommenterUncomment :call NERDComment("x", "Uncomment")
nnoremap <silent> <Plug>NERDCommenterUncomment :call NERDComment("n", "Uncomment")
xnoremap <silent> <Plug>NERDCommenterAlignBoth :call NERDComment("x", "AlignBoth")
nnoremap <silent> <Plug>NERDCommenterAlignBoth :call NERDComment("n", "AlignBoth")
xnoremap <silent> <Plug>NERDCommenterAlignLeft :call NERDComment("x", "AlignLeft")
nnoremap <silent> <Plug>NERDCommenterAlignLeft :call NERDComment("n", "AlignLeft")
nnoremap <silent> <Plug>NERDCommenterAppend :call NERDComment("n", "Append")
xnoremap <silent> <Plug>NERDCommenterYank :call NERDComment("x", "Yank")
nnoremap <silent> <Plug>NERDCommenterYank :call NERDComment("n", "Yank")
xnoremap <silent> <Plug>NERDCommenterSexy :call NERDComment("x", "Sexy")
nnoremap <silent> <Plug>NERDCommenterSexy :call NERDComment("n", "Sexy")
xnoremap <silent> <Plug>NERDCommenterInvert :call NERDComment("x", "Invert")
nnoremap <silent> <Plug>NERDCommenterInvert :call NERDComment("n", "Invert")
nnoremap <silent> <Plug>NERDCommenterToEOL :call NERDComment("n", "ToEOL")
xnoremap <silent> <Plug>NERDCommenterNested :call NERDComment("x", "Nested")
nnoremap <silent> <Plug>NERDCommenterNested :call NERDComment("n", "Nested")
xnoremap <silent> <Plug>NERDCommenterMinimal :call NERDComment("x", "Minimal")
nnoremap <silent> <Plug>NERDCommenterMinimal :call NERDComment("n", "Minimal")
xnoremap <silent> <Plug>NERDCommenterToggle :call NERDComment("x", "Toggle")
nnoremap <silent> <Plug>NERDCommenterToggle :call NERDComment("n", "Toggle")
xnoremap <silent> <Plug>NERDCommenterComment :call NERDComment("x", "Comment")
nnoremap <silent> <Plug>NERDCommenterComment :call NERDComment("n", "Comment")
nmap <F10> :call ToggleMappings()
nmap <F2> :call FirstThings()
nmap <F4> :call ToggleMappings2()
nmap <F6> :VimwikiTabIndex
nmap <F8> :TagbarToggle
nnoremap <silent> <Plug>SurroundRepeat .
nnoremap <silent> <Plug>(ale_go_to_type_definition_in_vsplit) :ALEGoToTypeDefinitionInVSplit
nnoremap <silent> <Plug>(ale_go_to_type_definition_in_split) :ALEGoToTypeDefinitionInSplit
nnoremap <silent> <Plug>(ale_go_to_type_definition_in_tab) :ALEGoToTypeDefinitionInTab
nnoremap <silent> <Plug>(ale_go_to_definition_in_vsplit) :ALEGoToDefinitionInVSplit
nnoremap <silent> <Plug>(ale_go_to_definition_in_split) :ALEGoToDefinitionInSplit
nnoremap <silent> <Plug>(ale_go_to_definition_in_tab) :ALEGoToDefinitionInTab
nnoremap <silent> <Plug>(ale_repeat_selection) :ALERepeatSelection
nnoremap <silent> <Plug>(ale_rename) :ALERename
nnoremap <silent> <Plug>(ale_documentation) :ALEDocumentation
nnoremap <silent> <Plug>(ale_hover) :ALEHover
nnoremap <silent> <Plug>(ale_find_references) :ALEFindReferences
nnoremap <silent> <Plug>(ale_go_to_type_definition) :ALEGoToTypeDefinition
nnoremap <silent> <Plug>(ale_go_to_definition) :ALEGoToDefinition
nnoremap <silent> <Plug>(ale_fix) :ALEFix
nnoremap <silent> <Plug>(ale_detail) :ALEDetail
nnoremap <silent> <Plug>(ale_lint) :ALELint
nnoremap <silent> <Plug>(ale_reset_buffer) :ALEResetBuffer
nnoremap <silent> <Plug>(ale_disable_buffer) :ALEDisableBuffer
nnoremap <silent> <Plug>(ale_enable_buffer) :ALEEnableBuffer
nnoremap <silent> <Plug>(ale_toggle_buffer) :ALEToggleBuffer
nnoremap <silent> <Plug>(ale_reset) :ALEReset
nnoremap <silent> <Plug>(ale_disable) :ALEDisable
nnoremap <silent> <Plug>(ale_enable) :ALEEnable
nnoremap <silent> <Plug>(ale_toggle) :ALEToggle
nnoremap <silent> <Plug>(ale_last) :ALELast
nnoremap <silent> <Plug>(ale_first) :ALEFirst
nnoremap <silent> <Plug>(ale_next_wrap_warning) :ALENext -wrap -warning
nnoremap <silent> <Plug>(ale_next_warning) :ALENext -warning
nnoremap <silent> <Plug>(ale_next_wrap_error) :ALENext -wrap -error
nnoremap <silent> <Plug>(ale_next_error) :ALENext -error
nnoremap <silent> <Plug>(ale_next_wrap) :ALENextWrap
nnoremap <silent> <Plug>(ale_next) :ALENext
nnoremap <silent> <Plug>(ale_previous_wrap_warning) :ALEPrevious -wrap -warning
nnoremap <silent> <Plug>(ale_previous_warning) :ALEPrevious -warning
nnoremap <silent> <Plug>(ale_previous_wrap_error) :ALEPrevious -wrap -error
nnoremap <silent> <Plug>(ale_previous_error) :ALEPrevious -error
nnoremap <silent> <Plug>(ale_previous_wrap) :ALEPreviousWrap
nnoremap <silent> <Plug>(ale_previous) :ALEPrevious
vmap <F5> <Plug>ToggleBackground
nmap <F5> <Plug>ToggleBackground
nnoremap <C-H> 
nnoremap <C-L> 
nnoremap <C-K> 
nnoremap <C-J> <NL>
imap S <Plug>ISurround
imap s <Plug>Isurround
inoremap <expr> 	 pumvisible() ? "\" : "\	"
imap 	 <Plug>snipMateShow
imap  <Plug>Isurround
let &cpo=s:cpo_save
unlet s:cpo_save
set autoindent
set background=dark
set backspace=2
set clipboard=unnamed
set completeopt=preview,menuone
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=de
set hlsearch
set ruler
set runtimepath=~/.vim,~/.vim/bundle/Vundle.vim,~/.vim/bundle/SimpylFold,~/.vim/bundle/indentpython.vim,~/.vim/bundle/vim-flake8,~/.vim/bundle/Zenburn,~/.vim/bundle/vim-colors-solarized,~/.vim/bundle/nerdtree,~/.vim/bundle/vim-nerdtree-tabs,~/.vim/bundle/ctrlp.vim,~/.vim/bundle/vim-fugitive,~/.vim/bundle/vim-addon-mw-utils,~/.vim/bundle/tlib_vim,~/.vim/bundle/vim-snipmate,~/.vim/bundle/vim-snippets,~/.vim/bundle/powerline/powerline/bindings/vim/,~/.vim/bundle/YouCompleteMe,~/.vim/bundle/vimwiki,~/.vim/bundle/vim-rainbow,~/.vim/bundle/vim-hardtime,~/.vim/bundle/vim-pug-complete,~/.vim/plugged/nord-vim,~/.vim/plugged/oceanic-material,~/.vim/plugged/fzf,~/.vim/plugged/fzf.vim,~/.vim/plugged/embark,~/.vim/bundle/SimpylFold,~/.vim/bundle/YouCompleteMe,~/.vim/bundle/Zenburn,~/.vim/bundle/ctrlp.vim,~/.vim/bundle/indentpython.vim,~/.vim/bundle/nerdtree,~/.vim/bundle/powerline,~/.vim/bundle/powerline-develop,~/.vim/bundle/python-mode,~/.vim/bundle/tagbar-master,~/.vim/bundle/tlib_vim,~/.vim/bundle/ultisnips,~/.vim/bundle/vim-addon-mw-utils,~/.vim/bundle/vim-colors-solarized,~/.vim/bundle/vim-flake8,~/.vim/bundle/vim-fugitive,~/.vim/bundle/vim-gutentags,~/.vim/bundle/vim-hardtime,~/.vim/bundle/vim-nerdtree-tabs,~/.vim/bundle/vim-pug,~/.vim/bundle/vim-pug-complete,~/.vim/bundle/vim-rainbow,~/.vim/bundle/vim-snipmate,~/.vim/bundle/vim-snippets,~/.vim/bundle/vimwiki,~/.vim/pack/tpope/start/surround,~/.vim/pack/plugins/start/vimwiki,~/.vim/pack/git-plugins/start/ale,/usr/share/vim/vimfiles,/usr/share/vim/vim82,/usr/share/vim/vimfiles/after,~/.vim/bundle/vim-snipmate/after,~/.vim/bundle/vim-pug-complete/after,~/.vim/bundle/ultisnips/after,~/.vim/bundle/python-mode/after,~/.vim/after,~/.vim/bundle/Vundle.vim/after,~/.vim/bundle/SimpylFold/after,~/.vim/bundle/indentpython.vim/after,~/.vim/bundle/vim-flake8/after,~/.vim/bundle/Zenburn/after,~/.vim/bundle/vim-colors-solarized/after,~/.vim/bundle/nerdtree/after,~/.vim/bundle/vim-nerdtree-tabs/after,~/.vim/bundle/ctrlp.vim/after,~/.vim/bundle/vim-fugitive/after,~/.vim/bundle/vim-addon-mw-utils/after,~/.vim/bundle/tlib_vim/after,~/.vim/bundle/vim-snipmate/after,~/.vim/bundle/vim-snippets/after,~/.vim/bundle/powerline/powerline/bindings/vim//after,~/.vim/bundle/YouCompleteMe/after,~/.vim/bundle/vimwiki/after,~/.vim/bundle/vim-rainbow/after,~/.vim/bundle/vim-hardtime/after,~/.vim/bundle/vim-pug-complete/after
set shell=/bin/bash
set shiftround
set statusline=%!py3eval('powerline.new_window()')
set suffixes=.bak,~,.o,.h,.info,.swp,.obj,.info,.aux,.log,.dvi,.bbl,.out,.o,.lo
set tabline=%!py3eval('powerline.tabline()')
set tags=~/mytags
set wildignore=*.pyc
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/workspace-noneclipse/reta
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd reta.py
set stal=2
tabnew
tabnew
tabnew
tabrewind
edit tableHandling.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 119 + 119) / 238)
exe 'vert 2resize ' . ((&columns * 118 + 119) / 238)
argglobal
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','i')
inoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','i')
inoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? pumvisible() ? "\" : "\<Down>" : TooSoon('<DOWN>','i')
inoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? pumvisible() ? "\" : "\<Up>" : TooSoon('<UP>','i')
inoremap <buffer> <silent> <Nul> =pymode#rope#complete(0)
inoremap <buffer> <silent> <C-Space> =pymode#rope#complete(0)
noremap <buffer> <silent> ra :PymodeRopeAutoImport
noremap <buffer> <silent> r1p :call pymode#rope#module_to_package()
noremap <buffer> <silent> rnc :call pymode#rope#generate_class()
noremap <buffer> <silent> rnp :call pymode#rope#generate_package()
noremap <buffer> <silent> rnf :call pymode#rope#generate_function()
noremap <buffer> <silent> ru :call pymode#rope#use_function()
noremap <buffer> <silent> rs :call pymode#rope#signature()
noremap <buffer> <silent> rv :call pymode#rope#move()
noremap <buffer> <silent> ri :call pymode#rope#inline()
vnoremap <buffer> <silent> rl :call pymode#rope#extract_variable()
vnoremap <buffer> <silent> rm :call pymode#rope#extract_method()
noremap <buffer> <silent> r1r :call pymode#rope#rename_module()
noremap <buffer> <silent> rr :call pymode#rope#rename()
noremap <buffer> <silent> ro :call pymode#rope#organize_imports()
noremap <buffer> <silent> f :call pymode#rope#find_it()
noremap <buffer> <silent> d :call pymode#rope#show_doc()
noremap <buffer> <silent> g :call pymode#rope#goto_definition()
xnoremap <buffer> <silent> <expr> + TryKey('+') ? '+' : TooSoon('+','x')
nnoremap <buffer> <silent> <expr> + TryKey('+') ? '+' : TooSoon('+','n')
xnoremap <buffer> <silent> <expr> - TryKey('-') ? '-' : TooSoon('-','x')
nnoremap <buffer> <silent> <expr> - TryKey('-') ? '-' : TooSoon('-','n')
onoremap <buffer> C :call pymode#motion#select('^\s*class\s', 0)
vnoremap <buffer> <silent> K :call pymode#doc#show(@*)
nnoremap <buffer> <silent> K :call pymode#doc#find()
onoremap <buffer> M :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
vnoremap <buffer> [M :call pymode#motion#vmove('^\s*def\s', 'b')
vnoremap <buffer> [[ :call pymode#motion#vmove('\v^(class|def)\s', 'b')
onoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
onoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
nnoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> <silent> \b :call pymode#breakpoint#operate(line('.'))
vnoremap <buffer> <silent> \r :PymodeRun
nnoremap <buffer> <silent> \r :PymodeRun
onoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
vnoremap <buffer> ]M :call pymode#motion#vmove('^\s*def\s', '')
vnoremap <buffer> ]] :call pymode#motion#vmove('\v^(class|def)\s', '')
onoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
onoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
nnoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
vnoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
vnoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
onoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
xnoremap <buffer> <silent> <expr> h TryKey('h') ? 'h' : TooSoon('h','x')
nnoremap <buffer> <silent> <expr> h TryKey('h') ? 'h' : TooSoon('h','n')
vnoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
onoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
vnoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
onoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
xnoremap <buffer> <silent> <expr> j TryKey('j') ? 'j' : TooSoon('j','x')
nnoremap <buffer> <silent> <expr> j TryKey('j') ? 'j' : TooSoon('j','n')
xnoremap <buffer> <silent> <expr> k TryKey('k') ? 'k' : TooSoon('k','x')
nnoremap <buffer> <silent> <expr> k TryKey('k') ? 'k' : TooSoon('k','n')
xnoremap <buffer> <silent> <expr> l TryKey('l') ? 'l' : TooSoon('l','x')
nnoremap <buffer> <silent> <expr> l TryKey('l') ? 'l' : TooSoon('l','n')
xnoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','x')
xnoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','x')
xnoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','x')
xnoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','x')
nnoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','n')
nnoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','n')
nnoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','n')
nnoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','n')
noremap <buffer> <F7> :call flake8#Flake8()
noremap <buffer> <silent> <C-C>ra :PymodeRopeAutoImport
noremap <buffer> <silent> <C-C>r1p :call pymode#rope#module_to_package()
noremap <buffer> <silent> <C-C>rnc :call pymode#rope#generate_class()
noremap <buffer> <silent> <C-C>rnp :call pymode#rope#generate_package()
noremap <buffer> <silent> <C-C>rnf :call pymode#rope#generate_function()
noremap <buffer> <silent> <C-C>ru :call pymode#rope#use_function()
noremap <buffer> <silent> <C-C>rs :call pymode#rope#signature()
noremap <buffer> <silent> <C-C>rv :call pymode#rope#move()
noremap <buffer> <silent> <C-C>ri :call pymode#rope#inline()
vnoremap <buffer> <silent> <C-C>rl :call pymode#rope#extract_variable()
vnoremap <buffer> <silent> <C-C>rm :call pymode#rope#extract_method()
noremap <buffer> <silent> <C-C>r1r :call pymode#rope#rename_module()
noremap <buffer> <silent> <C-C>rr :call pymode#rope#rename()
noremap <buffer> <silent> <C-C>ro :call pymode#rope#organize_imports()
noremap <buffer> <silent> <C-C>f :call pymode#rope#find_it()
noremap <buffer> <silent> <C-C>d :call pymode#rope#show_doc()
noremap <buffer> <silent> <C-C>g :call pymode#rope#goto_definition()
inoremap <buffer> <silent> . .=pymode#rope#complete_on_dot()
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),0],:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=+1
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=^s*\\(def\\|class\\)
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=SimpylFold#FoldExpr(v:lnum)
setlocal foldignore=#
set foldlevel=99
setlocal foldlevel=99
setlocal foldmarker={{{,}}}
set foldmethod=indent
setlocal foldmethod=indent
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=pymode#folding#text()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(substitute(substitute(v:fname,b:grandparent_match,b:grandparent_sub,''),b:parent_match,b:parent_sub,''),b:child_match,b:child_sub,'g')
setlocal indentexpr=pymode#indent#get_indent(v:lnum)
setlocal indentkeys=!^F,o,O,<:>,0),0],0},=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
set linebreak
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=pymode#rope#completions
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=4
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=%!py3eval('powerline.statusline(4)')
setlocal suffixesadd=.py
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal nowrap
setlocal wrapmargin=0
let s:l = 244 - ((27 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
244
normal! 05|
wincmd w
argglobal
if bufexists("tableHandling.py") | buffer tableHandling.py | else | edit tableHandling.py | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','i')
inoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','i')
inoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? pumvisible() ? "\" : "\<Down>" : TooSoon('<DOWN>','i')
inoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? pumvisible() ? "\" : "\<Up>" : TooSoon('<UP>','i')
inoremap <buffer> <silent> <Nul> =pymode#rope#complete(0)
inoremap <buffer> <silent> <C-Space> =pymode#rope#complete(0)
noremap <buffer> <silent> ra :PymodeRopeAutoImport
noremap <buffer> <silent> r1p :call pymode#rope#module_to_package()
noremap <buffer> <silent> rnc :call pymode#rope#generate_class()
noremap <buffer> <silent> rnp :call pymode#rope#generate_package()
noremap <buffer> <silent> rnf :call pymode#rope#generate_function()
noremap <buffer> <silent> ru :call pymode#rope#use_function()
noremap <buffer> <silent> rs :call pymode#rope#signature()
noremap <buffer> <silent> rv :call pymode#rope#move()
noremap <buffer> <silent> ri :call pymode#rope#inline()
vnoremap <buffer> <silent> rl :call pymode#rope#extract_variable()
vnoremap <buffer> <silent> rm :call pymode#rope#extract_method()
noremap <buffer> <silent> r1r :call pymode#rope#rename_module()
noremap <buffer> <silent> rr :call pymode#rope#rename()
noremap <buffer> <silent> ro :call pymode#rope#organize_imports()
noremap <buffer> <silent> f :call pymode#rope#find_it()
noremap <buffer> <silent> d :call pymode#rope#show_doc()
noremap <buffer> <silent> g :call pymode#rope#goto_definition()
xnoremap <buffer> <silent> <expr> + TryKey('+') ? '+' : TooSoon('+','x')
nnoremap <buffer> <silent> <expr> + TryKey('+') ? '+' : TooSoon('+','n')
xnoremap <buffer> <silent> <expr> - TryKey('-') ? '-' : TooSoon('-','x')
nnoremap <buffer> <silent> <expr> - TryKey('-') ? '-' : TooSoon('-','n')
onoremap <buffer> C :call pymode#motion#select('^\s*class\s', 0)
vnoremap <buffer> <silent> K :call pymode#doc#show(@*)
nnoremap <buffer> <silent> K :call pymode#doc#find()
onoremap <buffer> M :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
vnoremap <buffer> [M :call pymode#motion#vmove('^\s*def\s', 'b')
vnoremap <buffer> [[ :call pymode#motion#vmove('\v^(class|def)\s', 'b')
onoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
onoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
nnoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> <silent> \b :call pymode#breakpoint#operate(line('.'))
vnoremap <buffer> <silent> \r :PymodeRun
nnoremap <buffer> <silent> \r :PymodeRun
onoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
vnoremap <buffer> ]M :call pymode#motion#vmove('^\s*def\s', '')
vnoremap <buffer> ]] :call pymode#motion#vmove('\v^(class|def)\s', '')
onoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
onoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
nnoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
vnoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
vnoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
onoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
xnoremap <buffer> <silent> <expr> h TryKey('h') ? 'h' : TooSoon('h','x')
nnoremap <buffer> <silent> <expr> h TryKey('h') ? 'h' : TooSoon('h','n')
vnoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
onoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
vnoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
onoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
xnoremap <buffer> <silent> <expr> j TryKey('j') ? 'j' : TooSoon('j','x')
nnoremap <buffer> <silent> <expr> j TryKey('j') ? 'j' : TooSoon('j','n')
xnoremap <buffer> <silent> <expr> k TryKey('k') ? 'k' : TooSoon('k','x')
nnoremap <buffer> <silent> <expr> k TryKey('k') ? 'k' : TooSoon('k','n')
xnoremap <buffer> <silent> <expr> l TryKey('l') ? 'l' : TooSoon('l','x')
nnoremap <buffer> <silent> <expr> l TryKey('l') ? 'l' : TooSoon('l','n')
xnoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','x')
xnoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','x')
xnoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','x')
xnoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','x')
nnoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','n')
nnoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','n')
nnoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','n')
nnoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','n')
noremap <buffer> <F7> :call flake8#Flake8()
noremap <buffer> <silent> <C-C>ra :PymodeRopeAutoImport
noremap <buffer> <silent> <C-C>r1p :call pymode#rope#module_to_package()
noremap <buffer> <silent> <C-C>rnc :call pymode#rope#generate_class()
noremap <buffer> <silent> <C-C>rnp :call pymode#rope#generate_package()
noremap <buffer> <silent> <C-C>rnf :call pymode#rope#generate_function()
noremap <buffer> <silent> <C-C>ru :call pymode#rope#use_function()
noremap <buffer> <silent> <C-C>rs :call pymode#rope#signature()
noremap <buffer> <silent> <C-C>rv :call pymode#rope#move()
noremap <buffer> <silent> <C-C>ri :call pymode#rope#inline()
vnoremap <buffer> <silent> <C-C>rl :call pymode#rope#extract_variable()
vnoremap <buffer> <silent> <C-C>rm :call pymode#rope#extract_method()
noremap <buffer> <silent> <C-C>r1r :call pymode#rope#rename_module()
noremap <buffer> <silent> <C-C>rr :call pymode#rope#rename()
noremap <buffer> <silent> <C-C>ro :call pymode#rope#organize_imports()
noremap <buffer> <silent> <C-C>f :call pymode#rope#find_it()
noremap <buffer> <silent> <C-C>d :call pymode#rope#show_doc()
noremap <buffer> <silent> <C-C>g :call pymode#rope#goto_definition()
inoremap <buffer> <silent> . .=pymode#rope#complete_on_dot()
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),0],:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=+1
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=^s*\\(def\\|class\\)
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=SimpylFold#FoldExpr(v:lnum)
setlocal foldignore=#
set foldlevel=99
setlocal foldlevel=99
setlocal foldmarker={{{,}}}
set foldmethod=indent
setlocal foldmethod=indent
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=pymode#folding#text()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(substitute(substitute(v:fname,b:grandparent_match,b:grandparent_sub,''),b:parent_match,b:parent_sub,''),b:child_match,b:child_sub,'g')
setlocal indentexpr=pymode#indent#get_indent(v:lnum)
setlocal indentkeys=!^F,o,O,<:>,0),0],0},=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
set linebreak
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=pymode#rope#completions
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=4
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=%!py3eval('powerline.statusline(3)')
setlocal suffixesadd=.py
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal nowrap
setlocal wrapmargin=0
let s:l = 1393 - ((27 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1393
normal! 046|
wincmd w
exe 'vert 1resize ' . ((&columns * 119 + 119) / 238)
exe 'vert 2resize ' . ((&columns * 118 + 119) / 238)
tabnext
edit retaX
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','i')
inoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','i')
inoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? pumvisible() ? "\" : "\<Down>" : TooSoon('<DOWN>','i')
inoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? pumvisible() ? "\" : "\<Up>" : TooSoon('<UP>','i')
inoremap <buffer> <silent> <Nul> =pymode#rope#complete(0)
inoremap <buffer> <silent> <C-Space> =pymode#rope#complete(0)
noremap <buffer> <silent> ra :PymodeRopeAutoImport
noremap <buffer> <silent> r1p :call pymode#rope#module_to_package()
noremap <buffer> <silent> rnc :call pymode#rope#generate_class()
noremap <buffer> <silent> rnp :call pymode#rope#generate_package()
noremap <buffer> <silent> rnf :call pymode#rope#generate_function()
noremap <buffer> <silent> ru :call pymode#rope#use_function()
noremap <buffer> <silent> rs :call pymode#rope#signature()
noremap <buffer> <silent> rv :call pymode#rope#move()
noremap <buffer> <silent> ri :call pymode#rope#inline()
vnoremap <buffer> <silent> rl :call pymode#rope#extract_variable()
vnoremap <buffer> <silent> rm :call pymode#rope#extract_method()
noremap <buffer> <silent> r1r :call pymode#rope#rename_module()
noremap <buffer> <silent> rr :call pymode#rope#rename()
noremap <buffer> <silent> ro :call pymode#rope#organize_imports()
noremap <buffer> <silent> f :call pymode#rope#find_it()
noremap <buffer> <silent> d :call pymode#rope#show_doc()
noremap <buffer> <silent> g :call pymode#rope#goto_definition()
xnoremap <buffer> <silent> <expr> + TryKey('+') ? '+' : TooSoon('+','x')
nnoremap <buffer> <silent> <expr> + TryKey('+') ? '+' : TooSoon('+','n')
xnoremap <buffer> <silent> <expr> - TryKey('-') ? '-' : TooSoon('-','x')
nnoremap <buffer> <silent> <expr> - TryKey('-') ? '-' : TooSoon('-','n')
onoremap <buffer> C :call pymode#motion#select('^\s*class\s', 0)
vnoremap <buffer> <silent> K :call pymode#doc#show(@*)
nnoremap <buffer> <silent> K :call pymode#doc#find()
onoremap <buffer> M :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
vnoremap <buffer> [M :call pymode#motion#vmove('^\s*def\s', 'b')
vnoremap <buffer> [[ :call pymode#motion#vmove('\v^(class|def)\s', 'b')
onoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
onoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
nnoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> <silent> \b :call pymode#breakpoint#operate(line('.'))
vnoremap <buffer> <silent> \r :PymodeRun
nnoremap <buffer> <silent> \r :PymodeRun
onoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
vnoremap <buffer> ]M :call pymode#motion#vmove('^\s*def\s', '')
vnoremap <buffer> ]] :call pymode#motion#vmove('\v^(class|def)\s', '')
onoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
onoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
nnoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
vnoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
vnoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
onoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
xnoremap <buffer> <silent> <expr> h TryKey('h') ? 'h' : TooSoon('h','x')
nnoremap <buffer> <silent> <expr> h TryKey('h') ? 'h' : TooSoon('h','n')
vnoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
onoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
vnoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
onoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
xnoremap <buffer> <silent> <expr> j TryKey('j') ? 'j' : TooSoon('j','x')
nnoremap <buffer> <silent> <expr> j TryKey('j') ? 'j' : TooSoon('j','n')
xnoremap <buffer> <silent> <expr> k TryKey('k') ? 'k' : TooSoon('k','x')
nnoremap <buffer> <silent> <expr> k TryKey('k') ? 'k' : TooSoon('k','n')
xnoremap <buffer> <silent> <expr> l TryKey('l') ? 'l' : TooSoon('l','x')
nnoremap <buffer> <silent> <expr> l TryKey('l') ? 'l' : TooSoon('l','n')
xnoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','x')
xnoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','x')
xnoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','x')
xnoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','x')
nnoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','n')
nnoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','n')
nnoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','n')
nnoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','n')
noremap <buffer> <F7> :call flake8#Flake8()
noremap <buffer> <silent> <C-C>ra :PymodeRopeAutoImport
noremap <buffer> <silent> <C-C>r1p :call pymode#rope#module_to_package()
noremap <buffer> <silent> <C-C>rnc :call pymode#rope#generate_class()
noremap <buffer> <silent> <C-C>rnp :call pymode#rope#generate_package()
noremap <buffer> <silent> <C-C>rnf :call pymode#rope#generate_function()
noremap <buffer> <silent> <C-C>ru :call pymode#rope#use_function()
noremap <buffer> <silent> <C-C>rs :call pymode#rope#signature()
noremap <buffer> <silent> <C-C>rv :call pymode#rope#move()
noremap <buffer> <silent> <C-C>ri :call pymode#rope#inline()
vnoremap <buffer> <silent> <C-C>rl :call pymode#rope#extract_variable()
vnoremap <buffer> <silent> <C-C>rm :call pymode#rope#extract_method()
noremap <buffer> <silent> <C-C>r1r :call pymode#rope#rename_module()
noremap <buffer> <silent> <C-C>rr :call pymode#rope#rename()
noremap <buffer> <silent> <C-C>ro :call pymode#rope#organize_imports()
noremap <buffer> <silent> <C-C>f :call pymode#rope#find_it()
noremap <buffer> <silent> <C-C>d :call pymode#rope#show_doc()
noremap <buffer> <silent> <C-C>g :call pymode#rope#goto_definition()
inoremap <buffer> <silent> . .=pymode#rope#complete_on_dot()
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),0],:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=+1
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=^s*\\(def\\|class\\)
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=SimpylFold#FoldExpr(v:lnum)
setlocal foldignore=#
set foldlevel=99
setlocal foldlevel=99
setlocal foldmarker={{{,}}}
set foldmethod=indent
setlocal foldmethod=expr
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=pymode#folding#text()
setlocal formatexpr=
setlocal formatoptions=cq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(substitute(substitute(v:fname,b:grandparent_match,b:grandparent_sub,''),b:parent_match,b:parent_sub,''),b:child_match,b:child_sub,'g')
setlocal indentexpr=pymode#indent#get_indent(v:lnum)
setlocal indentkeys=!^F,o,O,<:>,0),0],0},=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
set linebreak
setlocal linebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=pymode#rope#completions
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=4
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=%!py3eval('powerline.statusline(7)')
setlocal suffixesadd=.py
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tagfunc=
setlocal tags=~/workspace-noneclipse/reta/tags,~/mytags
setlocal textwidth=80
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal nowrap
setlocal wrapmargin=0
let s:l = 9 - ((8 * winheight(0) + 28) / 57)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
9
normal! 0
tabnext
edit reta
set splitbelow splitright
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
argglobal
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','i')
inoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','i')
inoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? pumvisible() ? "\" : "\<Down>" : TooSoon('<DOWN>','i')
inoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? pumvisible() ? "\" : "\<Up>" : TooSoon('<UP>','i')
inoremap <buffer> <silent> <Nul> =pymode#rope#complete(0)
inoremap <buffer> <silent> <C-Space> =pymode#rope#complete(0)
noremap <buffer> <silent> ra :PymodeRopeAutoImport
noremap <buffer> <silent> r1p :call pymode#rope#module_to_package()
noremap <buffer> <silent> rnc :call pymode#rope#generate_class()
noremap <buffer> <silent> rnp :call pymode#rope#generate_package()
noremap <buffer> <silent> rnf :call pymode#rope#generate_function()
noremap <buffer> <silent> ru :call pymode#rope#use_function()
noremap <buffer> <silent> rs :call pymode#rope#signature()
noremap <buffer> <silent> rv :call pymode#rope#move()
noremap <buffer> <silent> ri :call pymode#rope#inline()
vnoremap <buffer> <silent> rl :call pymode#rope#extract_variable()
vnoremap <buffer> <silent> rm :call pymode#rope#extract_method()
noremap <buffer> <silent> r1r :call pymode#rope#rename_module()
noremap <buffer> <silent> rr :call pymode#rope#rename()
noremap <buffer> <silent> ro :call pymode#rope#organize_imports()
noremap <buffer> <silent> f :call pymode#rope#find_it()
noremap <buffer> <silent> d :call pymode#rope#show_doc()
noremap <buffer> <silent> g :call pymode#rope#goto_definition()
xnoremap <buffer> <silent> <expr> + TryKey('+') ? '+' : TooSoon('+','x')
nnoremap <buffer> <silent> <expr> + TryKey('+') ? '+' : TooSoon('+','n')
xnoremap <buffer> <silent> <expr> - TryKey('-') ? '-' : TooSoon('-','x')
nnoremap <buffer> <silent> <expr> - TryKey('-') ? '-' : TooSoon('-','n')
onoremap <buffer> C :call pymode#motion#select('^\s*class\s', 0)
vnoremap <buffer> <silent> K :call pymode#doc#show(@*)
nnoremap <buffer> <silent> K :call pymode#doc#find()
onoremap <buffer> M :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
vnoremap <buffer> [M :call pymode#motion#vmove('^\s*def\s', 'b')
vnoremap <buffer> [[ :call pymode#motion#vmove('\v^(class|def)\s', 'b')
onoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
onoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
nnoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> <silent> \b :call pymode#breakpoint#operate(line('.'))
vnoremap <buffer> <silent> \r :PymodeRun
nnoremap <buffer> <silent> \r :PymodeRun
onoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
vnoremap <buffer> ]M :call pymode#motion#vmove('^\s*def\s', '')
vnoremap <buffer> ]] :call pymode#motion#vmove('\v^(class|def)\s', '')
onoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
onoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
nnoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
vnoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
vnoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
onoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
xnoremap <buffer> <silent> <expr> h TryKey('h') ? 'h' : TooSoon('h','x')
nnoremap <buffer> <silent> <expr> h TryKey('h') ? 'h' : TooSoon('h','n')
vnoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
onoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
vnoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
onoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
xnoremap <buffer> <silent> <expr> j TryKey('j') ? 'j' : TooSoon('j','x')
nnoremap <buffer> <silent> <expr> j TryKey('j') ? 'j' : TooSoon('j','n')
xnoremap <buffer> <silent> <expr> k TryKey('k') ? 'k' : TooSoon('k','x')
nnoremap <buffer> <silent> <expr> k TryKey('k') ? 'k' : TooSoon('k','n')
xnoremap <buffer> <silent> <expr> l TryKey('l') ? 'l' : TooSoon('l','x')
nnoremap <buffer> <silent> <expr> l TryKey('l') ? 'l' : TooSoon('l','n')
xnoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','x')
xnoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','x')
xnoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','x')
xnoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','x')
nnoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','n')
nnoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','n')
nnoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','n')
nnoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','n')
noremap <buffer> <F7> :call flake8#Flake8()
noremap <buffer> <silent> <C-C>ra :PymodeRopeAutoImport
noremap <buffer> <silent> <C-C>r1p :call pymode#rope#module_to_package()
noremap <buffer> <silent> <C-C>rnc :call pymode#rope#generate_class()
noremap <buffer> <silent> <C-C>rnp :call pymode#rope#generate_package()
noremap <buffer> <silent> <C-C>rnf :call pymode#rope#generate_function()
noremap <buffer> <silent> <C-C>ru :call pymode#rope#use_function()
noremap <buffer> <silent> <C-C>rs :call pymode#rope#signature()
noremap <buffer> <silent> <C-C>rv :call pymode#rope#move()
noremap <buffer> <silent> <C-C>ri :call pymode#rope#inline()
vnoremap <buffer> <silent> <C-C>rl :call pymode#rope#extract_variable()
vnoremap <buffer> <silent> <C-C>rm :call pymode#rope#extract_method()
noremap <buffer> <silent> <C-C>r1r :call pymode#rope#rename_module()
noremap <buffer> <silent> <C-C>rr :call pymode#rope#rename()
noremap <buffer> <silent> <C-C>ro :call pymode#rope#organize_imports()
noremap <buffer> <silent> <C-C>f :call pymode#rope#find_it()
noremap <buffer> <silent> <C-C>d :call pymode#rope#show_doc()
noremap <buffer> <silent> <C-C>g :call pymode#rope#goto_definition()
inoremap <buffer> <silent> . .=pymode#rope#complete_on_dot()
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),0],:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=+1
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=^s*\\(def\\|class\\)
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=SimpylFold#FoldExpr(v:lnum)
setlocal foldignore=#
set foldlevel=99
setlocal foldlevel=99
setlocal foldmarker={{{,}}}
set foldmethod=indent
setlocal foldmethod=expr
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=pymode#folding#text()
setlocal formatexpr=
setlocal formatoptions=cq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(substitute(substitute(v:fname,b:grandparent_match,b:grandparent_sub,''),b:parent_match,b:parent_sub,''),b:child_match,b:child_sub,'g')
setlocal indentexpr=pymode#indent#get_indent(v:lnum)
setlocal indentkeys=!^F,o,O,<:>,0),0],0},=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
set linebreak
setlocal linebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=pymode#rope#completions
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=4
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=%!py3eval('powerline.statusline(6)')
setlocal suffixesadd=.py
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tagfunc=
setlocal tags=~/workspace-noneclipse/reta/tags,~/mytags
setlocal textwidth=80
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal nowrap
setlocal wrapmargin=0
let s:l = 5 - ((4 * winheight(0) + 28) / 57)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
5
normal! 0
tabnext
edit reta.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 119 + 119) / 238)
exe 'vert 2resize ' . ((&columns * 118 + 119) / 238)
argglobal
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','i')
inoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','i')
inoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','i')
inoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','i')
inoremap <buffer> <silent> <Nul> =pymode#rope#complete(0)
inoremap <buffer> <silent> <C-Space> =pymode#rope#complete(0)
noremap <buffer> <silent> ra :PymodeRopeAutoImport
noremap <buffer> <silent> r1p :call pymode#rope#module_to_package()
noremap <buffer> <silent> rnc :call pymode#rope#generate_class()
noremap <buffer> <silent> rnp :call pymode#rope#generate_package()
noremap <buffer> <silent> rnf :call pymode#rope#generate_function()
noremap <buffer> <silent> ru :call pymode#rope#use_function()
noremap <buffer> <silent> rs :call pymode#rope#signature()
noremap <buffer> <silent> rv :call pymode#rope#move()
noremap <buffer> <silent> ri :call pymode#rope#inline()
vnoremap <buffer> <silent> rl :call pymode#rope#extract_variable()
vnoremap <buffer> <silent> rm :call pymode#rope#extract_method()
noremap <buffer> <silent> r1r :call pymode#rope#rename_module()
noremap <buffer> <silent> rr :call pymode#rope#rename()
noremap <buffer> <silent> ro :call pymode#rope#organize_imports()
noremap <buffer> <silent> f :call pymode#rope#find_it()
noremap <buffer> <silent> d :call pymode#rope#show_doc()
noremap <buffer> <silent> g :call pymode#rope#goto_definition()
xnoremap <buffer> <silent> <expr> + TryKey('+') ? '+' : TooSoon('+','x')
nnoremap <buffer> <silent> <expr> + TryKey('+') ? '+' : TooSoon('+','n')
xnoremap <buffer> <silent> <expr> - TryKey('-') ? '-' : TooSoon('-','x')
nnoremap <buffer> <silent> <expr> - TryKey('-') ? '-' : TooSoon('-','n')
onoremap <buffer> C :call pymode#motion#select('^\s*class\s', 0)
vnoremap <buffer> <silent> K :call pymode#doc#show(@*)
nnoremap <buffer> <silent> K :call pymode#doc#find()
onoremap <buffer> M :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
vnoremap <buffer> [M :call pymode#motion#vmove('^\s*def\s', 'b')
vnoremap <buffer> [[ :call pymode#motion#vmove('\v^(class|def)\s', 'b')
onoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
onoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
nnoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> <silent> \b :call pymode#breakpoint#operate(line('.'))
vnoremap <buffer> <silent> \r :PymodeRun
nnoremap <buffer> <silent> \r :PymodeRun
onoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
vnoremap <buffer> ]M :call pymode#motion#vmove('^\s*def\s', '')
vnoremap <buffer> ]] :call pymode#motion#vmove('\v^(class|def)\s', '')
onoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
onoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
nnoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
vnoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
vnoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
onoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
xnoremap <buffer> <silent> <expr> h TryKey('h') ? 'h' : TooSoon('h','x')
nnoremap <buffer> <silent> <expr> h TryKey('h') ? 'h' : TooSoon('h','n')
vnoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
onoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
vnoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
onoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
xnoremap <buffer> <silent> <expr> j TryKey('j') ? 'j' : TooSoon('j','x')
nnoremap <buffer> <silent> <expr> j TryKey('j') ? 'j' : TooSoon('j','n')
xnoremap <buffer> <silent> <expr> k TryKey('k') ? 'k' : TooSoon('k','x')
nnoremap <buffer> <silent> <expr> k TryKey('k') ? 'k' : TooSoon('k','n')
xnoremap <buffer> <silent> <expr> l TryKey('l') ? 'l' : TooSoon('l','x')
nnoremap <buffer> <silent> <expr> l TryKey('l') ? 'l' : TooSoon('l','n')
xnoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','x')
xnoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','x')
xnoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','x')
xnoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','x')
nnoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','n')
nnoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','n')
nnoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','n')
nnoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','n')
noremap <buffer> <F7> :call flake8#Flake8()
noremap <buffer> <silent> <C-C>ra :PymodeRopeAutoImport
noremap <buffer> <silent> <C-C>r1p :call pymode#rope#module_to_package()
noremap <buffer> <silent> <C-C>rnc :call pymode#rope#generate_class()
noremap <buffer> <silent> <C-C>rnp :call pymode#rope#generate_package()
noremap <buffer> <silent> <C-C>rnf :call pymode#rope#generate_function()
noremap <buffer> <silent> <C-C>ru :call pymode#rope#use_function()
noremap <buffer> <silent> <C-C>rs :call pymode#rope#signature()
noremap <buffer> <silent> <C-C>rv :call pymode#rope#move()
noremap <buffer> <silent> <C-C>ri :call pymode#rope#inline()
vnoremap <buffer> <silent> <C-C>rl :call pymode#rope#extract_variable()
vnoremap <buffer> <silent> <C-C>rm :call pymode#rope#extract_method()
noremap <buffer> <silent> <C-C>r1r :call pymode#rope#rename_module()
noremap <buffer> <silent> <C-C>rr :call pymode#rope#rename()
noremap <buffer> <silent> <C-C>ro :call pymode#rope#organize_imports()
noremap <buffer> <silent> <C-C>f :call pymode#rope#find_it()
noremap <buffer> <silent> <C-C>d :call pymode#rope#show_doc()
noremap <buffer> <silent> <C-C>g :call pymode#rope#goto_definition()
inoremap <buffer> <silent> . .=pymode#rope#complete_on_dot()
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),0],:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=+1
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=^s*\\(def\\|class\\)
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=SimpylFold#FoldExpr(v:lnum)
setlocal foldignore=#
set foldlevel=99
setlocal foldlevel=99
setlocal foldmarker={{{,}}}
set foldmethod=indent
setlocal foldmethod=indent
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=pymode#folding#text()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(substitute(substitute(v:fname,b:grandparent_match,b:grandparent_sub,''),b:parent_match,b:parent_sub,''),b:child_match,b:child_sub,'g')
setlocal indentexpr=pymode#indent#get_indent(v:lnum)
setlocal indentkeys=!^F,o,O,<:>,0),0],0},=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
set linebreak
setlocal linebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=pymode#rope#completions
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=4
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=%!py3eval('powerline.statusline(1)')
setlocal suffixesadd=.py
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
let s:l = 129 - ((27 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
129
normal! 0
wincmd w
argglobal
if bufexists("reta.py") | buffer reta.py | else | edit reta.py | endif
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','i')
inoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','i')
inoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','i')
inoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','i')
inoremap <buffer> <silent> <Nul> =pymode#rope#complete(0)
inoremap <buffer> <silent> <C-Space> =pymode#rope#complete(0)
noremap <buffer> <silent> ra :PymodeRopeAutoImport
noremap <buffer> <silent> r1p :call pymode#rope#module_to_package()
noremap <buffer> <silent> rnc :call pymode#rope#generate_class()
noremap <buffer> <silent> rnp :call pymode#rope#generate_package()
noremap <buffer> <silent> rnf :call pymode#rope#generate_function()
noremap <buffer> <silent> ru :call pymode#rope#use_function()
noremap <buffer> <silent> rs :call pymode#rope#signature()
noremap <buffer> <silent> rv :call pymode#rope#move()
noremap <buffer> <silent> ri :call pymode#rope#inline()
vnoremap <buffer> <silent> rl :call pymode#rope#extract_variable()
vnoremap <buffer> <silent> rm :call pymode#rope#extract_method()
noremap <buffer> <silent> r1r :call pymode#rope#rename_module()
noremap <buffer> <silent> rr :call pymode#rope#rename()
noremap <buffer> <silent> ro :call pymode#rope#organize_imports()
noremap <buffer> <silent> f :call pymode#rope#find_it()
noremap <buffer> <silent> d :call pymode#rope#show_doc()
noremap <buffer> <silent> g :call pymode#rope#goto_definition()
xnoremap <buffer> <silent> <expr> + TryKey('+') ? '+' : TooSoon('+','x')
nnoremap <buffer> <silent> <expr> + TryKey('+') ? '+' : TooSoon('+','n')
xnoremap <buffer> <silent> <expr> - TryKey('-') ? '-' : TooSoon('-','x')
nnoremap <buffer> <silent> <expr> - TryKey('-') ? '-' : TooSoon('-','n')
onoremap <buffer> C :call pymode#motion#select('^\s*class\s', 0)
vnoremap <buffer> <silent> K :call pymode#doc#show(@*)
nnoremap <buffer> <silent> K :call pymode#doc#find()
onoremap <buffer> M :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
vnoremap <buffer> [M :call pymode#motion#vmove('^\s*def\s', 'b')
vnoremap <buffer> [[ :call pymode#motion#vmove('\v^(class|def)\s', 'b')
onoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
onoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
nnoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> <silent> \b :call pymode#breakpoint#operate(line('.'))
vnoremap <buffer> <silent> \r :PymodeRun
nnoremap <buffer> <silent> \r :PymodeRun
onoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
vnoremap <buffer> ]M :call pymode#motion#vmove('^\s*def\s', '')
vnoremap <buffer> ]] :call pymode#motion#vmove('\v^(class|def)\s', '')
onoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
onoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
nnoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
vnoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
vnoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
onoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
xnoremap <buffer> <silent> <expr> h TryKey('h') ? 'h' : TooSoon('h','x')
nnoremap <buffer> <silent> <expr> h TryKey('h') ? 'h' : TooSoon('h','n')
vnoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
onoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
vnoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
onoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
xnoremap <buffer> <silent> <expr> j TryKey('j') ? 'j' : TooSoon('j','x')
nnoremap <buffer> <silent> <expr> j TryKey('j') ? 'j' : TooSoon('j','n')
xnoremap <buffer> <silent> <expr> k TryKey('k') ? 'k' : TooSoon('k','x')
nnoremap <buffer> <silent> <expr> k TryKey('k') ? 'k' : TooSoon('k','n')
xnoremap <buffer> <silent> <expr> l TryKey('l') ? 'l' : TooSoon('l','x')
nnoremap <buffer> <silent> <expr> l TryKey('l') ? 'l' : TooSoon('l','n')
xnoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','x')
xnoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','x')
xnoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','x')
xnoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','x')
nnoremap <buffer> <silent> <expr> <Right> TryKey('<Right>') ? '<Right>' : TooSoon('<RIGHT>','n')
nnoremap <buffer> <silent> <expr> <Left> TryKey('<Left>') ? '<Left>' : TooSoon('<LEFT>','n')
nnoremap <buffer> <silent> <expr> <Down> TryKey('<Down>') ? '<Down>' : TooSoon('<DOWN>','n')
nnoremap <buffer> <silent> <expr> <Up> TryKey('<Up>') ? '<Up>' : TooSoon('<UP>','n')
noremap <buffer> <F7> :call flake8#Flake8()
noremap <buffer> <silent> <C-C>ra :PymodeRopeAutoImport
noremap <buffer> <silent> <C-C>r1p :call pymode#rope#module_to_package()
noremap <buffer> <silent> <C-C>rnc :call pymode#rope#generate_class()
noremap <buffer> <silent> <C-C>rnp :call pymode#rope#generate_package()
noremap <buffer> <silent> <C-C>rnf :call pymode#rope#generate_function()
noremap <buffer> <silent> <C-C>ru :call pymode#rope#use_function()
noremap <buffer> <silent> <C-C>rs :call pymode#rope#signature()
noremap <buffer> <silent> <C-C>rv :call pymode#rope#move()
noremap <buffer> <silent> <C-C>ri :call pymode#rope#inline()
vnoremap <buffer> <silent> <C-C>rl :call pymode#rope#extract_variable()
vnoremap <buffer> <silent> <C-C>rm :call pymode#rope#extract_method()
noremap <buffer> <silent> <C-C>r1r :call pymode#rope#rename_module()
noremap <buffer> <silent> <C-C>rr :call pymode#rope#rename()
noremap <buffer> <silent> <C-C>ro :call pymode#rope#organize_imports()
noremap <buffer> <silent> <C-C>f :call pymode#rope#find_it()
noremap <buffer> <silent> <C-C>d :call pymode#rope#show_doc()
noremap <buffer> <silent> <C-C>g :call pymode#rope#goto_definition()
inoremap <buffer> <silent> . .=pymode#rope#complete_on_dot()
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),0],:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=+1
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal cursorlineopt=both
setlocal define=^s*\\(def\\|class\\)
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=SimpylFold#FoldExpr(v:lnum)
setlocal foldignore=#
set foldlevel=99
setlocal foldlevel=99
setlocal foldmarker={{{,}}}
set foldmethod=indent
setlocal foldmethod=expr
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=pymode#folding#text()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(substitute(substitute(v:fname,b:grandparent_match,b:grandparent_sub,''),b:parent_match,b:parent_sub,''),b:child_match,b:child_sub,'g')
setlocal indentexpr=pymode#indent#get_indent(v:lnum)
setlocal indentkeys=!^F,o,O,<:>,0),0],0},=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=pydoc
set linebreak
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=pymode#rope#completions
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=4
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=%!py3eval('powerline.statusline(2)')
setlocal suffixesadd=.py
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal nowrap
setlocal wrapmargin=0
let s:l = 1797 - ((27 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1797
normal! 09|
wincmd w
exe 'vert 1resize ' . ((&columns * 119 + 119) / 238)
exe 'vert 2resize ' . ((&columns * 118 + 119) / 238)
tabnext 4
set stal=1
badd +1 tableHandling.py
badd +0 reta.py
badd +1 retaX
badd +1 reta
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOS
set winminheight=1 winminwidth=1
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
