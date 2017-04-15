# centOS install vs-code:

- **import rpm keys:**

    ` sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc `

    ` sudo sh -c 'echo -e "[code]\nname=Visual Studio       Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo' `

- **update and install code:**

    ` yum check-update `
    ` sudo yum install code `

***


# centOS install oh-my-zsh: 

1. **install zsh:**

    `sudo install zsh `

2. **install & config oh-my-zsh:**

    oh-my-zsh源码是放在github上的，所以先要安装git:   `sudo yum install git -y`

    - **auto install:**

        通过curl进行安装

        ` sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" `

        通过wget进行安装

        ` sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)" `

    - **manual install:**

        - Clone the repository:

            `git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh`
        - Optionally, backup your existing ~/.zshrc file:

            `cp ~/.zshrc ~/.zshrc.orig`
        - Create a new zsh configuration file

            `cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc`

        - Change your default shell
            
            `chsh -s /bin/zsh`
            
        - Initialize your new zsh configuration

            Once you open up a new terminal window, it should load zsh with Oh My Zsh's configuration.

3. **manual update:**
            
    `upgrade_oh_my_zsh`

4. **config oh-my-zsh:**

    - 安装autojump，配置到oh-my-zsh中永久生效

        `sudo yum install autojump autojump-zsh -y`
        
    - 安装Dracula主题

        `# -O参数：自定义存储的文件名`
        `# -c参数：支持断点续传`
        `# --no-check-certificate参数：忽略https验证`
        `wget -O dracula.zip -c --no-check-certificate https://github.com/dracula/zsh/archive/master.zip`
        `# 解压缩`
        `unzip dracula.zip`
        `# 将dracula.zsh-theme移动到oh-my-zsh主题目录`
        `mv zsh-master/dracula.zsh-theme .oh-my-zsh/themes/`

    - 接下来进行oh-my-zsh的配置

        修改~/.zshrc：

        `vim ~/.zshrc`

        修改 # export LANG=en_US.UTF-8 为 export LANG=en_US.UTF-8

        `# You may need to manually set your language environment`
        `export LANG=en_US.UTF-8`

    - 修改主题为Dracula

        `# ZSH_THEME="robbyrussell"`
        `ZSH_THEME="dracula"`

    - 开启常用插件：

        `plugins=(git autojump systemd yum wd common-aliases)`

    - 引用更改并立刻生效：

        `source ~/.zshrc`


***
