![logo](https://github.com/WR4THf/SHELL-bot-Discord/blob/main/shell-bot.png)
# SHELL-bot for Discord
A Discord bot that acts as a Unix-like terminal emulator, allowing authorized administrators to execute shell commands directly from Discord.

## ⚠️ Security Warning

**CRITICAL SECURITY NOTICE:** This bot can execute arbitrary shell commands with the permissions of the user running the bot. 

**USE WITH EXTREME CAUTION:**
- Only use in trusted environments
- Only grant administrator permissions to trusted users
- Consider running in a containerized/isolated environment
- The bot has the same system access as the user account running it
- All executed commands are logged for security auditing

## Features

- 🖥️ Execute shell commands via Discord
- ⏱️ 60-second timeout protection
- 👮 Administrator-only command access
- 📊 Separate stdout/stderr display
- 📝 Output length limiting (prevents Discord message limits)
- 🔒 Permission-based access control
- 📋 Command execution logging

## Quick Start

### Linux/Mac:
```bash
chmod +x run.sh
./run.sh
```

Windows:

```batch
run.bat
```

Installation

Method 1: Using Launcher Scripts (Recommended)

1. Clone the repository

```bash
git clone https://github.com/WR4THf/SHELL-bot-Discord.git
cd SHELL-bot-Discord
```

1. Run the launcher script

Linux/Mac:

```bash
chmod +x run.sh
./run.sh
```

Windows:

```batch
run.bat
```

The script will automatically:

· Create virtual environment
· Install dependencies
· Start the bot

Method 2: Manual Installation

1. Create virtual environment

```bash
python -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the bot

```bash
python bot.py
```

Bot Setup

1. Create Discord Application

1. Go to Discord Developer Portal
2. Click "New Application"
3. Enter a name for your bot

2. Create Bot User

1. Go to the "Bot" section in your application
2. Click "Add Bot"

3. Enable Privileged Gateway Intents

In the Bot section, enable:

· Message Content Intent
· Server Members Intent

4. Invite Bot to Server

Configuration

Environment Variables

Bot Permissions

The bot requires these Discord permissions:

· Send Messages
· Read Message History
· Use Slash Commands
· Mention Everyone (for command output)

Usage

Basic Commands

```bash
!run "ls -la"
!run "pwd"
!run "whoami"
!run "echo 'Hello World'"
```

Advanced Examples

```bash
!run "ps aux | grep discord"
!run "df -h"
!run "netstat -tulpn"
!run "systemctl status nginx"
```

## Troubleshooting

Common Issues

1. Bot doesn't respond to commands
   · Check bot has Message Content Intent enabled
   · Verify bot has necessary permissions in server
2. Permission errors
   · Ensure bot user has execute permissions on system
   · Check virtual environment permissions
3. Command timeout
   · Commands automatically timeout after 60 seconds
   · Consider breaking complex operations into smaller commands
4. Missing dependencies
   · Run pip install -r requirements.txt in virtual environment
