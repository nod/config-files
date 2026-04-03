
-- some taken from 
-- https://medium.com/@edominguez.se/so-i-switched-to-neovim-in-2025-163b85aa0935
-- https://github.com/nvim-lua/kickstart.nvim/blob/master/init.lua

vim.g.have_nerd_font = true

vim.o.mouse = 'a'

vim.opt.tabstop = 2
vim.opt.softtabstop = 2
vim.opt.shiftwidth = 2
vim.opt.expandtab = true
vim.opt.autoindent = true
vim.opt.smartindent = true
vim.opt.smarttab = true
vim.opt.list = true
vim.opt.listchars = "eol:.,tab:>-,trail:~,extends:>,precedes:<"


vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.cursorline = true
vim.opt.signcolumn = "yes:1"
vim.opt.scrolloff = 3
vim.opt.showcmd = true

vim.opt.swapfile = false
vim.opt.backup = false
vim.opt.undodir = os.getenv("HOME") .. "/.config/nvim/undodir"
vim.opt.undofile = true

vim.schedule(function() vim.o.clipboard = 'unnamedplus' end)

vim.opt.hlsearch = true
vim.opt.incsearch = true
vim.opt.ignorecase = true
vim.opt.smartcase =true


vim.o.breakindent = true

vim.opt.termguicolors = true

-- mode is in status line so don't show it
vim.opt.showmode = false

-- No automatic comment insertion
vim.cmd([[autocmd FileType * set formatoptions-=ro]])

-- clear highlights with an esc
vim.keymap.set('n', '<Esc>', '<cmd>nohlsearch<CR>')
